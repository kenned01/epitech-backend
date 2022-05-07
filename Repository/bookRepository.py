def getOneBook(book_id, cursor):
    query = "SELECT * FROM books WHERE id = %s"
    params = (book_id,)

    cursor.execute(query, params)
    book = cursor.fetchone()

    if not cursor.rowcount:
        return None

    return {
        "id": book[0],
        "title": book[2],
        "description": book[1],
        "author": book[3]
    }


def getAllBooks(cursor):
    query = "SELECT * FROM books"
    cursor.execute(query)
    books = cursor.fetchall()
    data = []

    for book in books:
        data.append({
            "id": book[0],
            "title": book[2],
            "description": book[1],
            "author": book[3]
        })

    return data


def createBook(cursor, con, title, description, author):
    query = "INSERT INTO books ( description, title, author) VALUES (%s, %s, %s) RETURNING id"
    params = (description, title, author)

    cursor.execute(query, params)
    con.commit()

    book_id = cursor.fetchone()

    if not cursor.rowcount:
        return None

    return {
        "id": book_id[0],
        "title": title,
        "description": description,
        "author": author
    }


def updateBook(cursor, con, title, description, author, book_id):
    query = "UPDATE books SET description = %s, title = %s, author = %s WHERE id = %s"
    params = (description, title, author, book_id)

    cursor.execute(query, params)
    con.commit()

    return None


def deleteBook(cursor, con, book_id):
    query = "DELETE FROM books WHERE id = %s"
    params = (book_id, )
    cursor.execute(query, params)
    con.commit()
    return None
