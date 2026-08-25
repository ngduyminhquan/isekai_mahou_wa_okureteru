import os

GLOSSARY_PATH = "D:/workspace/isekai_mahou_wa_okureteru/context/glossary.md"

with open(GLOSSARY_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

if "Biên niên sử Akashic" not in content:
    content += "\n- Akashic Records: Biên niên sử Akashic"
if "meister" not in content:
    content += "\n- Meister: Meister (Thầy / Người chế tạo)"

with open(GLOSSARY_PATH, 'w', encoding='utf-8') as f:
    f.write(content)
