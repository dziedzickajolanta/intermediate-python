import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_words = {row.letter:row.code for (index, row) in data.iterrows()}

word = input("Enter a word: ").upper()

letters_of_word = [n for n in word]
result = [phonetic_words[letter] for letter in word]
print(result)