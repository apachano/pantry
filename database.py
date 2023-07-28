import psycopg2

def get_connection():
    # Connect to your postgres DB
    conn = psycopg2.connect(host="postgres", dbname="postgres", user="postgres", password="salamander")

    # Open a cursor to perform database operations
    cur = conn.cursor()

    cur.execute("""
                CREATE TABLE IF NOT EXISTS pantry_items (
                id SERIAL PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                description TEXT,
                expiration TIMESTAMP,
                created TIMESTAMP,
                austin_eat BOOL,
                done BOOL);
                """)

    return cur