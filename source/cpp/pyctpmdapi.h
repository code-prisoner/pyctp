#ifndef __PYCTPMDSPI_H__
#define __PYCTPMDSPI_H__

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

    void RegisterSpi(void* api, CThostFtdcMdSpi * pSpi);

    int SubscribeMarketData(void* api, char * ppInstrumentID[], int nCount);

    int UnSubscribeMarketData(void* api, char * ppInstrumentID[], int nCount);

    int SubscribeForQuoteRsp(void* api, char * ppInstrumentID[], int nCount);

    int UnSubscribeForQuoteRsp(void* api, char * ppInstrumentID[], int nCount);

    int ReqUserLogin(void* api, CThostFtdcReqUserLoginField * pReqUserLoginField, int nRequestID);

    int ReqUserLogout(void* api, CThostFtdcUserLogoutField * pUserLogout, int nRequestID);


}

#endif
