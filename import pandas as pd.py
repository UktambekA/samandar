import psycopg2

# 📦 PostgreSQL ulanish ma’lumotlari
DB_HOST = "localhost"
DB_NAME = "bp"
DB_USER = "postgres"
DB_PASSWORD = "saman07"
DB_PORT = 5432  # odatiy port

# 🔗 Ulanish
conn = psycopg2.connect(
    host=DB_HOST,
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
    port=DB_PORT
)
conn.autocommit = True
cursor = conn.cursor()

cursor.execute("""
    SELECT * FROM imad;
""")
rows = cursor.fetchall()

# Natijalarni chiqarish
for row in rows:
    print(row)

