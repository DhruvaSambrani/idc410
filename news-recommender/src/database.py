import sqlite3
import numpy as np
import io

CONN = None

def get_cursor():
    global CONN
    if CONN is None:
        def adapt_array(arr):
            print("====================")
            out = io.BytesIO()
            np.save(out, arr)
            out.seek(0)
            return sqlite3.Binary(out.read())
        def convert_array(text):
            print("********************")
            out = io.BytesIO(text)
            out.seek(0)
            return np.load(out)
        sqlite3.register_adapter(np.ndarray, adapt_array)
        sqlite3.register_converter("array", convert_array)

        CONN = sqlite3.connect("news-recommender.db", detect_types=sqlite3.PARSE_DECLTYPES)
    return CONN.cursor()

def commit():
    global CONN
    if CONN is not None:
        CONN.commit()

def insert_into(tblname, keys, values):
    cur = get_cursor()
    try:
        pld = "(" + ", ".join(["?" for _ in keys]) + ")"
        cur.execute(f"""INSERT INTO {tblname} {keys} VALUES {pld}""", values)
        cur.close()
        commit()
        return True
    except e:
        print(e)
        return False

def exec_select(query, vals):
    cur = get_cursor()
    return cur.execute(query, vals).fetchall()
    

