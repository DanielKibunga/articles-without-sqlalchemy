from lib.db.connection import CONN, CURSOR

def setup_database():
    with open("lib/db/schema.sql") as f:
        sql = f.read()
        CURSOR.executescript(sql)
        CONN.commit()
        print("✅ Database setup complete!")

if __name__ == "__main__":
    setup_database()
