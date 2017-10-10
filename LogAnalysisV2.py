#!/usr/bin/python
import psycopg2


def Quest1():
    """ Udacity FSND Log Analysis task question #1 """
    conn = None
    try:
        # connect to the PostgreSQL server
        conn = psycopg2.connect("dbname=news")

        cur = conn.cursor()
        sql = ('select a.title as Title, count(l.id) as ArticleCount '
               'from articles as a inner join log as l '
               'on a.slug = substring(l.path from 10 '
               'for char_length(l.path)) '
               'group by a.title '
               'order by count(l.id) desc limit 3')
        print('\n1. What are the most popular three articles of all time?\n')
        cur.execute(sql)
        row = cur.fetchone()

        while row is not None:
            print row[0], '-', row[1], ' views'
            row = cur.fetchone()

    # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def Quest2():
    """ Udacity FSND Log Analysis task question #2 """
    conn = None
    try:
        # connect to the PostgreSQL server
        conn = psycopg2.connect("dbname=news")

        cur = conn.cursor()
        sql = ('select c.name, count(l.id) as articlecount '
               'from articles as a inner join authors as c '
               'on c.id = a.author '
               'inner join log as l '
               'on a.slug = substring(l.path from 10 '
               ' for char_length(l.path)) group by c.name '
               'order by count(l.id) desc')
        print('\n2. Who are the most popular article authors of all time?\n ')
        cur.execute(sql)
        row = cur.fetchone()

        while row is not None:
            print row[0], '-', row[1], ' views'
            row = cur.fetchone()

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def Quest3():
    """ Udacity FSND Log Analysis task question #3 """
    conn = None
    try:
        # connect to the PostgreSQL server
        conn = psycopg2.connect("dbname=news")

        cur = conn.cursor()
        sql = ('select logdate as D1, cast(round(perc_failed::numeric, 1) '
               ' as numeric) as P1 from log_percent_failed '
               ' where perc_failed > 1.0')
        print('\n3. On which days did more than 1% of'
              ' requests lead to errors? \n ')
        cur.execute(sql)
        row = cur.fetchone()

        print row[0], '-', row[1], '% errors'
        print('\n')
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    Quest1()
    Quest2()
    Quest3()
