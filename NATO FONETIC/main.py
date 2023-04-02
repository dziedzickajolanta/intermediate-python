import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_words = {row.letter:row.code for (index, row) in data.iterrows()}

def function():
    word = input("Enter a word: ").upper()
    try:
        result = [phonetic_words[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in alphabet.")
        function()
    else:
        print(result)

function()
