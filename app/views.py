from aiohttp import web
import aiohttp_jinja2

'''
返回的形式有：
return web.Response()


'''
async def testHandle1(request):
    """返回字符串"""
    return web.Response(text="HELLO,WORLD!")

async def testHandle2(request):
    """返回格式化字符串"""
    name="xiaoing"
    text="hello,{}".format(name)
    return web.Response(text=name)


async def testHandle3(request):
    """返回json格式的数据"""
    data={"a":"hhh","b":"jjj"}
    return web.json_response(data)

@aiohttp_jinja2.template("index.html")
async def indexHandle(request):
    """返回html页面加模板数据"""
    return {"index":"HAA"}

@aiohttp_jinja2.template('register.html')
async def register(request):
    '''返回注册页面'''
    return {}


async def registersucc(request):
    '''从post请求中取数据'''
    data=await request.post()
    name=data["username"]
    pwd=data["password"]
    text="{},{},successful".format(name,pwd)
    return web.Response(text=text)





'''follow are showed how to use session in aiohttp'''
# import asyncio
# import time
# import base64
# from cryptography import fernet
# from aiohttp import web
# from aiohttp_session import setup, get_session, session_middleware
# from aiohttp_session.cookie_storage import EncryptedCookieStorage
#
# async def handler(request):
#     session = await get_session(request)
#     last_visit = session['last_visit'] if 'last_visit' in session else None
#     text = 'Last visited: {}'.format(last_visit)
#     return web.Response(text=text)
#
# def make_app():
#     app = web.Application()
#     # secret_key must be 32 url-safe base64-encoded bytes
#     fernet_key = fernet.Fernet.generate_key()
#     secret_key = base64.urlsafe_b64decode(fernet_key)
#     setup(app, EncryptedCookieStorage(secret_key))
#     app.router.add_route('GET', '/', handler)
#     return app
#
# web.run_app(make_app())
#
