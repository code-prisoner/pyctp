# -*- coding: UTF-8 -*-

from ctp.PyCtpObject import *;

class CThostFtdcMdApi(PyCtpObject):

    def __init__(self, path):
        self.__api = CThostFtdcMdApi._dll.CreateApi(path)

    def GetApi(self):
        return self.__api


    def Release(self):
        return CThostFtdcMdApi._dll.Release(self.__api)

    def Init(self):
        return CThostFtdcMdApi._dll.Init(self.__api)

    def Join(self):
        return CThostFtdcMdApi._dll.Join(self.__api)

    def GetTradingDay(self):
        return CThostFtdcMdApi._dll.GetTradingDay(self.__api)

    def RegisterFront(self, pszFrontAddress):
        return CThostFtdcMdApi._dll.RegisterFront(self.__api, pszFrontAddress)

    def RegisterNameServer(self, pszNsAddress):
        return CThostFtdcMdApi._dll.RegisterNameServer(self.__api, pszNsAddress)

    def RegisterFensUserInfo(self, pFensUserInfo):
        return CThostFtdcMdApi._dll.RegisterFensUserInfo(self.__api, pFensUserInfo)

    def RegisterSpi(self, pSpi):
        return CThostFtdcMdApi._dll.RegisterSpi(self.__api, pSpi)

    def SubscribeMarketData(self, ppInstrumentID, nCount):
        return CThostFtdcMdApi._dll.SubscribeMarketData(self.__api, ppInstrumentID, nCount)

    def UnSubscribeMarketData(self, ppInstrumentID, nCount):
        return CThostFtdcMdApi._dll.UnSubscribeMarketData(self.__api, ppInstrumentID, nCount)

    def SubscribeForQuoteRsp(self, ppInstrumentID, nCount):
        return CThostFtdcMdApi._dll.SubscribeForQuoteRsp(self.__api, ppInstrumentID, nCount)

    def UnSubscribeForQuoteRsp(self, ppInstrumentID, nCount):
        return CThostFtdcMdApi._dll.UnSubscribeForQuoteRsp(self.__api, ppInstrumentID, nCount)

    def ReqUserLogin(self, pReqUserLoginField, nRequestID):
        return CThostFtdcMdApi._dll.ReqUserLogin(self.__api, pReqUserLoginField, nRequestID)

    def ReqUserLogout(self, pUserLogout, nRequestID):
        return CThostFtdcMdApi._dll.ReqUserLogout(self.__api, pUserLogout, nRequestID)

