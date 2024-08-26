
import pandas

data = pandas.read_csv('/home/daler/code/100-days-of-code/code/day-26/nato_phonetic_alphabet.csv')

phonetic_dic = {row.letter: row.code for (index, row) in data.iterrows()}

def generate():
    word = input("Enter a word: ").upper()
    try:
        list = [phonetic_dic[letter] for letter in word]
    except KeyError:
        print('WTF man, go sleep')
        generate()
    else:

        print(list)

generate()