import os
import re

progress_file = "progress_vol_6.md"
translated_dir = "translated/vol_6"

with open(progress_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if "| **" in line and ".md" in line:
        parts = line.split("|")
        if len(parts) >= 8:
            filename = parts[7].strip().replace("`", "")
            if filename != "N/A" and filename.endswith(".md"):
                filepath = os.path.join(translated_dir, filename)
                if os.path.exists(filepath):
                    lines[i] = line.replace("**Chưa bắt đầu**", "**Hoàn thành**")

with open(progress_file, "w", encoding="utf-8") as f:
    f.writelines(lines)
