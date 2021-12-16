import json


def main():
    with open('books.json', 'r') as books_file:
        books = json.load(books_file)

    for i, book in enumerate(books):
        del book['imageLink']
        book['id'] = i + 1
        book['reviews'] = []

    with open('books.json', 'w') as books_file:
        json.dump(books, books_file)


if __name__ == '__main__':
    main()
