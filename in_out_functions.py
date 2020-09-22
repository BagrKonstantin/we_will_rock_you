import sqlite3


def update_total_amount(detail, amount, cur): #если идёт списание деталей, то передавать с минусом
    cur.execute("""update details set amount = amount + ? where title = ?""", (detail, amount))