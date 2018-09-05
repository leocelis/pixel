import MySQLdb


def get_connect():
    db = MySQLdb.connect(host='localhost',
                         port=int(3306),
                         user='root',
                         passwd='root',
                         db='pixel',
                         connect_timeout=int(10))

    return db


def dictfetchall(cursor):
    """
    Fetch results from MySQL
    """
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
        ]
