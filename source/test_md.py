# -*- coding: UTF-8 -*-

import threading, signal, sys, os
from ctypes import *;

from ctp.CtpApiStruct import *;
from ctp.CThostFtdcMdSpi import *;
from ctp.CThostFtdcMdApi import *;

class MyMdSpi(CThostFtdcMdSpi):
    def OnFrontConnected(self):
        print('connect successfully.')
        field = CThostFtdcReqUserLoginField()
        field.BrokerID = b'broker888'
        field.UserID = b'user'
        field.Password = b'passwd'
        api.ReqUserLogin(byref(field), 1000)

    def OnFrontDisconnected(self, nReason):
        print('disconnect: ' + str(nReason))

    def OnRspUserLogin(self, pRspUserLogin, pRspInfo, nRequestID, bIsLast):
        print('login successfully.')
        insts = (c_char_p * 3)()
        insts[0] = b'ZC801'
        insts[1] = b'rb1801'
        api.SubscribeMarketData(byref(insts), 2)

    def OnRspSubMarketData(self, pSpecificInstrument, pRspInfo, nRequestID, bIsLast):
        print('subscribe: ' + pSpecificInstrument.contents.InstrumentID.decode())

    def OnRtnDepthMarketData(self, pDepthMarketData):
        print ("%s.%s %s %.2f %.2f %d %.2f %d %d %.2f" %
                    (pDepthMarketData.contents.UpdateTime,
                     pDepthMarketData.contents.UpdateMillisec,
                     pDepthMarketData.contents.InstrumentID,
                     pDepthMarketData.contents.LastPrice,
                     pDepthMarketData.contents.BidPrice1,
                     pDepthMarketData.contents.BidVolume1,
                     pDepthMarketData.contents.AskPrice1,
                     pDepthMarketData.contents.AskVolume1,
                     pDepthMarketData.contents.Volume,
                     pDepthMarketData.contents.Turnover))


CDLL("./v6.3.6/libthostmduserapi.so", mode=RTLD_GLOBAL)
CDLL("./v6.3.6/libthosttraderapi.so", mode=RTLD_GLOBAL)

CThostFtdcMdSpi._dll = cdll.LoadLibrary('./libpyctpmdapi.so')
CThostFtdcMdApi._dll = cdll.LoadLibrary('./libpyctpmdapi.so')

md_addr = b'tcp://180.168.102.194:41213'


tmp_path = './tmp'
if not os.path.exists(tmp_path):
    os.makedirs(tmp_path)

spi = MyMdSpi()
api = CThostFtdcMdApi(tmp_path + '/')

def run():
    global api
    global md_addr
    print('connect to market server: ' + md_addr.decode())
    api.RegisterSpi(spi.GetSpi())
    api.RegisterFront(md_addr)
    api.Init()
    print("market run...")

def quit(signo, frame):
    global api
    global spi
    print("exit(%d)!" % signo)
    api.RegisterSpi(None)
    api.Release()
    del spi
    sys.exit()

signal.signal(signal.SIGINT, quit)
signal.signal(signal.SIGTERM, quit)
ser = threading.Thread(target = run)
ser.setDaemon(True)
ser.start()
while True:
    pass


