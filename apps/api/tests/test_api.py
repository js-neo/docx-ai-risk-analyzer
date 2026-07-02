from io import BytesIO

from docx import Document
from fastapi.testclient import TestClient

from docx_ai_risk_api.main import app

client = TestClient(app)


def create_docx_bytes(text: str) -> bytes:
    buffer = BytesIO()
    document = Document()
    document.add_paragraph(text)
    document.save(buffer)
    return buffer.getvalue()


def test_health_check_returns_ok() -> None:
    response = client.get("/api/v1/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_analyze_rejects_non_docx_file() -> None:
    response = client.post(
        "/api/v1/analyze",
        files={
            "file": (
                "sample.txt",
                b"plain text",
                "text/plain",
            )
        },
    )

    assert response.status_code == 400
    assert response.json()["detail"] == "Only .docx files are supported"


def test_analyze_rejects_empty_file() -> None:
    response = client.post(
        "/api/v1/analyze",
        files={
            "file": (
                "empty.docx",
                b"",
                "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            )
        },
    )

    assert response.status_code == 400
    assert response.json()["detail"] == "Uploaded file is empty"


def test_analyze_valid_docx_returns_analysis_result() -> None:
    docx_content = create_docx_bytes(
        "Кафе использует прогноз посещаемости для планирования смены. "
        "Администратор сравнивает ожидаемое количество гостей с фактической загрузкой. "
        "При высокой посещаемости заранее усиливается смена сотрудников."
    )

    response = client.post(
        "/api/v1/analyze",
        files={
            "file": (
                "sample.docx",
                docx_content,
                "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            )
        },
    )

    data = response.json()

    assert response.status_code == 200
    assert data["status"] == "analyzed"
    assert data["document"]["filename"] == "sample.docx"
    assert data["document"]["words"] > 0
    assert data["summary"]["overall_risk"] in {"low", "medium", "high"}
    assert len(data["blocks"]) >= 1
