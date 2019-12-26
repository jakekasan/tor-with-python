from collections import namedtuple

SQLTable = namedtuple("SQLTable", [
    "name",
    "schema"
])

db_path = "data.db"

schema_strings = [
    (
        "known_nodes",
        [
            ("addr","text"),
            ("pub_key","text"),
            ("date_added","text")
        ]
    ),
    (
        "node_pings",
        [
            ("addr","text"),
            ("pinged_at","text"),
            ("responded_at","text")
        ]
    )
]

schema_dict = {
    "known_nodes":[
        ("addr","text"),
        ("pub_key","text"),
        ("date_added","text")
    ],
    "node_pings":[
        ("addr","text"),
        ("pinged_at","text"),
        ("responded_at","text")
    ]
}

class DBConfig:
    path = "data.db"
    schemas = [
        SQLTable(name, schema)
        for name,schema in schema_strings
    ]
    tables = {
        name: SQLTable(name, schema) for name, schema in schema_dict.keys()
    }

string_to_datetime_format = "%Y-%m-%d %H-%M-%S"

