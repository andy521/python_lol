#!/usr/bin/python
# -*- coding=utf-8 -*-
from functools import wraps
from flask import Flask, jsonify , make_response
import urllib2
import json
import time

# 解决unicode错误
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
# ------- cors --------
def allow_cross_domain(fun):
    @wraps(fun)
    def wrapper_fun(*args, **kwargs):
        rst = make_response(fun(*args, **kwargs))
        rst.headers['Access-Control-Allow-Origin'] = '*'
        rst.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'
        allow_headers = "Referer,Accept,Origin,User-Agent"
        rst.headers['Access-Control-Allow-Headers'] = allow_headers
        return rst
    return wrapper_fun


# ------- methods -------
def get_user_list_by_summoner_name(summoner):
    request_url = 'http://api.lolbox.duowan.com/api/v2/player/search/?player_name_list=%s&callback=jQuery111200161216930093' \
          '95033_1470488155157&_=%s' % ( summoner , get_time_stamp() )
    return get_requst(request_url)

def get_detail_by_user_id(area,id):
    path = area + "/" + id
    request_url = "http://api.lolbox.duowan.com/api/v3/player/%s/?callback=jQuery111101163928349854364_1489317803513&_=%s" \
    % ( path , get_time_stamp() )
    return get_requst(request_url)


def query_list(area,id):
    request_url = "http://api.lolbox.duowan.com/api/v3/player/%s/%s/game_recent/?callback=jQuery111106418592439849586_1489477834856&_=%s" \
    % ( area , id  , get_time_stamp() )
    return get_requst(request_url)

def get_battle_detail(area,uid,bid):
    request_url = "http://api.lolbox.duowan.com/api/v3/player/%s/%s/game/%s/?callback=jQuery11110940651086145784_1489478249766&_=%s" \
    % ( area , uid , bid , get_time_stamp() )
    return get_requst(request_url)

# ------ common -------
def get_requst(url):
    res = urllib2.urlopen(url)
    return res_handler(res)


def get_time_stamp():
    return str(time.time())[0:-3]

def res_handler(res):
    raw = res.read()
    first_char_index = raw.index('(')+1
    return raw[first_char_index:-1]



# ------- server -------
application = Flask(__name__)
@application.route("/")
@allow_cross_domain
def hello():
    return "<h1 style='color:blue'>Hello Summoner!</h1>"

@application.route("/search/<summoner>")
@allow_cross_domain
def search(summoner):
    return get_user_list_by_summoner_name(summoner)

@application.route("/user/detail/<area>/<id>")
@allow_cross_domain
def userDetail(area,id):
    return get_detail_by_user_id(area,id)

@application.route("/battle/list/<area>/<id>")
@allow_cross_domain
def battle_list(area,id):
    return query_list(area,id)


@application.route("/battle/detail/<area>/<uid>/<bid>")
@allow_cross_domain
def battle_detail(area,uid,bid):
    return get_battle_detail(area,uid,bid)


if __name__ == "__main__":
    application.run(host='0.0.0.0')
