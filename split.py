import codecs
with codecs.open('D:/workspace/isekai_mahou_wa_okureteru/translated/vol_3/chapter_4_part_4.md', 'r', 'utf-8') as f:
    lines = f.readlines()

part4_lines = lines[:201]
part5_lines = lines[202:]

part4_content = ''.join(part4_lines) + '\n---\n\n* **Phần trước:** [Chapter 4 - Part 3](../vol_3/chapter_4_part_3.md)\n* **Phần tiếp theo:** [Chapter 4 - Part 5](../vol_3/chapter_4_part_5.md)\n'
part5_content = '# Chapter 4 - Part 5\n\n' + ''.join(part5_lines) + '\n---\n\n* **Phần trước:** [Chapter 4 - Part 4](../vol_3/chapter_4_part_4.md)\n* **Phần tiếp theo:** [Chapter 4 - Part 6](../vol_3/chapter_4_part_6.md)\n'

with codecs.open('D:/workspace/isekai_mahou_wa_okureteru/translated/vol_3/chapter_4_part_4.md', 'w', 'utf-8') as f:
    f.write(part4_content)

with codecs.open('D:/workspace/isekai_mahou_wa_okureteru/translated/vol_3/chapter_4_part_5.md', 'w', 'utf-8') as f:
    f.write(part5_content)

print('Split successful')
