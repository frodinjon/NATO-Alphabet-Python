import pandas as pd

student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

student_data_frame = pd.DataFrame(student_dict)

df = pd.read_csv("nato_phonetic_alphabet.csv")

phonetic_letters = {row.letter:row.code for (index, row) in df.iterrows()}

def generate_phonetic():
	word = input("Enter a word: ").upper()
	try:
		phonetic_word = [phonetic_letters[letter] for letter in word]
	except KeyError:
		print("Sorry, only letters in the alphabet please.")
		generate_phonetic()
	else:
		print(phonetic_word)


generate_phonetic()