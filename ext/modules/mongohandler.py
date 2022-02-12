import typing
from pymongo import MongoClient
from urllib.parse import quote_plus
import dotenv
import os

dotenv.load_dotenv()

PASSWORD = quote_plus(os.environ["PASSWORD"])


class Mongo:
    def __init__(self, db: typing.Optional[client.dbname] = None, client: typing.Optional[MongoClient] = None) :
        self.client = client
        self.db = db

    def status(self):
        serverStatusResult = self.db.command("serverStatus")
        return serverStatusResult

    def setup(self):
        self.client = MongoClient(f"mongodb+srv://FD:" + PASSWORD + "@cluster0.fct7e.mongodb.net/")
        self.db = self.client["test"]



if __name__ == "__main__":
    print('hi')