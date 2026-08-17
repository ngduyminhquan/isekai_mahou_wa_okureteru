import io
import re
import os

def clean_markdown_table(filepath):
    with io.open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    lines = content.split('\n')
    new_lines = []
    
    # Common Vietnamese typo fixes
    replacements = {
        "  ": " ",
        " ,": ",",
        " .": ".",
        " ?": "?",
        " !": "!",
        " :": ":",
    }
    
    for line in lines:
        if line.strip().startswith('|'):
            # It's a table row, let's fix spacing inside cells
            parts = line.split('|')
            cleaned_parts = []
            for part in parts:
                p = part.strip()
                for k, v in replacements.items():
                    p = p.replace(k, v)
                cleaned_parts.append(p)
            new_line = '| ' + ' | '.join(cleaned_parts)[1:-1].strip() + ' |'
            if line.strip().startswith('| ---'):
                new_line = line # keep header separator as is
            new_lines.append(new_line)
        else:
            for k, v in replacements.items():
                line = line.replace(k, v)
            new_lines.append(line)
            
    with io.open(filepath, 'w', encoding='utf-8') as f:
        f.write('\n'.join(new_lines))

files_to_clean = [
    r'D:\workspace\isekai_mahou_wa_okureteru\context\glossary.md',
    r'D:\workspace\isekai_mahou_wa_okureteru\context\characters.md',
    r'D:\workspace\isekai_mahou_wa_okureteru\context\relationships.md'
]

for f in files_to_clean:
    if os.path.exists(f):
        clean_markdown_table(f)
        print(f"Cleaned {f}")
