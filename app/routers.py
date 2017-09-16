"""路由系统"""
import pathlib
from app.views import indexHandle,register,testHandle1,testHandle2,registersucc
PROJECT_ROOT = pathlib.Path(__file__).parent.parent
def setup_routes(app):
    app.router.add_get("/",indexHandle)
    app.router.add_get("/test1",testHandle1)
    app.router.add_get("/test2",testHandle2)
    app.router.add_post("/registersucc",registersucc)
    app.router.add_get("/register",register)


    #提供静态资源服务
    app.router.add_static('/static/',
                          path=str(PROJECT_ROOT /'public' / 'static'),
                          name='static')
