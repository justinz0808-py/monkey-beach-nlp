import fitz
import json

pdf_path = r"_OceanofPDF.com_Monkey_Beach_-_Eden_Robinson.pdf"

doc = fitz.open(pdf_path)

with open("monkey_beach_pages.jsonl", "w", encoding="utf-8") as f:
    for page_num, page in enumerate(doc, start=1):
        text = page.get_text("text").strip()
        record = {
            "id": f"monkey_beach_page_{page_num}",
            "page": page_num,
            "text": text,
            "source": pdf_path
        }
        f.write(json.dumps(record, ensure_ascii=False) + "\n")

with open("monkey_beach_full_text.txt", "w", encoding="utf-8") as f:
    for page_num, page in enumerate(doc, start=1):
        text = page.get_text("text")
        f.write(f"\n\n--- PAGE {page_num} ---\n\n")
        f.write(text)

print("Done. Created monkey_beach_pages.jsonl and monkey_beach_full_text.txt")