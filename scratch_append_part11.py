import os

terms = [
    "| **Ground Lance** | Thạch Thương / Ground Lance | Ma thuật | Phép thuật hệ thổ tạo ra khối đất đâm lên nhắm vào kẻ thù. |\n",
    "| **Spontaneous psychokinetic control** | Kiểm soát năng lực tâm lý phát sinh tự phát | Khái niệm | Một kỹ thuật thông linh học vô thức tạo ra các hiện tượng ở môi trường xung quanh một người. |\n",
    "| **Recurrent spontaneous psychokinesis** / **RSPK** | Năng lực tâm lý phát sinh tự phát tái diễn / RSPK | Khái niệm | Một hiện tượng liên quan đến yêu tinh quậy phá, do sự rò rỉ ether hoặc sức mạnh tâm linh từ người có độ nhạy cảm cao gây ảnh hưởng lên môi trường. |\n",
    "| **poltergeist** | yêu tinh quậy phá / poltergeist | Khái niệm | Hiện tượng siêu nhiên gây ra tiếng ồn hoặc sự di chuyển vật thể không giải thích được. |\n"
]

with open('context/glossary.md', 'a', encoding='utf-8') as f:
    for term in terms:
        f.write(term)
