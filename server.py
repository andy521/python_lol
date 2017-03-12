#!/usr/bin/python
# -*- coding=utf-8 -*-


# def app(environ, start_response):
#         data = b"Hello, World!\n"
#         start_response("200 OK", [
#             ("Content-Type", "text/plain"),
#             ("Content-Length", str(len(data)))
#         ])
#         return iter([data])


from flask import Flask
import urllib2

# 解决unicode错误
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


# ------- methods -------
def getUserListBySummonerName(summoner):
    requestUrl = 'http://api.lolbox.duowan.com/api/v2/player/search/?player_name_list=%s&callback=jQuery111200161216930093' \
          '95033_1470488155157&_=1470488155158' % summoner
    res = urllib2.urlopen(requestUrl)
    html = res.read()[44:-1]
    return html

# ------- server -------
application = Flask(__name__)
@application.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"

@application.route("/search/<summoner>")
def search(summoner):
    return getUserListBySummonerName(summoner)

if __name__ == "__main__":
    application.run(host='0.0.0.0')
