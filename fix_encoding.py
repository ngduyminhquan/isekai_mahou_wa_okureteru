import os

chars = '''# Characters - Hồ sơ Nhân vật

## 1. Suimei Yakagi
- **Đặc điểm**: Nam chính, một pháp sư hiện đại bị triệu hồi sang thế giới khác cùng bạn bè nhưng giấu nghề.
- **Giọng văn/Tính cách**: Thường nói chuyện nghiêm túc, suy nghĩ logic, đôi khi tỏ ra mỉa mai, châm biếm khi cần.
- **Cách xưng hô thường dùng**: Tôi (với đa số), Tớ/cậu (với bạn bè như Reiji, Mizuki).

## 2. Reiji Hanao
- **Đặc điểm**: Bạn của Suimei, người được triệu hồi với tư cách Anh hùng.
- **Giọng văn/Tính cách**: Chính trực, nhiệt tình, ngay thẳng.

## 3. Mizuki Anou
- **Đặc điểm**: Bạn của Suimei và Reiji, cũng bị cuốn vào vụ triệu hồi. Có một quá khứ "chuunibyou" (dark past) hay nói những lời khoa trương. Hiện tại thi thoảng đang bị tinh linh nhập xác làm vật chứa.
- **Giọng văn/Tính cách**: Hiền lành, hay lo lắng cho bạn bè. Dễ xấu hổ khi nhắc về quá khứ đen tối.

## 4. Alshuna
- **Đặc điểm**: Nữ thần của thế giới này.
- **Giọng văn/Tính cách**: Trang trọng, quyền uy.

## 5. Felmenia Stingray
- **Đặc điểm**: Nữ pháp sư từ thế giới khác đi cùng Suimei.
- **Giọng văn/Tính cách**: Tôn trọng, lịch sự.

## 6. Lefille
- **Đặc điểm**: Nữ chiến binh/pháp sư từ thế giới khác đi cùng Suimei.
- **Giọng văn/Tính cách**: Trưởng thành, thân thiện.

## 7. Liliana
- **Đặc điểm**: Nữ pháp sư từ thế giới khác đi cùng Suimei. Có đôi mắt hay nhắm hờ ngái ngủ.
- **Giọng văn/Tính cách**: Ngập ngừng, hay nói ngắt quãng.

## 8. Hatsumi Kuchiba
- **Đặc điểm**: Bạn thời thơ ấu của Suimei từ Trái Đất, sống ở dinh thự Kuchiba ngay cạnh nhà Suimei. Cũng bị cuốn sang thế giới khác và giờ đã trở về.
- **Giọng văn/Tính cách**: Thân thiết, thẳng thắn, đôi khi mít ướt khi xúc động. Có mái tóc vàng.

## 9. Hydemary Alzbayne
- **Đặc điểm**: Đệ tử/trợ lý/sứ ma của Suimei, một pháp sư cấp High Grand của Hội. Cô là một homunculus (sinh vật nhân tạo) và là người sáng lập ra hệ thống phép thuật nguyên thủy (origin magicka) của riêng mình. Luôn mặc trang phục ảo thuật gia. Có sở thích làm búp bê.
- **Giọng văn/Tính cách**: Khuôn mặt luôn vô cảm nhưng giọng điệu và cử chỉ vô cùng biểu cảm, thỉnh thoảng hơi trẻ con, độc mồm độc miệng. Tự nhận mình là thiên tài.

## 10. Kuchiba Kiyoshiro
- **Đặc điểm**: Cha của Hatsumi, một bậc thầy kiếm thuật được gọi là Kiếm Vương (Sword of Swords). Là chú của Suimei.
- **Giọng văn/Tính cách**: Thường hay đùa giỡn, có vẻ ngoài trẻ trung nhưng ánh mắt đáng sợ.

## 11. Kuchiba Yukio
- **Đặc điểm**: Mẹ của Hatsumi, dì của Suimei.
- **Giọng văn/Tính cách**: Uyển chuyển, điềm tĩnh, dễ dàng đối phó với sự tinh nghịch của chồng.

## 12. Yakagi Kazamitsu
- **Đặc điểm**: Cha của Suimei, anh trai cực chéo của Kiyoshiro. Là một pháp sư vô cùng vĩ đại thuộc Hội (Society), nằm trong Thập Đại Tham Lam (Greed of Ten).

## 13. Kuchiba Haseto
- **Đặc điểm**: Em trai của Hatsumi, em họ của Suimei. Một cậu bé đẹp trai với mái tóc dài và phần mái vuốt ngược, trông rất giống cha mình (Kiyoshiro). Thường mặc võ phục đạo đường mang theo kiếm gỗ.
- **Giọng văn/Tính cách**: Vui vẻ, hay đùa, tính cách giống cha mình. Tôn trọng Suimei.

## 14. Rumeya
- **Đặc điểm**: Hội trưởng (Guild Master) ở thế giới bên kia.

## 15. Akitsuki
- **Đặc điểm**: Tài xế riêng của Suimei, cũng là một pháp sư của Hội. Một người đàn ông trẻ tuổi mặc vest xám, điềm đạm và tĩnh lặng. Đã phục vụ nhà Yakagi từ thế hệ của Kazamitsu.
- **Giọng văn/Tính cách**: Điềm đạm, lịch sự, luôn giữ thái độ tôn trọng với Suimei.
'''

rels = '''# Relationships - Mối quan hệ và Xưng hô

## 1. Suimei - Reiji
- **Quan hệ**: Bạn thân từ thế giới cũ.
- **Xưng hô (Tiếng Việt)**: Tớ - Cậu / Tôi - Cậu (tùy ngữ cảnh).

## 2. Suimei - Mizuki
- **Quan hệ**: Bạn bè.
- **Xưng hô (Tiếng Việt)**: Tớ - Cậu / Tôi - Cô.

## 3. Reiji - Mizuki
- **Quan hệ**: Bạn bè / Hơi có tình cảm.
- **Xưng hô (Tiếng Việt)**: Tớ - Cậu.

## 4. Alshuna - Các tinh linh/thuộc hạ
- **Quan hệ**: Nữ thần - Tôi tớ.
- **Xưng hô (Tiếng Việt)**: Ta - Ngươi.

## 5. Tinh linh (trong cơ thể Mizuki) - Alshuna
- **Quan hệ**: Bề tôi - Đấng Sáng Thế.
- **Xưng hô (Tiếng Việt)**: Thần - Người / Đấng Đại Mẫu. (Alshuna gọi là: Ta - Ngươi)

## 6. Suimei - Hatsumi
- **Quan hệ**: Bạn thanh mai trúc mã, hàng xóm sát vách.
- **Xưng hô (Tiếng Việt)**: Tớ - Cậu.

## 7. Suimei - Felmenia
- **Quan hệ**: Chủ - Tớ / Bạn đồng hành.
- **Xưng hô (Tiếng Việt)**: Tớ/Tôi - Cô / Suimei-dono - Ngài Suimei (Felmenia gọi).

## 8. Suimei - Lefille
- **Quan hệ**: Bạn đồng hành.
- **Xưng hô (Tiếng Việt)**: Tớ/Tôi - Cậu / Suimei-kun (Lefille gọi).

## 9. Suimei - Liliana
- **Quan hệ**: Bạn đồng hành.
- **Xưng hô (Tiếng Việt)**: Tớ/Tôi - Cô (Suimei gọi). Liliana xưng hô: Tôi - Cậu (hoặc gọi tên Suimei).

## 10. Suimei - Hydemary
- **Quan hệ**: Sư phụ - Đệ tử. Hydemary gọi Suimei là "Suimei-kun".
- **Xưng hô (Tiếng Việt)**: Anh - Em (Hydemary xưng hô). Suimei gọi là "Mary".

## 11. Suimei - Kuchiba Kiyoshiro
- **Quan hệ**: Cháu - Chú (Đồng thời Suimei gọi Kiyoshiro là Sư phụ).
- **Xưng hô (Tiếng Việt)**: Cháu - Chú / Cháu - Ta / Suimei gọi Kiyoshiro là "Sư phụ".

## 12. Hatsumi - Kiyoshiro / Yukio
- **Quan hệ**: Con gái - Cha mẹ.
- **Xưng hô (Tiếng Việt)**: Con - Bố/Mẹ.

## 13. Suimei - Kuchiba Haseto
- **Quan hệ**: Anh em họ. Cùng nhau lớn lên từ nhỏ.
- **Xưng hô (Tiếng Việt)**: Anh - Em. Haseto gọi Suimei là "Suimei-san". Suimei gọi là "Haseto".

## 14. Suimei - Akitsuki
- **Quan hệ**: Thiếu gia - Tài xế / Cấp dưới.
- **Xưng hô (Tiếng Việt)**: Cậu - Tôi. Akitsuki gọi Suimei là "Thiếu gia". Suimei gọi Akitsuki là "Akitsuki-san".
'''

glos = '''# Glossary - Danh mục Thuật ngữ

## 1. Tên Nhân vật (Characters)
- Suimei Yakagi: Suimei Yakagi
- Reiji Hanao: Reiji Hanao
- Mizuki Anou: Mizuki Anou
- Alshuna: Alshuna
- Felmenia Stingray: Felmenia Stingray
- Lefille: Lefille
- Liliana: Liliana
- Hatsumi Kuchiba: Hatsumi Kuchiba
- Hydemary Alzbayne: Hydemary Alzbayne
- Nicolas: Nicolas (Giáo sư)
- The Chairman: Chủ tịch (Hội Pháp sư)
- Kuchiba Kiyoshiro: Kuchiba Kiyoshiro
- Kuchiba Yukio: Kuchiba Yukio
- Yakagi Kazamitsu: Yakagi Kazamitsu

## 2. Địa danh (Locations)
- Astel: Astel
- Camellia: Camellia
- Yakagi: Yakagi (Dinh thự)
- Kuchiba: Kuchiba (Dinh thự)

## 3. Thuật ngữ & Kỹ năng (Terms & Skills)
- Sacrament: Thánh tích / Sacrament
- Hero: Anh hùng
- Caster: Pháp sư
- Creator: Đấng Sáng Tạo
- The Great Mother of Creation: Đấng Đại Mẫu Sáng Thế
- Source: Căn Nguyên
- Artifact: Tạo tác
- High grand class magician: Pháp sư cấp High Grand
- The Society: Hội (Hội Pháp sư)
- Homunculus: Homunculus (Người nhân tạo)
- Elements: Tinh Linh Nguyên Tố
- Mysteries: Những điều bí ẩn
- Magic: Ma thuật
- Magicka: Pháp thuật
- Origin magicka: Pháp thuật nguyên thủy
- Truth Flare: Chân Hỏa
- White Flame Hyacinth: Bạch Hỏa Dạ Lan Hương
- Sword of Swords: Kiếm Vương
- Phantom Sword of the Kurikara Dharani: Ảo Ảnh Kiếm của Câu Lợi Già La Đà La Ni
- Greed of Ten: Thập Đại Tham Lam
- Courier: Người chuyển phát nhanh (liên lạc của Hội/Pháp sư)
- Thousand Nights Association: Hội Ngàn Đêm
- Enforcer: Người Thực Thi
- Magicka Bureau: Cục Pháp Thuật
- Holy Inquisition: Tòa Án Dị Giáo
- Grimoire: Ma đạo thư
- Magickal tool: Ma cụ
- Astral plane: Chiều không gian linh hồn
- Mana: Mana
- Beasts of the apocalypse: Quái vật tận thế
- Glamour magic: Ma thuật ảo ảnh
- Enforcement request: Yêu cầu thực thi
- Eighth seat: Vị trí Thứ Bát
- Guild master: Hội trưởng
'''

with open('context/characters.md', 'w', encoding='utf-8') as f: f.write(chars)
with open('context/relationships.md', 'w', encoding='utf-8') as f: f.write(rels)
with open('context/glossary.md', 'w', encoding='utf-8') as f: f.write(glos)
