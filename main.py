def main():
    path_to_file = "books/frankenstein.txt"
    file_contents = ""

    with open(path_to_file) as f:
        file_contents = f.read()

    return file_contents

def count_words(text):
    words = text.split()
    return len(words)

def character_counts(text):
    characters = {}

    for char in text:

        if char.lower() in characters:
            characters[char.lower()] += 1
        else:
            characters[char.lower()] = 1
    
    return characters

def character_report(dictionary):
    for key, value in dictionary.items():
        if key.isalpha():
            print(f"the '{key}' character was found {value} times")

print("--- Begin report of books/frankenstein.txt ---")
print (f"{count_words(main())} words found in the document")
print()
character_report(character_counts(main()))