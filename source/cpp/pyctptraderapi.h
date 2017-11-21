#ifndef __PYCTPTRADERSPI_H__
#define __PYCTPTRADERSPI_H__

#include "ThostFtdcUserApiDataType.h"
#include "ThostFtdcUserApiStruct.h"
#include "ThostFtdcMdApi.h"
#include "ThostFtdcTraderApi.h"

extern "C" {

    void* CreateSpi();

    int RegCallBack(void* spi, char* name, void *callback);

    void* CreateApi(char* pszFlowPath);

    void Release(void* api);

    void Init(void* api);

    int Join(void* api);

    const char * GetTradingDay(void* api);

    void RegisterFront(void* api, char * pszFrontAddress);

    void RegisterNameServer(void* api, char * pszNsAddress);

    void RegisterFensUserInfo(void* api, CThostFtdcFensUserInfoField * pFensUserInfo);

    void RegisterSpi(void* api, CThostFtdcTraderSpi * pSpi);

    void SubscribePrivateTopic(void* api, THOST_TE_RESUME_TYPE nResumeType);

    void SubscribePublicTopic(void* api, THOST_TE_RESUME_TYPE nResumeType);

    int ReqAuthenticate(void* api, CThostFtdcReqAuthenticateField * pReqAuthenticateField, int nRequestID);

    int ReqUserLogin(void* api, CThostFtdcReqUserLoginField * pReqUserLoginField, int nRequestID);

    int ReqUserLogout(void* api, CThostFtdcUserLogoutField * pUserLogout, int nRequestID);

    int ReqUserPasswordUpdate(void* api, CThostFtdcUserPasswordUpdateField * pUserPasswordUpdate, int nRequestID);

    int ReqTradingAccountPasswordUpdate(void* api, CThostFtdcTradingAccountPasswordUpdateField * pTradingAccountPasswordUpdate, int nRequestID);

    int ReqOrderInsert(void* api, CThostFtdcInputOrderField * pInputOrder, int nRequestID);

    int ReqParkedOrderInsert(void* api, CThostFtdcParkedOrderField * pParkedOrder, int nRequestID);

    int ReqParkedOrderAction(void* api, CThostFtdcParkedOrderActionField * pParkedOrderAction, int nRequestID);

    int ReqOrderAction(void* api, CThostFtdcInputOrderActionField * pInputOrderAction, int nRequestID);

    int ReqQueryMaxOrderVolume(void* api, CThostFtdcQueryMaxOrderVolumeField * pQueryMaxOrderVolume, int nRequestID);

    int ReqSettlementInfoConfirm(void* api, CThostFtdcSettlementInfoConfirmField * pSettlementInfoConfirm, int nRequestID);

    int ReqRemoveParkedOrder(void* api, CThostFtdcRemoveParkedOrderField * pRemoveParkedOrder, int nRequestID);

    int ReqRemoveParkedOrderAction(void* api, CThostFtdcRemoveParkedOrderActionField * pRemoveParkedOrderAction, int nRequestID);

    int ReqExecOrderInsert(void* api, CThostFtdcInputExecOrderField * pInputExecOrder, int nRequestID);

    int ReqExecOrderAction(void* api, CThostFtdcInputExecOrderActionField * pInputExecOrderAction, int nRequestID);

    int ReqForQuoteInsert(void* api, CThostFtdcInputForQuoteField * pInputForQuote, int nRequestID);

    int ReqQuoteInsert(void* api, CThostFtdcInputQuoteField * pInputQuote, int nRequestID);

    int ReqQuoteAction(void* api, CThostFtdcInputQuoteActionField * pInputQuoteAction, int nRequestID);

    int ReqBatchOrderAction(void* api, CThostFtdcInputBatchOrderActionField * pInputBatchOrderAction, int nRequestID);

    int ReqCombActionInsert(void* api, CThostFtdcInputCombActionField * pInputCombAction, int nRequestID);

    int ReqQryOrder(void* api, CThostFtdcQryOrderField * pQryOrder, int nRequestID);

    int ReqQryTrade(void* api, CThostFtdcQryTradeField * pQryTrade, int nRequestID);

    int ReqQryInvestorPosition(void* api, CThostFtdcQryInvestorPositionField * pQryInvestorPosition, int nRequestID);

    int ReqQryTradingAccount(void* api, CThostFtdcQryTradingAccountField * pQryTradingAccount, int nRequestID);

    int ReqQryInvestor(void* api, CThostFtdcQryInvestorField * pQryInvestor, int nRequestID);

    int ReqQryTradingCode(void* api, CThostFtdcQryTradingCodeField * pQryTradingCode, int nRequestID);

    int ReqQryInstrumentMarginRate(void* api, CThostFtdcQryInstrumentMarginRateField * pQryInstrumentMarginRate, int nRequestID);

    int ReqQryInstrumentCommissionRate(void* api, CThostFtdcQryInstrumentCommissionRateField * pQryInstrumentCommissionRate, int nRequestID);

    int ReqQryExchange(void* api, CThostFtdcQryExchangeField * pQryExchange, int nRequestID);

    int ReqQryProduct(void* api, CThostFtdcQryProductField * pQryProduct, int nRequestID);

    int ReqQryInstrument(void* api, CThostFtdcQryInstrumentField * pQryInstrument, int nRequestID);

    int ReqQryDepthMarketData(void* api, CThostFtdcQryDepthMarketDataField * pQryDepthMarketData, int nRequestID);

    int ReqQrySettlementInfo(void* api, CThostFtdcQrySettlementInfoField * pQrySettlementInfo, int nRequestID);

    int ReqQryTransferBank(void* api, CThostFtdcQryTransferBankField * pQryTransferBank, int nRequestID);

    int ReqQryInvestorPositionDetail(void* api, CThostFtdcQryInvestorPositionDetailField * pQryInvestorPositionDetail, int nRequestID);

    int ReqQryNotice(void* api, CThostFtdcQryNoticeField * pQryNotice, int nRequestID);

    int ReqQrySettlementInfoConfirm(void* api, CThostFtdcQrySettlementInfoConfirmField * pQrySettlementInfoConfirm, int nRequestID);

    int ReqQryInvestorPositionCombineDetail(void* api, CThostFtdcQryInvestorPositionCombineDetailField * pQryInvestorPositionCombineDetail, int nRequestID);

    int ReqQryCFMMCTradingAccountKey(void* api, CThostFtdcQryCFMMCTradingAccountKeyField * pQryCFMMCTradingAccountKey, int nRequestID);

    int ReqQryEWarrantOffset(void* api, CThostFtdcQryEWarrantOffsetField * pQryEWarrantOffset, int nRequestID);

    int ReqQryInvestorProductGroupMargin(void* api, CThostFtdcQryInvestorProductGroupMarginField * pQryInvestorProductGroupMargin, int nRequestID);

    int ReqQryExchangeMarginRate(void* api, CThostFtdcQryExchangeMarginRateField * pQryExchangeMarginRate, int nRequestID);

    int ReqQryExchangeMarginRateAdjust(void* api, CThostFtdcQryExchangeMarginRateAdjustField * pQryExchangeMarginRateAdjust, int nRequestID);

    int ReqQryExchangeRate(void* api, CThostFtdcQryExchangeRateField * pQryExchangeRate, int nRequestID);

    int ReqQrySecAgentACIDMap(void* api, CThostFtdcQrySecAgentACIDMapField * pQrySecAgentACIDMap, int nRequestID);

    int ReqQryProductExchRate(void* api, CThostFtdcQryProductExchRateField * pQryProductExchRate, int nRequestID);

    int ReqQryProductGroup(void* api, CThostFtdcQryProductGroupField * pQryProductGroup, int nRequestID);

    int ReqQryMMInstrumentCommissionRate(void* api, CThostFtdcQryMMInstrumentCommissionRateField * pQryMMInstrumentCommissionRate, int nRequestID);

    int ReqQryMMOptionInstrCommRate(void* api, CThostFtdcQryMMOptionInstrCommRateField * pQryMMOptionInstrCommRate, int nRequestID);

    int ReqQryInstrumentOrderCommRate(void* api, CThostFtdcQryInstrumentOrderCommRateField * pQryInstrumentOrderCommRate, int nRequestID);

    int ReqQryOptionInstrTradeCost(void* api, CThostFtdcQryOptionInstrTradeCostField * pQryOptionInstrTradeCost, int nRequestID);

    int ReqQryOptionInstrCommRate(void* api, CThostFtdcQryOptionInstrCommRateField * pQryOptionInstrCommRate, int nRequestID);

    int ReqQryExecOrder(void* api, CThostFtdcQryExecOrderField * pQryExecOrder, int nRequestID);

    int ReqQryForQuote(void* api, CThostFtdcQryForQuoteField * pQryForQuote, int nRequestID);

    int ReqQryQuote(void* api, CThostFtdcQryQuoteField * pQryQuote, int nRequestID);

    int ReqQryCombInstrumentGuard(void* api, CThostFtdcQryCombInstrumentGuardField * pQryCombInstrumentGuard, int nRequestID);

    int ReqQryCombAction(void* api, CThostFtdcQryCombActionField * pQryCombAction, int nRequestID);

    int ReqQryTransferSerial(void* api, CThostFtdcQryTransferSerialField * pQryTransferSerial, int nRequestID);

    int ReqQryAccountregister(void* api, CThostFtdcQryAccountregisterField * pQryAccountregister, int nRequestID);

    int ReqQryContractBank(void* api, CThostFtdcQryContractBankField * pQryContractBank, int nRequestID);

    int ReqQryParkedOrder(void* api, CThostFtdcQryParkedOrderField * pQryParkedOrder, int nRequestID);

    int ReqQryParkedOrderAction(void* api, CThostFtdcQryParkedOrderActionField * pQryParkedOrderAction, int nRequestID);

    int ReqQryTradingNotice(void* api, CThostFtdcQryTradingNoticeField * pQryTradingNotice, int nRequestID);

    int ReqQryBrokerTradingParams(void* api, CThostFtdcQryBrokerTradingParamsField * pQryBrokerTradingParams, int nRequestID);

    int ReqQryBrokerTradingAlgos(void* api, CThostFtdcQryBrokerTradingAlgosField * pQryBrokerTradingAlgos, int nRequestID);

    int ReqQueryCFMMCTradingAccountToken(void* api, CThostFtdcQueryCFMMCTradingAccountTokenField * pQueryCFMMCTradingAccountToken, int nRequestID);

    int ReqFromBankToFutureByFuture(void* api, CThostFtdcReqTransferField * pReqTransfer, int nRequestID);

    int ReqFromFutureToBankByFuture(void* api, CThostFtdcReqTransferField * pReqTransfer, int nRequestID);

    int ReqQueryBankAccountMoneyByFuture(void* api, CThostFtdcReqQueryAccountField * pReqQueryAccount, int nRequestID);


}

#endif
