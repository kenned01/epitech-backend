from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from Service.BookService import BookService
bookB = Blueprint("book", __name__)


@bookB.route("/admin/book/all")
@jwt_required()
def getBooks():
    bookService = BookService()
    data = bookService.getAll()
    return data


@bookB.route("/admin/book/create", methods=['POST'])
@jwt_required()
def createBook():
    bookService = BookService()
    data = bookService.create(
        request.form.get("title"),
        request.form.get("description"),
        request.form.get("author")
    )
    return data


@bookB.route("/admin/book/<int:book_id>")
@jwt_required()
def getBook(book_id):
    bookService = BookService()
    data = bookService.getOne(book_id)
    return data


@bookB.route("/admin/book/<int:book_id>/update", methods=['PUT'])
@jwt_required()
def updateBook(book_id):
    bookService = BookService()
    data = bookService.update(
        request.form.get("title"),
        request.form.get("description"),
        request.form.get("author"),
        book_id
    )
    return data


@bookB.route("/admin/book/<int:book_id>/delete", methods=['DELETE'])
@jwt_required()
def deleteBook(book_id):
    bookService = BookService()
    data = bookService.delete(book_id)
    return data
