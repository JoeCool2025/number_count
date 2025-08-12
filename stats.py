def num_word_count(num_text):
    
    words = num_text.split()

    return len(words)

def count_num_characters(num_text):
    characters = {}

    for char in num_text:
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1

    return characters

def sort_character_count(characters):
    sorted_dictionaries = []

    for key in characters:
        sorted_dictionaries.append({"name": key, "num": characters[key]})
    
    def sort_on(items):
        return items["num"]
    
    sorted_dictionaries.sort(reverse=True, key=sort_on)

    return sorted_dictionaries