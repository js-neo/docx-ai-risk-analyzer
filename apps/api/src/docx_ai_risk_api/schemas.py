from pydantic import BaseModel, Field


class RiskSentence(BaseModel):
    sentence_index: int
    sentence: str
    markers: list[str]


class BlockAnalysis(BaseModel):
    block_name: str
    text: str
    words: int
    characters: int
    sentences: int
    avg_sentence_len: float
    sentence_len_std: float
    cliches_count: int
    cliches_found: dict[str, int]
    abstract_words_count: int
    abstract_words_found: dict[str, int]
    repeated_starts: dict[str, int]
    risk_score: int
    risk_level: str
    risky_sentences: list[RiskSentence]


class DocumentStats(BaseModel):
    filename: str
    content_type: str
    size_bytes: int
    characters: int
    words: int
    paragraphs: int
    blocks: int


class AnalysisSummary(BaseModel):
    overall_risk: str
    total_risk_score: int
    high_risk_blocks: int
    medium_risk_blocks: int
    low_risk_blocks: int
    cliches_total: int
    abstract_words_total: int


class AnalyzeResponse(BaseModel):
    status: str = Field(default="analyzed")
    document: DocumentStats
    summary: AnalysisSummary
    blocks: list[BlockAnalysis]
    limitations: list[str]
