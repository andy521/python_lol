#!/usr/bin/python
# -*- coding=utf-8 -*-


# def app(environ, start_response):
#         data = b"Hello, World!\n"
#         start_response("200 OK", [
#             ("Content-Type", "text/plain"),
#             ("Content-Length", str(len(data)))
#         ])
#         return iter([data])


from flask import Flask, jsonify
import urllib2
import json
# 解决unicode错误
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


# ------- methods -------
def get_user_list_by_summoner_name(summoner):
    request_url = 'http://api.lolbox.duowan.com/api/v2/player/search/?player_name_list=%s&callback=jQuery111200161216930093' \
          '95033_1470488155157&_=1470488155158' % summoner
    res = urllib2.urlopen(request_url)
    return res_handler(res);


def get_detail_by_user_id(id):
    request_url = "http://api.lolbox.duowan.com/api/v3/player/dx1/%s/?callback=jQuery111101163928349854364_1489317803513&_=1489317803514" \
    % id
    res = urllib2.urlopen(request_url)
    return res_handler(res);

def res_handler(res):
    raw = res.read()
    first_char_index = raw.index('(')+1
    return raw[first_char_index:-1]


# ------- server -------
application = Flask(__name__)
@application.route("/")
def hello():
    return "<h1 style='color:blue'>Hello Summoner!</h1>"

@application.route("/search/<summoner>")
def search(summoner):
    return get_user_list_by_summoner_name(summoner)

@application.route("/user/detail/<id>")
def userDetail(id):
    return get_detail_by_user_id(id)


if __name__ == "__main__":
    application.run(host='0.0.0.0')
