import sqlite3

class KnownNode:
    def __init__(self, addr = None):
        self.addedAt = datetime.datetime.now()
        self.addr = addr

    def __repr__(self):
        return "<{} @={}".format(self.__class__.__name__, self.addr)

    def _addToDatabase(self):
        pass

    @staticmethod
    def getAll():
        """
            Returns all known nodes from database
        """
        return []

class Connection:
    def __init__(self):
        pass