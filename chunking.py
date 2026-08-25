import os
import re

base_dir = r"D:\workspace\translate\isekai_mahou_wa_okureteru"
vol_id = "vol_9"
raw_text_path = os.path.join(base_dir, "source", vol_id, "raw_text.txt")
out_dir = os.path.join(base_dir, "source", vol_id)

with open(raw_text_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

# Clean up OceanofPDF.com mentions and weird newlines if possible
cleaned_lines = []
for line in lines:
    clean = line.strip()
    if clean == "OceanofPDF.com":
        continue
    cleaned_lines.append(line)

lines = cleaned_lines

chapters = []
current_chapter = None
current_content = []

chapter_patterns = [
    r"^Prologue:",
    r"^Chapter \d+:",
    r"^Epilogue:",
    r"^Afterword"
]

def is_chapter_heading(line):
    for p in chapter_patterns:
        if re.match(p, line.strip()):
            return True
    return False

for i, line in enumerate(lines):
    if i > 9100 and "Table of Contents" in line: # simplistic end detection
        break
    
    if is_chapter_heading(line):
        if current_chapter is not None:
            chapters.append((current_chapter, current_content))
        current_chapter = line.strip().replace(":", " -").replace("?", "")
        current_content = [line]
    elif current_chapter is not None:
        current_content.append(line)

if current_chapter is not None:
    chapters.append((current_chapter, current_content))

phases = []
phase_idx = 1
total_words = 0
total_lines = 0
total_paras = 0

for ch_name, ch_lines in chapters:
    # Safe filename
    safe_ch_name = re.sub(r'[\\/*?:"<>|]', "", ch_name)
    safe_ch_name = safe_ch_name.lower().replace(" ", "_").replace("-", "").replace("__", "_")
    
    # Split into chunks of max 200 lines
    parts = []
    current_part = []
    
    for line in ch_lines:
        current_part.append(line)
        if len(current_part) >= 190 and line.strip() == "":
            parts.append(current_part)
            current_part = []
    
    if len(current_part) > 0:
        if len(current_part) < 20 and len(parts) > 0:
            parts[-1].extend(current_part)
        else:
            parts.append(current_part)
    
    for i, part in enumerate(parts):
        part_name = safe_ch_name
        if len(parts) > 1:
            part_name += f"_part_{i+1}"
        
        file_name = f"{part_name}.txt"
        file_path = os.path.join(out_dir, file_name)
        
        # Write file
        with open(file_path, "w", encoding="utf-8") as f:
            f.writelines(part)
        
        word_count = sum(len(l.split()) for l in part)
        line_count = len(part)
        para_count = len([l for l in part if l.strip() != ""])
        
        total_words += word_count
        total_lines += line_count
        total_paras += para_count
        
        display_name = ch_name
        if len(parts) > 1:
            display_name += f" - Part {i+1}"
            
        md_file = f"{part_name}.md"
        phases.append((phase_idx, display_name, file_name, para_count, line_count, word_count, md_file))
        phase_idx += 1

# Write progress.md
progress_content = f"""# Progress Log - Tiến độ dịch thuật Volume 9

---

## 1. Project Metadata

- **Tên tác phẩm gốc**: *The Magic in this Other World is Too Far Behind! Volume 9*
- **Tên tác phẩm dịch (tạm dịch)**: *[Tên tiếng Việt]*
- **Tác giả**: Gamei Hitsuji
- **Minh họa**: [Tên]
- **Nguồn bản dịch**: OceanofPDF.com
- **Ngày bắt đầu**: 2026-08-25
- **Ngôn ngữ nguồn**: Tiếng Anh
- **Ngôn ngữ đích**: Tiếng Việt
- **Tổng số từ nguồn**: {total_words} từ
- **Tổng số đoạn**: {total_paras} đoạn
- **Tổng số dòng**: {total_lines} dòng
- **Trạng thái hiện tại**: Đang tiến hành

---

## 2. Translation Phases & Progress List

Dưới đây là danh sách các Phase tương ứng với từng phần dịch (chunk). Mỗi phần sẽ được dịch, áp dụng glossary/character/relationship và ghi nhận kết quả vào thư mục `translated/vol_9/`.

| Phase | Nội dung dịch | File nguồn thô (Raw File) | Số đoạn (Paras) | Số dòng (Lines) | Số từ nguồn (Words) | File kết quả dịch (Translated) | Trạng thái |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- | :---: |
| **0** | Khởi tạo dự án và tài nguyên | *N/A* | - | - | - | *N/A* | **Hoàn thành** |
"""
for p in phases:
    progress_content += f"| **{p[0]}** | {p[1]} | `{p[2]}` | {p[3]} | {p[4]} | {p[5]} | `{p[6]}` | **Chưa bắt đầu** |\n"

progress_content += """
---

## 3. Quy tắc định dạng & Ghi chú dịch thuật
- **Ngắt dòng thoại**: Mọi lời thoại của các nhân vật phải được tách biệt hoàn toàn trên các dòng riêng biệt (không gộp nhiều lời thoại của các nhân vật khác nhau trên cùng một dòng), và được phân tách với nhau bằng một dòng trống.
"""

with open(os.path.join(base_dir, "progress_vol_9.md"), "w", encoding="utf-8") as f:
    f.write(progress_content)

print(f"Created {len(phases)} phases.")
