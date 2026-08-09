import os

characters_file = r'D:\workspace\isekai_mahou_wa_okureteru\context\characters.md'
glossary_file = r'D:\workspace\isekai_mahou_wa_okureteru\context\glossary.md'
relationships_file = r'D:\workspace\isekai_mahou_wa_okureteru\context\relationships.md'

chars_append = """
### 35. Ilzarl
- **Vai trò**: Một trong các Ma Tướng phục vụ dưới trướng Ma Vương Nakshatra. Mang hình dáng một người đàn ông với mái tóc dài màu trắng, đôi mắt đỏ ngầu và vóc dáng mảnh khảnh.
- **Tính cách**: Khinh khỉnh, lạnh lùng, tự mãn.
- **Giọng thoại**: Đều đều, khinh miệt kẻ yếu (xưng "Ta", gọi "Ngươi / Tên khốn"). Tôn kính Ma Vương (xưng "Thần", gọi "Bệ hạ").

### 36. Latora
- **Vai trò**: Một nữ Ma Tướng phục vụ dưới trướng Ma Vương Nakshatra, mang hình dáng một cô gái trẻ độ xuân thì có đôi cánh dơi đen nhánh.
- **Tính cách**: Dâm đãng, tàn độc, thích đùa giỡn và đập nát kẻ thù.
- **Giọng thoại**: Cợt nhả, chế giễu (thường cười Ahahaha).
"""

glossary_append = """| **Ilzarl** | Ilzarl | Tên riêng | Một trong các Ma Tướng phục vụ dưới trướng Ma Vương Nakshatra. |
| **Latora** | Latora | Tên riêng | Một nữ Ma Tướng phục vụ dưới trướng Ma Vương Nakshatra, có đôi cánh dơi. |
| **Grallajearus** | Grallajearus | Tên riêng | Một Ma Tướng phục vụ dưới trướng Ma Vương Nakshatra. |
| **Striga** | Striga | Tên riêng | Một Ma Tướng phục vụ dưới trướng Ma Vương Nakshatra. |
"""

relationships_append = """
### Lực lượng của Ma Vương Nakshatra
- **Nakshatra <-> Vuishta / Ilzarl / Latora**: Bề trên / Kẻ dưới. Các Ma Tướng gọi Nakshatra là "Your Majesty / Bệ hạ" và xưng "Thần". Nakshatra xưng "Ta", gọi bề tôi là "Ngươi" hoặc tên.
- **Ilzarl <-> Vuishta**: Ilzarl khinh bỉ Vuishta vì đã lợi dụng cái chết của Mauhario làm mồi nhử (xưng "Ta", gọi "Ngươi / Tên khốn"). Vuishta không bận tâm, chỉ cười cợt nhả.
- **Latora <-> Vuishta**: Latora nghi ngờ khả năng của Vuishta, thích cách hành quyết tàn bạo. Vuishta tự tin đáp trả.
- **Khối thịt <-> Vuishta**: Khối thịt thường xuyên mỉa mai, nói móc Vuishta vì thói ngạo mạn. Vuishta phớt lờ.
"""

with open(characters_file, 'a', encoding='utf-8') as f:
    f.write(chars_append)

with open(glossary_file, 'a', encoding='utf-8') as f:
    f.write(glossary_append)

with open(relationships_file, 'a', encoding='utf-8') as f:
    f.write(relationships_append)

print("Appended successfully.")
