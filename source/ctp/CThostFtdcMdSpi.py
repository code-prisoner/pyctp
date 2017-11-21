# -*- coding: UTF-8 -*-

from ctp.PyCtpObject import *;
from ctp.CtpApiStruct import *;

class CThostFtdcMdSpi(PyCtpObject):
    __SpiToObj = {}
    def __init__(self):
        self.__spi = CThostFtdcMdSpi._dll.CreateSpi()
        self.__SpiToObj[self.__spi] = self
        self.__callback = {
             b'OnFrontConnected' : CFUNCTYPE(None, c_void_p)(CThostFtdcMdSpi.__OnFrontConnected),
             b'OnFrontDisconnected' : CFUNCTYPE(None, c_void_p, c_int)(CThostFtdcMdSpi.__OnFrontDisconnected),
             b'OnHeartBeatWarning' : CFUNCTYPE(None, c_void_p, c_int)(CThostFtdcMdSpi.__OnHeartBeatWarning),
             b'OnRspUserLogin' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcRspUserLoginField), POINTER(CThostFtdcRspInfoField), c_int, c_bool)(CThostFtdcMdSpi.__OnRspUserLogin),
             b'OnRspUserLogout' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcUserLogoutField), POINTER(CThostFtdcRspInfoField), c_int, c_bool)(CThostFtdcMdSpi.__OnRspUserLogout),
             b'OnRspError' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcRspInfoField), c_int, c_bool)(CThostFtdcMdSpi.__OnRspError),
             b'OnRspSubMarketData' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcSpecificInstrumentField), POINTER(CThostFtdcRspInfoField), c_int, c_bool)(CThostFtdcMdSpi.__OnRspSubMarketData),
             b'OnRspUnSubMarketData' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcSpecificInstrumentField), POINTER(CThostFtdcRspInfoField), c_int, c_bool)(CThostFtdcMdSpi.__OnRspUnSubMarketData),
             b'OnRspSubForQuoteRsp' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcSpecificInstrumentField), POINTER(CThostFtdcRspInfoField), c_int, c_bool)(CThostFtdcMdSpi.__OnRspSubForQuoteRsp),
             b'OnRspUnSubForQuoteRsp' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcSpecificInstrumentField), POINTER(CThostFtdcRspInfoField), c_int, c_bool)(CThostFtdcMdSpi.__OnRspUnSubForQuoteRsp),
             b'OnRtnDepthMarketData' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcDepthMarketDataField))(CThostFtdcMdSpi.__OnRtnDepthMarketData),
             b'OnRtnForQuoteRsp' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcForQuoteRspField))(CThostFtdcMdSpi.__OnRtnForQuoteRsp)
        }
        for (k, v) in self.__callback.items():
            CThostFtdcMdSpi._dll.RegCallBack(self.__spi, k, v)

    def __del__(self):
        del self.__spi

    def GetSpi(self):
        return self.__spi


    def OnFrontConnected(self):
        pass

    def OnFrontDisconnected(self, nReason):
        pass

    def OnHeartBeatWarning(self, nTimeLapse):
        pass

    def OnRspUserLogin(self, pRspUserLogin, pRspInfo, nRequestID, bIsLast):
        pass

    def OnRspUserLogout(self, pUserLogout, pRspInfo, nRequestID, bIsLast):
        pass

    def OnRspError(self, pRspInfo, nRequestID, bIsLast):
        pass

    def OnRspSubMarketData(self, pSpecificInstrument, pRspInfo, nRequestID, bIsLast):
        pass

    def OnRspUnSubMarketData(self, pSpecificInstrument, pRspInfo, nRequestID, bIsLast):
        pass

    def OnRspSubForQuoteRsp(self, pSpecificInstrument, pRspInfo, nRequestID, bIsLast):
        pass

    def OnRspUnSubForQuoteRsp(self, pSpecificInstrument, pRspInfo, nRequestID, bIsLast):
        pass

    def OnRtnDepthMarketData(self, pDepthMarketData):
        pass

    def OnRtnForQuoteRsp(self, pForQuoteRsp):
        pass


    @staticmethod
    def __OnFrontConnected(spi):
        CThostFtdcMdSpi.__SpiToObj[spi].OnFrontConnected()

    @staticmethod
    def __OnFrontDisconnected(spi, nReason):
        CThostFtdcMdSpi.__SpiToObj[spi].OnFrontDisconnected(nReason)

    @staticmethod
    def __OnHeartBeatWarning(spi, nTimeLapse):
        CThostFtdcMdSpi.__SpiToObj[spi].OnHeartBeatWarning(nTimeLapse)

    @staticmethod
    def __OnRspUserLogin(spi, pRspUserLogin, pRspInfo, nRequestID, bIsLast):
        CThostFtdcMdSpi.__SpiToObj[spi].OnRspUserLogin(pRspUserLogin, pRspInfo, nRequestID, bIsLast)

    @staticmethod
    def __OnRspUserLogout(spi, pUserLogout, pRspInfo, nRequestID, bIsLast):
        CThostFtdcMdSpi.__SpiToObj[spi].OnRspUserLogout(pUserLogout, pRspInfo, nRequestID, bIsLast)

    @staticmethod
    def __OnRspError(spi, pRspInfo, nRequestID, bIsLast):
        CThostFtdcMdSpi.__SpiToObj[spi].OnRspError(pRspInfo, nRequestID, bIsLast)

    @staticmethod
    def __OnRspSubMarketData(spi, pSpecificInstrument, pRspInfo, nRequestID, bIsLast):
        CThostFtdcMdSpi.__SpiToObj[spi].OnRspSubMarketData(pSpecificInstrument, pRspInfo, nRequestID, bIsLast)

    @staticmethod
    def __OnRspUnSubMarketData(spi, pSpecificInstrument, pRspInfo, nRequestID, bIsLast):
        CThostFtdcMdSpi.__SpiToObj[spi].OnRspUnSubMarketData(pSpecificInstrument, pRspInfo, nRequestID, bIsLast)

    @staticmethod
    def __OnRspSubForQuoteRsp(spi, pSpecificInstrument, pRspInfo, nRequestID, bIsLast):
        CThostFtdcMdSpi.__SpiToObj[spi].OnRspSubForQuoteRsp(pSpecificInstrument, pRspInfo, nRequestID, bIsLast)

    @staticmethod
    def __OnRspUnSubForQuoteRsp(spi, pSpecificInstrument, pRspInfo, nRequestID, bIsLast):
        CThostFtdcMdSpi.__SpiToObj[spi].OnRspUnSubForQuoteRsp(pSpecificInstrument, pRspInfo, nRequestID, bIsLast)

    @staticmethod
    def __OnRtnDepthMarketData(spi, pDepthMarketData):
        CThostFtdcMdSpi.__SpiToObj[spi].OnRtnDepthMarketData(pDepthMarketData)

    @staticmethod
    def __OnRtnForQuoteRsp(spi, pForQuoteRsp):
        CThostFtdcMdSpi.__SpiToObj[spi].OnRtnForQuoteRsp(pForQuoteRsp)

