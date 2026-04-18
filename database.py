import sqlite3

DB_NAME = "malware_hashes.db"


def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS hashes (
            hash TEXT PRIMARY KEY
        )
    """)

    conn.commit()
    conn.close()


def add_hash(file_hash):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO hashes (hash) VALUES (?)", (file_hash,))
        conn.commit()
        print("Хэш добавлен в базу")
    except sqlite3.IntegrityError:
        print("Хэш уже существует в базе")

    conn.close()


def check_local_db(file_hash):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT hash FROM hashes WHERE hash=?", (file_hash,))
    result = cursor.fetchone()

    conn.close()
    return result is not None


def get_all_hashes():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT hash FROM hashes")
    results = cursor.fetchall()

    conn.close()
    return results