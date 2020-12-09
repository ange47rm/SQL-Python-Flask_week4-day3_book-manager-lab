import repositories.book_repository as book_repository
import repositories.author_repository as author_repository
from models.book import Book
from models.author import Author

book_repository.delete_all()
author_repository.delete_all()

author_1 = Author ('Leo', 'Tolstoy')
author_repository.save (author_1)

author_2 = Author ('William', 'Shakespeare')
author_repository.save (author_2)

book_1 = Book ('War and Peace', 'novel', 'The Russian Messenger', author_1)
book_repository.save (book_1)

book_2 = Book ('The Cambridge Shakespeare', 'collection', 'Cambridge University Press', author_2)
book_repository.save (book_2)