import psycopg2
# Establish a connection to the PostgreSQL database using "with"
with psycopg2.connect(
    dbname="TestDatabase", user="postgres", password="M_Toha444202", host="localhost", port="5432"
) as conn:
    # Create a cursor object to interact with the database
    with conn.cursor() as cur:
        # Execute SQL queries
        # sql = "SELECT * FROM your_table_name"
        sql = '''CREATE TABLE your_table_name (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    email VARCHAR(100)
);   '''
        cur.execute(sql)
        # rows = cur.fetchall()

        # Print the results
        # for row in rows:
        #    print(row)

