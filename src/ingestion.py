from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document


splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)


def ingest_pdf(pdf_path, report_year):
    reader = PdfReader(pdf_path)

    documents = []

    for page_no, page in enumerate(reader.pages, start=1):

        text = page.extract_text()

        if not text:
            continue

        text = text.strip()
        text = " ".join(text.split())

        chunks = splitter.split_text(text)

        for chunk in chunks:
            documents.append(
                Document(
                    page_content=chunk,
                    metadata={
                        "page_no": page_no,
                        "source": pdf_path,
                        "report": report_year
                    }
                )
            )

    return documents