from stats import num_word_count, count_num_characters, sort_character_count
from count_text import count_to_num_as_text
import sys

number_text = ""

try:
    input_num = int(sys.argv[1])

    try:
        number_text = count_to_num_as_text(input_num)
    except ValueError:
        print("The number is too large for this program to handle. Please choose a number less than or equal to 1000000.")
        sys.exit(1)
except ValueError:
    print("Please provide a valid integer as an argument.")
    sys.exit(1)
except Exception as e:
    print("Usage: python3 main.py <integer>")
    sys.exit(1)

def main():
    characters_used = count_num_characters(number_text)

    print("============ NUMBOT ============")
    print("----------- Word Count ----------")
    print(f"Found {num_word_count(number_text)} total words")
    print("--------- Character Count -------")
    for dictionary in sort_character_count(characters_used):
        if dictionary["name"].isalpha() == True:
            print(f"{dictionary["name"]}: {dictionary["num"]}")
    print("============= END ===============")


main()
