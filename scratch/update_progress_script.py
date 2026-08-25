import os

PROGRESS_PATH = "D:/workspace/isekai_mahou_wa_okureteru/progress_vol_9.md"

with open(PROGRESS_PATH, 'r', encoding='utf-8') as f:
    lines = f.readlines()

with open(PROGRESS_PATH, 'w', encoding='utf-8') as f:
    for line in lines:
        if "| **32** | Chapter 4 - The Way of a Genius - Part 8 |" in line:
            line = line.replace("**Chưa bắt đầu**", "**Hoàn thành**")
        f.write(line)
