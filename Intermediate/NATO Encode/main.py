import pandas

lst = pandas.read_csv("nato_phonetic_alphabet.csv")
name = input()
name = name.upper()
nato_dict = {row.letter: row.code for (index, row) in lst.iterrows()}

nato_coded = [nato_dict[letter] for letter in name]

print(nato_coded)
