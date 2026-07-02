import re
from statistics import mean, pstdev

from docx_ai_risk_api.schemas import BlockAnalysis, RiskSentence

CLICHES = [
    "таким образом",
    "следует отметить",
    "важно отметить",
    "можно сделать вывод",
    "это позволяет",
    "позволяет обеспечить",
    "повысить эффективность",
    "оптимизировать",
    "на основе анализа",
    "в результате",
    "данный",
    "данная",
    "данные позволяют",
    "алгоритм позволяет",
    "машинное обучение позволяет",
    "искусственный интеллект позволяет",
    "руководство может",
    "для последующего анализа",
]

ABSTRACT_WORDS = [
    "эффективность",
    "оптимизация",
    "автоматизация",
    "закономерности",
    "анализ",
    "прогнозирование",
    "система",
    "алгоритм",
    "процесс",
    "результат",
    "показатель",
    "информация",
]

RISK_PHRASES = sorted(set(CLICHES + ABSTRACT_WORDS))


def count_words(text: str) -> int:
    return len(re.findall(r"\b[А-Яа-яA-Za-zЁё0-9-]+\b", text))


def split_paragraphs(text: str) -> list[str]:
    return [paragraph.strip() for paragraph in re.split(r"\n\s*\n", text) if paragraph.strip()]


def split_sentences(text: str) -> list[str]:
    sentences = re.split(r"(?<=[.!?])\s+", text)
    return [sentence.strip() for sentence in sentences if sentence.strip()]


def split_text_into_blocks(text: str, target_words: int = 300) -> list[str]:
    paragraphs = split_paragraphs(text)

    blocks: list[str] = []
    current: list[str] = []
    current_words = 0

    for paragraph in paragraphs:
        current.append(paragraph)
        current_words += count_words(paragraph)

        if current_words >= target_words:
            blocks.append("\n\n".join(current))
            current = []
            current_words = 0

    if current:
        blocks.append("\n\n".join(current))

    return blocks


def count_occurrences(text: str, phrases: list[str]) -> dict[str, int]:
    text_lower = text.lower()
    found: dict[str, int] = {}

    for phrase in phrases:
        count = text_lower.count(phrase.lower())
        if count:
            found[phrase] = count

    return found


def find_repeated_sentence_starts(sentences: list[str]) -> dict[str, int]:
    starts: dict[str, int] = {}

    for sentence in sentences:
        words = sentence.lower().split()
        if len(words) >= 3:
            start = " ".join(words[:3])
            starts[start] = starts.get(start, 0) + 1

    return {start: count for start, count in starts.items() if count > 1}


def find_risky_sentences(sentences: list[str]) -> list[RiskSentence]:
    risky_sentences: list[RiskSentence] = []

    for index, sentence in enumerate(sentences, start=1):
        sentence_lower = sentence.lower()
        markers = [phrase for phrase in RISK_PHRASES if phrase in sentence_lower]

        if markers:
            risky_sentences.append(
                RiskSentence(
                    sentence_index=index,
                    sentence=sentence,
                    markers=markers,
                )
            )

    return risky_sentences


def get_risk_level(score: int) -> str:
    if score >= 8:
        return "high"

    if score >= 4:
        return "medium"

    return "low"


def analyze_block(block_name: str, text: str) -> BlockAnalysis:
    words = count_words(text)
    sentences = split_sentences(text)

    sentence_lengths = [count_words(sentence) for sentence in sentences]
    avg_sentence_len = round(mean(sentence_lengths), 2) if sentence_lengths else 0.0
    sentence_len_std = round(pstdev(sentence_lengths), 2) if len(sentence_lengths) > 1 else 0.0

    cliches_found = count_occurrences(text, CLICHES)
    abstract_words_found = count_occurrences(text, ABSTRACT_WORDS)
    repeated_starts = find_repeated_sentence_starts(sentences)
    risky_sentences = find_risky_sentences(sentences)

    cliches_count = sum(cliches_found.values())
    abstract_words_count = sum(abstract_words_found.values())

    score = 0

    if len(cliches_found) >= 4:
        score += 3
    elif len(cliches_found) >= 2:
        score += 2
    elif len(cliches_found) == 1:
        score += 1

    if abstract_words_count >= 20:
        score += 3
    elif abstract_words_count >= 10:
        score += 2
    elif abstract_words_count >= 5:
        score += 1

    if avg_sentence_len > 22:
        score += 2
    elif avg_sentence_len > 18:
        score += 1

    if sentence_len_std < 6 and len(sentences) >= 6:
        score += 2

    if len(repeated_starts) >= 2:
        score += 2
    elif len(repeated_starts) == 1:
        score += 1

    return BlockAnalysis(
        block_name=block_name,
        text=text,
        words=words,
        characters=len(text),
        sentences=len(sentences),
        avg_sentence_len=avg_sentence_len,
        sentence_len_std=sentence_len_std,
        cliches_count=cliches_count,
        cliches_found=cliches_found,
        abstract_words_count=abstract_words_count,
        abstract_words_found=abstract_words_found,
        repeated_starts=repeated_starts,
        risk_score=score,
        risk_level=get_risk_level(score),
        risky_sentences=risky_sentences,
    )


def analyze_text(text: str) -> list[BlockAnalysis]:
    blocks = split_text_into_blocks(text)

    return [
        analyze_block(block_name=f"block_{index:02}", text=block)
        for index, block in enumerate(blocks, start=1)
    ]
