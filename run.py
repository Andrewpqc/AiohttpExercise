import asyncio
import argparse
import logging
import sys
import jinja2
import aiohttp_jinja2
from trafaret_config import commandline
from aiohttp import web
from app.routers import setup_routes
from app.middlewares import setup_middlewares
from app.utils import TRAFARET



def init_app(loop, argv):
    '''初始化程序实例'''
    ap = argparse.ArgumentParser()
    commandline.standard_argparse_options(ap,
        default_config='./app/config.yaml')
    options = ap.parse_args(argv)
    config = commandline.config_from_options(options, TRAFARET)
    #上面的主要是读取配置文件


    app = web.Application(loop=loop) #创建程序实例
    app['config'] = config#将配置文件的内容加载进程序实例

    #提供template服务
    aiohttp_jinja2.setup(app,
        loader=jinja2.FileSystemLoader('../aiohttpLearn/public/templates/'))
    #或者像下面的这样，下面的这种情况需要public目录是一个python包
    # aiohttp_jinja2.setup(app,
    #                      loader=jinja2.PackageLoader('public','templates'))

    # # create connection to the database
    # app.on_startup.append(init_pg)
    # # shutdown db connection on exit
    # app.on_cleanup.append(close_pg)
    # # setup views and routes
    setup_routes(app)#安装路由
    setup_middlewares(app)#安装错误处理的中间件
    return app


def main(argv):
    # init logging
    logging.basicConfig(level=logging.DEBUG)

    loop = asyncio.get_event_loop()

    app = init_app(loop, argv)
    web.run_app(app,host=app['config']['host'],port=app['config']['port'])

if __name__ == '__main__':
    main(sys.argv[1:])


