#!/usr/bin/python
import psycopg2
import csv
# import pandas
try:
    conn = psycopg2.connect(
        host="localhost",
        database="spmpambilan",
        user="postgres",
        password="password")

    # create a cursor
    cur = conn.cursor()

    # execute a statement
    # print('PostgreSQL database version:')
    # cur.execute('SELECT version()')

    # display the PostgreSQL database server version
    # db_version = cur.fetchone()
    # print(db_version)

    # file = open('Sekolah_Lookup.csv')
    # csvreader = csv.reader(file)
    # header = []
    # header = next(csvreader)
    # header

    with open('Sekolah_Lookup.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        csv_data = {row['school_code'] for row in reader}
    print(csv_data)

    #

    # col_list = ['school_code', 'name', 'type', 'phone', 'address', 'postcode', 'state', 'city', 'ppd', 'location', 'integration']
    # df = pandas.read_csv("Sekolah_Lookup.csv", usecols=col_list)
    # print(df["school_code"])
    # close the communication with the PostgreSQL
    cur.close()
except (Exception, psycopg2.Error) as error:
    print("Error while fetching data from PostgreSQL", error)

finally:
    # closing database connection.
    if conn:
        cur.close()
        conn.close()
        print("PostgreSQL connection is closed")