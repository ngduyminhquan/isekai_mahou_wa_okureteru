import os

def replace_in_file(filepath, replacements):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for old, new in replacements:
        content = content.replace(old, new)
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

p1 = r"D:\workspace\isekai_mahou_wa_okureteru\translated\vol_6\chapter_1_the_dragonnewt_in_the_part_1.md"
p2 = r"D:\workspace\isekai_mahou_wa_okureteru\translated\vol_6\chapter_1_the_dragonnewt_in_the_part_2.md"

replacements_p1 = [
    ("Thật sự thì, cậu nói cũng có lý đấy.", "Thật sự thì, ngươi nói cũng có lý đấy."),
    ("Cậu phải lên trước đã,", "Ngươi phải lên trước đã,"),
    ("tên của cậu.", "tên của ngươi."),
    ("cậu định đưa ra", "ngươi định đưa ra"),
    ("Cậu vừa nói là", "Ngươi vừa nói là"),
    ("cậu chính là người", "ngươi chính là người"),
    ("nợ cậu cả một", "nợ ngươi cả một"),
    ("người đàn ông mà cậu đang nghĩ đến", "người đàn ông mà ngươi đang nghĩ đến"),
    ("nghe nói cậu chính là người", "nghe nói ngươi chính là người"),
    ("cảm ơn vì cậu đã đặt dấu chấm hết", "cảm ơn vì ngươi đã đặt dấu chấm hết"),
    ("gửi lời cảm ơn đến cậu.", "gửi lời cảm ơn đến ngươi."),
    ("mắc nợ cậu.", "mắc nợ ngươi."),
    ("Cậu nói hoàn toàn đúng.", "Ngươi nói hoàn toàn đúng."),
    ("những gì cậu nói.", "những gì ngươi nói."),
    ("Trực giác của cậu quá nhạy bén.", "Trực giác của ngươi quá nhạy bén."),
    ("hoảng loạn, cậu vẫn vô cùng sắc sảo.", "hoảng loạn, ngươi vẫn vô cùng sắc sảo."),
    ("cậu lại là người đánh bại", "ngươi lại là người đánh bại"),
    ("trả ơn cậu.", "trả ơn ngươi."),
    ("cả cậu nữa.", "cả ngươi nữa."),
    ("sức mạnh mà cậu sở hữu", "sức mạnh mà ngươi sở hữu"),
    ("khiến cậu sợ hãi đến vậy?", "khiến ngươi sợ hãi đến vậy?"),
    ("Nếu cậu nắm giữ", "Nếu ngươi nắm giữ"),
    ("các cậu định làm thế nào đây?", "các ngươi định làm thế nào đây?"),
    ("cậu biết đấy.", "ngươi biết đấy."),
    ("Nếu cậu không thích,", "Nếu ngươi không thích,"),
    ("tất cả những gì cậu phải làm", "tất cả những gì ngươi phải làm")
]

replacements_p2 = [
    ("hạ gục cậu bằng một đòn", "hạ gục ngươi bằng một đòn"),
    ("đối với cậu thì không phải vậy sao?", "đối với ngươi thì không phải vậy sao?"),
    ("phong cách của cậu sao?", "phong cách của ngươi sao?"),
    ("cậu nên tiết lộ", "ngươi nên tiết lộ"),
    ("giải quyết được cậu bằng đòn đó", "giải quyết được ngươi bằng đòn đó"),
    ("cậu đã di chuyển xung quanh", "ngươi đã di chuyển xung quanh"),
    ("cậu dừng lại để chữa trị", "ngươi dừng lại để chữa trị"),
    ("Hôm đó chúng tớ đã chiến thắng", "Hôm đó tớ và cha đã chiến thắng")
]

replace_in_file(p1, replacements_p1)
replace_in_file(p2, replacements_p2)

print("Done")
