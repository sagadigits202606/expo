import os
from pdf2image import convert_from_path

POPPLER_PATH = r"C:\poppler\Library\bin"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

pdfs = ["PDF1.pdf", "PDF2.pdf", "PDF3.pdf"]

for pdf_name in pdfs:
    pdf_path = os.path.join(BASE_DIR, pdf_name)
    if not os.path.exists(pdf_path):
        print(f"スキップ: {pdf_name} が見つかりません")
        continue

    folder_name = os.path.splitext(pdf_name)[0]
    output_dir = os.path.join(BASE_DIR, "images", folder_name)
    os.makedirs(output_dir, exist_ok=True)

    print(f"変換中: {pdf_name} ...")
    pages = convert_from_path(pdf_path, dpi=200, poppler_path=POPPLER_PATH)

    for i, page in enumerate(pages):
        out_path = os.path.join(output_dir, f"page_{i+1:02d}.png")
        page.save(out_path, "PNG")
        print(f"  保存: {out_path}")

print("完了！")
