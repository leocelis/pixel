import MySQLdb
from flask import request
from flask_restful import Resource
from flask_restful import reqparse

from logger import logger
from mysqlfunc import get_connect
from sqlqueries import SAVE_EVENT_SQL

parser = reqparse.RequestParser()
parser.add_argument('ad_id', type=str)
parser.add_argument('event_name', type=str)
parser.add_argument('value', type=str)


class Pixel(Resource):
    def get(self):
        params = parser.parse_args()

        ad_id = params['ad_id']
        event_name = params['event_name']
        value = params['value']
        user_agent = request.headers.get('User-Agent')
        referrer = request.headers.get("Referer")
        ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)

        sql = SAVE_EVENT_SQL.format(
            ad_id=ad_id,
            event_name=event_name,
            value=value,
            ip=ip,
            user_agent=user_agent,
            referrer=referrer).encode('utf-8')

        try:
            conn = get_connect()
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()

        except MySQLdb.OperationalError as e:
            message = "EVENT MISSED: {sql} - ERROR {e}".format(sql=sql, e=e)
            logger.error(message)
        except MySQLdb.ProgrammingError as e:
            message = "EVENT MISSED: {sql} - ERROR {e}".format(sql=sql, e=e)
            logger.error(message)
        finally:
            cursor.close()

        return {"Status": "Success"}
