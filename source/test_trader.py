# -*- coding: UTF-8 -*-

import threading, signal, sys, os
from ctypes import *;

from ctp.CtpApiStruct import *;
from ctp.CThostFtdcTraderSpi import *;
from ctp.CThostFtdcTraderApi import *;



U_FrontID = 0
U_SessionID = 0
U_MaxOrderRef = 0
U_TradingDay = ''
U_SHFETime = ''
U_DCETime = ''
U_CZCETime = ''
U_FFEXTime = ''

U_BrokerId = b'9999'
U_BroderIP = b'tcp://180.168.146.187:10000'

U_UserId = b'xxxxx'
U_UserPwd = b'xxxxx'

U_ReqId = 0
def GetReqId():
    global U_ReqId
    U_ReqId += 1
    return U_ReqId

def GetOrderRef():
    global U_MaxOrderRef
    U_MaxOrderRef += 1
    return U_MaxOrderRef

def SetInvestorInfo(req, brokerId, userId):
    req.BrokerID = brokerId
    req.InvestorID = userId

def DoReqSettlementInfoConfirm():
    req = CThostFtdcSettlementInfoConfirmField()
    SetInvestorInfo(req, U_BrokerId, U_UserId)
    tDay = c_char_p(api.GetTradingDay())
    req.ConfirmDate = tDay.value
    retVal = api.ReqSettlementInfoConfirm(byref(req), GetReqId())
    print('DoReqSettlementInfoConfirm:' + tDay.value.decode() + ' ' + str(retVal))

def DoReqQrySettlementInfo():
    req = CThostFtdcQrySettlementInfoField()
    SetInvestorInfo(req, U_BrokerId, U_UserId)
    retVal = api.ReqQrySettlementInfo(byref(req), GetReqId())

def DoReqQrySettlementInfoConfirm():
    req = CThostFtdcQrySettlementInfoConfirmField()
    SetInvestorInfo(req, U_BrokerId, U_UserId)
    retVal = api.ReqQrySettlementInfoConfirm(byref(req), GetReqId())

def DoReqOrderInsert(isopen, istoday, isbuy, code, vol, price):
    req = CThostFtdcInputOrderField()
    SetInvestorInfo(req, U_BrokerId, U_UserId)
    req.UserID = U_UserId
    req.InstrumentID = code
    if price == 0:
        req.OrderPriceType = THOST_FTDC_OPT_AnyPrice
        req.TimeCondition = THOST_FTDC_TC_IOC
    else:
        req.OrderPriceType = THOST_FTDC_OPT_LimitPrice
        req.TimeCondition = THOST_FTDC_TC_GFD
        req.LimitPrice = price
    req.VolumeCondition = THOST_FTDC_VC_AV
    req.MinVolume = 1
    req.CombHedgeFlag = THOST_FTDC_HF_Speculation
    req.ContingentCondition = THOST_FTDC_CC_Immediately
    req.ForceCloseReason = THOST_FTDC_FCC_NotForceClose
    req.IsAutoSuspend = 0
    req.Direction = THOST_FTDC_D_Buy if isbuy else THOST_FTDC_D_Sell
    if isopen:
        req.CombOffsetFlag = THOST_FTDC_OF_Open
    else:
        req.CombOffsetFlag = THOST_FTDC_OF_CloseToday if istoday else THOST_FTDC_OF_CloseYesterday
    req.VolumeTotalOriginal = vol
    req.OrderRef = str(GetOrderRef()).encode('utf-8')
    api.ReqOrderInsert(byref(req), GetReqId());

def DoReqOrderAction(instrument):
    req = CThostFtdcInputOrderActionField()
    req.ActionFlag = THOST_FTDC_AF_Delete
    SetInvestorInfo(req, U_BrokerId, U_UserId)
    req.InstrumentID = instrument
    req.SessionID = U_SessionID
    req.FrontID = U_FrontID
    req.OrderRef = str(GetOrderRef())
    api.ReqOrderAction(byref(req), GetReqId())

##############################################
class MyTraderSpi(CThostFtdcTraderSpi):
    def OnFrontConnected(self):
        print('connect successfully.')
        field = CThostFtdcReqUserLoginField()
        field.BrokerID = U_BrokerId
        field.UserID = U_UserId
        field.Password = U_UserPwd
        api.ReqUserLogin(byref(field), 1000)

    def OnFrontDisconnected(self, nReason):
        print('disconnect: ' + str(nReason))

    def OnRspUserLogin(self, pRspUserLogin, pRspInfo, nRequestID, bIsLast):
        FrontID = pRspUserLogin.contents.FrontID
        SessionID = pRspUserLogin.contents.SessionID
        MaxOrderRef = int(pRspUserLogin.contents.MaxOrderRef)
        TradingDay = pRspUserLogin.contents.TradingDay
        SHFETime = pRspUserLogin.contents.SHFETime
        DCETime = pRspUserLogin.contents.DCETime
        CZCETime = pRspUserLogin.contents.CZCETime
        FFEXTime = pRspUserLogin.contents.FFEXTime
        DoReqSettlementInfoConfirm()

    def OnRspSettlementInfoConfirm(self, pSettlementInfoConfirm, pRspInfo, nRequestID, bIsLast):
        print('Settlement: %s %s' % (pSettlementInfoConfirm.contents.ConfirmDate,
                pSettlementInfoConfirm.contents.ConfirmTime))
        DoReqOrderInsert(True, True, True, b'rb1801', 1, 3700)

    def OnRspError(self, resp, request_id, is_last):
        if not resp:
            print("error: %d %s" % (resp.contents.ErrorID, resp.contents.ErrorMsg))

    def OnRspOrderInsert(self, field, rsp_info, request_id, is_last):
        if not rsp_info:
            print("OnRspOrderInsert error: %d %s" % (rsp_info.contents.ErrorID, rsp_info.contents.ErrorMsg))

    def OnErrRtnOrderInsert(self, resp, rsp_info):
        if not rsp_info:
            print("OnErrRtnOrderInsert error: %d %s" % (rsp_info.contents.ErrorID, rsp_info.contents.ErrorMsg))

    def OnRtnOrder(self, resp):
        if not resp:
            return
        print("Status: %s - %s - %s - %s - %.2f - %d/%d - %s/%s - %s" % (resp.contents.OrderRef,
                resp.contents.InstrumentID,
                resp.contents.Direction,
                resp.contents.CombOffsetFlag,
                resp.contents.LimitPrice,
                resp.contents.VolumeTraded,
                resp.contents.VolumeTotalOriginal,
                resp.contents.OrderSubmitStatus,
                resp.contents.OrderStatus,
                resp.contents.OrderSysID))

    def OnRtnTrade(self, resp):
        if not resp:
            return
        print("Traded: %s - %s - %s - %s - %.2f - %d - %s" % (resp.contents.OrderRef,
                resp.contents.InstrumentID,
                resp.contents.Direction,
                resp.contents.OffsetFlag,
                resp.contents.Price,
                resp.contents.Volume,
                resp.contents.OrderSysID))


    def OnRspOrderAction(self, resp, rsp_info, request_id, is_last):
        if rsp_info:
            print("OnRspOrderAction error: %d %s" % (rsp_info.contents.ErrorID, rsp_info.contents.ErrorMsg))


    def OnErrRtnOrderAction(self, resp, rsp_info):
        if rsp_info:
            print("OnErrRtnOrderAction error: %d %s" % (rsp_info.contents.ErrorID, rsp_info.contents.ErrorMsg))



##############################################
CDLL("./v6.3.6/libthosttraderapi.so", mode=RTLD_GLOBAL)
CThostFtdcTraderApi._dll = cdll.LoadLibrary('./libpyctptraderapi.so')
CThostFtdcTraderSpi._dll = cdll.LoadLibrary('./libpyctptraderapi.so')

tmp_path = './tmp'
if not os.path.exists(tmp_path):
    os.makedirs(tmp_path)

spi = MyTraderSpi()
api = CThostFtdcTraderApi(tmp_path + '/')

def run():
    global spi
    global api
    api.RegisterSpi(spi.GetSpi())
    api.SubscribePrivateTopic(THOST_TERT_QUICK)
    api.RegisterFront(U_BroderIP)
    api.Init()
    print("trader run...")

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


