

def text_analise(file_n, letter, title=''):
    """
    function for counting percents of simbols by some text/
    after counting follows writing datas in 3.txt
    """
    dict_percent = {}
    other_signs2 = {}
    other_signs2_turn = {}

    for i in letter:
        with open(file_n) as f:
            text = f.read()
            count = 0
            count_others = 0
            for ch in text.lower():
                if ch == i:
                    count += 1
                if ch not in letter:
                    count_others += 1
                    other_signs2[ch] = count_others
                    # if ch not in other_signs:
                    #     other_signs.append(ch)
        procent = round((100 * count) / len(text), 2)
        procent_other = round((100 * count_others) / len(text), 2)

        dict_percent[procent] = [i, count]

    x = 0
    for key in sorted(dict_percent):
        print('Percent {} of letter {}'.format(key, dict_percent[key]))
        x += key
        with open('3.txt', 'a') as f:
            f.write(
                'Percent {} of letter {} \n'.format(key, dict_percent[key]))

    other_percents = round((100 - x), 2)
    print('Other: {} percent'.format(other_percents))
    print('ACTUAL Other: {} percent'.format(procent_other))
    print('Length of text: {}\n'.format(len(text)))
    # print(list(set(other_signs)))

    for a, b in other_signs2.items():
        if a != '\n':
            other_signs2_turn[b] = a
        elif a == '\n':
            other_signs2_turn[b] = 'Enter'

    with open('3.txt', 'a') as f:
        f.write('Other: {} percent\n'.format(round((100 - x), 2)))
        f.write('процентов учтено: {}\n'.format(x))
        f.write('Length of text: {}\n'.format(len(text)))
        f.write('Title of text: {}\n\n'.format(title))
        for key in sorted(other_signs2_turn):
            prnt = ('Letter {} used {} times'.format(
                    other_signs2_turn[key], key))
            prnt_wr = prnt + '\n'
            print(prnt)
            f.write(prnt_wr)


filename = '2.txt'
file_w = '3.txt'
title = 'THE DARK TOWER'
# filename = input('text.txt: ')
count2 = 0
letter = 'абвгдеёжзийклмнопрстуфхцчшщьыъэюя '

text_analise(filename, letter, title)

