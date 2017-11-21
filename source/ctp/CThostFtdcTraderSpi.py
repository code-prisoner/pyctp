# -*- coding: UTF-8 -*-

from ctp.PyCtpObject import *;
from ctp.CtpApiStruct import *;

class CThostFtdcTraderSpi(PyCtpObject):
    __SpiToObj = {}
    def __init__(self):
        self.__spi = CThostFtdcTraderSpi._dll.CreateSpi()
        self.__SpiToObj[self.__spi] = self
        self.__callback = {
             b'OnFrontConnected' : CFUNCTYPE(None, c_void_p)(CThostFtdcTraderSpi.__OnFrontConnected),
             b'OnFrontDisconnected' : CFUNCTYPE(None, c_void_p, c_int)(CThostFtdcTraderSpi.__OnFrontDisconnected),
             b'OnHeartBeatWarning' : CFUNCTYPE(None, c_void_p, c_int)(CThostFtdcTraderSpi.__OnHeartBeatWarning),
             b'OnRspAuthenticate' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcRspAuthenticateField), POINTER(CThostFtdcRspInfoField), c_int, c_bool)(CThostFtdcTraderSpi.__OnRspAuthenticate),
             b'OnRspUserLogin' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcRspUserLoginField), POINTER(CThostFtdcRspInfoField), c_int, c_bool)(CThostFtdcTraderSpi.__OnRspUserLogin),
             b'OnRspUserLogout' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcUserLogoutField), POINTER(CThostFtdcRspInfoField), c_int, c_bool)(CThostFtdcTraderSpi.__OnRspUserLogout),
             b'OnRspUserPasswordUpdate' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcUserPasswordUpdateField), POINTER(CThostFtdcRspInfoField), c_int, c_bool)(CThostFtdcTraderSpi.__OnRspUserPasswordUpdate),
             b'OnRspTradingAccountPasswordUpdate' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcTradingAccountPasswordUpdateField), POINTER(CThostFtdcRspInfoField), c_int, c_bool)(CThostFtdcTraderSpi.__OnRspTradingAccountPasswordUpdate),
             b'OnRspOrderInsert' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcInputOrderField), POINTER(CThostFtdcRspInfoField), c_int, c_bool)(CThostFtdcTraderSpi.__OnRspOrderInsert),
             b'OnRspParkedOrderInsert' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcParkedOrderField), POINTER(CThostFtdcRspInfoField), c_int, c_bool)(CThostFtdcTraderSpi.__OnRspParkedOrderInsert),
             b'OnRspParkedOrderAction' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcParkedOrderActionField), POINTER(CThostFtdcRspInfoField), c_int, c_bool)(CThostFtdcTraderSpi.__OnRspParkedOrderAction),
             b'OnRspOrderAction' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcInputOrderActionField), POINTER(CThostFtdcRspInfoField), c_int, c_bool)(CThostFtdcTraderSpi.__OnRspOrderAction),
             b'OnRspQueryMaxOrderVolume' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcQueryMaxOrderVolumeField), POINTER(CThostFtdcRspInfoField), c_int, c_bool)(CThostFtdcTraderSpi.__OnRspQueryMaxOrderVolume),
             b'OnRspSettlementInfoConfirm' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcSettlementInfoConfirmField), POINTER(CThostFtdcRspInfoField), c_int, c_bool)(CThostFtdcTraderSpi.__OnRspSettlementInfoConfirm),
             b'OnRspRemoveParkedOrder' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcRemoveParkedOrderField), POINTER(CThostFtdcRspInfoField), c_int, c_bool)(CThostFtdcTraderSpi.__OnRspRemoveParkedOrder),
             b'OnRspRemoveParkedOrderAction' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcRemoveParkedOrderActionField), POINTER(CThostFtdcRspInfoField), c_int, c_bool)(CThostFtdcTraderSpi.__OnRspRemoveParkedOrderAction),
             b'OnRspExecOrderInsert' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcInputExecOrderField), POINTER(CThostFtdcRspInfoField), c_int, c_bool)(CThostFtdcTraderSpi.__OnRspExecOrderInsert),
             b'OnRspExecOrderAction' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcInputExecOrderActionField), POINTER(CThostFtdcRspInfoField), c_int, c_bool)(CThostFtdcTraderSpi.__OnRspExecOrderAction),
             b'OnRspForQuoteInsert' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcInputForQuoteField), POINTER(CThostFtdcRspInfoField), c_int, c_bool)(CThostFtdcTraderSpi.__OnRspForQuoteInsert),
             b'OnRspQuoteInsert' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcInputQuoteField), POINTER(CThostFtdcRspInfoField), c_int, c_bool)(CThostFtdcTraderSpi.__OnRspQuoteInsert),
             b'OnRspQuoteAction' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcInputQuoteActionField), POINTER(CThostFtdcRspInfoField), c_int, c_bool)(CThostFtdcTraderSpi.__OnRspQuoteAction),
             b'OnRspBatchOrderAction' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcInputBatchOrderActionField), POINTER(CThostFtdcRspInfoField), c_int, c_bool)(CThostFtdcTraderSpi.__OnRspBatchOrderAction),
             b'OnRspCombActionInsert' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcInputCombActionField), POINTER(CThostFtdcRspInfoField), c_int, c_bool)(CThostFtdcTraderSpi.__OnRspCombActionInsert),
             b'OnRspQryOrder' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcOrderField), POINTER(CThostFtdcRspInfoField), c_int, c_bool)(CThostFtdcTraderSpi.__OnRspQryOrder),
             b'OnRspQryTrade' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcTradeField), POINTER(CThostFtdcRspInfoField), c_int, c_bool)(CThostFtdcTraderSpi.__OnRspQryTrade),
             b'OnRspQryInvestorPosition' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcInvestorPositionField), POINTER(CThostFtdcRspInfoField), c_int, c_bool)(CThostFtdcTraderSpi.__OnRspQryInvestorPosition),
             b'OnRspQryTradingAccount' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcTradingAccountField), POINTER(CThostFtdcRspInfoField), c_int, c_bool)(CThostFtdcTraderSpi.__OnRspQryTradingAccount),
             b'OnRspQryInvestor' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcInvestorField), POINTER(CThostFtdcRspInfoField), c_int, c_bool)(CThostFtdcTraderSpi.__OnRspQryInvestor),
             b'OnRspQryTradingCode' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcTradingCodeField), POINTER(CThostFtdcRspInfoField), c_int, c_bool)(CThostFtdcTraderSpi.__OnRspQryTradingCode),
             b'OnRspQryInstrumentMarginRate' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcInstrumentMarginRateField), POINTER(CThostFtdcRspInfoField), c_int, c_bool)(CThostFtdcTraderSpi.__OnRspQryInstrumentMarginRate),
             b'OnRspQryInstrumentCommissionRate' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcInstrumentCommissionRateField), POINTER(CThostFtdcRspInfoField), c_int, c_bool)(CThostFtdcTraderSpi.__OnRspQryInstrumentCommissionRate),
             b'OnRspQryExchange' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcExchangeField), POINTER(CThostFtdcRspInfoField), c_int, c_bool)(CThostFtdcTraderSpi.__OnRspQryExchange),
             b'OnRspQryProduct' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcProductField), POINTER(CThostFtdcRspInfoField), c_int, c_bool)(CThostFtdcTraderSpi.__OnRspQryProduct),
             b'OnRspQryInstrument' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcInstrumentField), POINTER(CThostFtdcRspInfoField), c_int, c_bool)(CThostFtdcTraderSpi.__OnRspQryInstrument),
             b'OnRspQryDepthMarketData' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcDepthMarketDataField), POINTER(CThostFtdcRspInfoField), c_int, c_bool)(CThostFtdcTraderSpi.__OnRspQryDepthMarketData),
             b'OnRspQrySettlementInfo' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcSettlementInfoField), POINTER(CThostFtdcRspInfoField), c_int, c_bool)(CThostFtdcTraderSpi.__OnRspQrySettlementInfo),
             b'OnRspQryTransferBank' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcTransferBankField), POINTER(CThostFtdcRspInfoField), c_int, c_bool)(CThostFtdcTraderSpi.__OnRspQryTransferBank),
             b'OnRspQryInvestorPositionDetail' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcInvestorPositionDetailField), POINTER(CThostFtdcRspInfoField), c_int, c_bool)(CThostFtdcTraderSpi.__OnRspQryInvestorPositionDetail),
             b'OnRspQryNotice' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcNoticeField), POINTER(CThostFtdcRspInfoField), c_int, c_bool)(CThostFtdcTraderSpi.__OnRspQryNotice),
             b'OnRspQrySettlementInfoConfirm' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcSettlementInfoConfirmField), POINTER(CThostFtdcRspInfoField), c_int, c_bool)(CThostFtdcTraderSpi.__OnRspQrySettlementInfoConfirm),
             b'OnRspQryInvestorPositionCombineDetail' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcInvestorPositionCombineDetailField), POINTER(CThostFtdcRspInfoField), c_int, c_bool)(CThostFtdcTraderSpi.__OnRspQryInvestorPositionCombineDetail),
             b'OnRspQryCFMMCTradingAccountKey' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcCFMMCTradingAccountKeyField), POINTER(CThostFtdcRspInfoField), c_int, c_bool)(CThostFtdcTraderSpi.__OnRspQryCFMMCTradingAccountKey),
             b'OnRspQryEWarrantOffset' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcEWarrantOffsetField), POINTER(CThostFtdcRspInfoField), c_int, c_bool)(CThostFtdcTraderSpi.__OnRspQryEWarrantOffset),
             b'OnRspQryInvestorProductGroupMargin' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcInvestorProductGroupMarginField), POINTER(CThostFtdcRspInfoField), c_int, c_bool)(CThostFtdcTraderSpi.__OnRspQryInvestorProductGroupMargin),
             b'OnRspQryExchangeMarginRate' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcExchangeMarginRateField), POINTER(CThostFtdcRspInfoField), c_int, c_bool)(CThostFtdcTraderSpi.__OnRspQryExchangeMarginRate),
             b'OnRspQryExchangeMarginRateAdjust' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcExchangeMarginRateAdjustField), POINTER(CThostFtdcRspInfoField), c_int, c_bool)(CThostFtdcTraderSpi.__OnRspQryExchangeMarginRateAdjust),
             b'OnRspQryExchangeRate' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcExchangeRateField), POINTER(CThostFtdcRspInfoField), c_int, c_bool)(CThostFtdcTraderSpi.__OnRspQryExchangeRate),
             b'OnRspQrySecAgentACIDMap' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcSecAgentACIDMapField), POINTER(CThostFtdcRspInfoField), c_int, c_bool)(CThostFtdcTraderSpi.__OnRspQrySecAgentACIDMap),
             b'OnRspQryProductExchRate' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcProductExchRateField), POINTER(CThostFtdcRspInfoField), c_int, c_bool)(CThostFtdcTraderSpi.__OnRspQryProductExchRate),
             b'OnRspQryProductGroup' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcProductGroupField), POINTER(CThostFtdcRspInfoField), c_int, c_bool)(CThostFtdcTraderSpi.__OnRspQryProductGroup),
             b'OnRspQryMMInstrumentCommissionRate' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcMMInstrumentCommissionRateField), POINTER(CThostFtdcRspInfoField), c_int, c_bool)(CThostFtdcTraderSpi.__OnRspQryMMInstrumentCommissionRate),
             b'OnRspQryMMOptionInstrCommRate' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcMMOptionInstrCommRateField), POINTER(CThostFtdcRspInfoField), c_int, c_bool)(CThostFtdcTraderSpi.__OnRspQryMMOptionInstrCommRate),
             b'OnRspQryInstrumentOrderCommRate' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcInstrumentOrderCommRateField), POINTER(CThostFtdcRspInfoField), c_int, c_bool)(CThostFtdcTraderSpi.__OnRspQryInstrumentOrderCommRate),
             b'OnRspQryOptionInstrTradeCost' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcOptionInstrTradeCostField), POINTER(CThostFtdcRspInfoField), c_int, c_bool)(CThostFtdcTraderSpi.__OnRspQryOptionInstrTradeCost),
             b'OnRspQryOptionInstrCommRate' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcOptionInstrCommRateField), POINTER(CThostFtdcRspInfoField), c_int, c_bool)(CThostFtdcTraderSpi.__OnRspQryOptionInstrCommRate),
             b'OnRspQryExecOrder' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcExecOrderField), POINTER(CThostFtdcRspInfoField), c_int, c_bool)(CThostFtdcTraderSpi.__OnRspQryExecOrder),
             b'OnRspQryForQuote' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcForQuoteField), POINTER(CThostFtdcRspInfoField), c_int, c_bool)(CThostFtdcTraderSpi.__OnRspQryForQuote),
             b'OnRspQryQuote' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcQuoteField), POINTER(CThostFtdcRspInfoField), c_int, c_bool)(CThostFtdcTraderSpi.__OnRspQryQuote),
             b'OnRspQryCombInstrumentGuard' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcCombInstrumentGuardField), POINTER(CThostFtdcRspInfoField), c_int, c_bool)(CThostFtdcTraderSpi.__OnRspQryCombInstrumentGuard),
             b'OnRspQryCombAction' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcCombActionField), POINTER(CThostFtdcRspInfoField), c_int, c_bool)(CThostFtdcTraderSpi.__OnRspQryCombAction),
             b'OnRspQryTransferSerial' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcTransferSerialField), POINTER(CThostFtdcRspInfoField), c_int, c_bool)(CThostFtdcTraderSpi.__OnRspQryTransferSerial),
             b'OnRspQryAccountregister' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcAccountregisterField), POINTER(CThostFtdcRspInfoField), c_int, c_bool)(CThostFtdcTraderSpi.__OnRspQryAccountregister),
             b'OnRspError' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcRspInfoField), c_int, c_bool)(CThostFtdcTraderSpi.__OnRspError),
             b'OnRtnOrder' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcOrderField))(CThostFtdcTraderSpi.__OnRtnOrder),
             b'OnRtnTrade' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcTradeField))(CThostFtdcTraderSpi.__OnRtnTrade),
             b'OnErrRtnOrderInsert' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcInputOrderField), POINTER(CThostFtdcRspInfoField))(CThostFtdcTraderSpi.__OnErrRtnOrderInsert),
             b'OnErrRtnOrderAction' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcOrderActionField), POINTER(CThostFtdcRspInfoField))(CThostFtdcTraderSpi.__OnErrRtnOrderAction),
             b'OnRtnInstrumentStatus' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcInstrumentStatusField))(CThostFtdcTraderSpi.__OnRtnInstrumentStatus),
             b'OnRtnBulletin' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcBulletinField))(CThostFtdcTraderSpi.__OnRtnBulletin),
             b'OnRtnTradingNotice' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcTradingNoticeInfoField))(CThostFtdcTraderSpi.__OnRtnTradingNotice),
             b'OnRtnErrorConditionalOrder' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcErrorConditionalOrderField))(CThostFtdcTraderSpi.__OnRtnErrorConditionalOrder),
             b'OnRtnExecOrder' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcExecOrderField))(CThostFtdcTraderSpi.__OnRtnExecOrder),
             b'OnErrRtnExecOrderInsert' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcInputExecOrderField), POINTER(CThostFtdcRspInfoField))(CThostFtdcTraderSpi.__OnErrRtnExecOrderInsert),
             b'OnErrRtnExecOrderAction' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcExecOrderActionField), POINTER(CThostFtdcRspInfoField))(CThostFtdcTraderSpi.__OnErrRtnExecOrderAction),
             b'OnErrRtnForQuoteInsert' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcInputForQuoteField), POINTER(CThostFtdcRspInfoField))(CThostFtdcTraderSpi.__OnErrRtnForQuoteInsert),
             b'OnRtnQuote' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcQuoteField))(CThostFtdcTraderSpi.__OnRtnQuote),
             b'OnErrRtnQuoteInsert' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcInputQuoteField), POINTER(CThostFtdcRspInfoField))(CThostFtdcTraderSpi.__OnErrRtnQuoteInsert),
             b'OnErrRtnQuoteAction' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcQuoteActionField), POINTER(CThostFtdcRspInfoField))(CThostFtdcTraderSpi.__OnErrRtnQuoteAction),
             b'OnRtnForQuoteRsp' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcForQuoteRspField))(CThostFtdcTraderSpi.__OnRtnForQuoteRsp),
             b'OnRtnCFMMCTradingAccountToken' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcCFMMCTradingAccountTokenField))(CThostFtdcTraderSpi.__OnRtnCFMMCTradingAccountToken),
             b'OnErrRtnBatchOrderAction' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcBatchOrderActionField), POINTER(CThostFtdcRspInfoField))(CThostFtdcTraderSpi.__OnErrRtnBatchOrderAction),
             b'OnRtnCombAction' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcCombActionField))(CThostFtdcTraderSpi.__OnRtnCombAction),
             b'OnErrRtnCombActionInsert' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcInputCombActionField), POINTER(CThostFtdcRspInfoField))(CThostFtdcTraderSpi.__OnErrRtnCombActionInsert),
             b'OnRspQryContractBank' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcContractBankField), POINTER(CThostFtdcRspInfoField), c_int, c_bool)(CThostFtdcTraderSpi.__OnRspQryContractBank),
             b'OnRspQryParkedOrder' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcParkedOrderField), POINTER(CThostFtdcRspInfoField), c_int, c_bool)(CThostFtdcTraderSpi.__OnRspQryParkedOrder),
             b'OnRspQryParkedOrderAction' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcParkedOrderActionField), POINTER(CThostFtdcRspInfoField), c_int, c_bool)(CThostFtdcTraderSpi.__OnRspQryParkedOrderAction),
             b'OnRspQryTradingNotice' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcTradingNoticeField), POINTER(CThostFtdcRspInfoField), c_int, c_bool)(CThostFtdcTraderSpi.__OnRspQryTradingNotice),
             b'OnRspQryBrokerTradingParams' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcBrokerTradingParamsField), POINTER(CThostFtdcRspInfoField), c_int, c_bool)(CThostFtdcTraderSpi.__OnRspQryBrokerTradingParams),
             b'OnRspQryBrokerTradingAlgos' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcBrokerTradingAlgosField), POINTER(CThostFtdcRspInfoField), c_int, c_bool)(CThostFtdcTraderSpi.__OnRspQryBrokerTradingAlgos),
             b'OnRspQueryCFMMCTradingAccountToken' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcQueryCFMMCTradingAccountTokenField), POINTER(CThostFtdcRspInfoField), c_int, c_bool)(CThostFtdcTraderSpi.__OnRspQueryCFMMCTradingAccountToken),
             b'OnRtnFromBankToFutureByBank' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcRspTransferField))(CThostFtdcTraderSpi.__OnRtnFromBankToFutureByBank),
             b'OnRtnFromFutureToBankByBank' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcRspTransferField))(CThostFtdcTraderSpi.__OnRtnFromFutureToBankByBank),
             b'OnRtnRepealFromBankToFutureByBank' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcRspRepealField))(CThostFtdcTraderSpi.__OnRtnRepealFromBankToFutureByBank),
             b'OnRtnRepealFromFutureToBankByBank' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcRspRepealField))(CThostFtdcTraderSpi.__OnRtnRepealFromFutureToBankByBank),
             b'OnRtnFromBankToFutureByFuture' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcRspTransferField))(CThostFtdcTraderSpi.__OnRtnFromBankToFutureByFuture),
             b'OnRtnFromFutureToBankByFuture' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcRspTransferField))(CThostFtdcTraderSpi.__OnRtnFromFutureToBankByFuture),
             b'OnRtnRepealFromBankToFutureByFutureManual' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcRspRepealField))(CThostFtdcTraderSpi.__OnRtnRepealFromBankToFutureByFutureManual),
             b'OnRtnRepealFromFutureToBankByFutureManual' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcRspRepealField))(CThostFtdcTraderSpi.__OnRtnRepealFromFutureToBankByFutureManual),
             b'OnRtnQueryBankBalanceByFuture' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcNotifyQueryAccountField))(CThostFtdcTraderSpi.__OnRtnQueryBankBalanceByFuture),
             b'OnErrRtnBankToFutureByFuture' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcReqTransferField), POINTER(CThostFtdcRspInfoField))(CThostFtdcTraderSpi.__OnErrRtnBankToFutureByFuture),
             b'OnErrRtnFutureToBankByFuture' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcReqTransferField), POINTER(CThostFtdcRspInfoField))(CThostFtdcTraderSpi.__OnErrRtnFutureToBankByFuture),
             b'OnErrRtnRepealBankToFutureByFutureManual' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcReqRepealField), POINTER(CThostFtdcRspInfoField))(CThostFtdcTraderSpi.__OnErrRtnRepealBankToFutureByFutureManual),
             b'OnErrRtnRepealFutureToBankByFutureManual' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcReqRepealField), POINTER(CThostFtdcRspInfoField))(CThostFtdcTraderSpi.__OnErrRtnRepealFutureToBankByFutureManual),
             b'OnErrRtnQueryBankBalanceByFuture' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcReqQueryAccountField), POINTER(CThostFtdcRspInfoField))(CThostFtdcTraderSpi.__OnErrRtnQueryBankBalanceByFuture),
             b'OnRtnRepealFromBankToFutureByFuture' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcRspRepealField))(CThostFtdcTraderSpi.__OnRtnRepealFromBankToFutureByFuture),
             b'OnRtnRepealFromFutureToBankByFuture' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcRspRepealField))(CThostFtdcTraderSpi.__OnRtnRepealFromFutureToBankByFuture),
             b'OnRspFromBankToFutureByFuture' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcReqTransferField), POINTER(CThostFtdcRspInfoField), c_int, c_bool)(CThostFtdcTraderSpi.__OnRspFromBankToFutureByFuture),
             b'OnRspFromFutureToBankByFuture' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcReqTransferField), POINTER(CThostFtdcRspInfoField), c_int, c_bool)(CThostFtdcTraderSpi.__OnRspFromFutureToBankByFuture),
             b'OnRspQueryBankAccountMoneyByFuture' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcReqQueryAccountField), POINTER(CThostFtdcRspInfoField), c_int, c_bool)(CThostFtdcTraderSpi.__OnRspQueryBankAccountMoneyByFuture),
             b'OnRtnOpenAccountByBank' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcOpenAccountField))(CThostFtdcTraderSpi.__OnRtnOpenAccountByBank),
             b'OnRtnCancelAccountByBank' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcCancelAccountField))(CThostFtdcTraderSpi.__OnRtnCancelAccountByBank),
             b'OnRtnChangeAccountByBank' : CFUNCTYPE(None, c_void_p, POINTER(CThostFtdcChangeAccountField))(CThostFtdcTraderSpi.__OnRtnChangeAccountByBank)
        }
        for (k, v) in self.__callback.items():
            CThostFtdcTraderSpi._dll.RegCallBack(self.__spi, k, v)

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

    def OnRspAuthenticate(self, pRspAuthenticateField, pRspInfo, nRequestID, bIsLast):
        pass

    def OnRspUserLogin(self, pRspUserLogin, pRspInfo, nRequestID, bIsLast):
        pass

    def OnRspUserLogout(self, pUserLogout, pRspInfo, nRequestID, bIsLast):
        pass

    def OnRspUserPasswordUpdate(self, pUserPasswordUpdate, pRspInfo, nRequestID, bIsLast):
        pass

    def OnRspTradingAccountPasswordUpdate(self, pTradingAccountPasswordUpdate, pRspInfo, nRequestID, bIsLast):
        pass

    def OnRspOrderInsert(self, pInputOrder, pRspInfo, nRequestID, bIsLast):
        pass

    def OnRspParkedOrderInsert(self, pParkedOrder, pRspInfo, nRequestID, bIsLast):
        pass

    def OnRspParkedOrderAction(self, pParkedOrderAction, pRspInfo, nRequestID, bIsLast):
        pass

    def OnRspOrderAction(self, pInputOrderAction, pRspInfo, nRequestID, bIsLast):
        pass

    def OnRspQueryMaxOrderVolume(self, pQueryMaxOrderVolume, pRspInfo, nRequestID, bIsLast):
        pass

    def OnRspSettlementInfoConfirm(self, pSettlementInfoConfirm, pRspInfo, nRequestID, bIsLast):
        pass

    def OnRspRemoveParkedOrder(self, pRemoveParkedOrder, pRspInfo, nRequestID, bIsLast):
        pass

    def OnRspRemoveParkedOrderAction(self, pRemoveParkedOrderAction, pRspInfo, nRequestID, bIsLast):
        pass

    def OnRspExecOrderInsert(self, pInputExecOrder, pRspInfo, nRequestID, bIsLast):
        pass

    def OnRspExecOrderAction(self, pInputExecOrderAction, pRspInfo, nRequestID, bIsLast):
        pass

    def OnRspForQuoteInsert(self, pInputForQuote, pRspInfo, nRequestID, bIsLast):
        pass

    def OnRspQuoteInsert(self, pInputQuote, pRspInfo, nRequestID, bIsLast):
        pass

    def OnRspQuoteAction(self, pInputQuoteAction, pRspInfo, nRequestID, bIsLast):
        pass

    def OnRspBatchOrderAction(self, pInputBatchOrderAction, pRspInfo, nRequestID, bIsLast):
        pass

    def OnRspCombActionInsert(self, pInputCombAction, pRspInfo, nRequestID, bIsLast):
        pass

    def OnRspQryOrder(self, pOrder, pRspInfo, nRequestID, bIsLast):
        pass

    def OnRspQryTrade(self, pTrade, pRspInfo, nRequestID, bIsLast):
        pass

    def OnRspQryInvestorPosition(self, pInvestorPosition, pRspInfo, nRequestID, bIsLast):
        pass

    def OnRspQryTradingAccount(self, pTradingAccount, pRspInfo, nRequestID, bIsLast):
        pass

    def OnRspQryInvestor(self, pInvestor, pRspInfo, nRequestID, bIsLast):
        pass

    def OnRspQryTradingCode(self, pTradingCode, pRspInfo, nRequestID, bIsLast):
        pass

    def OnRspQryInstrumentMarginRate(self, pInstrumentMarginRate, pRspInfo, nRequestID, bIsLast):
        pass

    def OnRspQryInstrumentCommissionRate(self, pInstrumentCommissionRate, pRspInfo, nRequestID, bIsLast):
        pass

    def OnRspQryExchange(self, pExchange, pRspInfo, nRequestID, bIsLast):
        pass

    def OnRspQryProduct(self, pProduct, pRspInfo, nRequestID, bIsLast):
        pass

    def OnRspQryInstrument(self, pInstrument, pRspInfo, nRequestID, bIsLast):
        pass

    def OnRspQryDepthMarketData(self, pDepthMarketData, pRspInfo, nRequestID, bIsLast):
        pass

    def OnRspQrySettlementInfo(self, pSettlementInfo, pRspInfo, nRequestID, bIsLast):
        pass

    def OnRspQryTransferBank(self, pTransferBank, pRspInfo, nRequestID, bIsLast):
        pass

    def OnRspQryInvestorPositionDetail(self, pInvestorPositionDetail, pRspInfo, nRequestID, bIsLast):
        pass

    def OnRspQryNotice(self, pNotice, pRspInfo, nRequestID, bIsLast):
        pass

    def OnRspQrySettlementInfoConfirm(self, pSettlementInfoConfirm, pRspInfo, nRequestID, bIsLast):
        pass

    def OnRspQryInvestorPositionCombineDetail(self, pInvestorPositionCombineDetail, pRspInfo, nRequestID, bIsLast):
        pass

    def OnRspQryCFMMCTradingAccountKey(self, pCFMMCTradingAccountKey, pRspInfo, nRequestID, bIsLast):
        pass

    def OnRspQryEWarrantOffset(self, pEWarrantOffset, pRspInfo, nRequestID, bIsLast):
        pass

    def OnRspQryInvestorProductGroupMargin(self, pInvestorProductGroupMargin, pRspInfo, nRequestID, bIsLast):
        pass

    def OnRspQryExchangeMarginRate(self, pExchangeMarginRate, pRspInfo, nRequestID, bIsLast):
        pass

    def OnRspQryExchangeMarginRateAdjust(self, pExchangeMarginRateAdjust, pRspInfo, nRequestID, bIsLast):
        pass

    def OnRspQryExchangeRate(self, pExchangeRate, pRspInfo, nRequestID, bIsLast):
        pass

    def OnRspQrySecAgentACIDMap(self, pSecAgentACIDMap, pRspInfo, nRequestID, bIsLast):
        pass

    def OnRspQryProductExchRate(self, pProductExchRate, pRspInfo, nRequestID, bIsLast):
        pass

    def OnRspQryProductGroup(self, pProductGroup, pRspInfo, nRequestID, bIsLast):
        pass

    def OnRspQryMMInstrumentCommissionRate(self, pMMInstrumentCommissionRate, pRspInfo, nRequestID, bIsLast):
        pass

    def OnRspQryMMOptionInstrCommRate(self, pMMOptionInstrCommRate, pRspInfo, nRequestID, bIsLast):
        pass

    def OnRspQryInstrumentOrderCommRate(self, pInstrumentOrderCommRate, pRspInfo, nRequestID, bIsLast):
        pass

    def OnRspQryOptionInstrTradeCost(self, pOptionInstrTradeCost, pRspInfo, nRequestID, bIsLast):
        pass

    def OnRspQryOptionInstrCommRate(self, pOptionInstrCommRate, pRspInfo, nRequestID, bIsLast):
        pass

    def OnRspQryExecOrder(self, pExecOrder, pRspInfo, nRequestID, bIsLast):
        pass

    def OnRspQryForQuote(self, pForQuote, pRspInfo, nRequestID, bIsLast):
        pass

    def OnRspQryQuote(self, pQuote, pRspInfo, nRequestID, bIsLast):
        pass

    def OnRspQryCombInstrumentGuard(self, pCombInstrumentGuard, pRspInfo, nRequestID, bIsLast):
        pass

    def OnRspQryCombAction(self, pCombAction, pRspInfo, nRequestID, bIsLast):
        pass

    def OnRspQryTransferSerial(self, pTransferSerial, pRspInfo, nRequestID, bIsLast):
        pass

    def OnRspQryAccountregister(self, pAccountregister, pRspInfo, nRequestID, bIsLast):
        pass

    def OnRspError(self, pRspInfo, nRequestID, bIsLast):
        pass

    def OnRtnOrder(self, pOrder):
        pass

    def OnRtnTrade(self, pTrade):
        pass

    def OnErrRtnOrderInsert(self, pInputOrder, pRspInfo):
        pass

    def OnErrRtnOrderAction(self, pOrderAction, pRspInfo):
        pass

    def OnRtnInstrumentStatus(self, pInstrumentStatus):
        pass

    def OnRtnBulletin(self, pBulletin):
        pass

    def OnRtnTradingNotice(self, pTradingNoticeInfo):
        pass

    def OnRtnErrorConditionalOrder(self, pErrorConditionalOrder):
        pass

    def OnRtnExecOrder(self, pExecOrder):
        pass

    def OnErrRtnExecOrderInsert(self, pInputExecOrder, pRspInfo):
        pass

    def OnErrRtnExecOrderAction(self, pExecOrderAction, pRspInfo):
        pass

    def OnErrRtnForQuoteInsert(self, pInputForQuote, pRspInfo):
        pass

    def OnRtnQuote(self, pQuote):
        pass

    def OnErrRtnQuoteInsert(self, pInputQuote, pRspInfo):
        pass

    def OnErrRtnQuoteAction(self, pQuoteAction, pRspInfo):
        pass

    def OnRtnForQuoteRsp(self, pForQuoteRsp):
        pass

    def OnRtnCFMMCTradingAccountToken(self, pCFMMCTradingAccountToken):
        pass

    def OnErrRtnBatchOrderAction(self, pBatchOrderAction, pRspInfo):
        pass

    def OnRtnCombAction(self, pCombAction):
        pass

    def OnErrRtnCombActionInsert(self, pInputCombAction, pRspInfo):
        pass

    def OnRspQryContractBank(self, pContractBank, pRspInfo, nRequestID, bIsLast):
        pass

    def OnRspQryParkedOrder(self, pParkedOrder, pRspInfo, nRequestID, bIsLast):
        pass

    def OnRspQryParkedOrderAction(self, pParkedOrderAction, pRspInfo, nRequestID, bIsLast):
        pass

    def OnRspQryTradingNotice(self, pTradingNotice, pRspInfo, nRequestID, bIsLast):
        pass

    def OnRspQryBrokerTradingParams(self, pBrokerTradingParams, pRspInfo, nRequestID, bIsLast):
        pass

    def OnRspQryBrokerTradingAlgos(self, pBrokerTradingAlgos, pRspInfo, nRequestID, bIsLast):
        pass

    def OnRspQueryCFMMCTradingAccountToken(self, pQueryCFMMCTradingAccountToken, pRspInfo, nRequestID, bIsLast):
        pass

    def OnRtnFromBankToFutureByBank(self, pRspTransfer):
        pass

    def OnRtnFromFutureToBankByBank(self, pRspTransfer):
        pass

    def OnRtnRepealFromBankToFutureByBank(self, pRspRepeal):
        pass

    def OnRtnRepealFromFutureToBankByBank(self, pRspRepeal):
        pass

    def OnRtnFromBankToFutureByFuture(self, pRspTransfer):
        pass

    def OnRtnFromFutureToBankByFuture(self, pRspTransfer):
        pass

    def OnRtnRepealFromBankToFutureByFutureManual(self, pRspRepeal):
        pass

    def OnRtnRepealFromFutureToBankByFutureManual(self, pRspRepeal):
        pass

    def OnRtnQueryBankBalanceByFuture(self, pNotifyQueryAccount):
        pass

    def OnErrRtnBankToFutureByFuture(self, pReqTransfer, pRspInfo):
        pass

    def OnErrRtnFutureToBankByFuture(self, pReqTransfer, pRspInfo):
        pass

    def OnErrRtnRepealBankToFutureByFutureManual(self, pReqRepeal, pRspInfo):
        pass

    def OnErrRtnRepealFutureToBankByFutureManual(self, pReqRepeal, pRspInfo):
        pass

    def OnErrRtnQueryBankBalanceByFuture(self, pReqQueryAccount, pRspInfo):
        pass

    def OnRtnRepealFromBankToFutureByFuture(self, pRspRepeal):
        pass

    def OnRtnRepealFromFutureToBankByFuture(self, pRspRepeal):
        pass

    def OnRspFromBankToFutureByFuture(self, pReqTransfer, pRspInfo, nRequestID, bIsLast):
        pass

    def OnRspFromFutureToBankByFuture(self, pReqTransfer, pRspInfo, nRequestID, bIsLast):
        pass

    def OnRspQueryBankAccountMoneyByFuture(self, pReqQueryAccount, pRspInfo, nRequestID, bIsLast):
        pass

    def OnRtnOpenAccountByBank(self, pOpenAccount):
        pass

    def OnRtnCancelAccountByBank(self, pCancelAccount):
        pass

    def OnRtnChangeAccountByBank(self, pChangeAccount):
        pass


    @staticmethod
    def __OnFrontConnected(spi):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnFrontConnected()

    @staticmethod
    def __OnFrontDisconnected(spi, nReason):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnFrontDisconnected(nReason)

    @staticmethod
    def __OnHeartBeatWarning(spi, nTimeLapse):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnHeartBeatWarning(nTimeLapse)

    @staticmethod
    def __OnRspAuthenticate(spi, pRspAuthenticateField, pRspInfo, nRequestID, bIsLast):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnRspAuthenticate(pRspAuthenticateField, pRspInfo, nRequestID, bIsLast)

    @staticmethod
    def __OnRspUserLogin(spi, pRspUserLogin, pRspInfo, nRequestID, bIsLast):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnRspUserLogin(pRspUserLogin, pRspInfo, nRequestID, bIsLast)

    @staticmethod
    def __OnRspUserLogout(spi, pUserLogout, pRspInfo, nRequestID, bIsLast):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnRspUserLogout(pUserLogout, pRspInfo, nRequestID, bIsLast)

    @staticmethod
    def __OnRspUserPasswordUpdate(spi, pUserPasswordUpdate, pRspInfo, nRequestID, bIsLast):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnRspUserPasswordUpdate(pUserPasswordUpdate, pRspInfo, nRequestID, bIsLast)

    @staticmethod
    def __OnRspTradingAccountPasswordUpdate(spi, pTradingAccountPasswordUpdate, pRspInfo, nRequestID, bIsLast):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnRspTradingAccountPasswordUpdate(pTradingAccountPasswordUpdate, pRspInfo, nRequestID, bIsLast)

    @staticmethod
    def __OnRspOrderInsert(spi, pInputOrder, pRspInfo, nRequestID, bIsLast):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnRspOrderInsert(pInputOrder, pRspInfo, nRequestID, bIsLast)

    @staticmethod
    def __OnRspParkedOrderInsert(spi, pParkedOrder, pRspInfo, nRequestID, bIsLast):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnRspParkedOrderInsert(pParkedOrder, pRspInfo, nRequestID, bIsLast)

    @staticmethod
    def __OnRspParkedOrderAction(spi, pParkedOrderAction, pRspInfo, nRequestID, bIsLast):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnRspParkedOrderAction(pParkedOrderAction, pRspInfo, nRequestID, bIsLast)

    @staticmethod
    def __OnRspOrderAction(spi, pInputOrderAction, pRspInfo, nRequestID, bIsLast):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnRspOrderAction(pInputOrderAction, pRspInfo, nRequestID, bIsLast)

    @staticmethod
    def __OnRspQueryMaxOrderVolume(spi, pQueryMaxOrderVolume, pRspInfo, nRequestID, bIsLast):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnRspQueryMaxOrderVolume(pQueryMaxOrderVolume, pRspInfo, nRequestID, bIsLast)

    @staticmethod
    def __OnRspSettlementInfoConfirm(spi, pSettlementInfoConfirm, pRspInfo, nRequestID, bIsLast):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnRspSettlementInfoConfirm(pSettlementInfoConfirm, pRspInfo, nRequestID, bIsLast)

    @staticmethod
    def __OnRspRemoveParkedOrder(spi, pRemoveParkedOrder, pRspInfo, nRequestID, bIsLast):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnRspRemoveParkedOrder(pRemoveParkedOrder, pRspInfo, nRequestID, bIsLast)

    @staticmethod
    def __OnRspRemoveParkedOrderAction(spi, pRemoveParkedOrderAction, pRspInfo, nRequestID, bIsLast):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnRspRemoveParkedOrderAction(pRemoveParkedOrderAction, pRspInfo, nRequestID, bIsLast)

    @staticmethod
    def __OnRspExecOrderInsert(spi, pInputExecOrder, pRspInfo, nRequestID, bIsLast):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnRspExecOrderInsert(pInputExecOrder, pRspInfo, nRequestID, bIsLast)

    @staticmethod
    def __OnRspExecOrderAction(spi, pInputExecOrderAction, pRspInfo, nRequestID, bIsLast):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnRspExecOrderAction(pInputExecOrderAction, pRspInfo, nRequestID, bIsLast)

    @staticmethod
    def __OnRspForQuoteInsert(spi, pInputForQuote, pRspInfo, nRequestID, bIsLast):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnRspForQuoteInsert(pInputForQuote, pRspInfo, nRequestID, bIsLast)

    @staticmethod
    def __OnRspQuoteInsert(spi, pInputQuote, pRspInfo, nRequestID, bIsLast):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnRspQuoteInsert(pInputQuote, pRspInfo, nRequestID, bIsLast)

    @staticmethod
    def __OnRspQuoteAction(spi, pInputQuoteAction, pRspInfo, nRequestID, bIsLast):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnRspQuoteAction(pInputQuoteAction, pRspInfo, nRequestID, bIsLast)

    @staticmethod
    def __OnRspBatchOrderAction(spi, pInputBatchOrderAction, pRspInfo, nRequestID, bIsLast):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnRspBatchOrderAction(pInputBatchOrderAction, pRspInfo, nRequestID, bIsLast)

    @staticmethod
    def __OnRspCombActionInsert(spi, pInputCombAction, pRspInfo, nRequestID, bIsLast):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnRspCombActionInsert(pInputCombAction, pRspInfo, nRequestID, bIsLast)

    @staticmethod
    def __OnRspQryOrder(spi, pOrder, pRspInfo, nRequestID, bIsLast):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnRspQryOrder(pOrder, pRspInfo, nRequestID, bIsLast)

    @staticmethod
    def __OnRspQryTrade(spi, pTrade, pRspInfo, nRequestID, bIsLast):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnRspQryTrade(pTrade, pRspInfo, nRequestID, bIsLast)

    @staticmethod
    def __OnRspQryInvestorPosition(spi, pInvestorPosition, pRspInfo, nRequestID, bIsLast):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnRspQryInvestorPosition(pInvestorPosition, pRspInfo, nRequestID, bIsLast)

    @staticmethod
    def __OnRspQryTradingAccount(spi, pTradingAccount, pRspInfo, nRequestID, bIsLast):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnRspQryTradingAccount(pTradingAccount, pRspInfo, nRequestID, bIsLast)

    @staticmethod
    def __OnRspQryInvestor(spi, pInvestor, pRspInfo, nRequestID, bIsLast):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnRspQryInvestor(pInvestor, pRspInfo, nRequestID, bIsLast)

    @staticmethod
    def __OnRspQryTradingCode(spi, pTradingCode, pRspInfo, nRequestID, bIsLast):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnRspQryTradingCode(pTradingCode, pRspInfo, nRequestID, bIsLast)

    @staticmethod
    def __OnRspQryInstrumentMarginRate(spi, pInstrumentMarginRate, pRspInfo, nRequestID, bIsLast):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnRspQryInstrumentMarginRate(pInstrumentMarginRate, pRspInfo, nRequestID, bIsLast)

    @staticmethod
    def __OnRspQryInstrumentCommissionRate(spi, pInstrumentCommissionRate, pRspInfo, nRequestID, bIsLast):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnRspQryInstrumentCommissionRate(pInstrumentCommissionRate, pRspInfo, nRequestID, bIsLast)

    @staticmethod
    def __OnRspQryExchange(spi, pExchange, pRspInfo, nRequestID, bIsLast):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnRspQryExchange(pExchange, pRspInfo, nRequestID, bIsLast)

    @staticmethod
    def __OnRspQryProduct(spi, pProduct, pRspInfo, nRequestID, bIsLast):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnRspQryProduct(pProduct, pRspInfo, nRequestID, bIsLast)

    @staticmethod
    def __OnRspQryInstrument(spi, pInstrument, pRspInfo, nRequestID, bIsLast):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnRspQryInstrument(pInstrument, pRspInfo, nRequestID, bIsLast)

    @staticmethod
    def __OnRspQryDepthMarketData(spi, pDepthMarketData, pRspInfo, nRequestID, bIsLast):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnRspQryDepthMarketData(pDepthMarketData, pRspInfo, nRequestID, bIsLast)

    @staticmethod
    def __OnRspQrySettlementInfo(spi, pSettlementInfo, pRspInfo, nRequestID, bIsLast):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnRspQrySettlementInfo(pSettlementInfo, pRspInfo, nRequestID, bIsLast)

    @staticmethod
    def __OnRspQryTransferBank(spi, pTransferBank, pRspInfo, nRequestID, bIsLast):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnRspQryTransferBank(pTransferBank, pRspInfo, nRequestID, bIsLast)

    @staticmethod
    def __OnRspQryInvestorPositionDetail(spi, pInvestorPositionDetail, pRspInfo, nRequestID, bIsLast):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnRspQryInvestorPositionDetail(pInvestorPositionDetail, pRspInfo, nRequestID, bIsLast)

    @staticmethod
    def __OnRspQryNotice(spi, pNotice, pRspInfo, nRequestID, bIsLast):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnRspQryNotice(pNotice, pRspInfo, nRequestID, bIsLast)

    @staticmethod
    def __OnRspQrySettlementInfoConfirm(spi, pSettlementInfoConfirm, pRspInfo, nRequestID, bIsLast):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnRspQrySettlementInfoConfirm(pSettlementInfoConfirm, pRspInfo, nRequestID, bIsLast)

    @staticmethod
    def __OnRspQryInvestorPositionCombineDetail(spi, pInvestorPositionCombineDetail, pRspInfo, nRequestID, bIsLast):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnRspQryInvestorPositionCombineDetail(pInvestorPositionCombineDetail, pRspInfo, nRequestID, bIsLast)

    @staticmethod
    def __OnRspQryCFMMCTradingAccountKey(spi, pCFMMCTradingAccountKey, pRspInfo, nRequestID, bIsLast):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnRspQryCFMMCTradingAccountKey(pCFMMCTradingAccountKey, pRspInfo, nRequestID, bIsLast)

    @staticmethod
    def __OnRspQryEWarrantOffset(spi, pEWarrantOffset, pRspInfo, nRequestID, bIsLast):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnRspQryEWarrantOffset(pEWarrantOffset, pRspInfo, nRequestID, bIsLast)

    @staticmethod
    def __OnRspQryInvestorProductGroupMargin(spi, pInvestorProductGroupMargin, pRspInfo, nRequestID, bIsLast):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnRspQryInvestorProductGroupMargin(pInvestorProductGroupMargin, pRspInfo, nRequestID, bIsLast)

    @staticmethod
    def __OnRspQryExchangeMarginRate(spi, pExchangeMarginRate, pRspInfo, nRequestID, bIsLast):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnRspQryExchangeMarginRate(pExchangeMarginRate, pRspInfo, nRequestID, bIsLast)

    @staticmethod
    def __OnRspQryExchangeMarginRateAdjust(spi, pExchangeMarginRateAdjust, pRspInfo, nRequestID, bIsLast):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnRspQryExchangeMarginRateAdjust(pExchangeMarginRateAdjust, pRspInfo, nRequestID, bIsLast)

    @staticmethod
    def __OnRspQryExchangeRate(spi, pExchangeRate, pRspInfo, nRequestID, bIsLast):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnRspQryExchangeRate(pExchangeRate, pRspInfo, nRequestID, bIsLast)

    @staticmethod
    def __OnRspQrySecAgentACIDMap(spi, pSecAgentACIDMap, pRspInfo, nRequestID, bIsLast):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnRspQrySecAgentACIDMap(pSecAgentACIDMap, pRspInfo, nRequestID, bIsLast)

    @staticmethod
    def __OnRspQryProductExchRate(spi, pProductExchRate, pRspInfo, nRequestID, bIsLast):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnRspQryProductExchRate(pProductExchRate, pRspInfo, nRequestID, bIsLast)

    @staticmethod
    def __OnRspQryProductGroup(spi, pProductGroup, pRspInfo, nRequestID, bIsLast):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnRspQryProductGroup(pProductGroup, pRspInfo, nRequestID, bIsLast)

    @staticmethod
    def __OnRspQryMMInstrumentCommissionRate(spi, pMMInstrumentCommissionRate, pRspInfo, nRequestID, bIsLast):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnRspQryMMInstrumentCommissionRate(pMMInstrumentCommissionRate, pRspInfo, nRequestID, bIsLast)

    @staticmethod
    def __OnRspQryMMOptionInstrCommRate(spi, pMMOptionInstrCommRate, pRspInfo, nRequestID, bIsLast):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnRspQryMMOptionInstrCommRate(pMMOptionInstrCommRate, pRspInfo, nRequestID, bIsLast)

    @staticmethod
    def __OnRspQryInstrumentOrderCommRate(spi, pInstrumentOrderCommRate, pRspInfo, nRequestID, bIsLast):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnRspQryInstrumentOrderCommRate(pInstrumentOrderCommRate, pRspInfo, nRequestID, bIsLast)

    @staticmethod
    def __OnRspQryOptionInstrTradeCost(spi, pOptionInstrTradeCost, pRspInfo, nRequestID, bIsLast):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnRspQryOptionInstrTradeCost(pOptionInstrTradeCost, pRspInfo, nRequestID, bIsLast)

    @staticmethod
    def __OnRspQryOptionInstrCommRate(spi, pOptionInstrCommRate, pRspInfo, nRequestID, bIsLast):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnRspQryOptionInstrCommRate(pOptionInstrCommRate, pRspInfo, nRequestID, bIsLast)

    @staticmethod
    def __OnRspQryExecOrder(spi, pExecOrder, pRspInfo, nRequestID, bIsLast):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnRspQryExecOrder(pExecOrder, pRspInfo, nRequestID, bIsLast)

    @staticmethod
    def __OnRspQryForQuote(spi, pForQuote, pRspInfo, nRequestID, bIsLast):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnRspQryForQuote(pForQuote, pRspInfo, nRequestID, bIsLast)

    @staticmethod
    def __OnRspQryQuote(spi, pQuote, pRspInfo, nRequestID, bIsLast):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnRspQryQuote(pQuote, pRspInfo, nRequestID, bIsLast)

    @staticmethod
    def __OnRspQryCombInstrumentGuard(spi, pCombInstrumentGuard, pRspInfo, nRequestID, bIsLast):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnRspQryCombInstrumentGuard(pCombInstrumentGuard, pRspInfo, nRequestID, bIsLast)

    @staticmethod
    def __OnRspQryCombAction(spi, pCombAction, pRspInfo, nRequestID, bIsLast):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnRspQryCombAction(pCombAction, pRspInfo, nRequestID, bIsLast)

    @staticmethod
    def __OnRspQryTransferSerial(spi, pTransferSerial, pRspInfo, nRequestID, bIsLast):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnRspQryTransferSerial(pTransferSerial, pRspInfo, nRequestID, bIsLast)

    @staticmethod
    def __OnRspQryAccountregister(spi, pAccountregister, pRspInfo, nRequestID, bIsLast):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnRspQryAccountregister(pAccountregister, pRspInfo, nRequestID, bIsLast)

    @staticmethod
    def __OnRspError(spi, pRspInfo, nRequestID, bIsLast):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnRspError(pRspInfo, nRequestID, bIsLast)

    @staticmethod
    def __OnRtnOrder(spi, pOrder):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnRtnOrder(pOrder)

    @staticmethod
    def __OnRtnTrade(spi, pTrade):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnRtnTrade(pTrade)

    @staticmethod
    def __OnErrRtnOrderInsert(spi, pInputOrder, pRspInfo):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnErrRtnOrderInsert(pInputOrder, pRspInfo)

    @staticmethod
    def __OnErrRtnOrderAction(spi, pOrderAction, pRspInfo):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnErrRtnOrderAction(pOrderAction, pRspInfo)

    @staticmethod
    def __OnRtnInstrumentStatus(spi, pInstrumentStatus):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnRtnInstrumentStatus(pInstrumentStatus)

    @staticmethod
    def __OnRtnBulletin(spi, pBulletin):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnRtnBulletin(pBulletin)

    @staticmethod
    def __OnRtnTradingNotice(spi, pTradingNoticeInfo):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnRtnTradingNotice(pTradingNoticeInfo)

    @staticmethod
    def __OnRtnErrorConditionalOrder(spi, pErrorConditionalOrder):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnRtnErrorConditionalOrder(pErrorConditionalOrder)

    @staticmethod
    def __OnRtnExecOrder(spi, pExecOrder):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnRtnExecOrder(pExecOrder)

    @staticmethod
    def __OnErrRtnExecOrderInsert(spi, pInputExecOrder, pRspInfo):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnErrRtnExecOrderInsert(pInputExecOrder, pRspInfo)

    @staticmethod
    def __OnErrRtnExecOrderAction(spi, pExecOrderAction, pRspInfo):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnErrRtnExecOrderAction(pExecOrderAction, pRspInfo)

    @staticmethod
    def __OnErrRtnForQuoteInsert(spi, pInputForQuote, pRspInfo):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnErrRtnForQuoteInsert(pInputForQuote, pRspInfo)

    @staticmethod
    def __OnRtnQuote(spi, pQuote):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnRtnQuote(pQuote)

    @staticmethod
    def __OnErrRtnQuoteInsert(spi, pInputQuote, pRspInfo):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnErrRtnQuoteInsert(pInputQuote, pRspInfo)

    @staticmethod
    def __OnErrRtnQuoteAction(spi, pQuoteAction, pRspInfo):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnErrRtnQuoteAction(pQuoteAction, pRspInfo)

    @staticmethod
    def __OnRtnForQuoteRsp(spi, pForQuoteRsp):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnRtnForQuoteRsp(pForQuoteRsp)

    @staticmethod
    def __OnRtnCFMMCTradingAccountToken(spi, pCFMMCTradingAccountToken):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnRtnCFMMCTradingAccountToken(pCFMMCTradingAccountToken)

    @staticmethod
    def __OnErrRtnBatchOrderAction(spi, pBatchOrderAction, pRspInfo):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnErrRtnBatchOrderAction(pBatchOrderAction, pRspInfo)

    @staticmethod
    def __OnRtnCombAction(spi, pCombAction):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnRtnCombAction(pCombAction)

    @staticmethod
    def __OnErrRtnCombActionInsert(spi, pInputCombAction, pRspInfo):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnErrRtnCombActionInsert(pInputCombAction, pRspInfo)

    @staticmethod
    def __OnRspQryContractBank(spi, pContractBank, pRspInfo, nRequestID, bIsLast):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnRspQryContractBank(pContractBank, pRspInfo, nRequestID, bIsLast)

    @staticmethod
    def __OnRspQryParkedOrder(spi, pParkedOrder, pRspInfo, nRequestID, bIsLast):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnRspQryParkedOrder(pParkedOrder, pRspInfo, nRequestID, bIsLast)

    @staticmethod
    def __OnRspQryParkedOrderAction(spi, pParkedOrderAction, pRspInfo, nRequestID, bIsLast):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnRspQryParkedOrderAction(pParkedOrderAction, pRspInfo, nRequestID, bIsLast)

    @staticmethod
    def __OnRspQryTradingNotice(spi, pTradingNotice, pRspInfo, nRequestID, bIsLast):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnRspQryTradingNotice(pTradingNotice, pRspInfo, nRequestID, bIsLast)

    @staticmethod
    def __OnRspQryBrokerTradingParams(spi, pBrokerTradingParams, pRspInfo, nRequestID, bIsLast):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnRspQryBrokerTradingParams(pBrokerTradingParams, pRspInfo, nRequestID, bIsLast)

    @staticmethod
    def __OnRspQryBrokerTradingAlgos(spi, pBrokerTradingAlgos, pRspInfo, nRequestID, bIsLast):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnRspQryBrokerTradingAlgos(pBrokerTradingAlgos, pRspInfo, nRequestID, bIsLast)

    @staticmethod
    def __OnRspQueryCFMMCTradingAccountToken(spi, pQueryCFMMCTradingAccountToken, pRspInfo, nRequestID, bIsLast):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnRspQueryCFMMCTradingAccountToken(pQueryCFMMCTradingAccountToken, pRspInfo, nRequestID, bIsLast)

    @staticmethod
    def __OnRtnFromBankToFutureByBank(spi, pRspTransfer):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnRtnFromBankToFutureByBank(pRspTransfer)

    @staticmethod
    def __OnRtnFromFutureToBankByBank(spi, pRspTransfer):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnRtnFromFutureToBankByBank(pRspTransfer)

    @staticmethod
    def __OnRtnRepealFromBankToFutureByBank(spi, pRspRepeal):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnRtnRepealFromBankToFutureByBank(pRspRepeal)

    @staticmethod
    def __OnRtnRepealFromFutureToBankByBank(spi, pRspRepeal):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnRtnRepealFromFutureToBankByBank(pRspRepeal)

    @staticmethod
    def __OnRtnFromBankToFutureByFuture(spi, pRspTransfer):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnRtnFromBankToFutureByFuture(pRspTransfer)

    @staticmethod
    def __OnRtnFromFutureToBankByFuture(spi, pRspTransfer):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnRtnFromFutureToBankByFuture(pRspTransfer)

    @staticmethod
    def __OnRtnRepealFromBankToFutureByFutureManual(spi, pRspRepeal):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnRtnRepealFromBankToFutureByFutureManual(pRspRepeal)

    @staticmethod
    def __OnRtnRepealFromFutureToBankByFutureManual(spi, pRspRepeal):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnRtnRepealFromFutureToBankByFutureManual(pRspRepeal)

    @staticmethod
    def __OnRtnQueryBankBalanceByFuture(spi, pNotifyQueryAccount):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnRtnQueryBankBalanceByFuture(pNotifyQueryAccount)

    @staticmethod
    def __OnErrRtnBankToFutureByFuture(spi, pReqTransfer, pRspInfo):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnErrRtnBankToFutureByFuture(pReqTransfer, pRspInfo)

    @staticmethod
    def __OnErrRtnFutureToBankByFuture(spi, pReqTransfer, pRspInfo):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnErrRtnFutureToBankByFuture(pReqTransfer, pRspInfo)

    @staticmethod
    def __OnErrRtnRepealBankToFutureByFutureManual(spi, pReqRepeal, pRspInfo):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnErrRtnRepealBankToFutureByFutureManual(pReqRepeal, pRspInfo)

    @staticmethod
    def __OnErrRtnRepealFutureToBankByFutureManual(spi, pReqRepeal, pRspInfo):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnErrRtnRepealFutureToBankByFutureManual(pReqRepeal, pRspInfo)

    @staticmethod
    def __OnErrRtnQueryBankBalanceByFuture(spi, pReqQueryAccount, pRspInfo):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnErrRtnQueryBankBalanceByFuture(pReqQueryAccount, pRspInfo)

    @staticmethod
    def __OnRtnRepealFromBankToFutureByFuture(spi, pRspRepeal):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnRtnRepealFromBankToFutureByFuture(pRspRepeal)

    @staticmethod
    def __OnRtnRepealFromFutureToBankByFuture(spi, pRspRepeal):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnRtnRepealFromFutureToBankByFuture(pRspRepeal)

    @staticmethod
    def __OnRspFromBankToFutureByFuture(spi, pReqTransfer, pRspInfo, nRequestID, bIsLast):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnRspFromBankToFutureByFuture(pReqTransfer, pRspInfo, nRequestID, bIsLast)

    @staticmethod
    def __OnRspFromFutureToBankByFuture(spi, pReqTransfer, pRspInfo, nRequestID, bIsLast):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnRspFromFutureToBankByFuture(pReqTransfer, pRspInfo, nRequestID, bIsLast)

    @staticmethod
    def __OnRspQueryBankAccountMoneyByFuture(spi, pReqQueryAccount, pRspInfo, nRequestID, bIsLast):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnRspQueryBankAccountMoneyByFuture(pReqQueryAccount, pRspInfo, nRequestID, bIsLast)

    @staticmethod
    def __OnRtnOpenAccountByBank(spi, pOpenAccount):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnRtnOpenAccountByBank(pOpenAccount)

    @staticmethod
    def __OnRtnCancelAccountByBank(spi, pCancelAccount):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnRtnCancelAccountByBank(pCancelAccount)

    @staticmethod
    def __OnRtnChangeAccountByBank(spi, pChangeAccount):
        CThostFtdcTraderSpi.__SpiToObj[spi].OnRtnChangeAccountByBank(pChangeAccount)

