from pymongo import MongoClient
import logging


class Database:

    MONGODB_ATLAS_URI = "mongodb+srv://smarthome.aqnjrxz.mongodb.net/?authSource=%24external&authMechanism=MONGODB-X509&retryWrites=true&w=majority"
    MONGODB_CERT_PATH = "../Resources/X509-cert-2696376426828117784.pem"

    MIN_PASSWORD_LENGTH = 3
    MAX_PASSWORD_LENGTH = 50

    def __int__(self):
        self.mongodb_client = MongoClient(Database.MONGODB_ATLAS_URI, tls=True, tlsCertificateKeyFile=Database.MONGODB_CERT_PATH)
        self.smart_home_database = self.mongodb_client["SmartHome"]
        self.users_table = self.smart_home_database["Users"]

    def get_user_secret(self, username: str, password: str):
        query_result = self.users_table.find_one({"username": username, "password": password})
        return query_result["_id"]

    def add_user(self, username: str, password: str):
        self.check_password_strength(password)
        self.check_user_and_password_exists(username, password)
        query_result = self.users_table.insert_one({"username": username, "password": password})
        logging.debug("user created")

    @staticmethod
    def check_password_strength(password: str):
        # TODO: make the check better
        # TODO: create custom exception
        if not password\
            or password == ""\
            or not (Database.MAX_PASSWORD_LENGTH > len(password) > Database.MIN_PASSWORD_LENGTH):

            raise Exception("invalid password")

    def check_user_and_password_exists(self, username: str, password: str):
        query_result = self.users_table.count_documents({"username": username, "password": password})

        if query_result != 0:
            raise Exception("invalid password")


