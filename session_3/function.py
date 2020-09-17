import sqlite3


def get_data(path):
    con = sqlite3.connect(path)
    cur = con.cursor()
    data = cur.execute("""select * from tech_cards""").fetchall()
    return data
