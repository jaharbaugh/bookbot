def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
        wcount = word_count(file_contents)
        ccount= char_count(file_contents)
        print_report(wcount,ccount, f)
def print_report(word_counts, char_counts, file):
    print("--- Begin report of books/frankenstein.txt")
    print(f"{word_counts} words found in the document")
    print()
    for key in char_counts:
        print(f"The '{key['char']}' character was found {key['num']} times")
    print("--- End report ---")
def word_count(file_contents):
    words = file_contents.split()
    wcount = len(words) 
    return wcount
def char_count(file_contents):
    alph = {
        'a':0,
        'b':0,
        'c':0,
        'd':0,
        'e':0,
        'f':0,
        'g':0,
        'h':0,
        'i':0,
        'j':0,
        'k':0,
        'l':0,
        'm':0,
        'n':0,
        'o':0,
        'p':0,
        'q':0,
        'r':0,
        's':0,
        't':0,
        'u':0,
        'v':0,
        'w':0,
        'x':0,
        'y':0,
        'z':0,
        ' ':0
    }
    for char in file_contents.lower():
        if char in alph:
            alph[char] += 1

    char_list = []
    for char, count in alph.items():
        if char.isalpha():  # only include letters
            char_list.append({"char": char, "num": count})
    
    char_list.sort(reverse=True, key=sort_on)
    return char_list

def sort_on(dict):
    return dict["num"]
main()