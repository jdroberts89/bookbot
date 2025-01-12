def get_book_data(book):
    with open(book, 'r') as f:
        return f.read()

def word_count(words):
    alpha = {}
    for word in words:
        letters = list(word.lower())
        for letter in letters:
            if letter in alpha:
                alpha[letter] += 1
            else:
                alpha[letter] = 1
    return alpha

def sort_alphabet(alpha):
    return dict(sorted(alpha.items()))


def main():
    book = 'books/frankenstein.txt'
    book_data = get_book_data(book)
    words = book_data.split()
    alphabet = word_count(words)
    sorted_list = sort_alphabet(alphabet)
    newline = '\n'
    print('---Report for {book} ---')
    print(f'{len(words)} words found in {book}')
    for k in sorted_list:
        if k.isalpha():
            print(f'The letter {k} was seen {sorted_list[k]} times in {book}')
    


main()