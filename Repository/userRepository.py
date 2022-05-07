def findUser(email, password, cursor):

    try:

        query = "SELECT * FROM users WHERE email = %s AND password = %s"
        params = (email, password)

        cursor.execute(query, params)
        user = cursor.fetchone()

        if not cursor.rowcount:
            return None

        return user[0]
    except Exception as err:
        print(err.__str__())
