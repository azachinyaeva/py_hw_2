import codecs

file_list = ['1.txt', '2.txt', '3.txt']

output_file = 'result.txt'

with codecs.open(output_file, 'w', encoding='utf-8') as outfile:
    file_strings = []
    file_info = []
    for file_name in file_list:
        str_count = 0
        with open(file_name, 'r', encoding='utf-8') as infile:
            content = infile.readlines()
            count_line = str(len(content))
            file_strings.append(["\n" + file_name + "\n"] + [count_line + "\n"] + content)
    final_text = "".join(sum((sorted(file_strings, key=len)), []))
    outfile.write(final_text)

