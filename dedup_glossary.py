import re
import io

def deduplicate_glossary(filepath):
    with io.open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    lines = content.split('\n')
    seen = set()
    new_lines = []
    
    header_mode = True
    
    for line in lines:
        if line.strip().startswith('|') and 'Thuật ngữ gốc' not in line and '---' not in line:
            parts = [p.strip() for p in line.split('|')]
            if len(parts) >= 3:
                term = parts[1].strip()
                if term:
                    if term.lower() in seen:
                        continue
                    seen.add(term.lower())
        new_lines.append(line)
        
    with io.open(filepath, 'w', encoding='utf-8') as f:
        f.write('\n'.join(new_lines))

deduplicate_glossary(r'D:\workspace\isekai_mahou_wa_okureteru\context\glossary.md')
