def get_dict_file_line(file_name_list):
    dict_lines = {}
    for file_name in file_name_list:
        list_lines = []
        with open(file_name, encoding='utf-8') as file:
            while True:
                line = file.readline().strip()
                if not line:
                    break
                else:
                    list_lines.append(line)
        dict_lines[file_name] = list_lines
    return dict_lines
dict_lines = get_dict_file_line(["1.txt", "2.txt", "3.txt"])
def get_final_file(dict=dict_lines):
    dict_len = {}
    for name, value in dict.items():
        dict_len[len(value)] = name
    for count in sorted(dict_len):
        with open('final_file.txt', 'a', encoding='utf-8') as ffile:
            ffile.write(f'{str(dict_len[count])}\n')
            ffile.write(f'{str(count)}\n')
            list_str = dict[dict_len[count]]
            for line in list_str:
                ffile.write(f'{line}\n')
get_final_file()
