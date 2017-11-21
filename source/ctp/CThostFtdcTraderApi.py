# -*- coding: UTF-8 -*-

from ctp.PyCtpObject import *;

class CThostFtdcTraderApi(PyCtpObject):

    def __init__(self, path):
        self.__api = CThostFtdcTraderApi._dll.CreateApi(path)

    def GetApi(self):
        return self.__api


    def Release(self):
        return CThostFtdcTraderApi._dll.Release(self.__api)

    def Init(self):
        return CThostFtdcTraderApi._dll.Init(self.__api)

    def Join(self):
        return CThostFtdcTraderApi._dll.Join(self.__api)

    def GetTradingDay(self):
        return CThostFtdcTraderApi._dll.GetTradingDay(self.__api)

    def RegisterFront(self, pszFrontAddress):
        return CThostFtdcTraderApi._dll.RegisterFront(self.__api, pszFrontAddress)

    def RegisterNameServer(self, pszNsAddress):
        return CThostFtdcTraderApi._dll.RegisterNameServer(self.__api, pszNsAddress)

    def RegisterFensUserInfo(self, pFensUserInfo):
        return CThostFtdcTraderApi._dll.RegisterFensUserInfo(self.__api, pFensUserInfo)

    def RegisterSpi(self, pSpi):
        return CThostFtdcTraderApi._dll.RegisterSpi(self.__api, pSpi)

    def SubscribePrivateTopic(self, nResumeType):
        return CThostFtdcTraderApi._dll.SubscribePrivateTopic(self.__api, nResumeType)

    def SubscribePublicTopic(self, nResumeType):
        return CThostFtdcTraderApi._dll.SubscribePublicTopic(self.__api, nResumeType)

    def ReqAuthenticate(self, pReqAuthenticateField, nRequestID):
        return CThostFtdcTraderApi._dll.ReqAuthenticate(self.__api, pReqAuthenticateField, nRequestID)

    def ReqUserLogin(self, pReqUserLoginField, nRequestID):
        return CThostFtdcTraderApi._dll.ReqUserLogin(self.__api, pReqUserLoginField, nRequestID)

    def ReqUserLogout(self, pUserLogout, nRequestID):
        return CThostFtdcTraderApi._dll.ReqUserLogout(self.__api, pUserLogout, nRequestID)

    def ReqUserPasswordUpdate(self, pUserPasswordUpdate, nRequestID):
        return CThostFtdcTraderApi._dll.ReqUserPasswordUpdate(self.__api, pUserPasswordUpdate, nRequestID)

    def ReqTradingAccountPasswordUpdate(self, pTradingAccountPasswordUpdate, nRequestID):
        return CThostFtdcTraderApi._dll.ReqTradingAccountPasswordUpdate(self.__api, pTradingAccountPasswordUpdate, nRequestID)

    def ReqOrderInsert(self, pInputOrder, nRequestID):
        return CThostFtdcTraderApi._dll.ReqOrderInsert(self.__api, pInputOrder, nRequestID)

    def ReqParkedOrderInsert(self, pParkedOrder, nRequestID):
        return CThostFtdcTraderApi._dll.ReqParkedOrderInsert(self.__api, pParkedOrder, nRequestID)

    def ReqParkedOrderAction(self, pParkedOrderAction, nRequestID):
        return CThostFtdcTraderApi._dll.ReqParkedOrderAction(self.__api, pParkedOrderAction, nRequestID)

    def ReqOrderAction(self, pInputOrderAction, nRequestID):
        return CThostFtdcTraderApi._dll.ReqOrderAction(self.__api, pInputOrderAction, nRequestID)

    def ReqQueryMaxOrderVolume(self, pQueryMaxOrderVolume, nRequestID):
        return CThostFtdcTraderApi._dll.ReqQueryMaxOrderVolume(self.__api, pQueryMaxOrderVolume, nRequestID)

    def ReqSettlementInfoConfirm(self, pSettlementInfoConfirm, nRequestID):
        return CThostFtdcTraderApi._dll.ReqSettlementInfoConfirm(self.__api, pSettlementInfoConfirm, nRequestID)

    def ReqRemoveParkedOrder(self, pRemoveParkedOrder, nRequestID):
        return CThostFtdcTraderApi._dll.ReqRemoveParkedOrder(self.__api, pRemoveParkedOrder, nRequestID)

    def ReqRemoveParkedOrderAction(self, pRemoveParkedOrderAction, nRequestID):
        return CThostFtdcTraderApi._dll.ReqRemoveParkedOrderAction(self.__api, pRemoveParkedOrderAction, nRequestID)

    def ReqExecOrderInsert(self, pInputExecOrder, nRequestID):
        return CThostFtdcTraderApi._dll.ReqExecOrderInsert(self.__api, pInputExecOrder, nRequestID)

    def ReqExecOrderAction(self, pInputExecOrderAction, nRequestID):
        return CThostFtdcTraderApi._dll.ReqExecOrderAction(self.__api, pInputExecOrderAction, nRequestID)

    def ReqForQuoteInsert(self, pInputForQuote, nRequestID):
        return CThostFtdcTraderApi._dll.ReqForQuoteInsert(self.__api, pInputForQuote, nRequestID)

    def ReqQuoteInsert(self, pInputQuote, nRequestID):
        return CThostFtdcTraderApi._dll.ReqQuoteInsert(self.__api, pInputQuote, nRequestID)

    def ReqQuoteAction(self, pInputQuoteAction, nRequestID):
        return CThostFtdcTraderApi._dll.ReqQuoteAction(self.__api, pInputQuoteAction, nRequestID)

    def ReqBatchOrderAction(self, pInputBatchOrderAction, nRequestID):
        return CThostFtdcTraderApi._dll.ReqBatchOrderAction(self.__api, pInputBatchOrderAction, nRequestID)

    def ReqCombActionInsert(self, pInputCombAction, nRequestID):
        return CThostFtdcTraderApi._dll.ReqCombActionInsert(self.__api, pInputCombAction, nRequestID)

    def ReqQryOrder(self, pQryOrder, nRequestID):
        return CThostFtdcTraderApi._dll.ReqQryOrder(self.__api, pQryOrder, nRequestID)

    def ReqQryTrade(self, pQryTrade, nRequestID):
        return CThostFtdcTraderApi._dll.ReqQryTrade(self.__api, pQryTrade, nRequestID)

    def ReqQryInvestorPosition(self, pQryInvestorPosition, nRequestID):
        return CThostFtdcTraderApi._dll.ReqQryInvestorPosition(self.__api, pQryInvestorPosition, nRequestID)

    def ReqQryTradingAccount(self, pQryTradingAccount, nRequestID):
        return CThostFtdcTraderApi._dll.ReqQryTradingAccount(self.__api, pQryTradingAccount, nRequestID)

    def ReqQryInvestor(self, pQryInvestor, nRequestID):
        return CThostFtdcTraderApi._dll.ReqQryInvestor(self.__api, pQryInvestor, nRequestID)

    def ReqQryTradingCode(self, pQryTradingCode, nRequestID):
        return CThostFtdcTraderApi._dll.ReqQryTradingCode(self.__api, pQryTradingCode, nRequestID)

    def ReqQryInstrumentMarginRate(self, pQryInstrumentMarginRate, nRequestID):
        return CThostFtdcTraderApi._dll.ReqQryInstrumentMarginRate(self.__api, pQryInstrumentMarginRate, nRequestID)

    def ReqQryInstrumentCommissionRate(self, pQryInstrumentCommissionRate, nRequestID):
        return CThostFtdcTraderApi._dll.ReqQryInstrumentCommissionRate(self.__api, pQryInstrumentCommissionRate, nRequestID)

    def ReqQryExchange(self, pQryExchange, nRequestID):
        return CThostFtdcTraderApi._dll.ReqQryExchange(self.__api, pQryExchange, nRequestID)

    def ReqQryProduct(self, pQryProduct, nRequestID):
        return CThostFtdcTraderApi._dll.ReqQryProduct(self.__api, pQryProduct, nRequestID)

    def ReqQryInstrument(self, pQryInstrument, nRequestID):
        return CThostFtdcTraderApi._dll.ReqQryInstrument(self.__api, pQryInstrument, nRequestID)

    def ReqQryDepthMarketData(self, pQryDepthMarketData, nRequestID):
        return CThostFtdcTraderApi._dll.ReqQryDepthMarketData(self.__api, pQryDepthMarketData, nRequestID)

    def ReqQrySettlementInfo(self, pQrySettlementInfo, nRequestID):
        return CThostFtdcTraderApi._dll.ReqQrySettlementInfo(self.__api, pQrySettlementInfo, nRequestID)

    def ReqQryTransferBank(self, pQryTransferBank, nRequestID):
        return CThostFtdcTraderApi._dll.ReqQryTransferBank(self.__api, pQryTransferBank, nRequestID)

    def ReqQryInvestorPositionDetail(self, pQryInvestorPositionDetail, nRequestID):
        return CThostFtdcTraderApi._dll.ReqQryInvestorPositionDetail(self.__api, pQryInvestorPositionDetail, nRequestID)

    def ReqQryNotice(self, pQryNotice, nRequestID):
        return CThostFtdcTraderApi._dll.ReqQryNotice(self.__api, pQryNotice, nRequestID)

    def ReqQrySettlementInfoConfirm(self, pQrySettlementInfoConfirm, nRequestID):
        return CThostFtdcTraderApi._dll.ReqQrySettlementInfoConfirm(self.__api, pQrySettlementInfoConfirm, nRequestID)

    def ReqQryInvestorPositionCombineDetail(self, pQryInvestorPositionCombineDetail, nRequestID):
        return CThostFtdcTraderApi._dll.ReqQryInvestorPositionCombineDetail(self.__api, pQryInvestorPositionCombineDetail, nRequestID)

    def ReqQryCFMMCTradingAccountKey(self, pQryCFMMCTradingAccountKey, nRequestID):
        return CThostFtdcTraderApi._dll.ReqQryCFMMCTradingAccountKey(self.__api, pQryCFMMCTradingAccountKey, nRequestID)

    def ReqQryEWarrantOffset(self, pQryEWarrantOffset, nRequestID):
        return CThostFtdcTraderApi._dll.ReqQryEWarrantOffset(self.__api, pQryEWarrantOffset, nRequestID)

    def ReqQryInvestorProductGroupMargin(self, pQryInvestorProductGroupMargin, nRequestID):
        return CThostFtdcTraderApi._dll.ReqQryInvestorProductGroupMargin(self.__api, pQryInvestorProductGroupMargin, nRequestID)

    def ReqQryExchangeMarginRate(self, pQryExchangeMarginRate, nRequestID):
        return CThostFtdcTraderApi._dll.ReqQryExchangeMarginRate(self.__api, pQryExchangeMarginRate, nRequestID)

    def ReqQryExchangeMarginRateAdjust(self, pQryExchangeMarginRateAdjust, nRequestID):
        return CThostFtdcTraderApi._dll.ReqQryExchangeMarginRateAdjust(self.__api, pQryExchangeMarginRateAdjust, nRequestID)

    def ReqQryExchangeRate(self, pQryExchangeRate, nRequestID):
        return CThostFtdcTraderApi._dll.ReqQryExchangeRate(self.__api, pQryExchangeRate, nRequestID)

    def ReqQrySecAgentACIDMap(self, pQrySecAgentACIDMap, nRequestID):
        return CThostFtdcTraderApi._dll.ReqQrySecAgentACIDMap(self.__api, pQrySecAgentACIDMap, nRequestID)

    def ReqQryProductExchRate(self, pQryProductExchRate, nRequestID):
        return CThostFtdcTraderApi._dll.ReqQryProductExchRate(self.__api, pQryProductExchRate, nRequestID)

    def ReqQryProductGroup(self, pQryProductGroup, nRequestID):
        return CThostFtdcTraderApi._dll.ReqQryProductGroup(self.__api, pQryProductGroup, nRequestID)

    def ReqQryMMInstrumentCommissionRate(self, pQryMMInstrumentCommissionRate, nRequestID):
        return CThostFtdcTraderApi._dll.ReqQryMMInstrumentCommissionRate(self.__api, pQryMMInstrumentCommissionRate, nRequestID)

    def ReqQryMMOptionInstrCommRate(self, pQryMMOptionInstrCommRate, nRequestID):
        return CThostFtdcTraderApi._dll.ReqQryMMOptionInstrCommRate(self.__api, pQryMMOptionInstrCommRate, nRequestID)

    def ReqQryInstrumentOrderCommRate(self, pQryInstrumentOrderCommRate, nRequestID):
        return CThostFtdcTraderApi._dll.ReqQryInstrumentOrderCommRate(self.__api, pQryInstrumentOrderCommRate, nRequestID)

    def ReqQryOptionInstrTradeCost(self, pQryOptionInstrTradeCost, nRequestID):
        return CThostFtdcTraderApi._dll.ReqQryOptionInstrTradeCost(self.__api, pQryOptionInstrTradeCost, nRequestID)

    def ReqQryOptionInstrCommRate(self, pQryOptionInstrCommRate, nRequestID):
        return CThostFtdcTraderApi._dll.ReqQryOptionInstrCommRate(self.__api, pQryOptionInstrCommRate, nRequestID)

    def ReqQryExecOrder(self, pQryExecOrder, nRequestID):
        return CThostFtdcTraderApi._dll.ReqQryExecOrder(self.__api, pQryExecOrder, nRequestID)

    def ReqQryForQuote(self, pQryForQuote, nRequestID):
        return CThostFtdcTraderApi._dll.ReqQryForQuote(self.__api, pQryForQuote, nRequestID)

    def ReqQryQuote(self, pQryQuote, nRequestID):
        return CThostFtdcTraderApi._dll.ReqQryQuote(self.__api, pQryQuote, nRequestID)

    def ReqQryCombInstrumentGuard(self, pQryCombInstrumentGuard, nRequestID):
        return CThostFtdcTraderApi._dll.ReqQryCombInstrumentGuard(self.__api, pQryCombInstrumentGuard, nRequestID)

    def ReqQryCombAction(self, pQryCombAction, nRequestID):
        return CThostFtdcTraderApi._dll.ReqQryCombAction(self.__api, pQryCombAction, nRequestID)

    def ReqQryTransferSerial(self, pQryTransferSerial, nRequestID):
        return CThostFtdcTraderApi._dll.ReqQryTransferSerial(self.__api, pQryTransferSerial, nRequestID)

    def ReqQryAccountregister(self, pQryAccountregister, nRequestID):
        return CThostFtdcTraderApi._dll.ReqQryAccountregister(self.__api, pQryAccountregister, nRequestID)

    def ReqQryContractBank(self, pQryContractBank, nRequestID):
        return CThostFtdcTraderApi._dll.ReqQryContractBank(self.__api, pQryContractBank, nRequestID)

    def ReqQryParkedOrder(self, pQryParkedOrder, nRequestID):
        return CThostFtdcTraderApi._dll.ReqQryParkedOrder(self.__api, pQryParkedOrder, nRequestID)

    def ReqQryParkedOrderAction(self, pQryParkedOrderAction, nRequestID):
        return CThostFtdcTraderApi._dll.ReqQryParkedOrderAction(self.__api, pQryParkedOrderAction, nRequestID)

    def ReqQryTradingNotice(self, pQryTradingNotice, nRequestID):
        return CThostFtdcTraderApi._dll.ReqQryTradingNotice(self.__api, pQryTradingNotice, nRequestID)

    def ReqQryBrokerTradingParams(self, pQryBrokerTradingParams, nRequestID):
        return CThostFtdcTraderApi._dll.ReqQryBrokerTradingParams(self.__api, pQryBrokerTradingParams, nRequestID)

    def ReqQryBrokerTradingAlgos(self, pQryBrokerTradingAlgos, nRequestID):
        return CThostFtdcTraderApi._dll.ReqQryBrokerTradingAlgos(self.__api, pQryBrokerTradingAlgos, nRequestID)

    def ReqQueryCFMMCTradingAccountToken(self, pQueryCFMMCTradingAccountToken, nRequestID):
        return CThostFtdcTraderApi._dll.ReqQueryCFMMCTradingAccountToken(self.__api, pQueryCFMMCTradingAccountToken, nRequestID)

    def ReqFromBankToFutureByFuture(self, pReqTransfer, nRequestID):
        return CThostFtdcTraderApi._dll.ReqFromBankToFutureByFuture(self.__api, pReqTransfer, nRequestID)

    def ReqFromFutureToBankByFuture(self, pReqTransfer, nRequestID):
        return CThostFtdcTraderApi._dll.ReqFromFutureToBankByFuture(self.__api, pReqTransfer, nRequestID)

    def ReqQueryBankAccountMoneyByFuture(self, pReqQueryAccount, nRequestID):
        return CThostFtdcTraderApi._dll.ReqQueryBankAccountMoneyByFuture(self.__api, pReqQueryAccount, nRequestID)

