

def text_analise(file_n, title=''):
    """
    Analising all simbols from text
    """
    other_signs2 = {}
    other_signs2_turn = {}

    with open(file_n) as f:
        text = f.read()
        for ch in text.lower():
            if ch not in other_signs2:
                other_signs2[ch] = 1
            elif ch in other_signs2:
                other_signs2[ch] = other_signs2[ch] + 1

    for a, b in other_signs2.items():
        if a != '\n':
            other_signs2_turn[b] = a
        elif a == '\n':
            other_signs2_turn[b] = 'Ent'

    with open('3.txt', 'a') as f:
        prnt2 = ('Length of text: {}\n'.format(len(text)))
        prnt_wr2 = prnt2 + '\n'
        print(prnt2)
        f.write(prnt_wr2)

        for key in sorted(other_signs2_turn):
            procent_other = round((100 * key) / len(text), 4)
            prnt = ('Letter  -  {}   used   {}   times. Percent  {}'.format(
                    other_signs2_turn[key], key, procent_other))
            prnt_wr = prnt + '\n'
            print(prnt)
            f.write(prnt_wr)


def word_analise(filename):
    signs = ['.', ',', '_', '...', '?', '(', ')', '-']
    count = 0

    with open(filename) as words:
        content_1 = words.read()
        content = content_1.lower()
        # new_removed = content.replace(',', '')
        # for i in content:
        #     if i in signs:
        #         new_removed = content.replace(i, '')

        # print(words)
        # words_set.split(' ')
        # finish_words_set = set(sorted(words_set))
        translation_table = dict.fromkeys(map(ord, '.,_-...&?()\'!:;'), None)
        content = content.translate(translation_table)
        content = sorted(set(content.split()))

    with open('words.txt', 'a') as f:
        for w in content:
            count += 1
            f.write('{} - {}\n'.format(count, w))

filename = '2.txt'
file_w = '3.txt'
title = 'THE DARK TOWER'
# filename = input('text.txt: ')
count2 = 0

# text_analise(filename, title)

word_analise(filename)


"""
короче для удаления знаков пунктуации из строки читаем
http://qaru.site/questions/21810/remove-specific-characters-from-a-string-in-python





"""