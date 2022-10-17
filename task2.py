def get_count_char(str_):
    str_ = str_.lower()
    char_counts = {}
    for char in str_:
        if char.isalpha():
            char_counts[char] = char_counts.setdefault(char, 0) + 1
    return char_counts


def convert_count_char_to_percent(dict_):
    dict_percent = {}
    char_count = sum(dict_.values())
    for char, count in dict_.items():
        dict_percent[char] = round(count / char_count * 100, 1)
    return dict_percent


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
