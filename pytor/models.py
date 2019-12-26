from datetime import datetime
import sqlite3
import .config

class NodeModel:
    def __init__(self, addr, dateAdded):
        self.addr = addr
        self.date_added = date_added

    @classmethod
    def new(self, addr):
        return NodeModel(addr, datetime.now())

    @classmethod
    def q()

    @classmethod
    def get(addr):
        return self.q()

    @classmethod
    def get_all(self):
        return [
            NodeModel(addr, dt)
            for addr, dt in run_query(
                """select * from {}""",
                config.node_tbl
            )
        ]