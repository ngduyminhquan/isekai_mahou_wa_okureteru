import os

def fix_file(filepath):
    with open(filepath, 'rb') as f:
        raw_data = f.read()

    text = raw_data.decode('utf-8')
    fixed_bytes = bytearray()
    i = 0
    while i < len(text):
        c = text[i]
        try:
            b = c.encode('cp1252')
            fixed_bytes.extend(b)
        except Exception:
            fixed_bytes.extend(c.encode('utf-8'))
        i += 1

    try:
        final_text = fixed_bytes.decode('utf-8')
        with open(filepath + '_fixed.md', 'w', encoding='utf-8') as f2:
            f2.write(final_text)
        print('SUCCESS')
    except Exception as e:
        print('Decode error:', e)

if __name__ == '__main__':
    fix_file('context/characters.md')
