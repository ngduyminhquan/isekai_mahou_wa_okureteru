import os

def process_glossary():
    path = 'context/glossary.md'
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    new_lines = []
    seen_rajas = False
    for line in lines:
        if '| **Vuishta** | Vuishta | Tên riêng | Một con quỷ được Ma Vương Nakshatra ra lệnh tập hợp lực lượng. |' in line:
            continue
        if '| **Rajas** | Tướng quỷ Rajas | Tên riêng | Một tướng quỷ đã bị nhóm của Reiji đánh bại trước đó. |' in line:
            if not seen_rajas:
                seen_rajas = True
                new_lines.append(line)
            continue
        new_lines.append(line)
        
    # Add orichalcos at the end of the table
    for i in range(len(new_lines)-1, -1, -1):
        if new_lines[i].strip().startswith('|'):
            new_lines.insert(i+1, '| **orichalcos** | orichalcos | Vật phẩm | Một loại kim loại/quặng đặc biệt tỏa sáng tự nhiên. |\n')
            break
            
    with open(path, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)

def process_relationships():
    path = 'context/relationships.md'
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    new_lines = []
    seen_rajas = False
    for line in lines:
        if '| **Rajas** | **Lefille / Suimei** |' in line:
            if not seen_rajas:
                seen_rajas = True
                new_lines.append(line)
            continue
        new_lines.append(line)

    with open(path, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)

process_glossary()
process_relationships()
print('Context updated')
