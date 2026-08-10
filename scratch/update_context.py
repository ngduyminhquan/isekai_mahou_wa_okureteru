import os

def update_glossary(path):
    with open(path, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()
    
    new_terms = """
| **Ishar Cluster** | Kiếm tinh thể Ishar Cluster / Ishar Cluster | Vật phẩm / Khái niệm | Thanh kiếm tinh thể của Reiji. |
| **Cathedral Forge** | Lò rèn Thánh đường / Cathedral Forge | Ma thuật | Ma pháp kết hợp do Mizuki (Io Kuzami) thi triển. |
"""
    if "Ishar Cluster" not in content:
        content = content.strip() + new_terms
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)

def update_characters(path):
    with open(path, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()
    
    if "Thiên Không Thánh Vương, Io Kuzami" not in content:
        old_str = 'tự xưng là "Thiên Không Thánh Vương, Anou Mizuki".'
        new_str = 'tự xưng là "Thiên Không Thánh Vương, Anou Mizuki" (hay "Thiên Không Thánh Vương, Io Kuzami"). Ở Volume 6, nhân cách này đã thức tỉnh để chiến đấu với Ilzarl.'
        if old_str in content:
            content = content.replace(old_str, new_str)
        else:
            print("Couldn't find target string in characters.md")
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)

def clean_relationships(path):
    with open(path, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    base = r'D:\workspace\isekai_mahou_wa_okureteru\context'
    update_glossary(os.path.join(base, 'glossary.md'))
    update_characters(os.path.join(base, 'characters.md'))
    clean_relationships(os.path.join(base, 'relationships.md'))
    print("Done")
