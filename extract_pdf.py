import fitz
import os
import re

pdf_path = r"D:\workspace\translate\isekai_mahou_wa_okureteru\source\vol_5\_OceanofPDF.com_The_Magic_in_this_Other_World_is_Too_Far_Behind_Volume_5_-_Gamei_Hitsuji.pdf"
out_dir = r"D:\workspace\translate\isekai_mahou_wa_okureteru\source\vol_5"
img_dir = r"D:\workspace\translate\isekai_mahou_wa_okureteru\source\images\vol_5"

os.makedirs(out_dir, exist_ok=True)
os.makedirs(img_dir, exist_ok=True)

doc = fitz.open(pdf_path)
full_text = ""
img_count = 0

for page_num in range(len(doc)):
    page = doc[page_num]
    # Extract text
    text = page.get_text()
    if text:
        full_text += text + "\n\n--- PAGE BREAK ---\n\n"
        
    # Extract images
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
            
with open(os.path.join(out_dir, "raw.txt"), "w", encoding="utf-8") as f:
    f.write(full_text)

print(f"Extracted {img_count} images.")
print(f"Text saved to {os.path.join(out_dir, 'raw.txt')}")
