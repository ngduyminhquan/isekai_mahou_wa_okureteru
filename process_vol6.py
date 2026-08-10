import fitz
import os
import re
from datetime import datetime

base_dir = r"D:\workspace\isekai_mahou_wa_okureteru"
pdf_path = os.path.join(base_dir, "source", "vol_6", "_OceanofPDF.com_The_Magic_in_this_Other_World_is_Too_Far_Behind_Volume_6_-_Gamei_Hitsuji.pdf")
out_dir = os.path.join(base_dir, "source", "vol_6")
img_dir = os.path.join(base_dir, "source", "images", "vol_6")
translated_dir = os.path.join(base_dir, "translated", "vol_6")
progress_path = os.path.join(base_dir, "progress_vol_6.md")

os.makedirs(out_dir, exist_ok=True)
os.makedirs(img_dir, exist_ok=True)
os.makedirs(translated_dir, exist_ok=True)
os.makedirs(os.path.join(base_dir, "context"), exist_ok=True)

# 1. Extract PDF
doc = fitz.open(pdf_path)
full_text = ""
img_count = 0

for page_num in range(len(doc)):
    page = doc[page_num]
    text = page.get_text()
    if text:
        full_text += text + "\n\n--- PAGE BREAK ---\n\n"
        
    image_list = page.get_images()
    for img_index, img in enumerate(image_list):
        xref = img[0]
        base_image = doc.extract_image(xref)
        image_bytes = base_image["image"]
        image_ext = base_image["ext"]
        
        img_count += 1
        img_name = f"image_{img_count:03d}.{image_ext}"
        if img_count == 1:
            img_name = f"cover.{image_ext}"
            
        with open(os.path.join(img_dir, img_name), "wb") as f:
            f.write(image_bytes)

raw_path = os.path.join(out_dir, "raw.txt")
with open(raw_path, "w", encoding="utf-8") as f:
    f.write(full_text)

print(f"Extracted {img_count} images. Text saved to {raw_path}")

# 2. Chunking
with open(raw_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

cleaned_lines = []
for line in lines:
    line = line.strip()
    if line == "OceanofPDF.com" or line == "--- PAGE BREAK ---":
        continue
    if line == "":
        continue
    cleaned_lines.append(line)

chapters = []
current_chapter = None
seen_chapters = set()

for line in cleaned_lines:
    match = re.match(r"^(Prologue.*|Chapter \d+.*|Epilogue.*)$", line, re.IGNORECASE)
    if match:
        chapter_title = match.group(1).strip()
        if chapter_title in seen_chapters:
            break # Reached TOC
        seen_chapters.add(chapter_title)
        
        current_chapter = {
            "title": chapter_title,
            "lines": [],
            "parts": []
        }
        chapters.append(current_chapter)
    elif current_chapter is not None:
        current_chapter["lines"].append(line)

# Now chunk each chapter into max 200 lines
for chap in chapters:
    chap_lines = chap["lines"]
    # Safely handle colons and dots
    safe_title = re.sub(r'[\\/*?:"<>|]', "", chap["title"])
    chap_filename_base = safe_title.split("-")[0].strip().lower().replace(" ", "_").replace(":", "")
    
    chunk_size = 200
    for i in range(0, len(chap_lines), chunk_size):
        part_lines = chap_lines[i:i+chunk_size]
        part_num = (i // chunk_size) + 1
        
        part_filename = f"{chap_filename_base}_part_{part_num}.txt"
        words = sum(len(l.split()) for l in part_lines)
        
        chap["parts"].append({
            "filename": part_filename,
            "title": f"{chap['title']} - Part {part_num}",
            "lines": part_lines,
            "num_lines": len(part_lines),
            "num_words": words
        })

# Write out the parts
for chap in chapters:
    for part in chap["parts"]:
        part_path = os.path.join(out_dir, part["filename"])
        with open(part_path, "w", encoding="utf-8") as f:
            f.write("\n\n".join(part["lines"]))

# 3. Generate Progress Log
total_lines = sum(part["num_lines"] for chap in chapters for part in chap["parts"])
total_words = sum(part["num_words"] for chap in chapters for part in chap["parts"])

date_str = datetime.now().strftime("%Y-%m-%d")

md = f"""# Progress Log - Tiến độ dịch thuật Volume 6

---

## 1. Project Metadata

- **Tên tác phẩm gốc**: *The Magic in this Other World is Too Far Behind! Volume 6*
- **Tên tác phẩm dịch (tạm dịch)**: *Phép thuật ở Dị Giới này quá rớt lại phía sau! Volume 6*
- **Tác giả**: Gamei Hitsuji
- **Minh họa**: himesuz
- **Nguồn bản dịch**: OceanofPDF.com
- **Ngày bắt đầu**: {date_str}
- **Ngôn ngữ nguồn**: Tiếng Anh
- **Ngôn ngữ đích**: Tiếng Việt
- **Tổng số từ nguồn**: {total_words} từ
- **Tổng số đoạn**: {total_lines} đoạn
- **Tổng số dòng**: {total_lines} dòng
- **Trạng thái hiện tại**: Đang tiến hành

---

## 2. Translation Phases & Progress List

Dưới đây là danh sách các Phase tương ứng với từng phần dịch (chunk). Mỗi phần sẽ được dịch, áp dụng glossary/character/relationship và ghi nhận kết quả vào thư mục `translated/vol_6/`.

| Phase | Nội dung dịch | File nguồn thô (Raw File) | Số đoạn (Paras) | Số dòng (Lines) | Số từ nguồn (Words) | File kết quả dịch (Translated) | Trạng thái |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- | :---: |
| **0** | Khởi tạo dự án và tài nguyên | *N/A* | - | - | - | *N/A* | **Hoàn thành** |
"""

phase = 1
for chap in chapters:
    for part in chap["parts"]:
        md += f"| **{phase}** | {part['title']} | `{part['filename']}` | {part['num_lines']} | {part['num_lines']} | {part['num_words']} | `{part['filename'].replace('.txt', '.md')}` | **Chưa bắt đầu** |\n"
        phase += 1

md += """
---

## 3. Quy tắc định dạng & Ghi chú dịch thuật
- **Ngắt dòng thoại**: Mọi lời thoại của các nhân vật phải được tách biệt hoàn toàn trên các dòng riêng biệt (không gộp nhiều lời thoại của các nhân vật khác nhau trên cùng một dòng), và được phân tách với nhau bằng một dòng trống.
"""

with open(progress_path, "w", encoding="utf-8") as f:
    f.write(md)

# Create context files if they don't exist
for ctx_file in ["glossary.md", "characters.md", "relationships.md"]:
    p = os.path.join(base_dir, "context", ctx_file)
    if not os.path.exists(p):
        with open(p, "w", encoding="utf-8") as f:
            f.write(f"# {ctx_file.replace('.md', '').capitalize()}\n")

print("Done generating chapters and progress_vol_6.md")
