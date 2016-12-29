#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Flask, make_response, redirect, abort, current_app, session
import pickle

# current_app = LocalProxy(_find_app)
# request = LocalProxy(partial(_lookup_req_object, 'request'))
# session = LocalProxy(partial(_lookup_req_object, 'session'))
# g = LocalProxy(partial(_lookup_app_object, 'g'))
app = Flask(__name__)

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'


class device():
    def __init__(self, ip):
        self.ip = ip

    def printip(self):
        return "device ip:%s" % self.ip


@app.route("/<string:ip>")
def encode(ip):
    if ip in session:
        print '这个 ip 已经在session'
        dev = pickle.loads(session[ip])
        print dev.printip()
        return "存在"
    else:
        print 'session中没有,需要存进去'
        dev = device(ip)
        session[ip] = pickle.dumps(dev)
        return "不存在"


if __name__ == "__main__":
    app.run(debug=True)
