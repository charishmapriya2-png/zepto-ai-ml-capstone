import sqlite3

def inspect_db(db_name):
    print(f"\n--- Inspecting: {db_name} ---")
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    # Get all table names
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    print("Tables found:", [t[0] for t in tables])
    
    # Iterate through tables and print sample contents
    for table in tables:
        table_name = table[0]
        print(f"\nContents of table '{table_name}':")
        try:
            cursor.execute(f"SELECT * FROM {table_name} LIMIT 5;")
            rows = cursor.fetchall()
            for row in rows:
                print(row)
        except Exception as e:
            print(f"Could not read table {table_name}: {e}")
            
    conn.close()

if __name__ == "__main__":
    inspect_db("zepto.db")
    inspect_db("zepto_books.db")