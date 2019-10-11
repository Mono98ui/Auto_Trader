import firebase_admin
import os
from firebase_admin import credentials, firestore


class ServerComm:

    def __init__(self):
        self._cred = credentials.Certificate(os.path.dirname(os.path.abspath(__file__)) + "/ServiceAccountKey.json")
        self._default_app = firebase_admin.initialize_app(self._cred)
        self._db = firestore.client()
        self.db_cars = self._db.collection(u'Cars')

    def create_brands(self, brand_name):
        dic = {'name': brand_name.title()}
        self.db_cars.document(brand_name.title()).set(dic)

    def create_model(self):
        pass
