#include "pyctpmdapi.h"
#include <string>


class PyCtpMdSpi : public CThostFtdcMdSpi {
public:
    PyCtpMdSpi()
        :m_OnFrontConnected(NULL)
        ,m_OnFrontDisconnected(NULL)
        ,m_OnHeartBeatWarning(NULL)
        ,m_OnRspUserLogin(NULL)
        ,m_OnRspUserLogout(NULL)
        ,m_OnRspError(NULL)
        ,m_OnRspSubMarketData(NULL)
        ,m_OnRspUnSubMarketData(NULL)
        ,m_OnRspSubForQuoteRsp(NULL)
        ,m_OnRspUnSubForQuoteRsp(NULL)
        ,m_OnRtnDepthMarketData(NULL)
        ,m_OnRtnForQuoteRsp(NULL){}

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
        if (name == "OnRspUserLogin") {
            m_OnRspUserLogin = (void (*)(void*, CThostFtdcRspUserLoginField *, CThostFtdcRspInfoField *, int, bool))ptr;
            return true;
        }
        if (name == "OnRspUserLogout") {
            m_OnRspUserLogout = (void (*)(void*, CThostFtdcUserLogoutField *, CThostFtdcRspInfoField *, int, bool))ptr;
            return true;
        }
        if (name == "OnRspError") {
            m_OnRspError = (void (*)(void*, CThostFtdcRspInfoField *, int, bool))ptr;
            return true;
        }
        if (name == "OnRspSubMarketData") {
            m_OnRspSubMarketData = (void (*)(void*, CThostFtdcSpecificInstrumentField *, CThostFtdcRspInfoField *, int, bool))ptr;
            return true;
        }
        if (name == "OnRspUnSubMarketData") {
            m_OnRspUnSubMarketData = (void (*)(void*, CThostFtdcSpecificInstrumentField *, CThostFtdcRspInfoField *, int, bool))ptr;
            return true;
        }
        if (name == "OnRspSubForQuoteRsp") {
            m_OnRspSubForQuoteRsp = (void (*)(void*, CThostFtdcSpecificInstrumentField *, CThostFtdcRspInfoField *, int, bool))ptr;
            return true;
        }
        if (name == "OnRspUnSubForQuoteRsp") {
            m_OnRspUnSubForQuoteRsp = (void (*)(void*, CThostFtdcSpecificInstrumentField *, CThostFtdcRspInfoField *, int, bool))ptr;
            return true;
        }
        if (name == "OnRtnDepthMarketData") {
            m_OnRtnDepthMarketData = (void (*)(void*, CThostFtdcDepthMarketDataField *))ptr;
            return true;
        }
        if (name == "OnRtnForQuoteRsp") {
            m_OnRtnForQuoteRsp = (void (*)(void*, CThostFtdcForQuoteRspField *))ptr;
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
    virtual void OnRspUserLogin(CThostFtdcRspUserLoginField *pRspUserLogin, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
        if (!m_OnRspUserLogin) { return; }
        m_OnRspUserLogin(this, pRspUserLogin, pRspInfo, nRequestID, bIsLast);
    }
    virtual void OnRspUserLogout(CThostFtdcUserLogoutField *pUserLogout, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
        if (!m_OnRspUserLogout) { return; }
        m_OnRspUserLogout(this, pUserLogout, pRspInfo, nRequestID, bIsLast);
    }
    virtual void OnRspError(CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
        if (!m_OnRspError) { return; }
        m_OnRspError(this, pRspInfo, nRequestID, bIsLast);
    }
    virtual void OnRspSubMarketData(CThostFtdcSpecificInstrumentField *pSpecificInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
        if (!m_OnRspSubMarketData) { return; }
        m_OnRspSubMarketData(this, pSpecificInstrument, pRspInfo, nRequestID, bIsLast);
    }
    virtual void OnRspUnSubMarketData(CThostFtdcSpecificInstrumentField *pSpecificInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
        if (!m_OnRspUnSubMarketData) { return; }
        m_OnRspUnSubMarketData(this, pSpecificInstrument, pRspInfo, nRequestID, bIsLast);
    }
    virtual void OnRspSubForQuoteRsp(CThostFtdcSpecificInstrumentField *pSpecificInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
        if (!m_OnRspSubForQuoteRsp) { return; }
        m_OnRspSubForQuoteRsp(this, pSpecificInstrument, pRspInfo, nRequestID, bIsLast);
    }
    virtual void OnRspUnSubForQuoteRsp(CThostFtdcSpecificInstrumentField *pSpecificInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
        if (!m_OnRspUnSubForQuoteRsp) { return; }
        m_OnRspUnSubForQuoteRsp(this, pSpecificInstrument, pRspInfo, nRequestID, bIsLast);
    }
    virtual void OnRtnDepthMarketData(CThostFtdcDepthMarketDataField *pDepthMarketData) {
        if (!m_OnRtnDepthMarketData) { return; }
        m_OnRtnDepthMarketData(this, pDepthMarketData);
    }
    virtual void OnRtnForQuoteRsp(CThostFtdcForQuoteRspField *pForQuoteRsp) {
        if (!m_OnRtnForQuoteRsp) { return; }
        m_OnRtnForQuoteRsp(this, pForQuoteRsp);
    }
private:
    void (*m_OnFrontConnected)(void*);
    void (*m_OnFrontDisconnected)(void*, int);
    void (*m_OnHeartBeatWarning)(void*, int);
    void (*m_OnRspUserLogin)(void*, CThostFtdcRspUserLoginField *, CThostFtdcRspInfoField *, int, bool);
    void (*m_OnRspUserLogout)(void*, CThostFtdcUserLogoutField *, CThostFtdcRspInfoField *, int, bool);
    void (*m_OnRspError)(void*, CThostFtdcRspInfoField *, int, bool);
    void (*m_OnRspSubMarketData)(void*, CThostFtdcSpecificInstrumentField *, CThostFtdcRspInfoField *, int, bool);
    void (*m_OnRspUnSubMarketData)(void*, CThostFtdcSpecificInstrumentField *, CThostFtdcRspInfoField *, int, bool);
    void (*m_OnRspSubForQuoteRsp)(void*, CThostFtdcSpecificInstrumentField *, CThostFtdcRspInfoField *, int, bool);
    void (*m_OnRspUnSubForQuoteRsp)(void*, CThostFtdcSpecificInstrumentField *, CThostFtdcRspInfoField *, int, bool);
    void (*m_OnRtnDepthMarketData)(void*, CThostFtdcDepthMarketDataField *);
    void (*m_OnRtnForQuoteRsp)(void*, CThostFtdcForQuoteRspField *);
};


void* CreateSpi() {
    return new PyCtpMdSpi();
}

int RegCallBack(void* spi, char* name, void *callback) {
    return ((PyCtpMdSpi*)spi)->registry(name, callback) ? 0 : -1;
}

void* CreateApi(char* pszFlowPath) {
    return CThostFtdcMdApi::CreateFtdcMdApi(pszFlowPath);
}


void Release(void* api) {
    ((CThostFtdcMdApi*)api)->Release();
}

void Init(void* api) {
    ((CThostFtdcMdApi*)api)->Init();
}

int Join(void* api) {
    return ((CThostFtdcMdApi*)api)->Join();
}

const char * GetTradingDay(void* api) {
    return ((CThostFtdcMdApi*)api)->GetTradingDay();
}

void RegisterFront(void* api, char * pszFrontAddress) {
    ((CThostFtdcMdApi*)api)->RegisterFront(pszFrontAddress);
}

void RegisterNameServer(void* api, char * pszNsAddress) {
    ((CThostFtdcMdApi*)api)->RegisterNameServer(pszNsAddress);
}

void RegisterFensUserInfo(void* api, CThostFtdcFensUserInfoField * pFensUserInfo) {
    ((CThostFtdcMdApi*)api)->RegisterFensUserInfo(pFensUserInfo);
}

void RegisterSpi(void* api, CThostFtdcMdSpi * pSpi) {
    ((CThostFtdcMdApi*)api)->RegisterSpi(pSpi);
}

int SubscribeMarketData(void* api, char * ppInstrumentID[], int nCount) {
    return ((CThostFtdcMdApi*)api)->SubscribeMarketData(ppInstrumentID, nCount);
}

int UnSubscribeMarketData(void* api, char * ppInstrumentID[], int nCount) {
    return ((CThostFtdcMdApi*)api)->UnSubscribeMarketData(ppInstrumentID, nCount);
}

int SubscribeForQuoteRsp(void* api, char * ppInstrumentID[], int nCount) {
    return ((CThostFtdcMdApi*)api)->SubscribeForQuoteRsp(ppInstrumentID, nCount);
}

int UnSubscribeForQuoteRsp(void* api, char * ppInstrumentID[], int nCount) {
    return ((CThostFtdcMdApi*)api)->UnSubscribeForQuoteRsp(ppInstrumentID, nCount);
}

int ReqUserLogin(void* api, CThostFtdcReqUserLoginField * pReqUserLoginField, int nRequestID) {
    return ((CThostFtdcMdApi*)api)->ReqUserLogin(pReqUserLoginField, nRequestID);
}

int ReqUserLogout(void* api, CThostFtdcUserLogoutField * pUserLogout, int nRequestID) {
    return ((CThostFtdcMdApi*)api)->ReqUserLogout(pUserLogout, nRequestID);
}


