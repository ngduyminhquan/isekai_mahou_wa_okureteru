import re
import os

raw_path = r"D:\workspace\translate\isekai_mahou_wa_okureteru\source\vol_5\raw.txt"
out_dir = r"D:\workspace\translate\isekai_mahou_wa_okureteru\source\vol_5"
progress_path = r"D:\workspace\translate\isekai_mahou_wa_okureteru\progress_vol_5.md"

with open(raw_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

# Clean up lines
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

# We assume TOC is at the end, so if we see Chapter 1 again, we stop.
seen_chapters = set()

for line in cleaned_lines:
    match = re.match(r"^(Prologue.*|Chapter \d+:.*|Epilogue)$", line, re.IGNORECASE)
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
    
    # Safe filename
    chap_filename_base = chap["title"].split(":")[0].strip().lower().replace(" ", "_")
    
    # split into parts
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

# Create translated dir
translated_dir = r"D:\workspace\translate\isekai_mahou_wa_okureteru\translated\vol_5"
os.makedirs(translated_dir, exist_ok=True)

# Generate progress log
total_lines = sum(part["num_lines"] for chap in chapters for part in chap["parts"])
total_words = sum(part["num_words"] for chap in chapters for part in chap["parts"])

md = f"""# Progress Log - Tiến độ dịch thuật Volume 5

---

## 1. Project Metadata

- **Tên tác phẩm gốc**: *The Magic in this Other World is Too Far Behind! Volume 5*
- **Tên tác phẩm dịch (tạm dịch)**: *Phép thuật ở Dị Giới này quá rớt lại phía sau! Volume 5*
- **Tác giả**: Gamei Hitsuji
- **Minh họa**: himesuz
- **Nguồn bản dịch**: OceanofPDF.com
- **Ngày bắt đầu**: 2026-08-06
- **Ngôn ngữ nguồn**: Tiếng Anh
- **Ngôn ngữ đích**: Tiếng Việt
- **Tổng số từ nguồn**: {total_words} từ
- **Tổng số đoạn**: {total_lines} đoạn
- **Tổng số dòng**: {total_lines} dòng
- **Trạng thái hiện tại**: Đang tiến hành

---

## 2. Translation Phases & Progress List

Dưới đây là danh sách các Phase tương ứng với từng phần dịch (chunk). Mỗi phần sẽ được dịch, áp dụng glossary/character/relationship và ghi nhận kết quả vào thư mục `translated/vol_5/`.

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

print("Done generating chapters and progress.md")
