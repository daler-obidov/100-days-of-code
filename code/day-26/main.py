
import pandas

data = pandas.read_csv('/home/daler/code/100-days-of-code/code/day-26/nato_phonetic_alphabet.csv')

phonetic_dic = {row.letter: row.code for (index, row) in data.iterrows()}

word = input("Enter a word: ").upper()
list = [phonetic_dic[letter] for letter in word]
print(list)