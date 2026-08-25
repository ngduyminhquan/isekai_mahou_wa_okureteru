import os
import fitz
import re

pdf_path = r"D:\workspace\translate\isekai_mahou_wa_okureteru\source\vol_9\_OceanofPDF.com_The_Magic_in_this_Other_World_is_Too_Far_Behind_Volume_9_-_Gamei_Hitsuji.pdf"
base_dir = r"D:\workspace\translate\isekai_mahou_wa_okureteru"
vol_id = "vol_9"

# Create directories
os.makedirs(os.path.join(base_dir, "source", "images", vol_id), exist_ok=True)
os.makedirs(os.path.join(base_dir, "translated", vol_id), exist_ok=True)
os.makedirs(os.path.join(base_dir, "context"), exist_ok=True)

# Open PDF
doc = fitz.open(pdf_path)

all_text = []
image_count = 0

for i in range(len(doc)):
    page = doc[i]
    
    # Extract text
    text = page.get_text()
    if text:
        all_text.append(text)
        
    # Extract images
    image_list = page.get_images(full=True)
    for img_index, img in enumerate(image_list):
        xref = img[0]
        base_image = doc.extract_image(xref)
        image_bytes = base_image["image"]
        image_ext = base_image["ext"]
        
        # Name images logically if possible, but basic count for now
        image_filename = f"image_{image_count}.{image_ext}"
        if image_count == 0:
            image_filename = "cover.jpg" # Assuming first is cover
            
        image_filepath = os.path.join(base_dir, "source", "images", vol_id, image_filename)
        with open(image_filepath, "wb") as f:
            f.write(image_bytes)
        image_count += 1

# Save full text
raw_text_path = os.path.join(base_dir, "source", vol_id, "raw_text.txt")
with open(raw_text_path, "w", encoding="utf-8") as f:
    f.write("\n".join(all_text))

print(f"Extracted {len(all_text)} pages of text.")
print(f"Extracted {image_count} images.")
