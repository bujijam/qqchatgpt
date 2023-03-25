from flask import Flask, request
from flask_restful import Api, Resource
from gevent import pywsgi
from handlemsg import *
import json

app = Flask(__name__)
api = Api(app)
hm = HandleMsg()

#bot信息
bot_name = json.loads(json.dumps(requests.post(url + '/get_login_info').json()))['data']['nickname']
bot_uid = json.loads(json.dumps(requests.post(url + '/get_login_info').json()))['data']['user_id']

class RecvMsg(Resource):
    def post(self):
        _ = request.json
        mess = ''
        if _.get('message_type') == 'group':
            mess = _['raw_message']
            #被@时进行回应
            if mess.split(' ')[0] == '@'+bot_name or mess.split(' ')[0] == '[CQ:at,qq=%s]'%(bot_uid):
                gid = _['group_id']
                content = mess.split(' ')[1]
                if content == '重置对话':
                    try:
                        chatbot.reset(convo_id=str(gid))
                        send(gid, 'group', '已重置')
                    except:
                        send(gid, 'group', '重置失败')
                else:
                    nickname = _['sender']['nickname']
                    hm.gro_msg(gid, content, '@'+nickname+' ')
api.add_resource(RecvMsg, "/")

if __name__ == '__main__':
    #app.run("0.0.0.0", 5701)
    server = pywsgi.WSGIServer(("0.0.0.0", 5701), app)
    server.serve_forever()