import psycopg2
from sql_queries import create_table_queries, drop_table_queries


def create_database():
    # connect to default database
    conn = psycopg2.connect("host=127.0.0.1 dbname=studentdb user=postgres password=0617")
    conn.set_session(autocommit=True)
    cur = conn.cursor()
    
    # create sparkify database with UTF8 encoding
    cur.execute("DROP DATABASE IF EXISTS sparkifydb")
    cur.execute("CREATE DATABASE sparkifydb WITH ENCODING 'utf8' TEMPLATE template0")

    # close connection to default database
    conn.close()    
    
    # connect to sparkify database
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=postgres password=0617")
    cur = conn.cursor()
    
    return cur, conn


def drop_tables(cur, conn):
    print('-----Start dropping Table-----')
    length = len(drop_table_queries)
    for n,query in enumerate(drop_table_queries):
        print(f'Start dropping Table {n+1}/{length}')
        try:
            cur.execute(query)
            conn.commit()
            print(f'Table {n+1}/{length} dropped successfully')
        except psycopg2.exception as e:
            print(f'Failed to drop table {n+1}/{length}')
            print(e)
            
        


def create_tables(cur, conn):
    print('-----Start Creating Table-----')
    length = len(create_table_queries)
    for n,query in enumerate(create_table_queries):
        print(f'Start creating Table {n+1}/{length}')
        try:
            cur.execute(query)
            conn.commit()
            print(f'Table {n+1}/{length} created successfully')

        except psycopg2.exception as e:
            print(f'Failed to create table {n+1}/{length}')
            print(e)



def main():
    try:
        cur, conn = create_database()
        print("Successfully created database")
    except Exception as e:
        print("Failed to create database")
        print(e)
    
    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()
    
