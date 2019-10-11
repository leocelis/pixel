import os

import MySQLdb


def get_connect():
    db = MySQLdb.connect(host=os.environ.get('DB_HOST'),
                         port=int(os.environ.get('DB_PORT', 3306)),
                         user=os.environ.get('DB_USER'),
                         passwd=os.environ.get('DB_PASSWORD'),
                         db='pixel',
                         connect_timeout=int(10))

    return db


def dictfetchall(cursor):
    """
    Fetch results from MySQL
    """
    desc = cursor.description
    return [dict(zip([col[0] for col in desc], row)) for row in cursor.fetchall()]
