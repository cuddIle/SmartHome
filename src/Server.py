from ClientsManager import ClientsManager
from Database import Database
from Parser import Parser

from flask import Flask, request


class Server:
    def __init__(self):
        self.clients_manager = ClientsManager()
        self.database = Database()
        self.parser = Parser()

        self.flask_server = Flask(__name__)
        self.flask_server.add_url_rule("/login", view_func=self.login)
        self.flask_server.add_url_rule("/signup", view_func=self.signup)

    def login(self):
        return "logged in " + request.data

    def signup(self):
        return "signed up " + request.data


    def run(self):
        self.flask_server.run()



