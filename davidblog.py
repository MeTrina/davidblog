#!/usr/bin/env python2.6
#coding:utf-8

import web
from settings import render_mako
import views

urls = (
        '/', 'views.index',    
        '/entry/(.*)/', 'views.entry',    
        '/category/(.*)/', 'views.category',    
        '/tag/(.*)/', 'views.tag',    
        '/add_comment/', 'views.addComment',    
        '^/rss.xml$', 'views.rss',
    )

app = web.application(urls, globals(), autoreload = True)
session = web.session.Session(app, web.session.DiskStore('sessions'), initializer={'captcha': 0})

render = render_mako(
        directories = ['/home/icefox/flyingeagle/davidblog/templates'],
        input_encoding = 'utf-8',
        output_encoding = 'utf-8',
    )

if __name__ == '__main__':
    #web.wsgi.runwsgi = lambda func, addr=None: web.wsgi.runfcgi(func, addr)
    app.run()
