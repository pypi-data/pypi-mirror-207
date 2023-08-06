#星尘协议之信使
#stat和msg变量用于控制_thread控制的异步
#wsStat和wsMsg用于控制asyncio控制的异步
#workModuel是当前运行的模块；menu菜单也是一个模块，属于基础模块
#shipei记录的是调用的那种适配类
#output函数用于同时向网页和单色屏显示内容
#由于windows没有单色屏，用print模拟，可以再控制台预览输出
class starMessager:
    def __init__(self):
        self.stat = "waiting"
        self.msg = ""
        try:
            from . import wa
        except:
            from wadapter import wa
        self.workModule = None
        self.wsStat = "waiting"
        self.wsMsg = ""
        self.closedWs = []
        self.shipei = wa
        self.allServers = []
    def output(self,str):
        if sm.shipei.name == 'win':
            print("{}\n{}\n{}".format("-"*20,str,"-"*20))
        self.wsStat = "screen"
        self.shipei.DrawStdLines(str)
        self.wsMsg = str
    def startServers(self):
        for func in self.allServers:
            func()
        
sm = starMessager()



#基于线程的输入输出控制
if sm.shipei.name == 'zkb':
    from mpython import *
    def inputP(_):
        sm.workModule.InputKey("P")
    def inputY(_):
        sm.workModule.InputKey("Y")
    def inputT(_):
        sm.workModule.InputKey("T")
    def inputH(_):
        sm.workModule.InputKey("H")
    def inputO(_):
        sm.workModule.InputKey("O")
    def inputN(_):
        sm.workModule.InputKey("N")
    def inputA(_):
        sm.workModule.InputKey("A")
    def inputB(_):
        sm.workModule.InputKey("B")
    def zkbControl():
        touchpad_p.event_pressed = inputP
        touchpad_y.event_pressed = inputY
        touchpad_t.event_pressed = inputT
        touchpad_h.event_pressed = inputH
        touchpad_o.event_pressed = inputO
        touchpad_n.event_pressed = inputN
        button_a.event_pressed = inputA
        button_b.event_pressed = inputB
    sm.allServers.append(zkbControl)

if sm.shipei.name == 'mwu':
    from m5stack import btnA,btnB,btnC
    from m5stack_ui import M5Btn,FONT_UNICODE_24
    def inputA():
        sm.workModule.InputKey("U")
    def inputB():
        sm.workModule.InputKey("D")
    def inputC():
        sm.workModule.InputKey("B")
    def inputD():
        sm.workModule.InputKey("L")
    def mwuControl():
        btnWidth = 60
        btnHeight = 40
        btnY = 186
        touch_button0 = M5Btn(
            text='↑', x=30, y=btnY, w=btnWidth, h=btnHeight, bg_c=0xbfffc9, 
            text_c=0x1a09c0, font=FONT_UNICODE_24, parent=None)
        touch_button1 = M5Btn(
            text='↓', x=125, y=btnY, w=btnWidth, h=btnHeight, bg_c=0xbfffc9, 
            text_c=0x1a09c0, font=FONT_UNICODE_24, parent=None)
        touch_button2 = M5Btn(
            text='进入', x=220, y=btnY, w=btnWidth, h=btnHeight, bg_c=0xbfffc9, 
            text_c=0x1a09c0, font=FONT_UNICODE_24, parent=None)
        touch_button3 = M5Btn(
            text='返回', x=247, y=20, w=btnWidth, h=btnHeight, bg_c=0xbfffc9, 
            text_c=0x1a09c0, font=FONT_UNICODE_24, parent=None)
        touch_button0.pressed(inputA)
        touch_button1.pressed(inputB)
        touch_button2.pressed(inputC)
        touch_button3.pressed(inputD)
        btnA.wasPressed(inputA)
        btnB.wasPressed(inputB)
        btnC.wasPressed(inputC)
    sm.allServers.append(mwuControl)

if sm.shipei.name == 'wlb':
    def wlbKey(_):
        from future import sensor
        while True:
            sm.shipei.Sleep(0.2)
            if sensor.btnValue("a"):
                sm.workModule.InputKey("A")
            elif sensor.btnValue("b"):
                sm.workModule.InputKey("B")
    def wlbControl():
        import _thread as th
        th.start_new_thread(wlbKey,(None,))
    sm.allServers.append(wlbControl)

########## ws服务器实体  ################
class webConfig():
    def __init__(self):
        self.wsPort = '8525'
        self.httpPort = '8081'
        import os
        self.webPath = os.path.join(os.path.dirname(__file__),'stardevice')
        self.bdzPath = '/sdcard/qpython/projects3/WalArtMinS/gTixi/stardevice'
webConf = webConfig()

if not sm.shipei.name in ['zkb','wlb']:
    import asyncio
    import websockets
    import json

    def d2j(dict):
        return json.dumps(dict,ensure_ascii=False)

    ScreenSize = (240,120)
    alllink = []
    async def sendscreen(svgContent):
        from . import SvgScreen
        try:
            for ws in alllink:
                try:
                    await ws.send(d2j({"type":"screen","msg":SvgScreen(ScreenSize).DrawStdLines(svgContent)}))
                except:
                    sm.closedWs.append(id(ws))
            return True
        except:
            print("Connection Closed...")
            return False

    if sm.shipei.name == 'smp':
        def hardIn():
            while True:
                inputmsg = sm.shipei.CheckKey()
                sm.workModule.InputKey(inputmsg)

        import threading
        hin = threading.Thread(target=hardIn)
        hin.start()

    async def sendKey(websocket):
        while True:
            while sm.stat == "waiting" and id(websocket) not in sm.closedWs:
                await asyncio.sleep(0.05)
            if sm.stat == "key":
                sm.workModule.InputKey(sm.msg)
            sm.stat = "waiting"
            if id(websocket) in sm.closedWs:
                break

    async def webOut(websocket):
        while True:
            while sm.wsStat == "waiting" and id(websocket) not in sm.closedWs:
                await asyncio.sleep(0.05)
            if sm.wsStat == "screen":
                sm.wsStat = "waiting"
                await sendscreen(sm.wsMsg)
            sm.wsStat = "waiting"
            if id(websocket) in sm.closedWs:
                break

    async def webIn(websocket):
        while True:
            try:
                message = await websocket.recv()
            except:
                sm.closedWs.append(id(websocket))
                break
            message = json.loads(message)
            if message['type'] == 'key':
                sm.stat = "key"
                sm.msg = message['msg']

    async def echo(websocket, path):
        alllink.append(websocket)
        from . import SvgScreen
        await websocket.send(d2j({"type":"screen","msg":SvgScreen(ScreenSize).DrawStdLines("欢迎来到星尘演示机\n")}))
        await asyncio.sleep(1)
        sm.workModule.show()
        await asyncio.gather(webIn(websocket),webOut(websocket),sendKey(websocket))
        alllink.remove(websocket)
        sm.closedWs.remove(id(websocket))
        

    loop = None
    def wsStart():
        try:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            loop.run_until_complete(websockets.serve(echo, '0.0.0.0', webConf.wsPort))
            print('Star Socket Server Start!')
            print('---------------------------')
        except Exception as e:
            print("Port {} has been binded to wsServer!".format(webConf.wsPort))
            print(e)

        loop.run_forever()
    def wsStop():
        if loop:
            loop.stop()

    import threading
    wsServer = threading.Thread(target=wsStart)
    class wsCtrl():
        def __init__(self):
            self.loop = loop
            self.t1 = threading.Thread(target=wsStart)
        def stop(self):
            loop.stop()
        def start(self):
            if not self.loop.is_running():
                if self.t1.is_alive():
                    self.t1.join()
                self.t1.start()
                if sm.shipei.name == 'smp':
                    sm.shipei.InitDisplay()
else:
    wsServer = None
    class wsCtrl():
        pass

######### WEBAPP ROUTERS ###############
"""
This is a sample for qpython webapp
"""
if not sm.shipei.name in ['zkb','wlb']:#只有bdz需要自己建立bottle架构的网络服务器
    from bottle import Bottle, ServerAdapter
    from bottle import run, debug, route, error, static_file, template, post

    ######### QPYTHON WEB SERVER ###############

    class MyWSGIRefServer(ServerAdapter):
        server = None

        def run(self, handler):
            from wsgiref.simple_server import make_server, WSGIRequestHandler
            if self.quiet:
                class QuietHandler(WSGIRequestHandler):
                    def log_request(*args, **kw): pass
                self.options['handler_class'] = QuietHandler
            self.server = make_server(self.host, self.port, handler, **self.options)
            self.server.serve_forever()

        def stop(self):
            #sys.stderr.close()
            import threading
            threading.Thread(target=self.server.shutdown).start()
            #self.server.shutdown()
            self.server.server_close() #<--- alternative but causes bad fd exception
            print("# qpyhttpd stop")
    
    def httpSrv():
        ######### BUILT-IN ROUTERS ###############
        @route('/__exit', method=['GET','HEAD'])
        def __exit():
            global server
            server.stop()

        @route('/<filepath:path>')
        def serverstatic(filepath):
            if sm.shipei.name == 'bdz':
                return static_file(filepath, root=webConf.bdzPath)
            else:
                return static_file(filepath,root=webConf.webPath)


        ######### WEBAPP ROUTERS ###############
        @route('/')
        def home():
            if sm.shipei.name == 'bdz':
                return static_file("index.html", root=webConf.bdzPath)
            else:
                return static_file("index.html",root=webConf.webPath)
        @post('/deviceStart')
        def startws():
            wsCtrl().start()
        @post('/deviceStop')
        def stopws():
            wsCtrl().stop()

        app = Bottle()
        app.route('/', method='GET')(home)
        app.route('/__exit', method=['GET','HEAD'])(__exit)
        app.route('/<filepath:path>', method='GET')(serverstatic)
        app.post('/deviceStop',method='POST')(stopws)
        app.post('/deviceStart',method='POST')(startws)
        server = MyWSGIRefServer(host="0.0.0.0", port=webConf.httpPort)
        app.run(server=server,reloader=False)
    import threading
    httpServer = threading.Thread(target=httpSrv)
else:
    httpServer = None

