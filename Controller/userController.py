from flask import Blueprint, jsonify, request
from Service.UserService import UserService
usersB = Blueprint("user", __name__)


@usersB.route("/admin/login",  methods=['POST'])
def login():
    userService = UserService()
    data = userService.getOne(request.form.get("email"), request.form.get("password"))

    return jsonify(data)
