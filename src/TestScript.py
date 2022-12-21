import requests as req
from pymongo import MongoClient


# r = req.get(url='http://127.0.0.1:5000', data="aaa")

# print(r.text)

MONGODB_ATLAS_URI = "mongodb+srv://smarthome.aqnjrxz.mongodb.net/?authSource=%24external&authMechanism=MONGODB-X509&retryWrites=true&w=majority"
MONGODB_CERT_PATH = "Resources/X509-cert-2696376426828117784.pem"

mongodb_client = MongoClient(
                            MONGODB_ATLAS_URI,
                            tls=True,
                            tlsCertificateKeyFile=MONGODB_CERT_PATH
                            )

db = mongodb_client['SmartHome']
collection = db["Users"]
mydict = {"name": "shay", "password": "1234"}
a = collection.find_one(mydict)
print(a["_id"])






