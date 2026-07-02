from fastapi import APIRouter, File, HTTPException, UploadFile

router = APIRouter()


@router.post("/analyze")
async def analyze_document(file: UploadFile = File(...)) -> dict[str, str | int]:
    if not file.filename:
        raise HTTPException(status_code=400, detail="Filename is required")

    if not file.filename.lower().endswith(".docx"):
        raise HTTPException(status_code=400, detail="Only .docx files are supported")

    content = await file.read()

    if not content:
        raise HTTPException(status_code=400, detail="Uploaded file is empty")

    return {
        "filename": file.filename,
        "content_type": file.content_type or "unknown",
        "size_bytes": len(content),
        "status": "received",
    }
