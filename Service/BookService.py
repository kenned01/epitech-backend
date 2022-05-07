from Util.db import DataBase
from Repository.bookRepository import *


class BookService:
    __db = None
    __con = None
    __cursor = None

    def __getCon(self):
        self.__db = DataBase()
        self.__con = self.__db.connectionPool.getconn()
        self.__cursor = self.__con.cursor()

    def __putCon(self):
        self.__cursor.close()
        self.__db.connectionPool.putconn(self.__con)

    def getOne(self, book_id):
        self.__getCon()
        book = getOneBook(book_id, self.__cursor)
        self.__putCon()

        if book is None:
            return {
                "data": "Book not found",
                "status": 404
            }

        return {
            "data": book,
            "status": 200
        }

    def getAll(self):
        self.__getCon()
        books = getAllBooks(self.__cursor)
        self.__putCon()
        return {
            "data": books,
            "status": 200
        }

    def create(self, title, description, author):
        self.__getCon()
        book = createBook(self.__cursor,self.__con, title, description, author)
        self.__putCon()

        if book is None:
            return {
                "data": "",
                "status": 500
            }

        return {
            "data": book,
            "status": 200
        }

    def update(self, title, description, author, book_id):
        self.__getCon()
        book = updateBook(self.__cursor, self.__con, title, description, author, book_id)
        self.__putCon()

        if book is None:
            return {
                "data": "Book update",
                "status": 200
            }

        return {
            "data": "",
            "status": 500
        }

    def delete(self, book_id):
        self.__getCon()
        book = deleteBook(self.__cursor, self.__con, book_id)
        self.__putCon()

        if book is None:
            return {
                "data": "Book deleted",
                "status": 200
            }

        return {
            "data": "",
            "status": 500
        }
