import psycopg2
conn_info = (
    "dbname=pem "
    "user=postgres "
    "password=root "
    "host=localhost "
    "port=5432"
)

try:
    # Connect to the PostgreSQL server
    with psycopg2.connect(conn_info) as conn:
        # Open a cursor to perform database operations
        with conn.cursor() as cur:
            # Execute a simple query
            cur.execute("SELECT version();")
            db_version = cur.fetchone()
            print("Connected to:", db_version[0])

            # Example: Parameterized query (prevents SQL injection)
            cur.execute("SELECT * FROM users")# WHERE id = %s;", (1,))
            user = cur.fetchone()
            print("User:", user)

except psycopg2.OperationalError as e:
    print(f"Connection failed: {e}")
