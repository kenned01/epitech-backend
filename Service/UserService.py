import hashlib
from Repository.userRepository import findUser
from Util.db import DataBase
from flask_jwt_extended import create_access_token


class UserService:

    def getOne(self, email, password):
        try:
            db = DataBase()
            con = db.connectionPool.getconn()
            cursor = con.cursor()

            pwd = hashlib.md5(str(password).encode('utf-8')).hexdigest()
            user = findUser(email, pwd, cursor)

            cursor.close()
            db.connectionPool.putconn(con)

            if user is None:
                return {
                    "data": "user not found",
                    "status": 404
                }

            token = create_access_token(identity=user)

            return {
                "data": token,
                "status": 200
            }

        except Exception as error:
            print(error.__str__())
