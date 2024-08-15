

HOLDER = "[name]"

with open("./Input/names/invited_.txt") as names_file:
    names = names_file.readlines()
with open("./Input/letters/starting_letter.txt") as letter_file:
    letters = letter_file.read()
    for name in names:
        stripped = name.strip()
        new_letter = letters.replace(HOLDER, stripped)
        with open(f"./output/letter_for_{stripped}.docx", "w") as completed_letter:
            completed_letter.write(new_letter)


