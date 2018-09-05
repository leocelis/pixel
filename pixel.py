import MySQLdb
from flask import request
from flask.ext.restful import Resource
from flask.ext.restful import reqparse
from logger import logger
from mysqlfunc import get_connect
from sqlqueries import SAVE_EVENT_SQL

parser = reqparse.RequestParser()
parser.add_argument('event', type=str)
parser.add_argument('age_group', type=str)
parser.add_argument('user_agent', type=str)
parser.add_argument('ip', type=str)
parser.add_argument('ad_id', type=str)
parser.add_argument('gender', type=str)
parser.add_argument('email', type=str)
parser.add_argument('channel', type=str)
parser.add_argument('client', type=str)
parser.add_argument('device', type=str)


class Pixel(Resource):
    def get(self):
        params = parser.parse_args()
        client = params['client']
        ip = params['ip'] if params['ip'] else request.remote_addr
        user_agent = params['user_agent']
        gender = params['gender']
        email = params['email']
        age_group = params['age_group']
        event_name = params['event']
        ad_id = params['ad_id']
        channel = params['channel']
        device = params['device']

        sql = SAVE_EVENT_SQL.format(
            event_name=event_name,
            client=client,
            value="",
            ip=ip,
            user_agent=user_agent,
            gender=gender,
            email=email,
            age_group=age_group,
            ad_id=ad_id,
            channel=channel,
            device=device).encode('utf-8')

        try:
            conn = get_connect()
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()

        except MySQLdb.OperationalError, e:
            message = "EVENT MISSED: {sql} - ERROR {e}".format(sql=sql, e=e)
            logger.error(message)
        except MySQLdb.ProgrammingError, e:
            message = "EVENT MISSED: {sql} - ERROR {e}".format(sql=sql, e=e)
            logger.error(message)
        finally:
            cursor.close()

        return {"Status": "Success"}
