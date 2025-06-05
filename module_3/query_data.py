import psycopg2

# Update these values with your actual PostgreSQL info
conn = psycopg2.connect(
    host="localhost",      # or your server address
    database="your_db_name",  # your database name
    user="your_username",     # your PostgreSQL username
    password="your_password"  # your PostgreSQL password
)

cur = conn.cursor()
cur.execute("SELECT version();")
version = cur.fetchone()
print("PostgreSQL version:", version)
cur.close()
conn.close()