#include "pyctptraderapi.h"
#include <string>


class PyCtpTraderSpi : public CThostFtdcTraderSpi {
public:
    PyCtpTraderSpi()
        :m_OnFrontConnected(NULL)
        ,m_OnFrontDisconnected(NULL)
        ,m_OnHeartBeatWarning(NULL)
        ,m_OnRspAuthenticate(NULL)
        ,m_OnRspUserLogin(NULL)
        ,m_OnRspUserLogout(NULL)
        ,m_OnRspUserPasswordUpdate(NULL)
        ,m_OnRspTradingAccountPasswordUpdate(NULL)
        ,m_OnRspOrderInsert(NULL)
        ,m_OnRspParkedOrderInsert(NULL)
        ,m_OnRspParkedOrderAction(NULL)
        ,m_OnRspOrderAction(NULL)
        ,m_OnRspQueryMaxOrderVolume(NULL)
        ,m_OnRspSettlementInfoConfirm(NULL)
        ,m_OnRspRemoveParkedOrder(NULL)
        ,m_OnRspRemoveParkedOrderAction(NULL)
        ,m_OnRspExecOrderInsert(NULL)
        ,m_OnRspExecOrderAction(NULL)
        ,m_OnRspForQuoteInsert(NULL)
        ,m_OnRspQuoteInsert(NULL)
        ,m_OnRspQuoteAction(NULL)
        ,m_OnRspBatchOrderAction(NULL)
        ,m_OnRspCombActionInsert(NULL)
        ,m_OnRspQryOrder(NULL)
        ,m_OnRspQryTrade(NULL)
        ,m_OnRspQryInvestorPosition(NULL)
        ,m_OnRspQryTradingAccount(NULL)
        ,m_OnRspQryInvestor(NULL)
        ,m_OnRspQryTradingCode(NULL)
        ,m_OnRspQryInstrumentMarginRate(NULL)
        ,m_OnRspQryInstrumentCommissionRate(NULL)
        ,m_OnRspQryExchange(NULL)
        ,m_OnRspQryProduct(NULL)
        ,m_OnRspQryInstrument(NULL)
        ,m_OnRspQryDepthMarketData(NULL)
        ,m_OnRspQrySettlementInfo(NULL)
        ,m_OnRspQryTransferBank(NULL)
        ,m_OnRspQryInvestorPositionDetail(NULL)
        ,m_OnRspQryNotice(NULL)
        ,m_OnRspQrySettlementInfoConfirm(NULL)
        ,m_OnRspQryInvestorPositionCombineDetail(NULL)
        ,m_OnRspQryCFMMCTradingAccountKey(NULL)
        ,m_OnRspQryEWarrantOffset(NULL)
        ,m_OnRspQryInvestorProductGroupMargin(NULL)
        ,m_OnRspQryExchangeMarginRate(NULL)
        ,m_OnRspQryExchangeMarginRateAdjust(NULL)
        ,m_OnRspQryExchangeRate(NULL)
        ,m_OnRspQrySecAgentACIDMap(NULL)
        ,m_OnRspQryProductExchRate(NULL)
        ,m_OnRspQryProductGroup(NULL)
        ,m_OnRspQryMMInstrumentCommissionRate(NULL)
        ,m_OnRspQryMMOptionInstrCommRate(NULL)
        ,m_OnRspQryInstrumentOrderCommRate(NULL)
        ,m_OnRspQryOptionInstrTradeCost(NULL)
        ,m_OnRspQryOptionInstrCommRate(NULL)
        ,m_OnRspQryExecOrder(NULL)
        ,m_OnRspQryForQuote(NULL)
        ,m_OnRspQryQuote(NULL)
        ,m_OnRspQryCombInstrumentGuard(NULL)
        ,m_OnRspQryCombAction(NULL)
        ,m_OnRspQryTransferSerial(NULL)
        ,m_OnRspQryAccountregister(NULL)
        ,m_OnRspError(NULL)
        ,m_OnRtnOrder(NULL)
        ,m_OnRtnTrade(NULL)
        ,m_OnErrRtnOrderInsert(NULL)
        ,m_OnErrRtnOrderAction(NULL)
        ,m_OnRtnInstrumentStatus(NULL)
        ,m_OnRtnBulletin(NULL)
        ,m_OnRtnTradingNotice(NULL)
        ,m_OnRtnErrorConditionalOrder(NULL)
        ,m_OnRtnExecOrder(NULL)
        ,m_OnErrRtnExecOrderInsert(NULL)
        ,m_OnErrRtnExecOrderAction(NULL)
        ,m_OnErrRtnForQuoteInsert(NULL)
        ,m_OnRtnQuote(NULL)
        ,m_OnErrRtnQuoteInsert(NULL)
        ,m_OnErrRtnQuoteAction(NULL)
        ,m_OnRtnForQuoteRsp(NULL)
        ,m_OnRtnCFMMCTradingAccountToken(NULL)
        ,m_OnErrRtnBatchOrderAction(NULL)
        ,m_OnRtnCombAction(NULL)
        ,m_OnErrRtnCombActionInsert(NULL)
        ,m_OnRspQryContractBank(NULL)
        ,m_OnRspQryParkedOrder(NULL)
        ,m_OnRspQryParkedOrderAction(NULL)
        ,m_OnRspQryTradingNotice(NULL)
        ,m_OnRspQryBrokerTradingParams(NULL)
        ,m_OnRspQryBrokerTradingAlgos(NULL)
        ,m_OnRspQueryCFMMCTradingAccountToken(NULL)
        ,m_OnRtnFromBankToFutureByBank(NULL)
        ,m_OnRtnFromFutureToBankByBank(NULL)
        ,m_OnRtnRepealFromBankToFutureByBank(NULL)
        ,m_OnRtnRepealFromFutureToBankByBank(NULL)
        ,m_OnRtnFromBankToFutureByFuture(NULL)
        ,m_OnRtnFromFutureToBankByFuture(NULL)
        ,m_OnRtnRepealFromBankToFutureByFutureManual(NULL)
        ,m_OnRtnRepealFromFutureToBankByFutureManual(NULL)
        ,m_OnRtnQueryBankBalanceByFuture(NULL)
        ,m_OnErrRtnBankToFutureByFuture(NULL)
        ,m_OnErrRtnFutureToBankByFuture(NULL)
        ,m_OnErrRtnRepealBankToFutureByFutureManual(NULL)
        ,m_OnErrRtnRepealFutureToBankByFutureManual(NULL)
        ,m_OnErrRtnQueryBankBalanceByFuture(NULL)
        ,m_OnRtnRepealFromBankToFutureByFuture(NULL)
        ,m_OnRtnRepealFromFutureToBankByFuture(NULL)
        ,m_OnRspFromBankToFutureByFuture(NULL)
        ,m_OnRspFromFutureToBankByFuture(NULL)
        ,m_OnRspQueryBankAccountMoneyByFuture(NULL)
        ,m_OnRtnOpenAccountByBank(NULL)
        ,m_OnRtnCancelAccountByBank(NULL)
        ,m_OnRtnChangeAccountByBank(NULL){}

    bool registry(std::string const& name, void* ptr) {
        if (name == "OnFrontConnected") {
            m_OnFrontConnected = (void (*)(void*))ptr;
            return true;
        }
        if (name == "OnFrontDisconnected") {
            m_OnFrontDisconnected = (void (*)(void*, int))ptr;
            return true;
        }
        if (name == "OnHeartBeatWarning") {
            m_OnHeartBeatWarning = (void (*)(void*, int))ptr;
            return true;
        }
        if (name == "OnRspAuthenticate") {
            m_OnRspAuthenticate = (void (*)(void*, CThostFtdcRspAuthenticateField *, CThostFtdcRspInfoField *, int, bool))ptr;
            return true;
        }
        if (name == "OnRspUserLogin") {
            m_OnRspUserLogin = (void (*)(void*, CThostFtdcRspUserLoginField *, CThostFtdcRspInfoField *, int, bool))ptr;
            return true;
        }
        if (name == "OnRspUserLogout") {
            m_OnRspUserLogout = (void (*)(void*, CThostFtdcUserLogoutField *, CThostFtdcRspInfoField *, int, bool))ptr;
            return true;
        }
        if (name == "OnRspUserPasswordUpdate") {
            m_OnRspUserPasswordUpdate = (void (*)(void*, CThostFtdcUserPasswordUpdateField *, CThostFtdcRspInfoField *, int, bool))ptr;
            return true;
        }
        if (name == "OnRspTradingAccountPasswordUpdate") {
            m_OnRspTradingAccountPasswordUpdate = (void (*)(void*, CThostFtdcTradingAccountPasswordUpdateField *, CThostFtdcRspInfoField *, int, bool))ptr;
            return true;
        }
        if (name == "OnRspOrderInsert") {
            m_OnRspOrderInsert = (void (*)(void*, CThostFtdcInputOrderField *, CThostFtdcRspInfoField *, int, bool))ptr;
            return true;
        }
        if (name == "OnRspParkedOrderInsert") {
            m_OnRspParkedOrderInsert = (void (*)(void*, CThostFtdcParkedOrderField *, CThostFtdcRspInfoField *, int, bool))ptr;
            return true;
        }
        if (name == "OnRspParkedOrderAction") {
            m_OnRspParkedOrderAction = (void (*)(void*, CThostFtdcParkedOrderActionField *, CThostFtdcRspInfoField *, int, bool))ptr;
            return true;
        }
        if (name == "OnRspOrderAction") {
            m_OnRspOrderAction = (void (*)(void*, CThostFtdcInputOrderActionField *, CThostFtdcRspInfoField *, int, bool))ptr;
            return true;
        }
        if (name == "OnRspQueryMaxOrderVolume") {
            m_OnRspQueryMaxOrderVolume = (void (*)(void*, CThostFtdcQueryMaxOrderVolumeField *, CThostFtdcRspInfoField *, int, bool))ptr;
            return true;
        }
        if (name == "OnRspSettlementInfoConfirm") {
            m_OnRspSettlementInfoConfirm = (void (*)(void*, CThostFtdcSettlementInfoConfirmField *, CThostFtdcRspInfoField *, int, bool))ptr;
            return true;
        }
        if (name == "OnRspRemoveParkedOrder") {
            m_OnRspRemoveParkedOrder = (void (*)(void*, CThostFtdcRemoveParkedOrderField *, CThostFtdcRspInfoField *, int, bool))ptr;
            return true;
        }
        if (name == "OnRspRemoveParkedOrderAction") {
            m_OnRspRemoveParkedOrderAction = (void (*)(void*, CThostFtdcRemoveParkedOrderActionField *, CThostFtdcRspInfoField *, int, bool))ptr;
            return true;
        }
        if (name == "OnRspExecOrderInsert") {
            m_OnRspExecOrderInsert = (void (*)(void*, CThostFtdcInputExecOrderField *, CThostFtdcRspInfoField *, int, bool))ptr;
            return true;
        }
        if (name == "OnRspExecOrderAction") {
            m_OnRspExecOrderAction = (void (*)(void*, CThostFtdcInputExecOrderActionField *, CThostFtdcRspInfoField *, int, bool))ptr;
            return true;
        }
        if (name == "OnRspForQuoteInsert") {
            m_OnRspForQuoteInsert = (void (*)(void*, CThostFtdcInputForQuoteField *, CThostFtdcRspInfoField *, int, bool))ptr;
            return true;
        }
        if (name == "OnRspQuoteInsert") {
            m_OnRspQuoteInsert = (void (*)(void*, CThostFtdcInputQuoteField *, CThostFtdcRspInfoField *, int, bool))ptr;
            return true;
        }
        if (name == "OnRspQuoteAction") {
            m_OnRspQuoteAction = (void (*)(void*, CThostFtdcInputQuoteActionField *, CThostFtdcRspInfoField *, int, bool))ptr;
            return true;
        }
        if (name == "OnRspBatchOrderAction") {
            m_OnRspBatchOrderAction = (void (*)(void*, CThostFtdcInputBatchOrderActionField *, CThostFtdcRspInfoField *, int, bool))ptr;
            return true;
        }
        if (name == "OnRspCombActionInsert") {
            m_OnRspCombActionInsert = (void (*)(void*, CThostFtdcInputCombActionField *, CThostFtdcRspInfoField *, int, bool))ptr;
            return true;
        }
        if (name == "OnRspQryOrder") {
            m_OnRspQryOrder = (void (*)(void*, CThostFtdcOrderField *, CThostFtdcRspInfoField *, int, bool))ptr;
            return true;
        }
        if (name == "OnRspQryTrade") {
            m_OnRspQryTrade = (void (*)(void*, CThostFtdcTradeField *, CThostFtdcRspInfoField *, int, bool))ptr;
            return true;
        }
        if (name == "OnRspQryInvestorPosition") {
            m_OnRspQryInvestorPosition = (void (*)(void*, CThostFtdcInvestorPositionField *, CThostFtdcRspInfoField *, int, bool))ptr;
            return true;
        }
        if (name == "OnRspQryTradingAccount") {
            m_OnRspQryTradingAccount = (void (*)(void*, CThostFtdcTradingAccountField *, CThostFtdcRspInfoField *, int, bool))ptr;
            return true;
        }
        if (name == "OnRspQryInvestor") {
            m_OnRspQryInvestor = (void (*)(void*, CThostFtdcInvestorField *, CThostFtdcRspInfoField *, int, bool))ptr;
            return true;
        }
        if (name == "OnRspQryTradingCode") {
            m_OnRspQryTradingCode = (void (*)(void*, CThostFtdcTradingCodeField *, CThostFtdcRspInfoField *, int, bool))ptr;
            return true;
        }
        if (name == "OnRspQryInstrumentMarginRate") {
            m_OnRspQryInstrumentMarginRate = (void (*)(void*, CThostFtdcInstrumentMarginRateField *, CThostFtdcRspInfoField *, int, bool))ptr;
            return true;
        }
        if (name == "OnRspQryInstrumentCommissionRate") {
            m_OnRspQryInstrumentCommissionRate = (void (*)(void*, CThostFtdcInstrumentCommissionRateField *, CThostFtdcRspInfoField *, int, bool))ptr;
            return true;
        }
        if (name == "OnRspQryExchange") {
            m_OnRspQryExchange = (void (*)(void*, CThostFtdcExchangeField *, CThostFtdcRspInfoField *, int, bool))ptr;
            return true;
        }
        if (name == "OnRspQryProduct") {
            m_OnRspQryProduct = (void (*)(void*, CThostFtdcProductField *, CThostFtdcRspInfoField *, int, bool))ptr;
            return true;
        }
        if (name == "OnRspQryInstrument") {
            m_OnRspQryInstrument = (void (*)(void*, CThostFtdcInstrumentField *, CThostFtdcRspInfoField *, int, bool))ptr;
            return true;
        }
        if (name == "OnRspQryDepthMarketData") {
            m_OnRspQryDepthMarketData = (void (*)(void*, CThostFtdcDepthMarketDataField *, CThostFtdcRspInfoField *, int, bool))ptr;
            return true;
        }
        if (name == "OnRspQrySettlementInfo") {
            m_OnRspQrySettlementInfo = (void (*)(void*, CThostFtdcSettlementInfoField *, CThostFtdcRspInfoField *, int, bool))ptr;
            return true;
        }
        if (name == "OnRspQryTransferBank") {
            m_OnRspQryTransferBank = (void (*)(void*, CThostFtdcTransferBankField *, CThostFtdcRspInfoField *, int, bool))ptr;
            return true;
        }
        if (name == "OnRspQryInvestorPositionDetail") {
            m_OnRspQryInvestorPositionDetail = (void (*)(void*, CThostFtdcInvestorPositionDetailField *, CThostFtdcRspInfoField *, int, bool))ptr;
            return true;
        }
        if (name == "OnRspQryNotice") {
            m_OnRspQryNotice = (void (*)(void*, CThostFtdcNoticeField *, CThostFtdcRspInfoField *, int, bool))ptr;
            return true;
        }
        if (name == "OnRspQrySettlementInfoConfirm") {
            m_OnRspQrySettlementInfoConfirm = (void (*)(void*, CThostFtdcSettlementInfoConfirmField *, CThostFtdcRspInfoField *, int, bool))ptr;
            return true;
        }
        if (name == "OnRspQryInvestorPositionCombineDetail") {
            m_OnRspQryInvestorPositionCombineDetail = (void (*)(void*, CThostFtdcInvestorPositionCombineDetailField *, CThostFtdcRspInfoField *, int, bool))ptr;
            return true;
        }
        if (name == "OnRspQryCFMMCTradingAccountKey") {
            m_OnRspQryCFMMCTradingAccountKey = (void (*)(void*, CThostFtdcCFMMCTradingAccountKeyField *, CThostFtdcRspInfoField *, int, bool))ptr;
            return true;
        }
        if (name == "OnRspQryEWarrantOffset") {
            m_OnRspQryEWarrantOffset = (void (*)(void*, CThostFtdcEWarrantOffsetField *, CThostFtdcRspInfoField *, int, bool))ptr;
            return true;
        }
        if (name == "OnRspQryInvestorProductGroupMargin") {
            m_OnRspQryInvestorProductGroupMargin = (void (*)(void*, CThostFtdcInvestorProductGroupMarginField *, CThostFtdcRspInfoField *, int, bool))ptr;
            return true;
        }
        if (name == "OnRspQryExchangeMarginRate") {
            m_OnRspQryExchangeMarginRate = (void (*)(void*, CThostFtdcExchangeMarginRateField *, CThostFtdcRspInfoField *, int, bool))ptr;
            return true;
        }
        if (name == "OnRspQryExchangeMarginRateAdjust") {
            m_OnRspQryExchangeMarginRateAdjust = (void (*)(void*, CThostFtdcExchangeMarginRateAdjustField *, CThostFtdcRspInfoField *, int, bool))ptr;
            return true;
        }
        if (name == "OnRspQryExchangeRate") {
            m_OnRspQryExchangeRate = (void (*)(void*, CThostFtdcExchangeRateField *, CThostFtdcRspInfoField *, int, bool))ptr;
            return true;
        }
        if (name == "OnRspQrySecAgentACIDMap") {
            m_OnRspQrySecAgentACIDMap = (void (*)(void*, CThostFtdcSecAgentACIDMapField *, CThostFtdcRspInfoField *, int, bool))ptr;
            return true;
        }
        if (name == "OnRspQryProductExchRate") {
            m_OnRspQryProductExchRate = (void (*)(void*, CThostFtdcProductExchRateField *, CThostFtdcRspInfoField *, int, bool))ptr;
            return true;
        }
        if (name == "OnRspQryProductGroup") {
            m_OnRspQryProductGroup = (void (*)(void*, CThostFtdcProductGroupField *, CThostFtdcRspInfoField *, int, bool))ptr;
            return true;
        }
        if (name == "OnRspQryMMInstrumentCommissionRate") {
            m_OnRspQryMMInstrumentCommissionRate = (void (*)(void*, CThostFtdcMMInstrumentCommissionRateField *, CThostFtdcRspInfoField *, int, bool))ptr;
            return true;
        }
        if (name == "OnRspQryMMOptionInstrCommRate") {
            m_OnRspQryMMOptionInstrCommRate = (void (*)(void*, CThostFtdcMMOptionInstrCommRateField *, CThostFtdcRspInfoField *, int, bool))ptr;
            return true;
        }
        if (name == "OnRspQryInstrumentOrderCommRate") {
            m_OnRspQryInstrumentOrderCommRate = (void (*)(void*, CThostFtdcInstrumentOrderCommRateField *, CThostFtdcRspInfoField *, int, bool))ptr;
            return true;
        }
        if (name == "OnRspQryOptionInstrTradeCost") {
            m_OnRspQryOptionInstrTradeCost = (void (*)(void*, CThostFtdcOptionInstrTradeCostField *, CThostFtdcRspInfoField *, int, bool))ptr;
            return true;
        }
        if (name == "OnRspQryOptionInstrCommRate") {
            m_OnRspQryOptionInstrCommRate = (void (*)(void*, CThostFtdcOptionInstrCommRateField *, CThostFtdcRspInfoField *, int, bool))ptr;
            return true;
        }
        if (name == "OnRspQryExecOrder") {
            m_OnRspQryExecOrder = (void (*)(void*, CThostFtdcExecOrderField *, CThostFtdcRspInfoField *, int, bool))ptr;
            return true;
        }
        if (name == "OnRspQryForQuote") {
            m_OnRspQryForQuote = (void (*)(void*, CThostFtdcForQuoteField *, CThostFtdcRspInfoField *, int, bool))ptr;
            return true;
        }
        if (name == "OnRspQryQuote") {
            m_OnRspQryQuote = (void (*)(void*, CThostFtdcQuoteField *, CThostFtdcRspInfoField *, int, bool))ptr;
            return true;
        }
        if (name == "OnRspQryCombInstrumentGuard") {
            m_OnRspQryCombInstrumentGuard = (void (*)(void*, CThostFtdcCombInstrumentGuardField *, CThostFtdcRspInfoField *, int, bool))ptr;
            return true;
        }
        if (name == "OnRspQryCombAction") {
            m_OnRspQryCombAction = (void (*)(void*, CThostFtdcCombActionField *, CThostFtdcRspInfoField *, int, bool))ptr;
            return true;
        }
        if (name == "OnRspQryTransferSerial") {
            m_OnRspQryTransferSerial = (void (*)(void*, CThostFtdcTransferSerialField *, CThostFtdcRspInfoField *, int, bool))ptr;
            return true;
        }
        if (name == "OnRspQryAccountregister") {
            m_OnRspQryAccountregister = (void (*)(void*, CThostFtdcAccountregisterField *, CThostFtdcRspInfoField *, int, bool))ptr;
            return true;
        }
        if (name == "OnRspError") {
            m_OnRspError = (void (*)(void*, CThostFtdcRspInfoField *, int, bool))ptr;
            return true;
        }
        if (name == "OnRtnOrder") {
            m_OnRtnOrder = (void (*)(void*, CThostFtdcOrderField *))ptr;
            return true;
        }
        if (name == "OnRtnTrade") {
            m_OnRtnTrade = (void (*)(void*, CThostFtdcTradeField *))ptr;
            return true;
        }
        if (name == "OnErrRtnOrderInsert") {
            m_OnErrRtnOrderInsert = (void (*)(void*, CThostFtdcInputOrderField *, CThostFtdcRspInfoField *))ptr;
            return true;
        }
        if (name == "OnErrRtnOrderAction") {
            m_OnErrRtnOrderAction = (void (*)(void*, CThostFtdcOrderActionField *, CThostFtdcRspInfoField *))ptr;
            return true;
        }
        if (name == "OnRtnInstrumentStatus") {
            m_OnRtnInstrumentStatus = (void (*)(void*, CThostFtdcInstrumentStatusField *))ptr;
            return true;
        }
        if (name == "OnRtnBulletin") {
            m_OnRtnBulletin = (void (*)(void*, CThostFtdcBulletinField *))ptr;
            return true;
        }
        if (name == "OnRtnTradingNotice") {
            m_OnRtnTradingNotice = (void (*)(void*, CThostFtdcTradingNoticeInfoField *))ptr;
            return true;
        }
        if (name == "OnRtnErrorConditionalOrder") {
            m_OnRtnErrorConditionalOrder = (void (*)(void*, CThostFtdcErrorConditionalOrderField *))ptr;
            return true;
        }
        if (name == "OnRtnExecOrder") {
            m_OnRtnExecOrder = (void (*)(void*, CThostFtdcExecOrderField *))ptr;
            return true;
        }
        if (name == "OnErrRtnExecOrderInsert") {
            m_OnErrRtnExecOrderInsert = (void (*)(void*, CThostFtdcInputExecOrderField *, CThostFtdcRspInfoField *))ptr;
            return true;
        }
        if (name == "OnErrRtnExecOrderAction") {
            m_OnErrRtnExecOrderAction = (void (*)(void*, CThostFtdcExecOrderActionField *, CThostFtdcRspInfoField *))ptr;
            return true;
        }
        if (name == "OnErrRtnForQuoteInsert") {
            m_OnErrRtnForQuoteInsert = (void (*)(void*, CThostFtdcInputForQuoteField *, CThostFtdcRspInfoField *))ptr;
            return true;
        }
        if (name == "OnRtnQuote") {
            m_OnRtnQuote = (void (*)(void*, CThostFtdcQuoteField *))ptr;
            return true;
        }
        if (name == "OnErrRtnQuoteInsert") {
            m_OnErrRtnQuoteInsert = (void (*)(void*, CThostFtdcInputQuoteField *, CThostFtdcRspInfoField *))ptr;
            return true;
        }
        if (name == "OnErrRtnQuoteAction") {
            m_OnErrRtnQuoteAction = (void (*)(void*, CThostFtdcQuoteActionField *, CThostFtdcRspInfoField *))ptr;
            return true;
        }
        if (name == "OnRtnForQuoteRsp") {
            m_OnRtnForQuoteRsp = (void (*)(void*, CThostFtdcForQuoteRspField *))ptr;
            return true;
        }
        if (name == "OnRtnCFMMCTradingAccountToken") {
            m_OnRtnCFMMCTradingAccountToken = (void (*)(void*, CThostFtdcCFMMCTradingAccountTokenField *))ptr;
            return true;
        }
        if (name == "OnErrRtnBatchOrderAction") {
            m_OnErrRtnBatchOrderAction = (void (*)(void*, CThostFtdcBatchOrderActionField *, CThostFtdcRspInfoField *))ptr;
            return true;
        }
        if (name == "OnRtnCombAction") {
            m_OnRtnCombAction = (void (*)(void*, CThostFtdcCombActionField *))ptr;
            return true;
        }
        if (name == "OnErrRtnCombActionInsert") {
            m_OnErrRtnCombActionInsert = (void (*)(void*, CThostFtdcInputCombActionField *, CThostFtdcRspInfoField *))ptr;
            return true;
        }
        if (name == "OnRspQryContractBank") {
            m_OnRspQryContractBank = (void (*)(void*, CThostFtdcContractBankField *, CThostFtdcRspInfoField *, int, bool))ptr;
            return true;
        }
        if (name == "OnRspQryParkedOrder") {
            m_OnRspQryParkedOrder = (void (*)(void*, CThostFtdcParkedOrderField *, CThostFtdcRspInfoField *, int, bool))ptr;
            return true;
        }
        if (name == "OnRspQryParkedOrderAction") {
            m_OnRspQryParkedOrderAction = (void (*)(void*, CThostFtdcParkedOrderActionField *, CThostFtdcRspInfoField *, int, bool))ptr;
            return true;
        }
        if (name == "OnRspQryTradingNotice") {
            m_OnRspQryTradingNotice = (void (*)(void*, CThostFtdcTradingNoticeField *, CThostFtdcRspInfoField *, int, bool))ptr;
            return true;
        }
        if (name == "OnRspQryBrokerTradingParams") {
            m_OnRspQryBrokerTradingParams = (void (*)(void*, CThostFtdcBrokerTradingParamsField *, CThostFtdcRspInfoField *, int, bool))ptr;
            return true;
        }
        if (name == "OnRspQryBrokerTradingAlgos") {
            m_OnRspQryBrokerTradingAlgos = (void (*)(void*, CThostFtdcBrokerTradingAlgosField *, CThostFtdcRspInfoField *, int, bool))ptr;
            return true;
        }
        if (name == "OnRspQueryCFMMCTradingAccountToken") {
            m_OnRspQueryCFMMCTradingAccountToken = (void (*)(void*, CThostFtdcQueryCFMMCTradingAccountTokenField *, CThostFtdcRspInfoField *, int, bool))ptr;
            return true;
        }
        if (name == "OnRtnFromBankToFutureByBank") {
            m_OnRtnFromBankToFutureByBank = (void (*)(void*, CThostFtdcRspTransferField *))ptr;
            return true;
        }
        if (name == "OnRtnFromFutureToBankByBank") {
            m_OnRtnFromFutureToBankByBank = (void (*)(void*, CThostFtdcRspTransferField *))ptr;
            return true;
        }
        if (name == "OnRtnRepealFromBankToFutureByBank") {
            m_OnRtnRepealFromBankToFutureByBank = (void (*)(void*, CThostFtdcRspRepealField *))ptr;
            return true;
        }
        if (name == "OnRtnRepealFromFutureToBankByBank") {
            m_OnRtnRepealFromFutureToBankByBank = (void (*)(void*, CThostFtdcRspRepealField *))ptr;
            return true;
        }
        if (name == "OnRtnFromBankToFutureByFuture") {
            m_OnRtnFromBankToFutureByFuture = (void (*)(void*, CThostFtdcRspTransferField *))ptr;
            return true;
        }
        if (name == "OnRtnFromFutureToBankByFuture") {
            m_OnRtnFromFutureToBankByFuture = (void (*)(void*, CThostFtdcRspTransferField *))ptr;
            return true;
        }
        if (name == "OnRtnRepealFromBankToFutureByFutureManual") {
            m_OnRtnRepealFromBankToFutureByFutureManual = (void (*)(void*, CThostFtdcRspRepealField *))ptr;
            return true;
        }
        if (name == "OnRtnRepealFromFutureToBankByFutureManual") {
            m_OnRtnRepealFromFutureToBankByFutureManual = (void (*)(void*, CThostFtdcRspRepealField *))ptr;
            return true;
        }
        if (name == "OnRtnQueryBankBalanceByFuture") {
            m_OnRtnQueryBankBalanceByFuture = (void (*)(void*, CThostFtdcNotifyQueryAccountField *))ptr;
            return true;
        }
        if (name == "OnErrRtnBankToFutureByFuture") {
            m_OnErrRtnBankToFutureByFuture = (void (*)(void*, CThostFtdcReqTransferField *, CThostFtdcRspInfoField *))ptr;
            return true;
        }
        if (name == "OnErrRtnFutureToBankByFuture") {
            m_OnErrRtnFutureToBankByFuture = (void (*)(void*, CThostFtdcReqTransferField *, CThostFtdcRspInfoField *))ptr;
            return true;
        }
        if (name == "OnErrRtnRepealBankToFutureByFutureManual") {
            m_OnErrRtnRepealBankToFutureByFutureManual = (void (*)(void*, CThostFtdcReqRepealField *, CThostFtdcRspInfoField *))ptr;
            return true;
        }
        if (name == "OnErrRtnRepealFutureToBankByFutureManual") {
            m_OnErrRtnRepealFutureToBankByFutureManual = (void (*)(void*, CThostFtdcReqRepealField *, CThostFtdcRspInfoField *))ptr;
            return true;
        }
        if (name == "OnErrRtnQueryBankBalanceByFuture") {
            m_OnErrRtnQueryBankBalanceByFuture = (void (*)(void*, CThostFtdcReqQueryAccountField *, CThostFtdcRspInfoField *))ptr;
            return true;
        }
        if (name == "OnRtnRepealFromBankToFutureByFuture") {
            m_OnRtnRepealFromBankToFutureByFuture = (void (*)(void*, CThostFtdcRspRepealField *))ptr;
            return true;
        }
        if (name == "OnRtnRepealFromFutureToBankByFuture") {
            m_OnRtnRepealFromFutureToBankByFuture = (void (*)(void*, CThostFtdcRspRepealField *))ptr;
            return true;
        }
        if (name == "OnRspFromBankToFutureByFuture") {
            m_OnRspFromBankToFutureByFuture = (void (*)(void*, CThostFtdcReqTransferField *, CThostFtdcRspInfoField *, int, bool))ptr;
            return true;
        }
        if (name == "OnRspFromFutureToBankByFuture") {
            m_OnRspFromFutureToBankByFuture = (void (*)(void*, CThostFtdcReqTransferField *, CThostFtdcRspInfoField *, int, bool))ptr;
            return true;
        }
        if (name == "OnRspQueryBankAccountMoneyByFuture") {
            m_OnRspQueryBankAccountMoneyByFuture = (void (*)(void*, CThostFtdcReqQueryAccountField *, CThostFtdcRspInfoField *, int, bool))ptr;
            return true;
        }
        if (name == "OnRtnOpenAccountByBank") {
            m_OnRtnOpenAccountByBank = (void (*)(void*, CThostFtdcOpenAccountField *))ptr;
            return true;
        }
        if (name == "OnRtnCancelAccountByBank") {
            m_OnRtnCancelAccountByBank = (void (*)(void*, CThostFtdcCancelAccountField *))ptr;
            return true;
        }
        if (name == "OnRtnChangeAccountByBank") {
            m_OnRtnChangeAccountByBank = (void (*)(void*, CThostFtdcChangeAccountField *))ptr;
            return true;
        }
        return false;
    }

    virtual void OnFrontConnected() {
        if (!m_OnFrontConnected) { return; }
        m_OnFrontConnected(this);
    }
    virtual void OnFrontDisconnected(int nReason) {
        if (!m_OnFrontDisconnected) { return; }
        m_OnFrontDisconnected(this, nReason);
    }
    virtual void OnHeartBeatWarning(int nTimeLapse) {
        if (!m_OnHeartBeatWarning) { return; }
        m_OnHeartBeatWarning(this, nTimeLapse);
    }
    virtual void OnRspAuthenticate(CThostFtdcRspAuthenticateField *pRspAuthenticateField, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
        if (!m_OnRspAuthenticate) { return; }
        m_OnRspAuthenticate(this, pRspAuthenticateField, pRspInfo, nRequestID, bIsLast);
    }
    virtual void OnRspUserLogin(CThostFtdcRspUserLoginField *pRspUserLogin, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
        if (!m_OnRspUserLogin) { return; }
        m_OnRspUserLogin(this, pRspUserLogin, pRspInfo, nRequestID, bIsLast);
    }
    virtual void OnRspUserLogout(CThostFtdcUserLogoutField *pUserLogout, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
        if (!m_OnRspUserLogout) { return; }
        m_OnRspUserLogout(this, pUserLogout, pRspInfo, nRequestID, bIsLast);
    }
    virtual void OnRspUserPasswordUpdate(CThostFtdcUserPasswordUpdateField *pUserPasswordUpdate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
        if (!m_OnRspUserPasswordUpdate) { return; }
        m_OnRspUserPasswordUpdate(this, pUserPasswordUpdate, pRspInfo, nRequestID, bIsLast);
    }
    virtual void OnRspTradingAccountPasswordUpdate(CThostFtdcTradingAccountPasswordUpdateField *pTradingAccountPasswordUpdate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
        if (!m_OnRspTradingAccountPasswordUpdate) { return; }
        m_OnRspTradingAccountPasswordUpdate(this, pTradingAccountPasswordUpdate, pRspInfo, nRequestID, bIsLast);
    }
    virtual void OnRspOrderInsert(CThostFtdcInputOrderField *pInputOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
        if (!m_OnRspOrderInsert) { return; }
        m_OnRspOrderInsert(this, pInputOrder, pRspInfo, nRequestID, bIsLast);
    }
    virtual void OnRspParkedOrderInsert(CThostFtdcParkedOrderField *pParkedOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
        if (!m_OnRspParkedOrderInsert) { return; }
        m_OnRspParkedOrderInsert(this, pParkedOrder, pRspInfo, nRequestID, bIsLast);
    }
    virtual void OnRspParkedOrderAction(CThostFtdcParkedOrderActionField *pParkedOrderAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
        if (!m_OnRspParkedOrderAction) { return; }
        m_OnRspParkedOrderAction(this, pParkedOrderAction, pRspInfo, nRequestID, bIsLast);
    }
    virtual void OnRspOrderAction(CThostFtdcInputOrderActionField *pInputOrderAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
        if (!m_OnRspOrderAction) { return; }
        m_OnRspOrderAction(this, pInputOrderAction, pRspInfo, nRequestID, bIsLast);
    }
    virtual void OnRspQueryMaxOrderVolume(CThostFtdcQueryMaxOrderVolumeField *pQueryMaxOrderVolume, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
        if (!m_OnRspQueryMaxOrderVolume) { return; }
        m_OnRspQueryMaxOrderVolume(this, pQueryMaxOrderVolume, pRspInfo, nRequestID, bIsLast);
    }
    virtual void OnRspSettlementInfoConfirm(CThostFtdcSettlementInfoConfirmField *pSettlementInfoConfirm, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
        if (!m_OnRspSettlementInfoConfirm) { return; }
        m_OnRspSettlementInfoConfirm(this, pSettlementInfoConfirm, pRspInfo, nRequestID, bIsLast);
    }
    virtual void OnRspRemoveParkedOrder(CThostFtdcRemoveParkedOrderField *pRemoveParkedOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
        if (!m_OnRspRemoveParkedOrder) { return; }
        m_OnRspRemoveParkedOrder(this, pRemoveParkedOrder, pRspInfo, nRequestID, bIsLast);
    }
    virtual void OnRspRemoveParkedOrderAction(CThostFtdcRemoveParkedOrderActionField *pRemoveParkedOrderAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
        if (!m_OnRspRemoveParkedOrderAction) { return; }
        m_OnRspRemoveParkedOrderAction(this, pRemoveParkedOrderAction, pRspInfo, nRequestID, bIsLast);
    }
    virtual void OnRspExecOrderInsert(CThostFtdcInputExecOrderField *pInputExecOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
        if (!m_OnRspExecOrderInsert) { return; }
        m_OnRspExecOrderInsert(this, pInputExecOrder, pRspInfo, nRequestID, bIsLast);
    }
    virtual void OnRspExecOrderAction(CThostFtdcInputExecOrderActionField *pInputExecOrderAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
        if (!m_OnRspExecOrderAction) { return; }
        m_OnRspExecOrderAction(this, pInputExecOrderAction, pRspInfo, nRequestID, bIsLast);
    }
    virtual void OnRspForQuoteInsert(CThostFtdcInputForQuoteField *pInputForQuote, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
        if (!m_OnRspForQuoteInsert) { return; }
        m_OnRspForQuoteInsert(this, pInputForQuote, pRspInfo, nRequestID, bIsLast);
    }
    virtual void OnRspQuoteInsert(CThostFtdcInputQuoteField *pInputQuote, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
        if (!m_OnRspQuoteInsert) { return; }
        m_OnRspQuoteInsert(this, pInputQuote, pRspInfo, nRequestID, bIsLast);
    }
    virtual void OnRspQuoteAction(CThostFtdcInputQuoteActionField *pInputQuoteAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
        if (!m_OnRspQuoteAction) { return; }
        m_OnRspQuoteAction(this, pInputQuoteAction, pRspInfo, nRequestID, bIsLast);
    }
    virtual void OnRspBatchOrderAction(CThostFtdcInputBatchOrderActionField *pInputBatchOrderAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
        if (!m_OnRspBatchOrderAction) { return; }
        m_OnRspBatchOrderAction(this, pInputBatchOrderAction, pRspInfo, nRequestID, bIsLast);
    }
    virtual void OnRspCombActionInsert(CThostFtdcInputCombActionField *pInputCombAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
        if (!m_OnRspCombActionInsert) { return; }
        m_OnRspCombActionInsert(this, pInputCombAction, pRspInfo, nRequestID, bIsLast);
    }
    virtual void OnRspQryOrder(CThostFtdcOrderField *pOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
        if (!m_OnRspQryOrder) { return; }
        m_OnRspQryOrder(this, pOrder, pRspInfo, nRequestID, bIsLast);
    }
    virtual void OnRspQryTrade(CThostFtdcTradeField *pTrade, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
        if (!m_OnRspQryTrade) { return; }
        m_OnRspQryTrade(this, pTrade, pRspInfo, nRequestID, bIsLast);
    }
    virtual void OnRspQryInvestorPosition(CThostFtdcInvestorPositionField *pInvestorPosition, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
        if (!m_OnRspQryInvestorPosition) { return; }
        m_OnRspQryInvestorPosition(this, pInvestorPosition, pRspInfo, nRequestID, bIsLast);
    }
    virtual void OnRspQryTradingAccount(CThostFtdcTradingAccountField *pTradingAccount, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
        if (!m_OnRspQryTradingAccount) { return; }
        m_OnRspQryTradingAccount(this, pTradingAccount, pRspInfo, nRequestID, bIsLast);
    }
    virtual void OnRspQryInvestor(CThostFtdcInvestorField *pInvestor, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
        if (!m_OnRspQryInvestor) { return; }
        m_OnRspQryInvestor(this, pInvestor, pRspInfo, nRequestID, bIsLast);
    }
    virtual void OnRspQryTradingCode(CThostFtdcTradingCodeField *pTradingCode, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
        if (!m_OnRspQryTradingCode) { return; }
        m_OnRspQryTradingCode(this, pTradingCode, pRspInfo, nRequestID, bIsLast);
    }
    virtual void OnRspQryInstrumentMarginRate(CThostFtdcInstrumentMarginRateField *pInstrumentMarginRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
        if (!m_OnRspQryInstrumentMarginRate) { return; }
        m_OnRspQryInstrumentMarginRate(this, pInstrumentMarginRate, pRspInfo, nRequestID, bIsLast);
    }
    virtual void OnRspQryInstrumentCommissionRate(CThostFtdcInstrumentCommissionRateField *pInstrumentCommissionRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
        if (!m_OnRspQryInstrumentCommissionRate) { return; }
        m_OnRspQryInstrumentCommissionRate(this, pInstrumentCommissionRate, pRspInfo, nRequestID, bIsLast);
    }
    virtual void OnRspQryExchange(CThostFtdcExchangeField *pExchange, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
        if (!m_OnRspQryExchange) { return; }
        m_OnRspQryExchange(this, pExchange, pRspInfo, nRequestID, bIsLast);
    }
    virtual void OnRspQryProduct(CThostFtdcProductField *pProduct, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
        if (!m_OnRspQryProduct) { return; }
        m_OnRspQryProduct(this, pProduct, pRspInfo, nRequestID, bIsLast);
    }
    virtual void OnRspQryInstrument(CThostFtdcInstrumentField *pInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
        if (!m_OnRspQryInstrument) { return; }
        m_OnRspQryInstrument(this, pInstrument, pRspInfo, nRequestID, bIsLast);
    }
    virtual void OnRspQryDepthMarketData(CThostFtdcDepthMarketDataField *pDepthMarketData, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
        if (!m_OnRspQryDepthMarketData) { return; }
        m_OnRspQryDepthMarketData(this, pDepthMarketData, pRspInfo, nRequestID, bIsLast);
    }
    virtual void OnRspQrySettlementInfo(CThostFtdcSettlementInfoField *pSettlementInfo, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
        if (!m_OnRspQrySettlementInfo) { return; }
        m_OnRspQrySettlementInfo(this, pSettlementInfo, pRspInfo, nRequestID, bIsLast);
    }
    virtual void OnRspQryTransferBank(CThostFtdcTransferBankField *pTransferBank, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
        if (!m_OnRspQryTransferBank) { return; }
        m_OnRspQryTransferBank(this, pTransferBank, pRspInfo, nRequestID, bIsLast);
    }
    virtual void OnRspQryInvestorPositionDetail(CThostFtdcInvestorPositionDetailField *pInvestorPositionDetail, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
        if (!m_OnRspQryInvestorPositionDetail) { return; }
        m_OnRspQryInvestorPositionDetail(this, pInvestorPositionDetail, pRspInfo, nRequestID, bIsLast);
    }
    virtual void OnRspQryNotice(CThostFtdcNoticeField *pNotice, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
        if (!m_OnRspQryNotice) { return; }
        m_OnRspQryNotice(this, pNotice, pRspInfo, nRequestID, bIsLast);
    }
    virtual void OnRspQrySettlementInfoConfirm(CThostFtdcSettlementInfoConfirmField *pSettlementInfoConfirm, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
        if (!m_OnRspQrySettlementInfoConfirm) { return; }
        m_OnRspQrySettlementInfoConfirm(this, pSettlementInfoConfirm, pRspInfo, nRequestID, bIsLast);
    }
    virtual void OnRspQryInvestorPositionCombineDetail(CThostFtdcInvestorPositionCombineDetailField *pInvestorPositionCombineDetail, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
        if (!m_OnRspQryInvestorPositionCombineDetail) { return; }
        m_OnRspQryInvestorPositionCombineDetail(this, pInvestorPositionCombineDetail, pRspInfo, nRequestID, bIsLast);
    }
    virtual void OnRspQryCFMMCTradingAccountKey(CThostFtdcCFMMCTradingAccountKeyField *pCFMMCTradingAccountKey, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
        if (!m_OnRspQryCFMMCTradingAccountKey) { return; }
        m_OnRspQryCFMMCTradingAccountKey(this, pCFMMCTradingAccountKey, pRspInfo, nRequestID, bIsLast);
    }
    virtual void OnRspQryEWarrantOffset(CThostFtdcEWarrantOffsetField *pEWarrantOffset, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
        if (!m_OnRspQryEWarrantOffset) { return; }
        m_OnRspQryEWarrantOffset(this, pEWarrantOffset, pRspInfo, nRequestID, bIsLast);
    }
    virtual void OnRspQryInvestorProductGroupMargin(CThostFtdcInvestorProductGroupMarginField *pInvestorProductGroupMargin, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
        if (!m_OnRspQryInvestorProductGroupMargin) { return; }
        m_OnRspQryInvestorProductGroupMargin(this, pInvestorProductGroupMargin, pRspInfo, nRequestID, bIsLast);
    }
    virtual void OnRspQryExchangeMarginRate(CThostFtdcExchangeMarginRateField *pExchangeMarginRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
        if (!m_OnRspQryExchangeMarginRate) { return; }
        m_OnRspQryExchangeMarginRate(this, pExchangeMarginRate, pRspInfo, nRequestID, bIsLast);
    }
    virtual void OnRspQryExchangeMarginRateAdjust(CThostFtdcExchangeMarginRateAdjustField *pExchangeMarginRateAdjust, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
        if (!m_OnRspQryExchangeMarginRateAdjust) { return; }
        m_OnRspQryExchangeMarginRateAdjust(this, pExchangeMarginRateAdjust, pRspInfo, nRequestID, bIsLast);
    }
    virtual void OnRspQryExchangeRate(CThostFtdcExchangeRateField *pExchangeRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
        if (!m_OnRspQryExchangeRate) { return; }
        m_OnRspQryExchangeRate(this, pExchangeRate, pRspInfo, nRequestID, bIsLast);
    }
    virtual void OnRspQrySecAgentACIDMap(CThostFtdcSecAgentACIDMapField *pSecAgentACIDMap, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
        if (!m_OnRspQrySecAgentACIDMap) { return; }
        m_OnRspQrySecAgentACIDMap(this, pSecAgentACIDMap, pRspInfo, nRequestID, bIsLast);
    }
    virtual void OnRspQryProductExchRate(CThostFtdcProductExchRateField *pProductExchRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
        if (!m_OnRspQryProductExchRate) { return; }
        m_OnRspQryProductExchRate(this, pProductExchRate, pRspInfo, nRequestID, bIsLast);
    }
    virtual void OnRspQryProductGroup(CThostFtdcProductGroupField *pProductGroup, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
        if (!m_OnRspQryProductGroup) { return; }
        m_OnRspQryProductGroup(this, pProductGroup, pRspInfo, nRequestID, bIsLast);
    }
    virtual void OnRspQryMMInstrumentCommissionRate(CThostFtdcMMInstrumentCommissionRateField *pMMInstrumentCommissionRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
        if (!m_OnRspQryMMInstrumentCommissionRate) { return; }
        m_OnRspQryMMInstrumentCommissionRate(this, pMMInstrumentCommissionRate, pRspInfo, nRequestID, bIsLast);
    }
    virtual void OnRspQryMMOptionInstrCommRate(CThostFtdcMMOptionInstrCommRateField *pMMOptionInstrCommRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
        if (!m_OnRspQryMMOptionInstrCommRate) { return; }
        m_OnRspQryMMOptionInstrCommRate(this, pMMOptionInstrCommRate, pRspInfo, nRequestID, bIsLast);
    }
    virtual void OnRspQryInstrumentOrderCommRate(CThostFtdcInstrumentOrderCommRateField *pInstrumentOrderCommRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
        if (!m_OnRspQryInstrumentOrderCommRate) { return; }
        m_OnRspQryInstrumentOrderCommRate(this, pInstrumentOrderCommRate, pRspInfo, nRequestID, bIsLast);
    }
    virtual void OnRspQryOptionInstrTradeCost(CThostFtdcOptionInstrTradeCostField *pOptionInstrTradeCost, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
        if (!m_OnRspQryOptionInstrTradeCost) { return; }
        m_OnRspQryOptionInstrTradeCost(this, pOptionInstrTradeCost, pRspInfo, nRequestID, bIsLast);
    }
    virtual void OnRspQryOptionInstrCommRate(CThostFtdcOptionInstrCommRateField *pOptionInstrCommRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
        if (!m_OnRspQryOptionInstrCommRate) { return; }
        m_OnRspQryOptionInstrCommRate(this, pOptionInstrCommRate, pRspInfo, nRequestID, bIsLast);
    }
    virtual void OnRspQryExecOrder(CThostFtdcExecOrderField *pExecOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
        if (!m_OnRspQryExecOrder) { return; }
        m_OnRspQryExecOrder(this, pExecOrder, pRspInfo, nRequestID, bIsLast);
    }
    virtual void OnRspQryForQuote(CThostFtdcForQuoteField *pForQuote, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
        if (!m_OnRspQryForQuote) { return; }
        m_OnRspQryForQuote(this, pForQuote, pRspInfo, nRequestID, bIsLast);
    }
    virtual void OnRspQryQuote(CThostFtdcQuoteField *pQuote, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
        if (!m_OnRspQryQuote) { return; }
        m_OnRspQryQuote(this, pQuote, pRspInfo, nRequestID, bIsLast);
    }
    virtual void OnRspQryCombInstrumentGuard(CThostFtdcCombInstrumentGuardField *pCombInstrumentGuard, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
        if (!m_OnRspQryCombInstrumentGuard) { return; }
        m_OnRspQryCombInstrumentGuard(this, pCombInstrumentGuard, pRspInfo, nRequestID, bIsLast);
    }
    virtual void OnRspQryCombAction(CThostFtdcCombActionField *pCombAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
        if (!m_OnRspQryCombAction) { return; }
        m_OnRspQryCombAction(this, pCombAction, pRspInfo, nRequestID, bIsLast);
    }
    virtual void OnRspQryTransferSerial(CThostFtdcTransferSerialField *pTransferSerial, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
        if (!m_OnRspQryTransferSerial) { return; }
        m_OnRspQryTransferSerial(this, pTransferSerial, pRspInfo, nRequestID, bIsLast);
    }
    virtual void OnRspQryAccountregister(CThostFtdcAccountregisterField *pAccountregister, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
        if (!m_OnRspQryAccountregister) { return; }
        m_OnRspQryAccountregister(this, pAccountregister, pRspInfo, nRequestID, bIsLast);
    }
    virtual void OnRspError(CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
        if (!m_OnRspError) { return; }
        m_OnRspError(this, pRspInfo, nRequestID, bIsLast);
    }
    virtual void OnRtnOrder(CThostFtdcOrderField *pOrder) {
        if (!m_OnRtnOrder) { return; }
        m_OnRtnOrder(this, pOrder);
    }
    virtual void OnRtnTrade(CThostFtdcTradeField *pTrade) {
        if (!m_OnRtnTrade) { return; }
        m_OnRtnTrade(this, pTrade);
    }
    virtual void OnErrRtnOrderInsert(CThostFtdcInputOrderField *pInputOrder, CThostFtdcRspInfoField *pRspInfo) {
        if (!m_OnErrRtnOrderInsert) { return; }
        m_OnErrRtnOrderInsert(this, pInputOrder, pRspInfo);
    }
    virtual void OnErrRtnOrderAction(CThostFtdcOrderActionField *pOrderAction, CThostFtdcRspInfoField *pRspInfo) {
        if (!m_OnErrRtnOrderAction) { return; }
        m_OnErrRtnOrderAction(this, pOrderAction, pRspInfo);
    }
    virtual void OnRtnInstrumentStatus(CThostFtdcInstrumentStatusField *pInstrumentStatus) {
        if (!m_OnRtnInstrumentStatus) { return; }
        m_OnRtnInstrumentStatus(this, pInstrumentStatus);
    }
    virtual void OnRtnBulletin(CThostFtdcBulletinField *pBulletin) {
        if (!m_OnRtnBulletin) { return; }
        m_OnRtnBulletin(this, pBulletin);
    }
    virtual void OnRtnTradingNotice(CThostFtdcTradingNoticeInfoField *pTradingNoticeInfo) {
        if (!m_OnRtnTradingNotice) { return; }
        m_OnRtnTradingNotice(this, pTradingNoticeInfo);
    }
    virtual void OnRtnErrorConditionalOrder(CThostFtdcErrorConditionalOrderField *pErrorConditionalOrder) {
        if (!m_OnRtnErrorConditionalOrder) { return; }
        m_OnRtnErrorConditionalOrder(this, pErrorConditionalOrder);
    }
    virtual void OnRtnExecOrder(CThostFtdcExecOrderField *pExecOrder) {
        if (!m_OnRtnExecOrder) { return; }
        m_OnRtnExecOrder(this, pExecOrder);
    }
    virtual void OnErrRtnExecOrderInsert(CThostFtdcInputExecOrderField *pInputExecOrder, CThostFtdcRspInfoField *pRspInfo) {
        if (!m_OnErrRtnExecOrderInsert) { return; }
        m_OnErrRtnExecOrderInsert(this, pInputExecOrder, pRspInfo);
    }
    virtual void OnErrRtnExecOrderAction(CThostFtdcExecOrderActionField *pExecOrderAction, CThostFtdcRspInfoField *pRspInfo) {
        if (!m_OnErrRtnExecOrderAction) { return; }
        m_OnErrRtnExecOrderAction(this, pExecOrderAction, pRspInfo);
    }
    virtual void OnErrRtnForQuoteInsert(CThostFtdcInputForQuoteField *pInputForQuote, CThostFtdcRspInfoField *pRspInfo) {
        if (!m_OnErrRtnForQuoteInsert) { return; }
        m_OnErrRtnForQuoteInsert(this, pInputForQuote, pRspInfo);
    }
    virtual void OnRtnQuote(CThostFtdcQuoteField *pQuote) {
        if (!m_OnRtnQuote) { return; }
        m_OnRtnQuote(this, pQuote);
    }
    virtual void OnErrRtnQuoteInsert(CThostFtdcInputQuoteField *pInputQuote, CThostFtdcRspInfoField *pRspInfo) {
        if (!m_OnErrRtnQuoteInsert) { return; }
        m_OnErrRtnQuoteInsert(this, pInputQuote, pRspInfo);
    }
    virtual void OnErrRtnQuoteAction(CThostFtdcQuoteActionField *pQuoteAction, CThostFtdcRspInfoField *pRspInfo) {
        if (!m_OnErrRtnQuoteAction) { return; }
        m_OnErrRtnQuoteAction(this, pQuoteAction, pRspInfo);
    }
    virtual void OnRtnForQuoteRsp(CThostFtdcForQuoteRspField *pForQuoteRsp) {
        if (!m_OnRtnForQuoteRsp) { return; }
        m_OnRtnForQuoteRsp(this, pForQuoteRsp);
    }
    virtual void OnRtnCFMMCTradingAccountToken(CThostFtdcCFMMCTradingAccountTokenField *pCFMMCTradingAccountToken) {
        if (!m_OnRtnCFMMCTradingAccountToken) { return; }
        m_OnRtnCFMMCTradingAccountToken(this, pCFMMCTradingAccountToken);
    }
    virtual void OnErrRtnBatchOrderAction(CThostFtdcBatchOrderActionField *pBatchOrderAction, CThostFtdcRspInfoField *pRspInfo) {
        if (!m_OnErrRtnBatchOrderAction) { return; }
        m_OnErrRtnBatchOrderAction(this, pBatchOrderAction, pRspInfo);
    }
    virtual void OnRtnCombAction(CThostFtdcCombActionField *pCombAction) {
        if (!m_OnRtnCombAction) { return; }
        m_OnRtnCombAction(this, pCombAction);
    }
    virtual void OnErrRtnCombActionInsert(CThostFtdcInputCombActionField *pInputCombAction, CThostFtdcRspInfoField *pRspInfo) {
        if (!m_OnErrRtnCombActionInsert) { return; }
        m_OnErrRtnCombActionInsert(this, pInputCombAction, pRspInfo);
    }
    virtual void OnRspQryContractBank(CThostFtdcContractBankField *pContractBank, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
        if (!m_OnRspQryContractBank) { return; }
        m_OnRspQryContractBank(this, pContractBank, pRspInfo, nRequestID, bIsLast);
    }
    virtual void OnRspQryParkedOrder(CThostFtdcParkedOrderField *pParkedOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
        if (!m_OnRspQryParkedOrder) { return; }
        m_OnRspQryParkedOrder(this, pParkedOrder, pRspInfo, nRequestID, bIsLast);
    }
    virtual void OnRspQryParkedOrderAction(CThostFtdcParkedOrderActionField *pParkedOrderAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
        if (!m_OnRspQryParkedOrderAction) { return; }
        m_OnRspQryParkedOrderAction(this, pParkedOrderAction, pRspInfo, nRequestID, bIsLast);
    }
    virtual void OnRspQryTradingNotice(CThostFtdcTradingNoticeField *pTradingNotice, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
        if (!m_OnRspQryTradingNotice) { return; }
        m_OnRspQryTradingNotice(this, pTradingNotice, pRspInfo, nRequestID, bIsLast);
    }
    virtual void OnRspQryBrokerTradingParams(CThostFtdcBrokerTradingParamsField *pBrokerTradingParams, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
        if (!m_OnRspQryBrokerTradingParams) { return; }
        m_OnRspQryBrokerTradingParams(this, pBrokerTradingParams, pRspInfo, nRequestID, bIsLast);
    }
    virtual void OnRspQryBrokerTradingAlgos(CThostFtdcBrokerTradingAlgosField *pBrokerTradingAlgos, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
        if (!m_OnRspQryBrokerTradingAlgos) { return; }
        m_OnRspQryBrokerTradingAlgos(this, pBrokerTradingAlgos, pRspInfo, nRequestID, bIsLast);
    }
    virtual void OnRspQueryCFMMCTradingAccountToken(CThostFtdcQueryCFMMCTradingAccountTokenField *pQueryCFMMCTradingAccountToken, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
        if (!m_OnRspQueryCFMMCTradingAccountToken) { return; }
        m_OnRspQueryCFMMCTradingAccountToken(this, pQueryCFMMCTradingAccountToken, pRspInfo, nRequestID, bIsLast);
    }
    virtual void OnRtnFromBankToFutureByBank(CThostFtdcRspTransferField *pRspTransfer) {
        if (!m_OnRtnFromBankToFutureByBank) { return; }
        m_OnRtnFromBankToFutureByBank(this, pRspTransfer);
    }
    virtual void OnRtnFromFutureToBankByBank(CThostFtdcRspTransferField *pRspTransfer) {
        if (!m_OnRtnFromFutureToBankByBank) { return; }
        m_OnRtnFromFutureToBankByBank(this, pRspTransfer);
    }
    virtual void OnRtnRepealFromBankToFutureByBank(CThostFtdcRspRepealField *pRspRepeal) {
        if (!m_OnRtnRepealFromBankToFutureByBank) { return; }
        m_OnRtnRepealFromBankToFutureByBank(this, pRspRepeal);
    }
    virtual void OnRtnRepealFromFutureToBankByBank(CThostFtdcRspRepealField *pRspRepeal) {
        if (!m_OnRtnRepealFromFutureToBankByBank) { return; }
        m_OnRtnRepealFromFutureToBankByBank(this, pRspRepeal);
    }
    virtual void OnRtnFromBankToFutureByFuture(CThostFtdcRspTransferField *pRspTransfer) {
        if (!m_OnRtnFromBankToFutureByFuture) { return; }
        m_OnRtnFromBankToFutureByFuture(this, pRspTransfer);
    }
    virtual void OnRtnFromFutureToBankByFuture(CThostFtdcRspTransferField *pRspTransfer) {
        if (!m_OnRtnFromFutureToBankByFuture) { return; }
        m_OnRtnFromFutureToBankByFuture(this, pRspTransfer);
    }
    virtual void OnRtnRepealFromBankToFutureByFutureManual(CThostFtdcRspRepealField *pRspRepeal) {
        if (!m_OnRtnRepealFromBankToFutureByFutureManual) { return; }
        m_OnRtnRepealFromBankToFutureByFutureManual(this, pRspRepeal);
    }
    virtual void OnRtnRepealFromFutureToBankByFutureManual(CThostFtdcRspRepealField *pRspRepeal) {
        if (!m_OnRtnRepealFromFutureToBankByFutureManual) { return; }
        m_OnRtnRepealFromFutureToBankByFutureManual(this, pRspRepeal);
    }
    virtual void OnRtnQueryBankBalanceByFuture(CThostFtdcNotifyQueryAccountField *pNotifyQueryAccount) {
        if (!m_OnRtnQueryBankBalanceByFuture) { return; }
        m_OnRtnQueryBankBalanceByFuture(this, pNotifyQueryAccount);
    }
    virtual void OnErrRtnBankToFutureByFuture(CThostFtdcReqTransferField *pReqTransfer, CThostFtdcRspInfoField *pRspInfo) {
        if (!m_OnErrRtnBankToFutureByFuture) { return; }
        m_OnErrRtnBankToFutureByFuture(this, pReqTransfer, pRspInfo);
    }
    virtual void OnErrRtnFutureToBankByFuture(CThostFtdcReqTransferField *pReqTransfer, CThostFtdcRspInfoField *pRspInfo) {
        if (!m_OnErrRtnFutureToBankByFuture) { return; }
        m_OnErrRtnFutureToBankByFuture(this, pReqTransfer, pRspInfo);
    }
    virtual void OnErrRtnRepealBankToFutureByFutureManual(CThostFtdcReqRepealField *pReqRepeal, CThostFtdcRspInfoField *pRspInfo) {
        if (!m_OnErrRtnRepealBankToFutureByFutureManual) { return; }
        m_OnErrRtnRepealBankToFutureByFutureManual(this, pReqRepeal, pRspInfo);
    }
    virtual void OnErrRtnRepealFutureToBankByFutureManual(CThostFtdcReqRepealField *pReqRepeal, CThostFtdcRspInfoField *pRspInfo) {
        if (!m_OnErrRtnRepealFutureToBankByFutureManual) { return; }
        m_OnErrRtnRepealFutureToBankByFutureManual(this, pReqRepeal, pRspInfo);
    }
    virtual void OnErrRtnQueryBankBalanceByFuture(CThostFtdcReqQueryAccountField *pReqQueryAccount, CThostFtdcRspInfoField *pRspInfo) {
        if (!m_OnErrRtnQueryBankBalanceByFuture) { return; }
        m_OnErrRtnQueryBankBalanceByFuture(this, pReqQueryAccount, pRspInfo);
    }
    virtual void OnRtnRepealFromBankToFutureByFuture(CThostFtdcRspRepealField *pRspRepeal) {
        if (!m_OnRtnRepealFromBankToFutureByFuture) { return; }
        m_OnRtnRepealFromBankToFutureByFuture(this, pRspRepeal);
    }
    virtual void OnRtnRepealFromFutureToBankByFuture(CThostFtdcRspRepealField *pRspRepeal) {
        if (!m_OnRtnRepealFromFutureToBankByFuture) { return; }
        m_OnRtnRepealFromFutureToBankByFuture(this, pRspRepeal);
    }
    virtual void OnRspFromBankToFutureByFuture(CThostFtdcReqTransferField *pReqTransfer, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
        if (!m_OnRspFromBankToFutureByFuture) { return; }
        m_OnRspFromBankToFutureByFuture(this, pReqTransfer, pRspInfo, nRequestID, bIsLast);
    }
    virtual void OnRspFromFutureToBankByFuture(CThostFtdcReqTransferField *pReqTransfer, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
        if (!m_OnRspFromFutureToBankByFuture) { return; }
        m_OnRspFromFutureToBankByFuture(this, pReqTransfer, pRspInfo, nRequestID, bIsLast);
    }
    virtual void OnRspQueryBankAccountMoneyByFuture(CThostFtdcReqQueryAccountField *pReqQueryAccount, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
        if (!m_OnRspQueryBankAccountMoneyByFuture) { return; }
        m_OnRspQueryBankAccountMoneyByFuture(this, pReqQueryAccount, pRspInfo, nRequestID, bIsLast);
    }
    virtual void OnRtnOpenAccountByBank(CThostFtdcOpenAccountField *pOpenAccount) {
        if (!m_OnRtnOpenAccountByBank) { return; }
        m_OnRtnOpenAccountByBank(this, pOpenAccount);
    }
    virtual void OnRtnCancelAccountByBank(CThostFtdcCancelAccountField *pCancelAccount) {
        if (!m_OnRtnCancelAccountByBank) { return; }
        m_OnRtnCancelAccountByBank(this, pCancelAccount);
    }
    virtual void OnRtnChangeAccountByBank(CThostFtdcChangeAccountField *pChangeAccount) {
        if (!m_OnRtnChangeAccountByBank) { return; }
        m_OnRtnChangeAccountByBank(this, pChangeAccount);
    }
private:
    void (*m_OnFrontConnected)(void*);
    void (*m_OnFrontDisconnected)(void*, int);
    void (*m_OnHeartBeatWarning)(void*, int);
    void (*m_OnRspAuthenticate)(void*, CThostFtdcRspAuthenticateField *, CThostFtdcRspInfoField *, int, bool);
    void (*m_OnRspUserLogin)(void*, CThostFtdcRspUserLoginField *, CThostFtdcRspInfoField *, int, bool);
    void (*m_OnRspUserLogout)(void*, CThostFtdcUserLogoutField *, CThostFtdcRspInfoField *, int, bool);
    void (*m_OnRspUserPasswordUpdate)(void*, CThostFtdcUserPasswordUpdateField *, CThostFtdcRspInfoField *, int, bool);
    void (*m_OnRspTradingAccountPasswordUpdate)(void*, CThostFtdcTradingAccountPasswordUpdateField *, CThostFtdcRspInfoField *, int, bool);
    void (*m_OnRspOrderInsert)(void*, CThostFtdcInputOrderField *, CThostFtdcRspInfoField *, int, bool);
    void (*m_OnRspParkedOrderInsert)(void*, CThostFtdcParkedOrderField *, CThostFtdcRspInfoField *, int, bool);
    void (*m_OnRspParkedOrderAction)(void*, CThostFtdcParkedOrderActionField *, CThostFtdcRspInfoField *, int, bool);
    void (*m_OnRspOrderAction)(void*, CThostFtdcInputOrderActionField *, CThostFtdcRspInfoField *, int, bool);
    void (*m_OnRspQueryMaxOrderVolume)(void*, CThostFtdcQueryMaxOrderVolumeField *, CThostFtdcRspInfoField *, int, bool);
    void (*m_OnRspSettlementInfoConfirm)(void*, CThostFtdcSettlementInfoConfirmField *, CThostFtdcRspInfoField *, int, bool);
    void (*m_OnRspRemoveParkedOrder)(void*, CThostFtdcRemoveParkedOrderField *, CThostFtdcRspInfoField *, int, bool);
    void (*m_OnRspRemoveParkedOrderAction)(void*, CThostFtdcRemoveParkedOrderActionField *, CThostFtdcRspInfoField *, int, bool);
    void (*m_OnRspExecOrderInsert)(void*, CThostFtdcInputExecOrderField *, CThostFtdcRspInfoField *, int, bool);
    void (*m_OnRspExecOrderAction)(void*, CThostFtdcInputExecOrderActionField *, CThostFtdcRspInfoField *, int, bool);
    void (*m_OnRspForQuoteInsert)(void*, CThostFtdcInputForQuoteField *, CThostFtdcRspInfoField *, int, bool);
    void (*m_OnRspQuoteInsert)(void*, CThostFtdcInputQuoteField *, CThostFtdcRspInfoField *, int, bool);
    void (*m_OnRspQuoteAction)(void*, CThostFtdcInputQuoteActionField *, CThostFtdcRspInfoField *, int, bool);
    void (*m_OnRspBatchOrderAction)(void*, CThostFtdcInputBatchOrderActionField *, CThostFtdcRspInfoField *, int, bool);
    void (*m_OnRspCombActionInsert)(void*, CThostFtdcInputCombActionField *, CThostFtdcRspInfoField *, int, bool);
    void (*m_OnRspQryOrder)(void*, CThostFtdcOrderField *, CThostFtdcRspInfoField *, int, bool);
    void (*m_OnRspQryTrade)(void*, CThostFtdcTradeField *, CThostFtdcRspInfoField *, int, bool);
    void (*m_OnRspQryInvestorPosition)(void*, CThostFtdcInvestorPositionField *, CThostFtdcRspInfoField *, int, bool);
    void (*m_OnRspQryTradingAccount)(void*, CThostFtdcTradingAccountField *, CThostFtdcRspInfoField *, int, bool);
    void (*m_OnRspQryInvestor)(void*, CThostFtdcInvestorField *, CThostFtdcRspInfoField *, int, bool);
    void (*m_OnRspQryTradingCode)(void*, CThostFtdcTradingCodeField *, CThostFtdcRspInfoField *, int, bool);
    void (*m_OnRspQryInstrumentMarginRate)(void*, CThostFtdcInstrumentMarginRateField *, CThostFtdcRspInfoField *, int, bool);
    void (*m_OnRspQryInstrumentCommissionRate)(void*, CThostFtdcInstrumentCommissionRateField *, CThostFtdcRspInfoField *, int, bool);
    void (*m_OnRspQryExchange)(void*, CThostFtdcExchangeField *, CThostFtdcRspInfoField *, int, bool);
    void (*m_OnRspQryProduct)(void*, CThostFtdcProductField *, CThostFtdcRspInfoField *, int, bool);
    void (*m_OnRspQryInstrument)(void*, CThostFtdcInstrumentField *, CThostFtdcRspInfoField *, int, bool);
    void (*m_OnRspQryDepthMarketData)(void*, CThostFtdcDepthMarketDataField *, CThostFtdcRspInfoField *, int, bool);
    void (*m_OnRspQrySettlementInfo)(void*, CThostFtdcSettlementInfoField *, CThostFtdcRspInfoField *, int, bool);
    void (*m_OnRspQryTransferBank)(void*, CThostFtdcTransferBankField *, CThostFtdcRspInfoField *, int, bool);
    void (*m_OnRspQryInvestorPositionDetail)(void*, CThostFtdcInvestorPositionDetailField *, CThostFtdcRspInfoField *, int, bool);
    void (*m_OnRspQryNotice)(void*, CThostFtdcNoticeField *, CThostFtdcRspInfoField *, int, bool);
    void (*m_OnRspQrySettlementInfoConfirm)(void*, CThostFtdcSettlementInfoConfirmField *, CThostFtdcRspInfoField *, int, bool);
    void (*m_OnRspQryInvestorPositionCombineDetail)(void*, CThostFtdcInvestorPositionCombineDetailField *, CThostFtdcRspInfoField *, int, bool);
    void (*m_OnRspQryCFMMCTradingAccountKey)(void*, CThostFtdcCFMMCTradingAccountKeyField *, CThostFtdcRspInfoField *, int, bool);
    void (*m_OnRspQryEWarrantOffset)(void*, CThostFtdcEWarrantOffsetField *, CThostFtdcRspInfoField *, int, bool);
    void (*m_OnRspQryInvestorProductGroupMargin)(void*, CThostFtdcInvestorProductGroupMarginField *, CThostFtdcRspInfoField *, int, bool);
    void (*m_OnRspQryExchangeMarginRate)(void*, CThostFtdcExchangeMarginRateField *, CThostFtdcRspInfoField *, int, bool);
    void (*m_OnRspQryExchangeMarginRateAdjust)(void*, CThostFtdcExchangeMarginRateAdjustField *, CThostFtdcRspInfoField *, int, bool);
    void (*m_OnRspQryExchangeRate)(void*, CThostFtdcExchangeRateField *, CThostFtdcRspInfoField *, int, bool);
    void (*m_OnRspQrySecAgentACIDMap)(void*, CThostFtdcSecAgentACIDMapField *, CThostFtdcRspInfoField *, int, bool);
    void (*m_OnRspQryProductExchRate)(void*, CThostFtdcProductExchRateField *, CThostFtdcRspInfoField *, int, bool);
    void (*m_OnRspQryProductGroup)(void*, CThostFtdcProductGroupField *, CThostFtdcRspInfoField *, int, bool);
    void (*m_OnRspQryMMInstrumentCommissionRate)(void*, CThostFtdcMMInstrumentCommissionRateField *, CThostFtdcRspInfoField *, int, bool);
    void (*m_OnRspQryMMOptionInstrCommRate)(void*, CThostFtdcMMOptionInstrCommRateField *, CThostFtdcRspInfoField *, int, bool);
    void (*m_OnRspQryInstrumentOrderCommRate)(void*, CThostFtdcInstrumentOrderCommRateField *, CThostFtdcRspInfoField *, int, bool);
    void (*m_OnRspQryOptionInstrTradeCost)(void*, CThostFtdcOptionInstrTradeCostField *, CThostFtdcRspInfoField *, int, bool);
    void (*m_OnRspQryOptionInstrCommRate)(void*, CThostFtdcOptionInstrCommRateField *, CThostFtdcRspInfoField *, int, bool);
    void (*m_OnRspQryExecOrder)(void*, CThostFtdcExecOrderField *, CThostFtdcRspInfoField *, int, bool);
    void (*m_OnRspQryForQuote)(void*, CThostFtdcForQuoteField *, CThostFtdcRspInfoField *, int, bool);
    void (*m_OnRspQryQuote)(void*, CThostFtdcQuoteField *, CThostFtdcRspInfoField *, int, bool);
    void (*m_OnRspQryCombInstrumentGuard)(void*, CThostFtdcCombInstrumentGuardField *, CThostFtdcRspInfoField *, int, bool);
    void (*m_OnRspQryCombAction)(void*, CThostFtdcCombActionField *, CThostFtdcRspInfoField *, int, bool);
    void (*m_OnRspQryTransferSerial)(void*, CThostFtdcTransferSerialField *, CThostFtdcRspInfoField *, int, bool);
    void (*m_OnRspQryAccountregister)(void*, CThostFtdcAccountregisterField *, CThostFtdcRspInfoField *, int, bool);
    void (*m_OnRspError)(void*, CThostFtdcRspInfoField *, int, bool);
    void (*m_OnRtnOrder)(void*, CThostFtdcOrderField *);
    void (*m_OnRtnTrade)(void*, CThostFtdcTradeField *);
    void (*m_OnErrRtnOrderInsert)(void*, CThostFtdcInputOrderField *, CThostFtdcRspInfoField *);
    void (*m_OnErrRtnOrderAction)(void*, CThostFtdcOrderActionField *, CThostFtdcRspInfoField *);
    void (*m_OnRtnInstrumentStatus)(void*, CThostFtdcInstrumentStatusField *);
    void (*m_OnRtnBulletin)(void*, CThostFtdcBulletinField *);
    void (*m_OnRtnTradingNotice)(void*, CThostFtdcTradingNoticeInfoField *);
    void (*m_OnRtnErrorConditionalOrder)(void*, CThostFtdcErrorConditionalOrderField *);
    void (*m_OnRtnExecOrder)(void*, CThostFtdcExecOrderField *);
    void (*m_OnErrRtnExecOrderInsert)(void*, CThostFtdcInputExecOrderField *, CThostFtdcRspInfoField *);
    void (*m_OnErrRtnExecOrderAction)(void*, CThostFtdcExecOrderActionField *, CThostFtdcRspInfoField *);
    void (*m_OnErrRtnForQuoteInsert)(void*, CThostFtdcInputForQuoteField *, CThostFtdcRspInfoField *);
    void (*m_OnRtnQuote)(void*, CThostFtdcQuoteField *);
    void (*m_OnErrRtnQuoteInsert)(void*, CThostFtdcInputQuoteField *, CThostFtdcRspInfoField *);
    void (*m_OnErrRtnQuoteAction)(void*, CThostFtdcQuoteActionField *, CThostFtdcRspInfoField *);
    void (*m_OnRtnForQuoteRsp)(void*, CThostFtdcForQuoteRspField *);
    void (*m_OnRtnCFMMCTradingAccountToken)(void*, CThostFtdcCFMMCTradingAccountTokenField *);
    void (*m_OnErrRtnBatchOrderAction)(void*, CThostFtdcBatchOrderActionField *, CThostFtdcRspInfoField *);
    void (*m_OnRtnCombAction)(void*, CThostFtdcCombActionField *);
    void (*m_OnErrRtnCombActionInsert)(void*, CThostFtdcInputCombActionField *, CThostFtdcRspInfoField *);
    void (*m_OnRspQryContractBank)(void*, CThostFtdcContractBankField *, CThostFtdcRspInfoField *, int, bool);
    void (*m_OnRspQryParkedOrder)(void*, CThostFtdcParkedOrderField *, CThostFtdcRspInfoField *, int, bool);
    void (*m_OnRspQryParkedOrderAction)(void*, CThostFtdcParkedOrderActionField *, CThostFtdcRspInfoField *, int, bool);
    void (*m_OnRspQryTradingNotice)(void*, CThostFtdcTradingNoticeField *, CThostFtdcRspInfoField *, int, bool);
    void (*m_OnRspQryBrokerTradingParams)(void*, CThostFtdcBrokerTradingParamsField *, CThostFtdcRspInfoField *, int, bool);
    void (*m_OnRspQryBrokerTradingAlgos)(void*, CThostFtdcBrokerTradingAlgosField *, CThostFtdcRspInfoField *, int, bool);
    void (*m_OnRspQueryCFMMCTradingAccountToken)(void*, CThostFtdcQueryCFMMCTradingAccountTokenField *, CThostFtdcRspInfoField *, int, bool);
    void (*m_OnRtnFromBankToFutureByBank)(void*, CThostFtdcRspTransferField *);
    void (*m_OnRtnFromFutureToBankByBank)(void*, CThostFtdcRspTransferField *);
    void (*m_OnRtnRepealFromBankToFutureByBank)(void*, CThostFtdcRspRepealField *);
    void (*m_OnRtnRepealFromFutureToBankByBank)(void*, CThostFtdcRspRepealField *);
    void (*m_OnRtnFromBankToFutureByFuture)(void*, CThostFtdcRspTransferField *);
    void (*m_OnRtnFromFutureToBankByFuture)(void*, CThostFtdcRspTransferField *);
    void (*m_OnRtnRepealFromBankToFutureByFutureManual)(void*, CThostFtdcRspRepealField *);
    void (*m_OnRtnRepealFromFutureToBankByFutureManual)(void*, CThostFtdcRspRepealField *);
    void (*m_OnRtnQueryBankBalanceByFuture)(void*, CThostFtdcNotifyQueryAccountField *);
    void (*m_OnErrRtnBankToFutureByFuture)(void*, CThostFtdcReqTransferField *, CThostFtdcRspInfoField *);
    void (*m_OnErrRtnFutureToBankByFuture)(void*, CThostFtdcReqTransferField *, CThostFtdcRspInfoField *);
    void (*m_OnErrRtnRepealBankToFutureByFutureManual)(void*, CThostFtdcReqRepealField *, CThostFtdcRspInfoField *);
    void (*m_OnErrRtnRepealFutureToBankByFutureManual)(void*, CThostFtdcReqRepealField *, CThostFtdcRspInfoField *);
    void (*m_OnErrRtnQueryBankBalanceByFuture)(void*, CThostFtdcReqQueryAccountField *, CThostFtdcRspInfoField *);
    void (*m_OnRtnRepealFromBankToFutureByFuture)(void*, CThostFtdcRspRepealField *);
    void (*m_OnRtnRepealFromFutureToBankByFuture)(void*, CThostFtdcRspRepealField *);
    void (*m_OnRspFromBankToFutureByFuture)(void*, CThostFtdcReqTransferField *, CThostFtdcRspInfoField *, int, bool);
    void (*m_OnRspFromFutureToBankByFuture)(void*, CThostFtdcReqTransferField *, CThostFtdcRspInfoField *, int, bool);
    void (*m_OnRspQueryBankAccountMoneyByFuture)(void*, CThostFtdcReqQueryAccountField *, CThostFtdcRspInfoField *, int, bool);
    void (*m_OnRtnOpenAccountByBank)(void*, CThostFtdcOpenAccountField *);
    void (*m_OnRtnCancelAccountByBank)(void*, CThostFtdcCancelAccountField *);
    void (*m_OnRtnChangeAccountByBank)(void*, CThostFtdcChangeAccountField *);
};


void* CreateSpi() {
    return new PyCtpTraderSpi();
}

int RegCallBack(void* spi, char* name, void *callback) {
    return ((PyCtpTraderSpi*)spi)->registry(name, callback) ? 0 : -1;
}

void* CreateApi(char* pszFlowPath) {
    return CThostFtdcTraderApi::CreateFtdcTraderApi(pszFlowPath);
}


void Release(void* api) {
    ((CThostFtdcTraderApi*)api)->Release();
}

void Init(void* api) {
    ((CThostFtdcTraderApi*)api)->Init();
}

int Join(void* api) {
    return ((CThostFtdcTraderApi*)api)->Join();
}

const char * GetTradingDay(void* api) {
    return ((CThostFtdcTraderApi*)api)->GetTradingDay();
}

void RegisterFront(void* api, char * pszFrontAddress) {
    ((CThostFtdcTraderApi*)api)->RegisterFront(pszFrontAddress);
}

void RegisterNameServer(void* api, char * pszNsAddress) {
    ((CThostFtdcTraderApi*)api)->RegisterNameServer(pszNsAddress);
}

void RegisterFensUserInfo(void* api, CThostFtdcFensUserInfoField * pFensUserInfo) {
    ((CThostFtdcTraderApi*)api)->RegisterFensUserInfo(pFensUserInfo);
}

void RegisterSpi(void* api, CThostFtdcTraderSpi * pSpi) {
    ((CThostFtdcTraderApi*)api)->RegisterSpi(pSpi);
}

void SubscribePrivateTopic(void* api, THOST_TE_RESUME_TYPE nResumeType) {
    ((CThostFtdcTraderApi*)api)->SubscribePrivateTopic(nResumeType);
}

void SubscribePublicTopic(void* api, THOST_TE_RESUME_TYPE nResumeType) {
    ((CThostFtdcTraderApi*)api)->SubscribePublicTopic(nResumeType);
}

int ReqAuthenticate(void* api, CThostFtdcReqAuthenticateField * pReqAuthenticateField, int nRequestID) {
    return ((CThostFtdcTraderApi*)api)->ReqAuthenticate(pReqAuthenticateField, nRequestID);
}

int ReqUserLogin(void* api, CThostFtdcReqUserLoginField * pReqUserLoginField, int nRequestID) {
    return ((CThostFtdcTraderApi*)api)->ReqUserLogin(pReqUserLoginField, nRequestID);
}

int ReqUserLogout(void* api, CThostFtdcUserLogoutField * pUserLogout, int nRequestID) {
    return ((CThostFtdcTraderApi*)api)->ReqUserLogout(pUserLogout, nRequestID);
}

int ReqUserPasswordUpdate(void* api, CThostFtdcUserPasswordUpdateField * pUserPasswordUpdate, int nRequestID) {
    return ((CThostFtdcTraderApi*)api)->ReqUserPasswordUpdate(pUserPasswordUpdate, nRequestID);
}

int ReqTradingAccountPasswordUpdate(void* api, CThostFtdcTradingAccountPasswordUpdateField * pTradingAccountPasswordUpdate, int nRequestID) {
    return ((CThostFtdcTraderApi*)api)->ReqTradingAccountPasswordUpdate(pTradingAccountPasswordUpdate, nRequestID);
}

int ReqOrderInsert(void* api, CThostFtdcInputOrderField * pInputOrder, int nRequestID) {
    return ((CThostFtdcTraderApi*)api)->ReqOrderInsert(pInputOrder, nRequestID);
}

int ReqParkedOrderInsert(void* api, CThostFtdcParkedOrderField * pParkedOrder, int nRequestID) {
    return ((CThostFtdcTraderApi*)api)->ReqParkedOrderInsert(pParkedOrder, nRequestID);
}

int ReqParkedOrderAction(void* api, CThostFtdcParkedOrderActionField * pParkedOrderAction, int nRequestID) {
    return ((CThostFtdcTraderApi*)api)->ReqParkedOrderAction(pParkedOrderAction, nRequestID);
}

int ReqOrderAction(void* api, CThostFtdcInputOrderActionField * pInputOrderAction, int nRequestID) {
    return ((CThostFtdcTraderApi*)api)->ReqOrderAction(pInputOrderAction, nRequestID);
}

int ReqQueryMaxOrderVolume(void* api, CThostFtdcQueryMaxOrderVolumeField * pQueryMaxOrderVolume, int nRequestID) {
    return ((CThostFtdcTraderApi*)api)->ReqQueryMaxOrderVolume(pQueryMaxOrderVolume, nRequestID);
}

int ReqSettlementInfoConfirm(void* api, CThostFtdcSettlementInfoConfirmField * pSettlementInfoConfirm, int nRequestID) {
    return ((CThostFtdcTraderApi*)api)->ReqSettlementInfoConfirm(pSettlementInfoConfirm, nRequestID);
}

int ReqRemoveParkedOrder(void* api, CThostFtdcRemoveParkedOrderField * pRemoveParkedOrder, int nRequestID) {
    return ((CThostFtdcTraderApi*)api)->ReqRemoveParkedOrder(pRemoveParkedOrder, nRequestID);
}

int ReqRemoveParkedOrderAction(void* api, CThostFtdcRemoveParkedOrderActionField * pRemoveParkedOrderAction, int nRequestID) {
    return ((CThostFtdcTraderApi*)api)->ReqRemoveParkedOrderAction(pRemoveParkedOrderAction, nRequestID);
}

int ReqExecOrderInsert(void* api, CThostFtdcInputExecOrderField * pInputExecOrder, int nRequestID) {
    return ((CThostFtdcTraderApi*)api)->ReqExecOrderInsert(pInputExecOrder, nRequestID);
}

int ReqExecOrderAction(void* api, CThostFtdcInputExecOrderActionField * pInputExecOrderAction, int nRequestID) {
    return ((CThostFtdcTraderApi*)api)->ReqExecOrderAction(pInputExecOrderAction, nRequestID);
}

int ReqForQuoteInsert(void* api, CThostFtdcInputForQuoteField * pInputForQuote, int nRequestID) {
    return ((CThostFtdcTraderApi*)api)->ReqForQuoteInsert(pInputForQuote, nRequestID);
}

int ReqQuoteInsert(void* api, CThostFtdcInputQuoteField * pInputQuote, int nRequestID) {
    return ((CThostFtdcTraderApi*)api)->ReqQuoteInsert(pInputQuote, nRequestID);
}

int ReqQuoteAction(void* api, CThostFtdcInputQuoteActionField * pInputQuoteAction, int nRequestID) {
    return ((CThostFtdcTraderApi*)api)->ReqQuoteAction(pInputQuoteAction, nRequestID);
}

int ReqBatchOrderAction(void* api, CThostFtdcInputBatchOrderActionField * pInputBatchOrderAction, int nRequestID) {
    return ((CThostFtdcTraderApi*)api)->ReqBatchOrderAction(pInputBatchOrderAction, nRequestID);
}

int ReqCombActionInsert(void* api, CThostFtdcInputCombActionField * pInputCombAction, int nRequestID) {
    return ((CThostFtdcTraderApi*)api)->ReqCombActionInsert(pInputCombAction, nRequestID);
}

int ReqQryOrder(void* api, CThostFtdcQryOrderField * pQryOrder, int nRequestID) {
    return ((CThostFtdcTraderApi*)api)->ReqQryOrder(pQryOrder, nRequestID);
}

int ReqQryTrade(void* api, CThostFtdcQryTradeField * pQryTrade, int nRequestID) {
    return ((CThostFtdcTraderApi*)api)->ReqQryTrade(pQryTrade, nRequestID);
}

int ReqQryInvestorPosition(void* api, CThostFtdcQryInvestorPositionField * pQryInvestorPosition, int nRequestID) {
    return ((CThostFtdcTraderApi*)api)->ReqQryInvestorPosition(pQryInvestorPosition, nRequestID);
}

int ReqQryTradingAccount(void* api, CThostFtdcQryTradingAccountField * pQryTradingAccount, int nRequestID) {
    return ((CThostFtdcTraderApi*)api)->ReqQryTradingAccount(pQryTradingAccount, nRequestID);
}

int ReqQryInvestor(void* api, CThostFtdcQryInvestorField * pQryInvestor, int nRequestID) {
    return ((CThostFtdcTraderApi*)api)->ReqQryInvestor(pQryInvestor, nRequestID);
}

int ReqQryTradingCode(void* api, CThostFtdcQryTradingCodeField * pQryTradingCode, int nRequestID) {
    return ((CThostFtdcTraderApi*)api)->ReqQryTradingCode(pQryTradingCode, nRequestID);
}

int ReqQryInstrumentMarginRate(void* api, CThostFtdcQryInstrumentMarginRateField * pQryInstrumentMarginRate, int nRequestID) {
    return ((CThostFtdcTraderApi*)api)->ReqQryInstrumentMarginRate(pQryInstrumentMarginRate, nRequestID);
}

int ReqQryInstrumentCommissionRate(void* api, CThostFtdcQryInstrumentCommissionRateField * pQryInstrumentCommissionRate, int nRequestID) {
    return ((CThostFtdcTraderApi*)api)->ReqQryInstrumentCommissionRate(pQryInstrumentCommissionRate, nRequestID);
}

int ReqQryExchange(void* api, CThostFtdcQryExchangeField * pQryExchange, int nRequestID) {
    return ((CThostFtdcTraderApi*)api)->ReqQryExchange(pQryExchange, nRequestID);
}

int ReqQryProduct(void* api, CThostFtdcQryProductField * pQryProduct, int nRequestID) {
    return ((CThostFtdcTraderApi*)api)->ReqQryProduct(pQryProduct, nRequestID);
}

int ReqQryInstrument(void* api, CThostFtdcQryInstrumentField * pQryInstrument, int nRequestID) {
    return ((CThostFtdcTraderApi*)api)->ReqQryInstrument(pQryInstrument, nRequestID);
}

int ReqQryDepthMarketData(void* api, CThostFtdcQryDepthMarketDataField * pQryDepthMarketData, int nRequestID) {
    return ((CThostFtdcTraderApi*)api)->ReqQryDepthMarketData(pQryDepthMarketData, nRequestID);
}

int ReqQrySettlementInfo(void* api, CThostFtdcQrySettlementInfoField * pQrySettlementInfo, int nRequestID) {
    return ((CThostFtdcTraderApi*)api)->ReqQrySettlementInfo(pQrySettlementInfo, nRequestID);
}

int ReqQryTransferBank(void* api, CThostFtdcQryTransferBankField * pQryTransferBank, int nRequestID) {
    return ((CThostFtdcTraderApi*)api)->ReqQryTransferBank(pQryTransferBank, nRequestID);
}

int ReqQryInvestorPositionDetail(void* api, CThostFtdcQryInvestorPositionDetailField * pQryInvestorPositionDetail, int nRequestID) {
    return ((CThostFtdcTraderApi*)api)->ReqQryInvestorPositionDetail(pQryInvestorPositionDetail, nRequestID);
}

int ReqQryNotice(void* api, CThostFtdcQryNoticeField * pQryNotice, int nRequestID) {
    return ((CThostFtdcTraderApi*)api)->ReqQryNotice(pQryNotice, nRequestID);
}

int ReqQrySettlementInfoConfirm(void* api, CThostFtdcQrySettlementInfoConfirmField * pQrySettlementInfoConfirm, int nRequestID) {
    return ((CThostFtdcTraderApi*)api)->ReqQrySettlementInfoConfirm(pQrySettlementInfoConfirm, nRequestID);
}

int ReqQryInvestorPositionCombineDetail(void* api, CThostFtdcQryInvestorPositionCombineDetailField * pQryInvestorPositionCombineDetail, int nRequestID) {
    return ((CThostFtdcTraderApi*)api)->ReqQryInvestorPositionCombineDetail(pQryInvestorPositionCombineDetail, nRequestID);
}

int ReqQryCFMMCTradingAccountKey(void* api, CThostFtdcQryCFMMCTradingAccountKeyField * pQryCFMMCTradingAccountKey, int nRequestID) {
    return ((CThostFtdcTraderApi*)api)->ReqQryCFMMCTradingAccountKey(pQryCFMMCTradingAccountKey, nRequestID);
}

int ReqQryEWarrantOffset(void* api, CThostFtdcQryEWarrantOffsetField * pQryEWarrantOffset, int nRequestID) {
    return ((CThostFtdcTraderApi*)api)->ReqQryEWarrantOffset(pQryEWarrantOffset, nRequestID);
}

int ReqQryInvestorProductGroupMargin(void* api, CThostFtdcQryInvestorProductGroupMarginField * pQryInvestorProductGroupMargin, int nRequestID) {
    return ((CThostFtdcTraderApi*)api)->ReqQryInvestorProductGroupMargin(pQryInvestorProductGroupMargin, nRequestID);
}

int ReqQryExchangeMarginRate(void* api, CThostFtdcQryExchangeMarginRateField * pQryExchangeMarginRate, int nRequestID) {
    return ((CThostFtdcTraderApi*)api)->ReqQryExchangeMarginRate(pQryExchangeMarginRate, nRequestID);
}

int ReqQryExchangeMarginRateAdjust(void* api, CThostFtdcQryExchangeMarginRateAdjustField * pQryExchangeMarginRateAdjust, int nRequestID) {
    return ((CThostFtdcTraderApi*)api)->ReqQryExchangeMarginRateAdjust(pQryExchangeMarginRateAdjust, nRequestID);
}

int ReqQryExchangeRate(void* api, CThostFtdcQryExchangeRateField * pQryExchangeRate, int nRequestID) {
    return ((CThostFtdcTraderApi*)api)->ReqQryExchangeRate(pQryExchangeRate, nRequestID);
}

int ReqQrySecAgentACIDMap(void* api, CThostFtdcQrySecAgentACIDMapField * pQrySecAgentACIDMap, int nRequestID) {
    return ((CThostFtdcTraderApi*)api)->ReqQrySecAgentACIDMap(pQrySecAgentACIDMap, nRequestID);
}

int ReqQryProductExchRate(void* api, CThostFtdcQryProductExchRateField * pQryProductExchRate, int nRequestID) {
    return ((CThostFtdcTraderApi*)api)->ReqQryProductExchRate(pQryProductExchRate, nRequestID);
}

int ReqQryProductGroup(void* api, CThostFtdcQryProductGroupField * pQryProductGroup, int nRequestID) {
    return ((CThostFtdcTraderApi*)api)->ReqQryProductGroup(pQryProductGroup, nRequestID);
}

int ReqQryMMInstrumentCommissionRate(void* api, CThostFtdcQryMMInstrumentCommissionRateField * pQryMMInstrumentCommissionRate, int nRequestID) {
    return ((CThostFtdcTraderApi*)api)->ReqQryMMInstrumentCommissionRate(pQryMMInstrumentCommissionRate, nRequestID);
}

int ReqQryMMOptionInstrCommRate(void* api, CThostFtdcQryMMOptionInstrCommRateField * pQryMMOptionInstrCommRate, int nRequestID) {
    return ((CThostFtdcTraderApi*)api)->ReqQryMMOptionInstrCommRate(pQryMMOptionInstrCommRate, nRequestID);
}

int ReqQryInstrumentOrderCommRate(void* api, CThostFtdcQryInstrumentOrderCommRateField * pQryInstrumentOrderCommRate, int nRequestID) {
    return ((CThostFtdcTraderApi*)api)->ReqQryInstrumentOrderCommRate(pQryInstrumentOrderCommRate, nRequestID);
}

int ReqQryOptionInstrTradeCost(void* api, CThostFtdcQryOptionInstrTradeCostField * pQryOptionInstrTradeCost, int nRequestID) {
    return ((CThostFtdcTraderApi*)api)->ReqQryOptionInstrTradeCost(pQryOptionInstrTradeCost, nRequestID);
}

int ReqQryOptionInstrCommRate(void* api, CThostFtdcQryOptionInstrCommRateField * pQryOptionInstrCommRate, int nRequestID) {
    return ((CThostFtdcTraderApi*)api)->ReqQryOptionInstrCommRate(pQryOptionInstrCommRate, nRequestID);
}

int ReqQryExecOrder(void* api, CThostFtdcQryExecOrderField * pQryExecOrder, int nRequestID) {
    return ((CThostFtdcTraderApi*)api)->ReqQryExecOrder(pQryExecOrder, nRequestID);
}

int ReqQryForQuote(void* api, CThostFtdcQryForQuoteField * pQryForQuote, int nRequestID) {
    return ((CThostFtdcTraderApi*)api)->ReqQryForQuote(pQryForQuote, nRequestID);
}

int ReqQryQuote(void* api, CThostFtdcQryQuoteField * pQryQuote, int nRequestID) {
    return ((CThostFtdcTraderApi*)api)->ReqQryQuote(pQryQuote, nRequestID);
}

int ReqQryCombInstrumentGuard(void* api, CThostFtdcQryCombInstrumentGuardField * pQryCombInstrumentGuard, int nRequestID) {
    return ((CThostFtdcTraderApi*)api)->ReqQryCombInstrumentGuard(pQryCombInstrumentGuard, nRequestID);
}

int ReqQryCombAction(void* api, CThostFtdcQryCombActionField * pQryCombAction, int nRequestID) {
    return ((CThostFtdcTraderApi*)api)->ReqQryCombAction(pQryCombAction, nRequestID);
}

int ReqQryTransferSerial(void* api, CThostFtdcQryTransferSerialField * pQryTransferSerial, int nRequestID) {
    return ((CThostFtdcTraderApi*)api)->ReqQryTransferSerial(pQryTransferSerial, nRequestID);
}

int ReqQryAccountregister(void* api, CThostFtdcQryAccountregisterField * pQryAccountregister, int nRequestID) {
    return ((CThostFtdcTraderApi*)api)->ReqQryAccountregister(pQryAccountregister, nRequestID);
}

int ReqQryContractBank(void* api, CThostFtdcQryContractBankField * pQryContractBank, int nRequestID) {
    return ((CThostFtdcTraderApi*)api)->ReqQryContractBank(pQryContractBank, nRequestID);
}

int ReqQryParkedOrder(void* api, CThostFtdcQryParkedOrderField * pQryParkedOrder, int nRequestID) {
    return ((CThostFtdcTraderApi*)api)->ReqQryParkedOrder(pQryParkedOrder, nRequestID);
}

int ReqQryParkedOrderAction(void* api, CThostFtdcQryParkedOrderActionField * pQryParkedOrderAction, int nRequestID) {
    return ((CThostFtdcTraderApi*)api)->ReqQryParkedOrderAction(pQryParkedOrderAction, nRequestID);
}

int ReqQryTradingNotice(void* api, CThostFtdcQryTradingNoticeField * pQryTradingNotice, int nRequestID) {
    return ((CThostFtdcTraderApi*)api)->ReqQryTradingNotice(pQryTradingNotice, nRequestID);
}

int ReqQryBrokerTradingParams(void* api, CThostFtdcQryBrokerTradingParamsField * pQryBrokerTradingParams, int nRequestID) {
    return ((CThostFtdcTraderApi*)api)->ReqQryBrokerTradingParams(pQryBrokerTradingParams, nRequestID);
}

int ReqQryBrokerTradingAlgos(void* api, CThostFtdcQryBrokerTradingAlgosField * pQryBrokerTradingAlgos, int nRequestID) {
    return ((CThostFtdcTraderApi*)api)->ReqQryBrokerTradingAlgos(pQryBrokerTradingAlgos, nRequestID);
}

int ReqQueryCFMMCTradingAccountToken(void* api, CThostFtdcQueryCFMMCTradingAccountTokenField * pQueryCFMMCTradingAccountToken, int nRequestID) {
    return ((CThostFtdcTraderApi*)api)->ReqQueryCFMMCTradingAccountToken(pQueryCFMMCTradingAccountToken, nRequestID);
}

int ReqFromBankToFutureByFuture(void* api, CThostFtdcReqTransferField * pReqTransfer, int nRequestID) {
    return ((CThostFtdcTraderApi*)api)->ReqFromBankToFutureByFuture(pReqTransfer, nRequestID);
}

int ReqFromFutureToBankByFuture(void* api, CThostFtdcReqTransferField * pReqTransfer, int nRequestID) {
    return ((CThostFtdcTraderApi*)api)->ReqFromFutureToBankByFuture(pReqTransfer, nRequestID);
}

int ReqQueryBankAccountMoneyByFuture(void* api, CThostFtdcReqQueryAccountField * pReqQueryAccount, int nRequestID) {
    return ((CThostFtdcTraderApi*)api)->ReqQueryBankAccountMoneyByFuture(pReqQueryAccount, nRequestID);
}


