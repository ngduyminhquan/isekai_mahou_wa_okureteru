import os

terms = [
    "| **Intrinsic Curse** | Lời nguyền Cố hữu / Intrinsic Curse | Ma thuật | Từ khóa trong câu chú của Liliana Zandyke. |\n",
    "| **Astral Dive** | Trầm luân Linh hồn / Astral Dive | Ma thuật | Từ khóa trong câu chú của Liliana Zandyke. |\n",
    "| **Howl of Absolute Destruction** | Tiếng hú Diệt vong / Howl of Absolute Destruction | Ma thuật | Đòn tấn công kết liễu của Howler do Liliana triệu hồi. |\n",
    "| **rebound air** | luồng khí dội ngược / rebound air | Khái niệm | Sự phản phệ của bí thuật cấp cao lên chính người thi triển khi yếu tố cốt lõi tạo nên sự huyền bí của thần chú bị cản trở. |\n"
]

with open('context/glossary.md', 'a', encoding='utf-8') as f:
    for term in terms:
        f.write(term)
