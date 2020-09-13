import sqlite3


def get_data():
    con = sqlite3.connect("../nti_base.db")
    cur = con.cursor()
    data = cur.execute("""select * from tech_cards""").fetchall()
    return data
