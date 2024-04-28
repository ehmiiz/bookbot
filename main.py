
def main():
    # Set path of book and read it's content
    path_to_file =  "books/frankenstein.txt"
    file_contents = get_book_content(path_to_file)

    # return the words!
    word_count = word_counter(file_contents)
    
    letter_count_dict = get_char_count(file_contents)
    
    print(f"--- Begin report of {path_to_file} ---")
    print(f"{word_count} words found in the document")
    sorted_dict(letter_count_dict)
    print(f"--- End report ---")
    

def get_book_content(path):
    # reads content of a text file
    with open(path) as f:
        return f.read()

def word_counter(input):
    # counts the words in a given book
    words = input.split()
    return len(words)

def get_char_count(input):
    # Returns a dict with character count: a: 250, b: 350 etc
    char_dict = {}
    edited_input = input.lower()
    
    for i in edited_input:
        # for each word in the book
        # check if the word contains a, b, c
            
        if char_dict.get(i):
            char_dict[i] += 1
        else:
            char_dict[i] = 1
    
    return char_dict


def sort_on(dict):
    # accepts a dict, and returns only the value specified
    return dict["num"]

def sorted_dict(input):
    list_of_dicts = []
    for i in input:
        if i.isalpha():
            new_little_dict = {"name": i, "num": input[i]}
            list_of_dicts.append(new_little_dict)

    list_of_dicts.sort(reverse=True, key=sort_on)
    for l in list_of_dicts:
        statement = f"The '{l["name"]}' character was found {l["num"]} times"
        print(statement)
    

main()