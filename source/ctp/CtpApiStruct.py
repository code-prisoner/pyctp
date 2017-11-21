# -*- coding: UTF-8 -*-
from ctypes import *

THOST_TERT_RESTART = 0
THOST_TERT_RESUME = 1
THOST_TERT_QUICK = 2

THOST_FTDC_EXP_Normal = b'0'
THOST_FTDC_EXP_GenOrderByTrade = b'1'
THOST_FTDC_ICT_EID = b'0'
THOST_FTDC_ICT_IDCard = b'1'
THOST_FTDC_ICT_OfficerIDCard = b'2'
THOST_FTDC_ICT_PoliceIDCard = b'3'
THOST_FTDC_ICT_SoldierIDCard = b'4'
THOST_FTDC_ICT_Passport = b'6'
THOST_FTDC_ICT_HomeComingCard = b'8'
THOST_FTDC_ICT_LicenseNo = b'9'
THOST_FTDC_ICT_TaxNo = b'A'
THOST_FTDC_ICT_TwMainlandTravelPermit = b'C'
THOST_FTDC_ICT_DrivingLicense = b'D'
THOST_FTDC_ICT_SocialID = b'F'
THOST_FTDC_ICT_LocalID = b'G'
THOST_FTDC_ICT_HKMCIDCard = b'I'
THOST_FTDC_ICT_AccountsPermits = b'J'
THOST_FTDC_ICT_OtherCard = b'x'
THOST_FTDC_IR_All = b'1'
THOST_FTDC_IR_Group = b'2'
THOST_FTDC_IR_Single = b'3'
THOST_FTDC_DR_All = b'1'
THOST_FTDC_DR_Group = b'2'
THOST_FTDC_DR_Single = b'3'
THOST_FTDC_DS_Asynchronous = b'1'
THOST_FTDC_DS_Synchronizing = b'2'
THOST_FTDC_DS_Synchronized = b'3'
THOST_FTDC_BDS_Synchronized = b'1'
THOST_FTDC_BDS_Synchronizing = b'2'
THOST_FTDC_ECS_NoConnection = b'1'
THOST_FTDC_ECS_QryInstrumentSent = b'2'
THOST_FTDC_ECS_GotInformation = b'9'
THOST_FTDC_TCS_NotConnected = b'1'
THOST_FTDC_TCS_Connected = b'2'
THOST_FTDC_TCS_QryInstrumentSent = b'3'
THOST_FTDC_TCS_SubPrivateFlow = b'4'
THOST_FTDC_FC_DataAsync = b'1'
THOST_FTDC_FC_ForceUserLogout = b'2'
THOST_FTDC_FC_UserPasswordUpdate = b'3'
THOST_FTDC_FC_BrokerPasswordUpdate = b'4'
THOST_FTDC_FC_InvestorPasswordUpdate = b'5'
THOST_FTDC_FC_OrderInsert = b'6'
THOST_FTDC_FC_OrderAction = b'7'
THOST_FTDC_FC_SyncSystemData = b'8'
THOST_FTDC_FC_SyncBrokerData = b'9'
THOST_FTDC_FC_BachSyncBrokerData = b'A'
THOST_FTDC_FC_SuperQuery = b'B'
THOST_FTDC_FC_ParkedOrderInsert = b'C'
THOST_FTDC_FC_ParkedOrderAction = b'D'
THOST_FTDC_FC_SyncOTP = b'E'
THOST_FTDC_FC_DeleteOrder = b'F'
THOST_FTDC_BFC_ForceUserLogout = b'1'
THOST_FTDC_BFC_UserPasswordUpdate = b'2'
THOST_FTDC_BFC_SyncBrokerData = b'3'
THOST_FTDC_BFC_BachSyncBrokerData = b'4'
THOST_FTDC_BFC_OrderInsert = b'5'
THOST_FTDC_BFC_OrderAction = b'6'
THOST_FTDC_BFC_AllQuery = b'7'
THOST_FTDC_BFC_log = b'a'
THOST_FTDC_BFC_BaseQry = b'b'
THOST_FTDC_BFC_TradeQry = b'c'
THOST_FTDC_BFC_Trade = b'd'
THOST_FTDC_BFC_Virement = b'e'
THOST_FTDC_BFC_Risk = b'f'
THOST_FTDC_BFC_Session = b'g'
THOST_FTDC_BFC_RiskNoticeCtl = b'h'
THOST_FTDC_BFC_RiskNotice = b'i'
THOST_FTDC_BFC_BrokerDeposit = b'j'
THOST_FTDC_BFC_QueryFund = b'k'
THOST_FTDC_BFC_QueryOrder = b'l'
THOST_FTDC_BFC_QueryTrade = b'm'
THOST_FTDC_BFC_QueryPosition = b'n'
THOST_FTDC_BFC_QueryMarketData = b'o'
THOST_FTDC_BFC_QueryUserEvent = b'p'
THOST_FTDC_BFC_QueryRiskNotify = b'q'
THOST_FTDC_BFC_QueryFundChange = b'r'
THOST_FTDC_BFC_QueryInvestor = b's'
THOST_FTDC_BFC_QueryTradingCode = b't'
THOST_FTDC_BFC_ForceClose = b'u'
THOST_FTDC_BFC_PressTest = b'v'
THOST_FTDC_BFC_RemainCalc = b'w'
THOST_FTDC_BFC_NetPositionInd = b'x'
THOST_FTDC_BFC_RiskPredict = b'y'
THOST_FTDC_BFC_DataExport = b'z'
THOST_FTDC_BFC_RiskTargetSetup = b'A'
THOST_FTDC_BFC_MarketDataWarn = b'B'
THOST_FTDC_BFC_QryBizNotice = b'C'
THOST_FTDC_BFC_CfgBizNotice = b'D'
THOST_FTDC_BFC_SyncOTP = b'E'
THOST_FTDC_BFC_SendBizNotice = b'F'
THOST_FTDC_BFC_CfgRiskLevelStd = b'G'
THOST_FTDC_BFC_TbCommand = b'H'
THOST_FTDC_BFC_DeleteOrder = b'J'
THOST_FTDC_BFC_ParkedOrderInsert = b'K'
THOST_FTDC_BFC_ParkedOrderAction = b'L'
THOST_FTDC_BFC_ExecOrderNoCheck = b'M'
THOST_FTDC_OAS_Submitted = b'a'
THOST_FTDC_OAS_Accepted = b'b'
THOST_FTDC_OAS_Rejected = b'c'
THOST_FTDC_OST_AllTraded = b'0'
THOST_FTDC_OST_PartTradedQueueing = b'1'
THOST_FTDC_OST_PartTradedNotQueueing = b'2'
THOST_FTDC_OST_NoTradeQueueing = b'3'
THOST_FTDC_OST_NoTradeNotQueueing = b'4'
THOST_FTDC_OST_Canceled = b'5'
THOST_FTDC_OST_Unknown = b'a'
THOST_FTDC_OST_NotTouched = b'b'
THOST_FTDC_OST_Touched = b'c'
THOST_FTDC_OSS_InsertSubmitted = b'0'
THOST_FTDC_OSS_CancelSubmitted = b'1'
THOST_FTDC_OSS_ModifySubmitted = b'2'
THOST_FTDC_OSS_Accepted = b'3'
THOST_FTDC_OSS_InsertRejected = b'4'
THOST_FTDC_OSS_CancelRejected = b'5'
THOST_FTDC_OSS_ModifyRejected = b'6'
THOST_FTDC_PSD_Today = b'1'
THOST_FTDC_PSD_History = b'2'
THOST_FTDC_PDT_UseHistory = b'1'
THOST_FTDC_PDT_NoUseHistory = b'2'
THOST_FTDC_ER_Broker = b'1'
THOST_FTDC_ER_Host = b'2'
THOST_FTDC_ER_Maker = b'3'
THOST_FTDC_PC_Futures = b'1'
THOST_FTDC_PC_Options = b'2'
THOST_FTDC_PC_Combination = b'3'
THOST_FTDC_PC_Spot = b'4'
THOST_FTDC_PC_EFP = b'5'
THOST_FTDC_PC_SpotOption = b'6'
THOST_FTDC_IP_NotStart = b'0'
THOST_FTDC_IP_Started = b'1'
THOST_FTDC_IP_Pause = b'2'
THOST_FTDC_IP_Expired = b'3'
THOST_FTDC_D_Buy = b'0'
THOST_FTDC_D_Sell = b'1'
THOST_FTDC_PT_Net = b'1'
THOST_FTDC_PT_Gross = b'2'
THOST_FTDC_PD_Net = b'1'
THOST_FTDC_PD_Long = b'2'
THOST_FTDC_PD_Short = b'3'
THOST_FTDC_SS_NonActive = b'1'
THOST_FTDC_SS_Startup = b'2'
THOST_FTDC_SS_Operating = b'3'
THOST_FTDC_SS_Settlement = b'4'
THOST_FTDC_SS_SettlementFinished = b'5'
THOST_FTDC_RA_Trade = b'0'
THOST_FTDC_RA_Settlement = b'1'
THOST_FTDC_HF_Speculation = b'1'
THOST_FTDC_HF_Arbitrage = b'2'
THOST_FTDC_HF_Hedge = b'3'
THOST_FTDC_HF_MarketMaker = b'5'
THOST_FTDC_BHF_Speculation = b'1'
THOST_FTDC_BHF_Arbitrage = b'2'
THOST_FTDC_BHF_Hedge = b'3'
THOST_FTDC_CIDT_Speculation = b'1'
THOST_FTDC_CIDT_Arbitrage = b'2'
THOST_FTDC_CIDT_Hedge = b'3'
THOST_FTDC_CIDT_MarketMaker = b'5'
THOST_FTDC_OPT_AnyPrice = b'1'
THOST_FTDC_OPT_LimitPrice = b'2'
THOST_FTDC_OPT_BestPrice = b'3'
THOST_FTDC_OPT_LastPrice = b'4'
THOST_FTDC_OPT_LastPricePlusOneTicks = b'5'
THOST_FTDC_OPT_LastPricePlusTwoTicks = b'6'
THOST_FTDC_OPT_LastPricePlusThreeTicks = b'7'
THOST_FTDC_OPT_AskPrice1 = b'8'
THOST_FTDC_OPT_AskPrice1PlusOneTicks = b'9'
THOST_FTDC_OPT_AskPrice1PlusTwoTicks = b'A'
THOST_FTDC_OPT_AskPrice1PlusThreeTicks = b'B'
THOST_FTDC_OPT_BidPrice1 = b'C'
THOST_FTDC_OPT_BidPrice1PlusOneTicks = b'D'
THOST_FTDC_OPT_BidPrice1PlusTwoTicks = b'E'
THOST_FTDC_OPT_BidPrice1PlusThreeTicks = b'F'
THOST_FTDC_OPT_FiveLevelPrice = b'G'
THOST_FTDC_OF_Open = b'0'
THOST_FTDC_OF_Close = b'1'
THOST_FTDC_OF_ForceClose = b'2'
THOST_FTDC_OF_CloseToday = b'3'
THOST_FTDC_OF_CloseYesterday = b'4'
THOST_FTDC_OF_ForceOff = b'5'
THOST_FTDC_OF_LocalForceClose = b'6'
THOST_FTDC_FCC_NotForceClose = b'0'
THOST_FTDC_FCC_LackDeposit = b'1'
THOST_FTDC_FCC_ClientOverPositionLimit = b'2'
THOST_FTDC_FCC_MemberOverPositionLimit = b'3'
THOST_FTDC_FCC_NotMultiple = b'4'
THOST_FTDC_FCC_Violation = b'5'
THOST_FTDC_FCC_Other = b'6'
THOST_FTDC_FCC_PersonDeliv = b'7'
THOST_FTDC_ORDT_Normal = b'0'
THOST_FTDC_ORDT_DeriveFromQuote = b'1'
THOST_FTDC_ORDT_DeriveFromCombination = b'2'
THOST_FTDC_ORDT_Combination = b'3'
THOST_FTDC_ORDT_ConditionalOrder = b'4'
THOST_FTDC_ORDT_Swap = b'5'
THOST_FTDC_TC_IOC = b'1'
THOST_FTDC_TC_GFS = b'2'
THOST_FTDC_TC_GFD = b'3'
THOST_FTDC_TC_GTD = b'4'
THOST_FTDC_TC_GTC = b'5'
THOST_FTDC_TC_GFA = b'6'
THOST_FTDC_VC_AV = b'1'
THOST_FTDC_VC_MV = b'2'
THOST_FTDC_VC_CV = b'3'
THOST_FTDC_CC_Immediately = b'1'
THOST_FTDC_CC_Touch = b'2'
THOST_FTDC_CC_TouchProfit = b'3'
THOST_FTDC_CC_ParkedOrder = b'4'
THOST_FTDC_CC_LastPriceGreaterThanStopPrice = b'5'
THOST_FTDC_CC_LastPriceGreaterEqualStopPrice = b'6'
THOST_FTDC_CC_LastPriceLesserThanStopPrice = b'7'
THOST_FTDC_CC_LastPriceLesserEqualStopPrice = b'8'
THOST_FTDC_CC_AskPriceGreaterThanStopPrice = b'9'
THOST_FTDC_CC_AskPriceGreaterEqualStopPrice = b'A'
THOST_FTDC_CC_AskPriceLesserThanStopPrice = b'B'
THOST_FTDC_CC_AskPriceLesserEqualStopPrice = b'C'
THOST_FTDC_CC_BidPriceGreaterThanStopPrice = b'D'
THOST_FTDC_CC_BidPriceGreaterEqualStopPrice = b'E'
THOST_FTDC_CC_BidPriceLesserThanStopPrice = b'F'
THOST_FTDC_CC_BidPriceLesserEqualStopPrice = b'H'
THOST_FTDC_AF_Delete = b'0'
THOST_FTDC_AF_Modify = b'3'
THOST_FTDC_TR_Allow = b'0'
THOST_FTDC_TR_CloseOnly = b'1'
THOST_FTDC_TR_Forbidden = b'2'
THOST_FTDC_OSRC_Participant = b'0'
THOST_FTDC_OSRC_Administrator = b'1'
THOST_FTDC_TRDT_SplitCombination = b'#'
THOST_FTDC_TRDT_Common = b'0'
THOST_FTDC_TRDT_OptionsExecution = b'1'
THOST_FTDC_TRDT_OTC = b'2'
THOST_FTDC_TRDT_EFPDerived = b'3'
THOST_FTDC_TRDT_CombinationDerived = b'4'
THOST_FTDC_PSRC_LastPrice = b'0'
THOST_FTDC_PSRC_Buy = b'1'
THOST_FTDC_PSRC_Sell = b'2'
THOST_FTDC_IS_BeforeTrading = b'0'
THOST_FTDC_IS_NoTrading = b'1'
THOST_FTDC_IS_Continous = b'2'
THOST_FTDC_IS_AuctionOrdering = b'3'
THOST_FTDC_IS_AuctionBalance = b'4'
THOST_FTDC_IS_AuctionMatch = b'5'
THOST_FTDC_IS_Closed = b'6'
THOST_FTDC_IER_Automatic = b'1'
THOST_FTDC_IER_Manual = b'2'
THOST_FTDC_IER_Fuse = b'3'
THOST_FTDC_BS_NoUpload = b'1'
THOST_FTDC_BS_Uploaded = b'2'
THOST_FTDC_BS_Failed = b'3'
THOST_FTDC_RS_All = b'1'
THOST_FTDC_RS_ByProduct = b'2'
THOST_FTDC_RP_ByVolume = b'1'
THOST_FTDC_RP_ByFeeOnHand = b'2'
THOST_FTDC_RL_Level1 = b'1'
THOST_FTDC_RL_Level2 = b'2'
THOST_FTDC_RL_Level3 = b'3'
THOST_FTDC_RL_Level4 = b'4'
THOST_FTDC_RL_Level5 = b'5'
THOST_FTDC_RL_Level6 = b'6'
THOST_FTDC_RL_Level7 = b'7'
THOST_FTDC_RL_Level8 = b'8'
THOST_FTDC_RL_Level9 = b'9'
THOST_FTDC_RSD_ByPeriod = b'1'
THOST_FTDC_RSD_ByStandard = b'2'
THOST_FTDC_MT_Out = b'0'
THOST_FTDC_MT_In = b'1'
THOST_FTDC_ISPI_MortgageRatio = b'4'
THOST_FTDC_ISPI_MarginWay = b'5'
THOST_FTDC_ISPI_BillDeposit = b'9'
THOST_FTDC_ESPI_MortgageRatio = b'1'
THOST_FTDC_ESPI_OtherFundItem = b'2'
THOST_FTDC_ESPI_OtherFundImport = b'3'
THOST_FTDC_ESPI_CFFEXMinPrepa = b'6'
THOST_FTDC_ESPI_CZCESettlementType = b'7'
THOST_FTDC_ESPI_ExchDelivFeeMode = b'9'
THOST_FTDC_ESPI_DelivFeeMode = b'0'
THOST_FTDC_ESPI_CZCEComMarginType = b'A'
THOST_FTDC_ESPI_DceComMarginType = b'B'
THOST_FTDC_ESPI_OptOutDisCountRate = b'a'
THOST_FTDC_ESPI_OptMiniGuarantee = b'b'
THOST_FTDC_SPI_InvestorIDMinLength = b'1'
THOST_FTDC_SPI_AccountIDMinLength = b'2'
THOST_FTDC_SPI_UserRightLogon = b'3'
THOST_FTDC_SPI_SettlementBillTrade = b'4'
THOST_FTDC_SPI_TradingCode = b'5'
THOST_FTDC_SPI_CheckFund = b'6'
THOST_FTDC_SPI_CommModelRight = b'7'
THOST_FTDC_SPI_MarginModelRight = b'9'
THOST_FTDC_SPI_IsStandardActive = b'8'
THOST_FTDC_SPI_UploadSettlementFile = b'U'
THOST_FTDC_SPI_DownloadCSRCFile = b'D'
THOST_FTDC_SPI_SettlementBillFile = b'S'
THOST_FTDC_SPI_CSRCOthersFile = b'C'
THOST_FTDC_SPI_InvestorPhoto = b'P'
THOST_FTDC_SPI_CSRCData = b'R'
THOST_FTDC_SPI_InvestorPwdModel = b'I'
THOST_FTDC_SPI_CFFEXInvestorSettleFile = b'F'
THOST_FTDC_SPI_InvestorIDType = b'a'
THOST_FTDC_SPI_FreezeMaxReMain = b'r'
THOST_FTDC_SPI_IsSync = b'A'
THOST_FTDC_SPI_RelieveOpenLimit = b'O'
THOST_FTDC_SPI_IsStandardFreeze = b'X'
THOST_FTDC_SPI_CZCENormalProductHedge = b'B'
THOST_FTDC_TPID_EncryptionStandard = b'E'
THOST_FTDC_TPID_RiskMode = b'R'
THOST_FTDC_TPID_RiskModeGlobal = b'G'
THOST_FTDC_TPID_modeEncode = b'P'
THOST_FTDC_TPID_tickMode = b'T'
THOST_FTDC_TPID_SingleUserSessionMaxNum = b'S'
THOST_FTDC_TPID_LoginFailMaxNum = b'L'
THOST_FTDC_TPID_IsAuthForce = b'A'
THOST_FTDC_TPID_IsPosiFreeze = b'F'
THOST_FTDC_TPID_IsPosiLimit = b'M'
THOST_FTDC_TPID_ForQuoteTimeInterval = b'Q'
THOST_FTDC_TPID_IsFuturePosiLimit = b'B'
THOST_FTDC_TPID_IsFutureOrderFreq = b'C'
THOST_FTDC_TPID_IsExecOrderProfit = b'H'
THOST_FTDC_FI_SettlementFund = b'F'
THOST_FTDC_FI_Trade = b'T'
THOST_FTDC_FI_InvestorPosition = b'P'
THOST_FTDC_FI_SubEntryFund = b'O'
THOST_FTDC_FI_CZCECombinationPos = b'C'
THOST_FTDC_FI_CSRCData = b'R'
THOST_FTDC_FI_CZCEClose = b'L'
THOST_FTDC_FI_CZCENoClose = b'N'
THOST_FTDC_FI_PositionDtl = b'D'
THOST_FTDC_FI_OptionStrike = b'S'
THOST_FTDC_FI_SettlementPriceComparison = b'M'
THOST_FTDC_FI_NonTradePosChange = b'B'
THOST_FTDC_FUT_Settlement = b'0'
THOST_FTDC_FUT_Check = b'1'
THOST_FTDC_FFT_Txt = b'0'
THOST_FTDC_FFT_Zip = b'1'
THOST_FTDC_FFT_DBF = b'2'
THOST_FTDC_FUS_SucceedUpload = b'1'
THOST_FTDC_FUS_FailedUpload = b'2'
THOST_FTDC_FUS_SucceedLoad = b'3'
THOST_FTDC_FUS_PartSucceedLoad = b'4'
THOST_FTDC_FUS_FailedLoad = b'5'
THOST_FTDC_TD_Out = b'0'
THOST_FTDC_TD_In = b'1'
THOST_FTDC_SC_NoSpecialRule = b'0'
THOST_FTDC_SC_NoSpringFestival = b'1'
THOST_FTDC_IPT_LastSettlement = b'1'
THOST_FTDC_IPT_LaseClose = b'2'
THOST_FTDC_PLP_Active = b'1'
THOST_FTDC_PLP_NonActive = b'2'
THOST_FTDC_PLP_Canceled = b'3'
THOST_FTDC_DM_CashDeliv = b'1'
THOST_FTDC_DM_CommodityDeliv = b'2'
THOST_FTDC_FIOT_FundIO = b'1'
THOST_FTDC_FIOT_Transfer = b'2'
THOST_FTDC_FIOT_SwapCurrency = b'3'
THOST_FTDC_FT_Deposite = b'1'
THOST_FTDC_FT_ItemFund = b'2'
THOST_FTDC_FT_Company = b'3'
THOST_FTDC_FT_InnerTransfer = b'4'
THOST_FTDC_FD_In = b'1'
THOST_FTDC_FD_Out = b'2'
THOST_FTDC_FS_Record = b'1'
THOST_FTDC_FS_Check = b'2'
THOST_FTDC_FS_Charge = b'3'
THOST_FTDC_PS_None = b'1'
THOST_FTDC_PS_Publishing = b'2'
THOST_FTDC_PS_Published = b'3'
THOST_FTDC_ES_NonActive = b'1'
THOST_FTDC_ES_Startup = b'2'
THOST_FTDC_ES_Initialize = b'3'
THOST_FTDC_ES_Initialized = b'4'
THOST_FTDC_ES_Close = b'5'
THOST_FTDC_ES_Closed = b'6'
THOST_FTDC_ES_Settlement = b'7'
THOST_FTDC_STS_Initialize = b'0'
THOST_FTDC_STS_Settlementing = b'1'
THOST_FTDC_STS_Settlemented = b'2'
THOST_FTDC_STS_Finished = b'3'
THOST_FTDC_CT_Person = b'0'
THOST_FTDC_CT_Company = b'1'
THOST_FTDC_CT_Fund = b'2'
THOST_FTDC_CT_SpecialOrgan = b'3'
THOST_FTDC_CT_Asset = b'4'
THOST_FTDC_BT_Trade = b'0'
THOST_FTDC_BT_TradeSettle = b'1'
THOST_FTDC_FAS_Low = b'1'
THOST_FTDC_FAS_Normal = b'2'
THOST_FTDC_FAS_Focus = b'3'
THOST_FTDC_FAS_Risk = b'4'
THOST_FTDC_FAS_ByTrade = b'1'
THOST_FTDC_FAS_ByDeliv = b'2'
THOST_FTDC_FAS_None = b'3'
THOST_FTDC_FAS_FixFee = b'4'
THOST_FTDC_PWDT_Trade = b'1'
THOST_FTDC_PWDT_Account = b'2'
THOST_FTDC_AG_All = b'1'
THOST_FTDC_AG_OnlyLost = b'2'
THOST_FTDC_AG_OnlyGain = b'3'
THOST_FTDC_AG_None = b'4'
THOST_FTDC_ICP_Include = b'0'
THOST_FTDC_ICP_NotInclude = b'2'
THOST_FTDC_AWT_Enable = b'0'
THOST_FTDC_AWT_Disable = b'2'
THOST_FTDC_AWT_NoHoldEnable = b'3'
THOST_FTDC_FPWD_UnCheck = b'0'
THOST_FTDC_FPWD_Check = b'1'
THOST_FTDC_TT_BankToFuture = b'0'
THOST_FTDC_TT_FutureToBank = b'1'
THOST_FTDC_TVF_Invalid = b'0'
THOST_FTDC_TVF_Valid = b'1'
THOST_FTDC_TVF_Reverse = b'2'
THOST_FTDC_RN_CD = b'0'
THOST_FTDC_RN_ZT = b'1'
THOST_FTDC_RN_QT = b'2'
THOST_FTDC_SEX_None = b'0'
THOST_FTDC_SEX_Man = b'1'
THOST_FTDC_SEX_Woman = b'2'
THOST_FTDC_UT_Investor = b'0'
THOST_FTDC_UT_Operator = b'1'
THOST_FTDC_UT_SuperUser = b'2'
THOST_FTDC_RATETYPE_MarginRate = b'2'
THOST_FTDC_NOTETYPE_TradeSettleBill = b'1'
THOST_FTDC_NOTETYPE_TradeSettleMonth = b'2'
THOST_FTDC_NOTETYPE_CallMarginNotes = b'3'
THOST_FTDC_NOTETYPE_ForceCloseNotes = b'4'
THOST_FTDC_NOTETYPE_TradeNotes = b'5'
THOST_FTDC_NOTETYPE_DelivNotes = b'6'
THOST_FTDC_SBS_Day = b'1'
THOST_FTDC_SBS_Volume = b'2'
THOST_FTDC_ST_Day = b'0'
THOST_FTDC_ST_Month = b'1'
THOST_FTDC_URT_Logon = b'1'
THOST_FTDC_URT_Transfer = b'2'
THOST_FTDC_URT_EMail = b'3'
THOST_FTDC_URT_Fax = b'4'
THOST_FTDC_URT_ConditionOrder = b'5'
THOST_FTDC_MPT_PreSettlementPrice = b'1'
THOST_FTDC_MPT_SettlementPrice = b'2'
THOST_FTDC_MPT_AveragePrice = b'3'
THOST_FTDC_MPT_OpenPrice = b'4'
THOST_FTDC_BGS_None = b'0'
THOST_FTDC_BGS_NoGenerated = b'1'
THOST_FTDC_BGS_Generated = b'2'
THOST_FTDC_AT_HandlePositionAlgo = b'1'
THOST_FTDC_AT_FindMarginRateAlgo = b'2'
THOST_FTDC_HPA_Base = b'1'
THOST_FTDC_HPA_DCE = b'2'
THOST_FTDC_HPA_CZCE = b'3'
THOST_FTDC_FMRA_Base = b'1'
THOST_FTDC_FMRA_DCE = b'2'
THOST_FTDC_FMRA_CZCE = b'3'
THOST_FTDC_HTAA_Base = b'1'
THOST_FTDC_HTAA_DCE = b'2'
THOST_FTDC_HTAA_CZCE = b'3'
THOST_FTDC_PST_Order = b'1'
THOST_FTDC_PST_Open = b'2'
THOST_FTDC_PST_Fund = b'3'
THOST_FTDC_PST_Settlement = b'4'
THOST_FTDC_PST_Company = b'5'
THOST_FTDC_PST_Corporation = b'6'
THOST_FTDC_PST_LinkMan = b'7'
THOST_FTDC_PST_Ledger = b'8'
THOST_FTDC_PST_Trustee = b'9'
THOST_FTDC_PST_TrusteeCorporation = b'A'
THOST_FTDC_PST_TrusteeOpen = b'B'
THOST_FTDC_PST_TrusteeContact = b'C'
THOST_FTDC_PST_ForeignerRefer = b'D'
THOST_FTDC_PST_CorporationRefer = b'E'
THOST_FTDC_QIR_All = b'1'
THOST_FTDC_QIR_Group = b'2'
THOST_FTDC_QIR_Single = b'3'
THOST_FTDC_IRS_Normal = b'1'
THOST_FTDC_IRS_Warn = b'2'
THOST_FTDC_IRS_Call = b'3'
THOST_FTDC_IRS_Force = b'4'
THOST_FTDC_IRS_Exception = b'5'
THOST_FTDC_UET_Login = b'1'
THOST_FTDC_UET_Logout = b'2'
THOST_FTDC_UET_Trading = b'3'
THOST_FTDC_UET_TradingError = b'4'
THOST_FTDC_UET_UpdatePassword = b'5'
THOST_FTDC_UET_Authenticate = b'6'
THOST_FTDC_UET_Other = b'9'
THOST_FTDC_ICS_Close = b'0'
THOST_FTDC_ICS_CloseToday = b'1'
THOST_FTDC_SM_Non = b'0'
THOST_FTDC_SM_Instrument = b'1'
THOST_FTDC_SM_Product = b'2'
THOST_FTDC_SM_Investor = b'3'
THOST_FTDC_PAOS_NotSend = b'1'
THOST_FTDC_PAOS_Send = b'2'
THOST_FTDC_PAOS_Deleted = b'3'
THOST_FTDC_VDS_Dealing = b'1'
THOST_FTDC_VDS_DeaclSucceed = b'2'
THOST_FTDC_ORGS_Standard = b'0'
THOST_FTDC_ORGS_ESunny = b'1'
THOST_FTDC_ORGS_KingStarV6 = b'2'
THOST_FTDC_VTS_NaturalDeal = b'0'
THOST_FTDC_VTS_SucceedEnd = b'1'
THOST_FTDC_VTS_FailedEND = b'2'
THOST_FTDC_VTS_Exception = b'3'
THOST_FTDC_VTS_ManualDeal = b'4'
THOST_FTDC_VTS_MesException = b'5'
THOST_FTDC_VTS_SysException = b'6'
THOST_FTDC_VBAT_BankBook = b'1'
THOST_FTDC_VBAT_BankCard = b'2'
THOST_FTDC_VBAT_CreditCard = b'3'
THOST_FTDC_VMS_Natural = b'0'
THOST_FTDC_VMS_Canceled = b'9'
THOST_FTDC_VAA_NoAvailAbility = b'0'
THOST_FTDC_VAA_AvailAbility = b'1'
THOST_FTDC_VAA_Repeal = b'2'
THOST_FTDC_VTC_BankBankToFuture = b'102001'
THOST_FTDC_VTC_BankFutureToBank = b'102002'
THOST_FTDC_VTC_FutureBankToFuture = b'202001'
THOST_FTDC_VTC_FutureFutureToBank = b'202002'
THOST_FTDC_GEN_Program = b'0'
THOST_FTDC_GEN_HandWork = b'1'
THOST_FTDC_CFMMCKK_REQUEST = b'R'
THOST_FTDC_CFMMCKK_AUTO = b'A'
THOST_FTDC_CFMMCKK_MANUAL = b'M'
THOST_FTDC_CFT_IDCard = b'0'
THOST_FTDC_CFT_Passport = b'1'
THOST_FTDC_CFT_OfficerIDCard = b'2'
THOST_FTDC_CFT_SoldierIDCard = b'3'
THOST_FTDC_CFT_HomeComingCard = b'4'
THOST_FTDC_CFT_LicenseNo = b'6'
THOST_FTDC_CFT_InstitutionCodeCard = b'7'
THOST_FTDC_CFT_TempLicenseNo = b'8'
THOST_FTDC_CFT_NoEnterpriseLicenseNo = b'9'
THOST_FTDC_CFT_OtherCard = b'x'
THOST_FTDC_CFT_SuperDepAgree = b'a'
THOST_FTDC_FBC_Others = b'0'
THOST_FTDC_FBC_TransferDetails = b'1'
THOST_FTDC_FBC_CustAccStatus = b'2'
THOST_FTDC_FBC_AccountTradeDetails = b'3'
THOST_FTDC_FBC_FutureAccountChangeInfoDetails = b'4'
THOST_FTDC_FBC_CustMoneyDetail = b'5'
THOST_FTDC_FBC_CustCancelAccountInfo = b'6'
THOST_FTDC_FBC_CustMoneyResult = b'7'
THOST_FTDC_FBC_OthersExceptionResult = b'8'
THOST_FTDC_FBC_CustInterestNetMoneyDetails = b'9'
THOST_FTDC_FBC_CustMoneySendAndReceiveDetails = b'a'
THOST_FTDC_FBC_CorporationMoneyTotal = b'b'
THOST_FTDC_FBC_MainbodyMoneyTotal = b'c'
THOST_FTDC_FBC_MainPartMonitorData = b'd'
THOST_FTDC_FBC_PreparationMoney = b'e'
THOST_FTDC_FBC_BankMoneyMonitorData = b'f'
THOST_FTDC_CEC_Exchange = b'1'
THOST_FTDC_CEC_Cash = b'2'
THOST_FTDC_YNI_Yes = b'0'
THOST_FTDC_YNI_No = b'1'
THOST_FTDC_BLT_CurrentMoney = b'0'
THOST_FTDC_BLT_UsableMoney = b'1'
THOST_FTDC_BLT_FetchableMoney = b'2'
THOST_FTDC_BLT_FreezeMoney = b'3'
THOST_FTDC_GD_Unknown = b'0'
THOST_FTDC_GD_Male = b'1'
THOST_FTDC_GD_Female = b'2'
THOST_FTDC_FPF_BEN = b'0'
THOST_FTDC_FPF_OUR = b'1'
THOST_FTDC_FPF_SHA = b'2'
THOST_FTDC_PWKT_ExchangeKey = b'0'
THOST_FTDC_PWKT_PassWordKey = b'1'
THOST_FTDC_PWKT_MACKey = b'2'
THOST_FTDC_PWKT_MessageKey = b'3'
THOST_FTDC_PWT_Query = b'0'
THOST_FTDC_PWT_Fetch = b'1'
THOST_FTDC_PWT_Transfer = b'2'
THOST_FTDC_PWT_Trade = b'3'
THOST_FTDC_EM_NoEncry = b'0'
THOST_FTDC_EM_DES = b'1'
THOST_FTDC_EM_3DES = b'2'
THOST_FTDC_BRF_BankNotNeedRepeal = b'0'
THOST_FTDC_BRF_BankWaitingRepeal = b'1'
THOST_FTDC_BRF_BankBeenRepealed = b'2'
THOST_FTDC_BRORF_BrokerNotNeedRepeal = b'0'
THOST_FTDC_BRORF_BrokerWaitingRepeal = b'1'
THOST_FTDC_BRORF_BrokerBeenRepealed = b'2'
THOST_FTDC_TS_Bank = b'0'
THOST_FTDC_TS_Future = b'1'
THOST_FTDC_TS_Store = b'2'
THOST_FTDC_LF_Yes = b'0'
THOST_FTDC_LF_No = b'1'
THOST_FTDC_BAS_Normal = b'0'
THOST_FTDC_BAS_Freeze = b'1'
THOST_FTDC_BAS_ReportLoss = b'2'
THOST_FTDC_MAS_Normal = b'0'
THOST_FTDC_MAS_Cancel = b'1'
THOST_FTDC_MSS_Point = b'0'
THOST_FTDC_MSS_PrePoint = b'1'
THOST_FTDC_MSS_CancelPoint = b'2'
THOST_FTDC_SYT_FutureBankTransfer = b'0'
THOST_FTDC_SYT_StockBankTransfer = b'1'
THOST_FTDC_SYT_TheThirdPartStore = b'2'
THOST_FTDC_TEF_NormalProcessing = b'0'
THOST_FTDC_TEF_Success = b'1'
THOST_FTDC_TEF_Failed = b'2'
THOST_FTDC_TEF_Abnormal = b'3'
THOST_FTDC_TEF_ManualProcessedForException = b'4'
THOST_FTDC_TEF_CommuFailedNeedManualProcess = b'5'
THOST_FTDC_TEF_SysErrorNeedManualProcess = b'6'
THOST_FTDC_PSS_NotProcess = b'0'
THOST_FTDC_PSS_StartProcess = b'1'
THOST_FTDC_PSS_Finished = b'2'
THOST_FTDC_CUSTT_Person = b'0'
THOST_FTDC_CUSTT_Institution = b'1'
THOST_FTDC_FBTTD_FromBankToFuture = b'1'
THOST_FTDC_FBTTD_FromFutureToBank = b'2'
THOST_FTDC_OOD_Open = b'1'
THOST_FTDC_OOD_Destroy = b'0'
THOST_FTDC_AVAF_Invalid = b'0'
THOST_FTDC_AVAF_Valid = b'1'
THOST_FTDC_AVAF_Repeal = b'2'
THOST_FTDC_OT_Bank = b'1'
THOST_FTDC_OT_Future = b'2'
THOST_FTDC_OT_PlateForm = b'9'
THOST_FTDC_OL_HeadQuarters = b'1'
THOST_FTDC_OL_Branch = b'2'
THOST_FTDC_PID_FutureProtocal = b'0'
THOST_FTDC_PID_ICBCProtocal = b'1'
THOST_FTDC_PID_ABCProtocal = b'2'
THOST_FTDC_PID_CBCProtocal = b'3'
THOST_FTDC_PID_CCBProtocal = b'4'
THOST_FTDC_PID_BOCOMProtocal = b'5'
THOST_FTDC_PID_FBTPlateFormProtocal = b'X'
THOST_FTDC_CM_ShortConnect = b'0'
THOST_FTDC_CM_LongConnect = b'1'
THOST_FTDC_SRM_ASync = b'0'
THOST_FTDC_SRM_Sync = b'1'
THOST_FTDC_BAT_BankBook = b'1'
THOST_FTDC_BAT_SavingCard = b'2'
THOST_FTDC_BAT_CreditCard = b'3'
THOST_FTDC_FAT_BankBook = b'1'
THOST_FTDC_FAT_SavingCard = b'2'
THOST_FTDC_FAT_CreditCard = b'3'
THOST_FTDC_OS_Ready = b'0'
THOST_FTDC_OS_CheckIn = b'1'
THOST_FTDC_OS_CheckOut = b'2'
THOST_FTDC_OS_CheckFileArrived = b'3'
THOST_FTDC_OS_CheckDetail = b'4'
THOST_FTDC_OS_DayEndClean = b'5'
THOST_FTDC_OS_Invalid = b'9'
THOST_FTDC_CCBFM_ByAmount = b'1'
THOST_FTDC_CCBFM_ByMonth = b'2'
THOST_FTDC_CAPIT_Client = b'1'
THOST_FTDC_CAPIT_Server = b'2'
THOST_FTDC_CAPIT_UserApi = b'3'
THOST_FTDC_LS_Connected = b'1'
THOST_FTDC_LS_Disconnected = b'2'
THOST_FTDC_BPWDF_NoCheck = b'0'
THOST_FTDC_BPWDF_BlankCheck = b'1'
THOST_FTDC_BPWDF_EncryptCheck = b'2'
THOST_FTDC_SAT_AccountID = b'1'
THOST_FTDC_SAT_CardID = b'2'
THOST_FTDC_SAT_SHStockholderID = b'3'
THOST_FTDC_SAT_SZStockholderID = b'4'
THOST_FTDC_TRFS_Normal = b'0'
THOST_FTDC_TRFS_Repealed = b'1'
THOST_FTDC_SPTYPE_Broker = b'0'
THOST_FTDC_SPTYPE_Bank = b'1'
THOST_FTDC_REQRSP_Request = b'0'
THOST_FTDC_REQRSP_Response = b'1'
THOST_FTDC_FBTUET_SignIn = b'0'
THOST_FTDC_FBTUET_FromBankToFuture = b'1'
THOST_FTDC_FBTUET_FromFutureToBank = b'2'
THOST_FTDC_FBTUET_OpenAccount = b'3'
THOST_FTDC_FBTUET_CancelAccount = b'4'
THOST_FTDC_FBTUET_ChangeAccount = b'5'
THOST_FTDC_FBTUET_RepealFromBankToFuture = b'6'
THOST_FTDC_FBTUET_RepealFromFutureToBank = b'7'
THOST_FTDC_FBTUET_QueryBankAccount = b'8'
THOST_FTDC_FBTUET_QueryFutureAccount = b'9'
THOST_FTDC_FBTUET_SignOut = b'A'
THOST_FTDC_FBTUET_SyncKey = b'B'
THOST_FTDC_FBTUET_ReserveOpenAccount = b'C'
THOST_FTDC_FBTUET_CancelReserveOpenAccount = b'D'
THOST_FTDC_FBTUET_ReserveOpenAccountConfirm = b'E'
THOST_FTDC_FBTUET_Other = b'Z'
THOST_FTDC_DBOP_Insert = b'0'
THOST_FTDC_DBOP_Update = b'1'
THOST_FTDC_DBOP_Delete = b'2'
THOST_FTDC_SYNF_Yes = b'0'
THOST_FTDC_SYNF_No = b'1'
THOST_FTDC_SYNT_OneOffSync = b'0'
THOST_FTDC_SYNT_TimerSync = b'1'
THOST_FTDC_SYNT_TimerFullSync = b'2'
THOST_FTDC_FBEDIR_Settlement = b'0'
THOST_FTDC_FBEDIR_Sale = b'1'
THOST_FTDC_FBERES_Success = b'0'
THOST_FTDC_FBERES_InsufficientBalance = b'1'
THOST_FTDC_FBERES_UnknownTrading = b'8'
THOST_FTDC_FBERES_Fail = b'x'
THOST_FTDC_FBEES_Normal = b'0'
THOST_FTDC_FBEES_ReExchange = b'1'
THOST_FTDC_FBEFG_DataPackage = b'0'
THOST_FTDC_FBEFG_File = b'1'
THOST_FTDC_FBEAT_NotTrade = b'0'
THOST_FTDC_FBEAT_Trade = b'1'
THOST_FTDC_FBEUET_SignIn = b'0'
THOST_FTDC_FBEUET_Exchange = b'1'
THOST_FTDC_FBEUET_ReExchange = b'2'
THOST_FTDC_FBEUET_QueryBankAccount = b'3'
THOST_FTDC_FBEUET_QueryExchDetial = b'4'
THOST_FTDC_FBEUET_QueryExchSummary = b'5'
THOST_FTDC_FBEUET_QueryExchRate = b'6'
THOST_FTDC_FBEUET_CheckBankAccount = b'7'
THOST_FTDC_FBEUET_SignOut = b'8'
THOST_FTDC_FBEUET_Other = b'Z'
THOST_FTDC_FBERF_UnProcessed = b'0'
THOST_FTDC_FBERF_WaitSend = b'1'
THOST_FTDC_FBERF_SendSuccess = b'2'
THOST_FTDC_FBERF_SendFailed = b'3'
THOST_FTDC_FBERF_WaitReSend = b'4'
THOST_FTDC_NC_NOERROR = b'0'
THOST_FTDC_NC_Warn = b'1'
THOST_FTDC_NC_Call = b'2'
THOST_FTDC_NC_Force = b'3'
THOST_FTDC_NC_CHUANCANG = b'4'
THOST_FTDC_NC_Exception = b'5'
THOST_FTDC_FCT_Manual = b'0'
THOST_FTDC_FCT_Single = b'1'
THOST_FTDC_FCT_Group = b'2'
THOST_FTDC_RNM_System = b'0'
THOST_FTDC_RNM_SMS = b'1'
THOST_FTDC_RNM_EMail = b'2'
THOST_FTDC_RNM_Manual = b'3'
THOST_FTDC_RNS_NotGen = b'0'
THOST_FTDC_RNS_Generated = b'1'
THOST_FTDC_RNS_SendError = b'2'
THOST_FTDC_RNS_SendOk = b'3'
THOST_FTDC_RNS_Received = b'4'
THOST_FTDC_RNS_Confirmed = b'5'
THOST_FTDC_RUE_ExportData = b'0'
THOST_FTDC_COST_LastPriceAsc = b'0'
THOST_FTDC_COST_LastPriceDesc = b'1'
THOST_FTDC_COST_AskPriceAsc = b'2'
THOST_FTDC_COST_AskPriceDesc = b'3'
THOST_FTDC_COST_BidPriceAsc = b'4'
THOST_FTDC_COST_BidPriceDesc = b'5'
THOST_FTDC_UOAST_NoSend = b'0'
THOST_FTDC_UOAST_Sended = b'1'
THOST_FTDC_UOAST_Generated = b'2'
THOST_FTDC_UOAST_SendFail = b'3'
THOST_FTDC_UOAST_Success = b'4'
THOST_FTDC_UOAST_Fail = b'5'
THOST_FTDC_UOAST_Cancel = b'6'
THOST_FTDC_UOACS_NoApply = b'1'
THOST_FTDC_UOACS_Submited = b'2'
THOST_FTDC_UOACS_Sended = b'3'
THOST_FTDC_UOACS_Success = b'4'
THOST_FTDC_UOACS_Refuse = b'5'
THOST_FTDC_UOACS_Cancel = b'6'
THOST_FTDC_QT_Radio = b'1'
THOST_FTDC_QT_Option = b'2'
THOST_FTDC_QT_Blank = b'3'
THOST_FTDC_BT_Request = b'1'
THOST_FTDC_BT_Response = b'2'
THOST_FTDC_BT_Notice = b'3'
THOST_FTDC_CRC_Success = b'0'
THOST_FTDC_CRC_Working = b'1'
THOST_FTDC_CRC_InfoFail = b'2'
THOST_FTDC_CRC_IDCardFail = b'3'
THOST_FTDC_CRC_OtherFail = b'4'
THOST_FTDC_CfMMCCT_All = b'0'
THOST_FTDC_CfMMCCT_Person = b'1'
THOST_FTDC_CfMMCCT_Company = b'2'
THOST_FTDC_CfMMCCT_Other = b'3'
THOST_FTDC_CfMMCCT_SpecialOrgan = b'4'
THOST_FTDC_CfMMCCT_Asset = b'5'
THOST_FTDC_EIDT_SHFE = b'S'
THOST_FTDC_EIDT_CZCE = b'Z'
THOST_FTDC_EIDT_DCE = b'D'
THOST_FTDC_EIDT_CFFEX = b'J'
THOST_FTDC_EIDT_INE = b'N'
THOST_FTDC_ECIDT_Hedge = b'1'
THOST_FTDC_ECIDT_Arbitrage = b'2'
THOST_FTDC_ECIDT_Speculation = b'3'
THOST_FTDC_UF_NoUpdate = b'0'
THOST_FTDC_UF_Success = b'1'
THOST_FTDC_UF_Fail = b'2'
THOST_FTDC_UF_TCSuccess = b'3'
THOST_FTDC_UF_TCFail = b'4'
THOST_FTDC_UF_Cancel = b'5'
THOST_FTDC_AOID_OpenInvestor = b'1'
THOST_FTDC_AOID_ModifyIDCard = b'2'
THOST_FTDC_AOID_ModifyNoIDCard = b'3'
THOST_FTDC_AOID_ApplyTradingCode = b'4'
THOST_FTDC_AOID_CancelTradingCode = b'5'
THOST_FTDC_AOID_CancelInvestor = b'6'
THOST_FTDC_AOID_FreezeAccount = b'8'
THOST_FTDC_AOID_ActiveFreezeAccount = b'9'
THOST_FTDC_ASID_NoComplete = b'1'
THOST_FTDC_ASID_Submited = b'2'
THOST_FTDC_ASID_Checked = b'3'
THOST_FTDC_ASID_Refused = b'4'
THOST_FTDC_ASID_Deleted = b'5'
THOST_FTDC_UOASM_ByAPI = b'1'
THOST_FTDC_UOASM_ByFile = b'2'
THOST_FTDC_EvM_ADD = b'1'
THOST_FTDC_EvM_UPDATE = b'2'
THOST_FTDC_EvM_DELETE = b'3'
THOST_FTDC_EvM_CHECK = b'4'
THOST_FTDC_EvM_COPY = b'5'
THOST_FTDC_EvM_CANCEL = b'6'
THOST_FTDC_EvM_Reverse = b'7'
THOST_FTDC_UOAA_ASR = b'1'
THOST_FTDC_UOAA_ASNR = b'2'
THOST_FTDC_UOAA_NSAR = b'3'
THOST_FTDC_UOAA_NSR = b'4'
THOST_FTDC_EvM_InvestorGroupFlow = b'1'
THOST_FTDC_EvM_InvestorRate = b'2'
THOST_FTDC_EvM_InvestorCommRateModel = b'3'
THOST_FTDC_CL_Zero = b'0'
THOST_FTDC_CL_One = b'1'
THOST_FTDC_CL_Two = b'2'
THOST_FTDC_CHS_Init = b'0'
THOST_FTDC_CHS_Checking = b'1'
THOST_FTDC_CHS_Checked = b'2'
THOST_FTDC_CHS_Refuse = b'3'
THOST_FTDC_CHS_Cancel = b'4'
THOST_FTDC_CHU_Unused = b'0'
THOST_FTDC_CHU_Used = b'1'
THOST_FTDC_CHU_Fail = b'2'
THOST_FTDC_BAO_ByAccProperty = b'0'
THOST_FTDC_BAO_ByFBTransfer = b'1'
THOST_FTDC_MBTS_ByInstrument = b'0'
THOST_FTDC_MBTS_ByDayInsPrc = b'1'
THOST_FTDC_MBTS_ByDayIns = b'2'
THOST_FTDC_FTC_BankLaunchBankToBroker = b'102001'
THOST_FTDC_FTC_BrokerLaunchBankToBroker = b'202001'
THOST_FTDC_FTC_BankLaunchBrokerToBank = b'102002'
THOST_FTDC_FTC_BrokerLaunchBrokerToBank = b'202002'
THOST_FTDC_OTP_NONE = b'0'
THOST_FTDC_OTP_TOTP = b'1'
THOST_FTDC_OTPS_Unused = b'0'
THOST_FTDC_OTPS_Used = b'1'
THOST_FTDC_OTPS_Disuse = b'2'
THOST_FTDC_BUT_Investor = b'1'
THOST_FTDC_BUT_BrokerUser = b'2'
THOST_FTDC_FUTT_Commodity = b'1'
THOST_FTDC_FUTT_Financial = b'2'
THOST_FTDC_FET_Restriction = b'0'
THOST_FTDC_FET_TodayRestriction = b'1'
THOST_FTDC_FET_Transfer = b'2'
THOST_FTDC_FET_Credit = b'3'
THOST_FTDC_FET_InvestorWithdrawAlm = b'4'
THOST_FTDC_FET_BankRestriction = b'5'
THOST_FTDC_FET_Accountregister = b'6'
THOST_FTDC_FET_ExchangeFundIO = b'7'
THOST_FTDC_FET_InvestorFundIO = b'8'
THOST_FTDC_AST_FBTransfer = b'0'
THOST_FTDC_AST_ManualEntry = b'1'
THOST_FTDC_CST_UnifyAccount = b'0'
THOST_FTDC_CST_ManualEntry = b'1'
THOST_FTDC_UR_All = b'0'
THOST_FTDC_UR_Single = b'1'
THOST_FTDC_BG_Investor = b'2'
THOST_FTDC_BG_Group = b'1'
THOST_FTDC_TSSM_Instrument = b'1'
THOST_FTDC_TSSM_Product = b'2'
THOST_FTDC_TSSM_Exchange = b'3'
THOST_FTDC_ESM_Relative = b'1'
THOST_FTDC_ESM_Typical = b'2'
THOST_FTDC_RIR_All = b'1'
THOST_FTDC_RIR_Model = b'2'
THOST_FTDC_RIR_Single = b'3'
THOST_FTDC_SDS_Initialize = b'0'
THOST_FTDC_SDS_Settlementing = b'1'
THOST_FTDC_SDS_Settlemented = b'2'
THOST_FTDC_TSRC_NORMAL = b'0'
THOST_FTDC_TSRC_QUERY = b'1'
THOST_FTDC_FSM_Product = b'1'
THOST_FTDC_FSM_Exchange = b'2'
THOST_FTDC_FSM_All = b'3'
THOST_FTDC_BIR_Property = b'1'
THOST_FTDC_BIR_All = b'2'
THOST_FTDC_PIR_All = b'1'
THOST_FTDC_PIR_Property = b'2'
THOST_FTDC_PIR_Single = b'3'
THOST_FTDC_FIS_NoCreate = b'0'
THOST_FTDC_FIS_Created = b'1'
THOST_FTDC_FIS_Failed = b'2'
THOST_FTDC_FGS_FileTransmit = b'0'
THOST_FTDC_FGS_FileGen = b'1'
THOST_FTDC_SoM_Add = b'1'
THOST_FTDC_SoM_Update = b'2'
THOST_FTDC_SoM_Delete = b'3'
THOST_FTDC_SoM_Copy = b'4'
THOST_FTDC_SoM_AcTive = b'5'
THOST_FTDC_SoM_CanCel = b'6'
THOST_FTDC_SoM_ReSet = b'7'
THOST_FTDC_SoT_UpdatePassword = b'0'
THOST_FTDC_SoT_UserDepartment = b'1'
THOST_FTDC_SoT_RoleManager = b'2'
THOST_FTDC_SoT_RoleFunction = b'3'
THOST_FTDC_SoT_BaseParam = b'4'
THOST_FTDC_SoT_SetUserID = b'5'
THOST_FTDC_SoT_SetUserRole = b'6'
THOST_FTDC_SoT_UserIpRestriction = b'7'
THOST_FTDC_SoT_DepartmentManager = b'8'
THOST_FTDC_SoT_DepartmentCopy = b'9'
THOST_FTDC_SoT_Tradingcode = b'A'
THOST_FTDC_SoT_InvestorStatus = b'B'
THOST_FTDC_SoT_InvestorAuthority = b'C'
THOST_FTDC_SoT_PropertySet = b'D'
THOST_FTDC_SoT_ReSetInvestorPasswd = b'E'
THOST_FTDC_SoT_InvestorPersonalityInfo = b'F'
THOST_FTDC_CSRCQ_Current = b'0'
THOST_FTDC_CSRCQ_History = b'1'
THOST_FTDC_FRS_Normal = b'1'
THOST_FTDC_FRS_Freeze = b'0'
THOST_FTDC_STST_Standard = b'0'
THOST_FTDC_STST_NonStandard = b'1'
THOST_FTDC_RPT_Freeze = b'1'
THOST_FTDC_RPT_FreezeActive = b'2'
THOST_FTDC_RPT_OpenLimit = b'3'
THOST_FTDC_RPT_RelieveOpenLimit = b'4'
THOST_FTDC_AMLDS_Normal = b'0'
THOST_FTDC_AMLDS_Deleted = b'1'
THOST_FTDC_AMLCHS_Init = b'0'
THOST_FTDC_AMLCHS_Checking = b'1'
THOST_FTDC_AMLCHS_Checked = b'2'
THOST_FTDC_AMLCHS_RefuseReport = b'3'
THOST_FTDC_AMLDT_DrawDay = b'0'
THOST_FTDC_AMLDT_TouchDay = b'1'
THOST_FTDC_AMLCL_CheckLevel0 = b'0'
THOST_FTDC_AMLCL_CheckLevel1 = b'1'
THOST_FTDC_AMLCL_CheckLevel2 = b'2'
THOST_FTDC_AMLCL_CheckLevel3 = b'3'
THOST_FTDC_EFT_CSV = b'0'
THOST_FTDC_EFT_EXCEL = b'1'
THOST_FTDC_EFT_DBF = b'2'
THOST_FTDC_SMT_Before = b'1'
THOST_FTDC_SMT_Settlement = b'2'
THOST_FTDC_SMT_After = b'3'
THOST_FTDC_SMT_Settlemented = b'4'
THOST_FTDC_SML_Must = b'1'
THOST_FTDC_SML_Alarm = b'2'
THOST_FTDC_SML_Prompt = b'3'
THOST_FTDC_SML_Ignore = b'4'
THOST_FTDC_SMG_Exhcange = b'1'
THOST_FTDC_SMG_ASP = b'2'
THOST_FTDC_SMG_CSRC = b'3'
THOST_FTDC_LUT_Repeatable = b'1'
THOST_FTDC_LUT_Unrepeatable = b'2'
THOST_FTDC_DAR_Settle = b'1'
THOST_FTDC_DAR_Exchange = b'2'
THOST_FTDC_DAR_CSRC = b'3'
THOST_FTDC_MGT_ExchMarginRate = b'0'
THOST_FTDC_MGT_InstrMarginRate = b'1'
THOST_FTDC_MGT_InstrMarginRateTrade = b'2'
THOST_FTDC_ACT_Intraday = b'1'
THOST_FTDC_ACT_Long = b'2'
THOST_FTDC_MRT_Exchange = b'1'
THOST_FTDC_MRT_Investor = b'2'
THOST_FTDC_MRT_InvestorTrade = b'3'
THOST_FTDC_BUS_UnBak = b'0'
THOST_FTDC_BUS_BakUp = b'1'
THOST_FTDC_BUS_BakUped = b'2'
THOST_FTDC_BUS_BakFail = b'3'
THOST_FTDC_SIS_UnInitialize = b'0'
THOST_FTDC_SIS_Initialize = b'1'
THOST_FTDC_SIS_Initialized = b'2'
THOST_FTDC_SRS_NoCreate = b'0'
THOST_FTDC_SRS_Create = b'1'
THOST_FTDC_SRS_Created = b'2'
THOST_FTDC_SRS_CreateFail = b'3'
THOST_FTDC_SSS_UnSaveData = b'0'
THOST_FTDC_SSS_SaveDatad = b'1'
THOST_FTDC_SAS_UnArchived = b'0'
THOST_FTDC_SAS_Archiving = b'1'
THOST_FTDC_SAS_Archived = b'2'
THOST_FTDC_SAS_ArchiveFail = b'3'
THOST_FTDC_CTPT_Unkown = b'0'
THOST_FTDC_CTPT_MainCenter = b'1'
THOST_FTDC_CTPT_BackUp = b'2'
THOST_FTDC_CDT_Normal = b'0'
THOST_FTDC_CDT_SpecFirst = b'1'
THOST_FTDC_MFUR_None = b'0'
THOST_FTDC_MFUR_Margin = b'1'
THOST_FTDC_MFUR_All = b'2'
THOST_FTDC_SPT_CzceHedge = b'1'
THOST_FTDC_SPT_IneForeignCurrency = b'2'
THOST_FTDC_SPT_DceOpenClose = b'3'
THOST_FTDC_FMT_Mortgage = b'1'
THOST_FTDC_FMT_Redemption = b'2'
THOST_FTDC_ASPI_BaseMargin = b'1'
THOST_FTDC_ASPI_LowestInterest = b'2'
THOST_FTDC_FMD_In = b'1'
THOST_FTDC_FMD_Out = b'2'
THOST_FTDC_BT_Profit = b'0'
THOST_FTDC_BT_Loss = b'1'
THOST_FTDC_BT_Other = b'Z'
THOST_FTDC_SST_Manual = b'0'
THOST_FTDC_SST_Automatic = b'1'
THOST_FTDC_CED_Settlement = b'0'
THOST_FTDC_CED_Sale = b'1'
THOST_FTDC_CSS_Entry = b'1'
THOST_FTDC_CSS_Approve = b'2'
THOST_FTDC_CSS_Refuse = b'3'
THOST_FTDC_CSS_Revoke = b'4'
THOST_FTDC_CSS_Send = b'5'
THOST_FTDC_CSS_Success = b'6'
THOST_FTDC_CSS_Failure = b'7'
THOST_FTDC_REQF_NoSend = b'0'
THOST_FTDC_REQF_SendSuccess = b'1'
THOST_FTDC_REQF_SendFailed = b'2'
THOST_FTDC_REQF_WaitReSend = b'3'
THOST_FTDC_RESF_Success = b'0'
THOST_FTDC_RESF_InsuffiCient = b'1'
THOST_FTDC_RESF_UnKnown = b'8'
THOST_FTDC_EXS_Before = b'0'
THOST_FTDC_EXS_After = b'1'
THOST_FTDC_CR_Domestic = b'1'
THOST_FTDC_CR_GMT = b'2'
THOST_FTDC_CR_Foreign = b'3'
THOST_FTDC_HB_No = b'0'
THOST_FTDC_HB_Yes = b'1'
THOST_FTDC_SM_Normal = b'1'
THOST_FTDC_SM_Emerge = b'2'
THOST_FTDC_SM_Restore = b'3'
THOST_FTDC_TPT_Full = b'1'
THOST_FTDC_TPT_Increment = b'2'
THOST_FTDC_TPT_BackUp = b'3'
THOST_FTDC_LM_Trade = b'0'
THOST_FTDC_LM_Transfer = b'1'
THOST_FTDC_CPT_Instrument = b'1'
THOST_FTDC_CPT_Margin = b'2'
THOST_FTDC_HT_Yes = b'1'
THOST_FTDC_HT_No = b'0'
THOST_FTDC_AMT_Bank = b'1'
THOST_FTDC_AMT_Securities = b'2'
THOST_FTDC_AMT_Fund = b'3'
THOST_FTDC_AMT_Insurance = b'4'
THOST_FTDC_AMT_Trust = b'5'
THOST_FTDC_AMT_Other = b'9'
THOST_FTDC_CFIOT_FundIO = b'0'
THOST_FTDC_CFIOT_SwapCurrency = b'1'
THOST_FTDC_CAT_Futures = b'1'
THOST_FTDC_CAT_AssetmgrFuture = b'2'
THOST_FTDC_CAT_AssetmgrTrustee = b'3'
THOST_FTDC_CAT_AssetmgrTransfer = b'4'
THOST_FTDC_LT_Chinese = b'1'
THOST_FTDC_LT_English = b'2'
THOST_FTDC_AMCT_Person = b'1'
THOST_FTDC_AMCT_Organ = b'2'
THOST_FTDC_AMCT_SpecialOrgan = b'4'
THOST_FTDC_ASST_Futures = b'3'
THOST_FTDC_ASST_SpecialOrgan = b'4'
THOST_FTDC_CIT_HasExch = b'0'
THOST_FTDC_CIT_HasATP = b'1'
THOST_FTDC_CIT_HasDiff = b'2'
THOST_FTDC_DT_HandDeliv = b'1'
THOST_FTDC_DT_PersonDeliv = b'2'
THOST_FTDC_MMSA_NO = b'0'
THOST_FTDC_MMSA_YES = b'1'
THOST_FTDC_CACT_Person = b'0'
THOST_FTDC_CACT_Company = b'1'
THOST_FTDC_CACT_Other = b'2'
THOST_FTDC_UOAAT_Futures = b'1'
THOST_FTDC_UOAAT_SpecialOrgan = b'2'
THOST_FTDC_DEN_Buy = b'0'
THOST_FTDC_DEN_Sell = b'1'
THOST_FTDC_OFEN_Open = b'0'
THOST_FTDC_OFEN_Close = b'1'
THOST_FTDC_OFEN_ForceClose = b'2'
THOST_FTDC_OFEN_CloseToday = b'3'
THOST_FTDC_OFEN_CloseYesterday = b'4'
THOST_FTDC_OFEN_ForceOff = b'5'
THOST_FTDC_OFEN_LocalForceClose = b'6'
THOST_FTDC_HFEN_Speculation = b'1'
THOST_FTDC_HFEN_Arbitrage = b'2'
THOST_FTDC_HFEN_Hedge = b'3'
THOST_FTDC_FIOTEN_FundIO = b'1'
THOST_FTDC_FIOTEN_Transfer = b'2'
THOST_FTDC_FIOTEN_SwapCurrency = b'3'
THOST_FTDC_FTEN_Deposite = b'1'
THOST_FTDC_FTEN_ItemFund = b'2'
THOST_FTDC_FTEN_Company = b'3'
THOST_FTDC_FTEN_InnerTransfer = b'4'
THOST_FTDC_FDEN_In = b'1'
THOST_FTDC_FDEN_Out = b'2'
THOST_FTDC_FMDEN_In = b'1'
THOST_FTDC_FMDEN_Out = b'2'
THOST_FTDC_CP_CallOptions = b'1'
THOST_FTDC_CP_PutOptions = b'2'
THOST_FTDC_STM_Continental = b'0'
THOST_FTDC_STM_American = b'1'
THOST_FTDC_STM_Bermuda = b'2'
THOST_FTDC_STT_Hedge = b'0'
THOST_FTDC_STT_Match = b'1'
THOST_FTDC_APPT_NotStrikeNum = b'4'
THOST_FTDC_GUDS_Gen = b'0'
THOST_FTDC_GUDS_Hand = b'1'
THOST_FTDC_OER_NoExec = b'n'
THOST_FTDC_OER_Canceled = b'c'
THOST_FTDC_OER_OK = b'0'
THOST_FTDC_OER_NoPosition = b'1'
THOST_FTDC_OER_NoDeposit = b'2'
THOST_FTDC_OER_NoParticipant = b'3'
THOST_FTDC_OER_NoClient = b'4'
THOST_FTDC_OER_NoInstrument = b'6'
THOST_FTDC_OER_NoRight = b'7'
THOST_FTDC_OER_InvalidVolume = b'8'
THOST_FTDC_OER_NoEnoughHistoryTrade = b'9'
THOST_FTDC_OER_Unknown = b'a'
THOST_FTDC_COMBT_Future = b'0'
THOST_FTDC_COMBT_BUL = b'1'
THOST_FTDC_COMBT_BER = b'2'
THOST_FTDC_COMBT_STD = b'3'
THOST_FTDC_COMBT_STG = b'4'
THOST_FTDC_COMBT_PRT = b'5'
THOST_FTDC_COMBT_CLD = b'6'
THOST_FTDC_ORPT_PreSettlementPrice = b'1'
THOST_FTDC_ORPT_OpenPrice = b'4'
THOST_FTDC_BLAG_Default = b'1'
THOST_FTDC_BLAG_IncludeOptValLost = b'2'
THOST_FTDC_ACTP_Exec = b'1'
THOST_FTDC_ACTP_Abandon = b'2'
THOST_FTDC_FQST_Submitted = b'a'
THOST_FTDC_FQST_Accepted = b'b'
THOST_FTDC_FQST_Rejected = b'c'
THOST_FTDC_VM_Absolute = b'0'
THOST_FTDC_VM_Ratio = b'1'
THOST_FTDC_EOPF_Reserve = b'0'
THOST_FTDC_EOPF_UnReserve = b'1'
THOST_FTDC_EOCF_AutoClose = b'0'
THOST_FTDC_EOCF_NotToClose = b'1'
THOST_FTDC_PTE_Futures = b'1'
THOST_FTDC_PTE_Options = b'2'
THOST_FTDC_CUFN_CUFN_O = b'O'
THOST_FTDC_CUFN_CUFN_T = b'T'
THOST_FTDC_CUFN_CUFN_P = b'P'
THOST_FTDC_CUFN_CUFN_N = b'N'
THOST_FTDC_CUFN_CUFN_L = b'L'
THOST_FTDC_CUFN_CUFN_F = b'F'
THOST_FTDC_CUFN_CUFN_C = b'C'
THOST_FTDC_CUFN_CUFN_M = b'M'
THOST_FTDC_DUFN_DUFN_O = b'O'
THOST_FTDC_DUFN_DUFN_T = b'T'
THOST_FTDC_DUFN_DUFN_P = b'P'
THOST_FTDC_DUFN_DUFN_F = b'F'
THOST_FTDC_DUFN_DUFN_C = b'C'
THOST_FTDC_DUFN_DUFN_D = b'D'
THOST_FTDC_DUFN_DUFN_M = b'M'
THOST_FTDC_DUFN_DUFN_S = b'S'
THOST_FTDC_SUFN_SUFN_O = b'O'
THOST_FTDC_SUFN_SUFN_T = b'T'
THOST_FTDC_SUFN_SUFN_P = b'P'
THOST_FTDC_SUFN_SUFN_F = b'F'
THOST_FTDC_CFUFN_SUFN_T = b'T'
THOST_FTDC_CFUFN_SUFN_P = b'P'
THOST_FTDC_CFUFN_SUFN_F = b'F'
THOST_FTDC_CFUFN_SUFN_S = b'S'
THOST_FTDC_CMDR_Comb = b'0'
THOST_FTDC_CMDR_UnComb = b'1'
THOST_FTDC_STOV_RealValue = b'1'
THOST_FTDC_STOV_ProfitValue = b'2'
THOST_FTDC_STOV_RealRatio = b'3'
THOST_FTDC_STOV_ProfitRatio = b'4'
THOST_FTDC_ROAST_Processing = b'0'
THOST_FTDC_ROAST_Cancelled = b'1'
THOST_FTDC_ROAST_Opened = b'2'
THOST_FTDC_ROAST_Invalid = b'3'



class CThostFtdcDisseminationField(Structure):
    _fields_ = [
        ('SequenceSeries', c_short),
        ('SequenceNo', c_int)
    ]

class CThostFtdcReqUserLoginField(Structure):
    _fields_ = [
        ('TradingDay', c_char * 9),
        ('BrokerID', c_char * 11),
        ('UserID', c_char * 16),
        ('Password', c_char * 41),
        ('UserProductInfo', c_char * 11),
        ('InterfaceProductInfo', c_char * 11),
        ('ProtocolInfo', c_char * 11),
        ('MacAddress', c_char * 21),
        ('OneTimePassword', c_char * 41),
        ('ClientIPAddress', c_char * 16),
        ('LoginRemark', c_char * 36)
    ]

class CThostFtdcRspUserLoginField(Structure):
    _fields_ = [
        ('TradingDay', c_char * 9),
        ('LoginTime', c_char * 9),
        ('BrokerID', c_char * 11),
        ('UserID', c_char * 16),
        ('SystemName', c_char * 41),
        ('FrontID', c_int),
        ('SessionID', c_int),
        ('MaxOrderRef', c_char * 13),
        ('SHFETime', c_char * 9),
        ('DCETime', c_char * 9),
        ('CZCETime', c_char * 9),
        ('FFEXTime', c_char * 9),
        ('INETime', c_char * 9)
    ]

class CThostFtdcUserLogoutField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('UserID', c_char * 16)
    ]

class CThostFtdcForceUserLogoutField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('UserID', c_char * 16)
    ]

class CThostFtdcReqAuthenticateField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('UserID', c_char * 16),
        ('UserProductInfo', c_char * 11),
        ('AuthCode', c_char * 17)
    ]

class CThostFtdcRspAuthenticateField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('UserID', c_char * 16),
        ('UserProductInfo', c_char * 11)
    ]

class CThostFtdcAuthenticationInfoField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('UserID', c_char * 16),
        ('UserProductInfo', c_char * 11),
        ('AuthInfo', c_char * 129),
        ('IsResult', c_int)
    ]

class CThostFtdcTransferHeaderField(Structure):
    _fields_ = [
        ('Version', c_char * 4),
        ('TradeCode', c_char * 7),
        ('TradeDate', c_char * 9),
        ('TradeTime', c_char * 9),
        ('TradeSerial', c_char * 9),
        ('FutureID', c_char * 11),
        ('BankID', c_char * 4),
        ('BankBrchID', c_char * 5),
        ('OperNo', c_char * 17),
        ('DeviceID', c_char * 3),
        ('RecordNum', c_char * 7),
        ('SessionID', c_int),
        ('RequestID', c_int)
    ]

class CThostFtdcTransferBankToFutureReqField(Structure):
    _fields_ = [
        ('FutureAccount', c_char * 13),
        ('FuturePwdFlag', c_char),
        ('FutureAccPwd', c_char * 17),
        ('TradeAmt', c_double),
        ('CustFee', c_double),
        ('CurrencyCode', c_char * 4)
    ]

class CThostFtdcTransferBankToFutureRspField(Structure):
    _fields_ = [
        ('RetCode', c_char * 5),
        ('RetInfo', c_char * 129),
        ('FutureAccount', c_char * 13),
        ('TradeAmt', c_double),
        ('CustFee', c_double),
        ('CurrencyCode', c_char * 4)
    ]

class CThostFtdcTransferFutureToBankReqField(Structure):
    _fields_ = [
        ('FutureAccount', c_char * 13),
        ('FuturePwdFlag', c_char),
        ('FutureAccPwd', c_char * 17),
        ('TradeAmt', c_double),
        ('CustFee', c_double),
        ('CurrencyCode', c_char * 4)
    ]

class CThostFtdcTransferFutureToBankRspField(Structure):
    _fields_ = [
        ('RetCode', c_char * 5),
        ('RetInfo', c_char * 129),
        ('FutureAccount', c_char * 13),
        ('TradeAmt', c_double),
        ('CustFee', c_double),
        ('CurrencyCode', c_char * 4)
    ]

class CThostFtdcTransferQryBankReqField(Structure):
    _fields_ = [
        ('FutureAccount', c_char * 13),
        ('FuturePwdFlag', c_char),
        ('FutureAccPwd', c_char * 17),
        ('CurrencyCode', c_char * 4)
    ]

class CThostFtdcTransferQryBankRspField(Structure):
    _fields_ = [
        ('RetCode', c_char * 5),
        ('RetInfo', c_char * 129),
        ('FutureAccount', c_char * 13),
        ('TradeAmt', c_double),
        ('UseAmt', c_double),
        ('FetchAmt', c_double),
        ('CurrencyCode', c_char * 4)
    ]

class CThostFtdcTransferQryDetailReqField(Structure):
    _fields_ = [
        ('FutureAccount', c_char * 13)
    ]

class CThostFtdcTransferQryDetailRspField(Structure):
    _fields_ = [
        ('TradeDate', c_char * 9),
        ('TradeTime', c_char * 9),
        ('TradeCode', c_char * 7),
        ('FutureSerial', c_int),
        ('FutureID', c_char * 11),
        ('FutureAccount', c_char * 22),
        ('BankSerial', c_int),
        ('BankID', c_char * 4),
        ('BankBrchID', c_char * 5),
        ('BankAccount', c_char * 41),
        ('CertCode', c_char * 21),
        ('CurrencyCode', c_char * 4),
        ('TxAmount', c_double),
        ('Flag', c_char)
    ]

class CThostFtdcRspInfoField(Structure):
    _fields_ = [
        ('ErrorID', c_int),
        ('ErrorMsg', c_char * 81)
    ]

class CThostFtdcExchangeField(Structure):
    _fields_ = [
        ('ExchangeID', c_char * 9),
        ('ExchangeName', c_char * 61),
        ('ExchangeProperty', c_char)
    ]

class CThostFtdcProductField(Structure):
    _fields_ = [
        ('ProductID', c_char * 31),
        ('ProductName', c_char * 21),
        ('ExchangeID', c_char * 9),
        ('ProductClass', c_char),
        ('VolumeMultiple', c_int),
        ('PriceTick', c_double),
        ('MaxMarketOrderVolume', c_int),
        ('MinMarketOrderVolume', c_int),
        ('MaxLimitOrderVolume', c_int),
        ('MinLimitOrderVolume', c_int),
        ('PositionType', c_char),
        ('PositionDateType', c_char),
        ('CloseDealType', c_char),
        ('TradeCurrencyID', c_char * 4),
        ('MortgageFundUseRange', c_char),
        ('ExchangeProductID', c_char * 31),
        ('UnderlyingMultiple', c_double)
    ]

class CThostFtdcInstrumentField(Structure):
    _fields_ = [
        ('InstrumentID', c_char * 31),
        ('ExchangeID', c_char * 9),
        ('InstrumentName', c_char * 21),
        ('ExchangeInstID', c_char * 31),
        ('ProductID', c_char * 31),
        ('ProductClass', c_char),
        ('DeliveryYear', c_int),
        ('DeliveryMonth', c_int),
        ('MaxMarketOrderVolume', c_int),
        ('MinMarketOrderVolume', c_int),
        ('MaxLimitOrderVolume', c_int),
        ('MinLimitOrderVolume', c_int),
        ('VolumeMultiple', c_int),
        ('PriceTick', c_double),
        ('CreateDate', c_char * 9),
        ('OpenDate', c_char * 9),
        ('ExpireDate', c_char * 9),
        ('StartDelivDate', c_char * 9),
        ('EndDelivDate', c_char * 9),
        ('InstLifePhase', c_char),
        ('IsTrading', c_int),
        ('PositionType', c_char),
        ('PositionDateType', c_char),
        ('LongMarginRatio', c_double),
        ('ShortMarginRatio', c_double),
        ('MaxMarginSideAlgorithm', c_char),
        ('UnderlyingInstrID', c_char * 31),
        ('StrikePrice', c_double),
        ('OptionsType', c_char),
        ('UnderlyingMultiple', c_double),
        ('CombinationType', c_char)
    ]

class CThostFtdcBrokerField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('BrokerAbbr', c_char * 9),
        ('BrokerName', c_char * 81),
        ('IsActive', c_int)
    ]

class CThostFtdcTraderField(Structure):
    _fields_ = [
        ('ExchangeID', c_char * 9),
        ('TraderID', c_char * 21),
        ('ParticipantID', c_char * 11),
        ('Password', c_char * 41),
        ('InstallCount', c_int),
        ('BrokerID', c_char * 11)
    ]

class CThostFtdcInvestorField(Structure):
    _fields_ = [
        ('InvestorID', c_char * 13),
        ('BrokerID', c_char * 11),
        ('InvestorGroupID', c_char * 13),
        ('InvestorName', c_char * 81),
        ('IdentifiedCardType', c_char),
        ('IdentifiedCardNo', c_char * 51),
        ('IsActive', c_int),
        ('Telephone', c_char * 41),
        ('Address', c_char * 101),
        ('OpenDate', c_char * 9),
        ('Mobile', c_char * 41),
        ('CommModelID', c_char * 13),
        ('MarginModelID', c_char * 13)
    ]

class CThostFtdcTradingCodeField(Structure):
    _fields_ = [
        ('InvestorID', c_char * 13),
        ('BrokerID', c_char * 11),
        ('ExchangeID', c_char * 9),
        ('ClientID', c_char * 11),
        ('IsActive', c_int),
        ('ClientIDType', c_char)
    ]

class CThostFtdcPartBrokerField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('ExchangeID', c_char * 9),
        ('ParticipantID', c_char * 11),
        ('IsActive', c_int)
    ]

class CThostFtdcSuperUserField(Structure):
    _fields_ = [
        ('UserID', c_char * 16),
        ('UserName', c_char * 81),
        ('Password', c_char * 41),
        ('IsActive', c_int)
    ]

class CThostFtdcSuperUserFunctionField(Structure):
    _fields_ = [
        ('UserID', c_char * 16),
        ('FunctionCode', c_char)
    ]

class CThostFtdcInvestorGroupField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('InvestorGroupID', c_char * 13),
        ('InvestorGroupName', c_char * 41)
    ]

class CThostFtdcTradingAccountField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('AccountID', c_char * 13),
        ('PreMortgage', c_double),
        ('PreCredit', c_double),
        ('PreDeposit', c_double),
        ('PreBalance', c_double),
        ('PreMargin', c_double),
        ('InterestBase', c_double),
        ('Interest', c_double),
        ('Deposit', c_double),
        ('Withdraw', c_double),
        ('FrozenMargin', c_double),
        ('FrozenCash', c_double),
        ('FrozenCommission', c_double),
        ('CurrMargin', c_double),
        ('CashIn', c_double),
        ('Commission', c_double),
        ('CloseProfit', c_double),
        ('PositionProfit', c_double),
        ('Balance', c_double),
        ('Available', c_double),
        ('WithdrawQuota', c_double),
        ('Reserve', c_double),
        ('TradingDay', c_char * 9),
        ('SettlementID', c_int),
        ('Credit', c_double),
        ('Mortgage', c_double),
        ('ExchangeMargin', c_double),
        ('DeliveryMargin', c_double),
        ('ExchangeDeliveryMargin', c_double),
        ('ReserveBalance', c_double),
        ('CurrencyID', c_char * 4),
        ('PreFundMortgageIn', c_double),
        ('PreFundMortgageOut', c_double),
        ('FundMortgageIn', c_double),
        ('FundMortgageOut', c_double),
        ('FundMortgageAvailable', c_double),
        ('MortgageableFund', c_double),
        ('SpecProductMargin', c_double),
        ('SpecProductFrozenMargin', c_double),
        ('SpecProductCommission', c_double),
        ('SpecProductFrozenCommission', c_double),
        ('SpecProductPositionProfit', c_double),
        ('SpecProductCloseProfit', c_double),
        ('SpecProductPositionProfitByAlg', c_double),
        ('SpecProductExchangeMargin', c_double)
    ]

class CThostFtdcInvestorPositionField(Structure):
    _fields_ = [
        ('InstrumentID', c_char * 31),
        ('BrokerID', c_char * 11),
        ('InvestorID', c_char * 13),
        ('PosiDirection', c_char),
        ('HedgeFlag', c_char),
        ('PositionDate', c_char),
        ('YdPosition', c_int),
        ('Position', c_int),
        ('LongFrozen', c_int),
        ('ShortFrozen', c_int),
        ('LongFrozenAmount', c_double),
        ('ShortFrozenAmount', c_double),
        ('OpenVolume', c_int),
        ('CloseVolume', c_int),
        ('OpenAmount', c_double),
        ('CloseAmount', c_double),
        ('PositionCost', c_double),
        ('PreMargin', c_double),
        ('UseMargin', c_double),
        ('FrozenMargin', c_double),
        ('FrozenCash', c_double),
        ('FrozenCommission', c_double),
        ('CashIn', c_double),
        ('Commission', c_double),
        ('CloseProfit', c_double),
        ('PositionProfit', c_double),
        ('PreSettlementPrice', c_double),
        ('SettlementPrice', c_double),
        ('TradingDay', c_char * 9),
        ('SettlementID', c_int),
        ('OpenCost', c_double),
        ('ExchangeMargin', c_double),
        ('CombPosition', c_int),
        ('CombLongFrozen', c_int),
        ('CombShortFrozen', c_int),
        ('CloseProfitByDate', c_double),
        ('CloseProfitByTrade', c_double),
        ('TodayPosition', c_int),
        ('MarginRateByMoney', c_double),
        ('MarginRateByVolume', c_double),
        ('StrikeFrozen', c_int),
        ('StrikeFrozenAmount', c_double),
        ('AbandonFrozen', c_int)
    ]

class CThostFtdcInstrumentMarginRateField(Structure):
    _fields_ = [
        ('InstrumentID', c_char * 31),
        ('InvestorRange', c_char),
        ('BrokerID', c_char * 11),
        ('InvestorID', c_char * 13),
        ('HedgeFlag', c_char),
        ('LongMarginRatioByMoney', c_double),
        ('LongMarginRatioByVolume', c_double),
        ('ShortMarginRatioByMoney', c_double),
        ('ShortMarginRatioByVolume', c_double),
        ('IsRelative', c_int)
    ]

class CThostFtdcInstrumentCommissionRateField(Structure):
    _fields_ = [
        ('InstrumentID', c_char * 31),
        ('InvestorRange', c_char),
        ('BrokerID', c_char * 11),
        ('InvestorID', c_char * 13),
        ('OpenRatioByMoney', c_double),
        ('OpenRatioByVolume', c_double),
        ('CloseRatioByMoney', c_double),
        ('CloseRatioByVolume', c_double),
        ('CloseTodayRatioByMoney', c_double),
        ('CloseTodayRatioByVolume', c_double)
    ]

class CThostFtdcDepthMarketDataField(Structure):
    _fields_ = [
        ('TradingDay', c_char * 9),
        ('InstrumentID', c_char * 31),
        ('ExchangeID', c_char * 9),
        ('ExchangeInstID', c_char * 31),
        ('LastPrice', c_double),
        ('PreSettlementPrice', c_double),
        ('PreClosePrice', c_double),
        ('PreOpenInterest', c_double),
        ('OpenPrice', c_double),
        ('HighestPrice', c_double),
        ('LowestPrice', c_double),
        ('Volume', c_int),
        ('Turnover', c_double),
        ('OpenInterest', c_double),
        ('ClosePrice', c_double),
        ('SettlementPrice', c_double),
        ('UpperLimitPrice', c_double),
        ('LowerLimitPrice', c_double),
        ('PreDelta', c_double),
        ('CurrDelta', c_double),
        ('UpdateTime', c_char * 9),
        ('UpdateMillisec', c_int),
        ('BidPrice1', c_double),
        ('BidVolume1', c_int),
        ('AskPrice1', c_double),
        ('AskVolume1', c_int),
        ('BidPrice2', c_double),
        ('BidVolume2', c_int),
        ('AskPrice2', c_double),
        ('AskVolume2', c_int),
        ('BidPrice3', c_double),
        ('BidVolume3', c_int),
        ('AskPrice3', c_double),
        ('AskVolume3', c_int),
        ('BidPrice4', c_double),
        ('BidVolume4', c_int),
        ('AskPrice4', c_double),
        ('AskVolume4', c_int),
        ('BidPrice5', c_double),
        ('BidVolume5', c_int),
        ('AskPrice5', c_double),
        ('AskVolume5', c_int),
        ('AveragePrice', c_double),
        ('ActionDay', c_char * 9)
    ]

class CThostFtdcInstrumentTradingRightField(Structure):
    _fields_ = [
        ('InstrumentID', c_char * 31),
        ('InvestorRange', c_char),
        ('BrokerID', c_char * 11),
        ('InvestorID', c_char * 13),
        ('TradingRight', c_char)
    ]

class CThostFtdcBrokerUserField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('UserID', c_char * 16),
        ('UserName', c_char * 81),
        ('UserType', c_char),
        ('IsActive', c_int),
        ('IsUsingOTP', c_int)
    ]

class CThostFtdcBrokerUserPasswordField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('UserID', c_char * 16),
        ('Password', c_char * 41)
    ]

class CThostFtdcBrokerUserFunctionField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('UserID', c_char * 16),
        ('BrokerFunctionCode', c_char)
    ]

class CThostFtdcTraderOfferField(Structure):
    _fields_ = [
        ('ExchangeID', c_char * 9),
        ('TraderID', c_char * 21),
        ('ParticipantID', c_char * 11),
        ('Password', c_char * 41),
        ('InstallID', c_int),
        ('OrderLocalID', c_char * 13),
        ('TraderConnectStatus', c_char),
        ('ConnectRequestDate', c_char * 9),
        ('ConnectRequestTime', c_char * 9),
        ('LastReportDate', c_char * 9),
        ('LastReportTime', c_char * 9),
        ('ConnectDate', c_char * 9),
        ('ConnectTime', c_char * 9),
        ('StartDate', c_char * 9),
        ('StartTime', c_char * 9),
        ('TradingDay', c_char * 9),
        ('BrokerID', c_char * 11),
        ('MaxTradeID', c_char * 21),
        ('MaxOrderMessageReference', c_char * 7)
    ]

class CThostFtdcSettlementInfoField(Structure):
    _fields_ = [
        ('TradingDay', c_char * 9),
        ('SettlementID', c_int),
        ('BrokerID', c_char * 11),
        ('InvestorID', c_char * 13),
        ('SequenceNo', c_int),
        ('Content', c_char * 501)
    ]

class CThostFtdcInstrumentMarginRateAdjustField(Structure):
    _fields_ = [
        ('InstrumentID', c_char * 31),
        ('InvestorRange', c_char),
        ('BrokerID', c_char * 11),
        ('InvestorID', c_char * 13),
        ('HedgeFlag', c_char),
        ('LongMarginRatioByMoney', c_double),
        ('LongMarginRatioByVolume', c_double),
        ('ShortMarginRatioByMoney', c_double),
        ('ShortMarginRatioByVolume', c_double),
        ('IsRelative', c_int)
    ]

class CThostFtdcExchangeMarginRateField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('InstrumentID', c_char * 31),
        ('HedgeFlag', c_char),
        ('LongMarginRatioByMoney', c_double),
        ('LongMarginRatioByVolume', c_double),
        ('ShortMarginRatioByMoney', c_double),
        ('ShortMarginRatioByVolume', c_double)
    ]

class CThostFtdcExchangeMarginRateAdjustField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('InstrumentID', c_char * 31),
        ('HedgeFlag', c_char),
        ('LongMarginRatioByMoney', c_double),
        ('LongMarginRatioByVolume', c_double),
        ('ShortMarginRatioByMoney', c_double),
        ('ShortMarginRatioByVolume', c_double),
        ('ExchLongMarginRatioByMoney', c_double),
        ('ExchLongMarginRatioByVolume', c_double),
        ('ExchShortMarginRatioByMoney', c_double),
        ('ExchShortMarginRatioByVolume', c_double),
        ('NoLongMarginRatioByMoney', c_double),
        ('NoLongMarginRatioByVolume', c_double),
        ('NoShortMarginRatioByMoney', c_double),
        ('NoShortMarginRatioByVolume', c_double)
    ]

class CThostFtdcExchangeRateField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('FromCurrencyID', c_char * 4),
        ('FromCurrencyUnit', c_double),
        ('ToCurrencyID', c_char * 4),
        ('ExchangeRate', c_double)
    ]

class CThostFtdcSettlementRefField(Structure):
    _fields_ = [
        ('TradingDay', c_char * 9),
        ('SettlementID', c_int)
    ]

class CThostFtdcCurrentTimeField(Structure):
    _fields_ = [
        ('CurrDate', c_char * 9),
        ('CurrTime', c_char * 9),
        ('CurrMillisec', c_int),
        ('ActionDay', c_char * 9)
    ]

class CThostFtdcCommPhaseField(Structure):
    _fields_ = [
        ('TradingDay', c_char * 9),
        ('CommPhaseNo', c_short),
        ('SystemID', c_char * 21)
    ]

class CThostFtdcLoginInfoField(Structure):
    _fields_ = [
        ('FrontID', c_int),
        ('SessionID', c_int),
        ('BrokerID', c_char * 11),
        ('UserID', c_char * 16),
        ('LoginDate', c_char * 9),
        ('LoginTime', c_char * 9),
        ('IPAddress', c_char * 16),
        ('UserProductInfo', c_char * 11),
        ('InterfaceProductInfo', c_char * 11),
        ('ProtocolInfo', c_char * 11),
        ('SystemName', c_char * 41),
        ('Password', c_char * 41),
        ('MaxOrderRef', c_char * 13),
        ('SHFETime', c_char * 9),
        ('DCETime', c_char * 9),
        ('CZCETime', c_char * 9),
        ('FFEXTime', c_char * 9),
        ('MacAddress', c_char * 21),
        ('OneTimePassword', c_char * 41),
        ('INETime', c_char * 9),
        ('IsQryControl', c_int),
        ('LoginRemark', c_char * 36)
    ]

class CThostFtdcLogoutAllField(Structure):
    _fields_ = [
        ('FrontID', c_int),
        ('SessionID', c_int),
        ('SystemName', c_char * 41)
    ]

class CThostFtdcFrontStatusField(Structure):
    _fields_ = [
        ('FrontID', c_int),
        ('LastReportDate', c_char * 9),
        ('LastReportTime', c_char * 9),
        ('IsActive', c_int)
    ]

class CThostFtdcUserPasswordUpdateField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('UserID', c_char * 16),
        ('OldPassword', c_char * 41),
        ('NewPassword', c_char * 41)
    ]

class CThostFtdcInputOrderField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('InvestorID', c_char * 13),
        ('InstrumentID', c_char * 31),
        ('OrderRef', c_char * 13),
        ('UserID', c_char * 16),
        ('OrderPriceType', c_char),
        ('Direction', c_char),
        ('CombOffsetFlag', c_char * 5),
        ('CombHedgeFlag', c_char * 5),
        ('LimitPrice', c_double),
        ('VolumeTotalOriginal', c_int),
        ('TimeCondition', c_char),
        ('GTDDate', c_char * 9),
        ('VolumeCondition', c_char),
        ('MinVolume', c_int),
        ('ContingentCondition', c_char),
        ('StopPrice', c_double),
        ('ForceCloseReason', c_char),
        ('IsAutoSuspend', c_int),
        ('BusinessUnit', c_char * 21),
        ('RequestID', c_int),
        ('UserForceClose', c_int),
        ('IsSwapOrder', c_int),
        ('ExchangeID', c_char * 9),
        ('InvestUnitID', c_char * 17),
        ('AccountID', c_char * 13),
        ('CurrencyID', c_char * 4),
        ('ClientID', c_char * 11),
        ('IPAddress', c_char * 16),
        ('MacAddress', c_char * 21)
    ]

class CThostFtdcOrderField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('InvestorID', c_char * 13),
        ('InstrumentID', c_char * 31),
        ('OrderRef', c_char * 13),
        ('UserID', c_char * 16),
        ('OrderPriceType', c_char),
        ('Direction', c_char),
        ('CombOffsetFlag', c_char * 5),
        ('CombHedgeFlag', c_char * 5),
        ('LimitPrice', c_double),
        ('VolumeTotalOriginal', c_int),
        ('TimeCondition', c_char),
        ('GTDDate', c_char * 9),
        ('VolumeCondition', c_char),
        ('MinVolume', c_int),
        ('ContingentCondition', c_char),
        ('StopPrice', c_double),
        ('ForceCloseReason', c_char),
        ('IsAutoSuspend', c_int),
        ('BusinessUnit', c_char * 21),
        ('RequestID', c_int),
        ('OrderLocalID', c_char * 13),
        ('ExchangeID', c_char * 9),
        ('ParticipantID', c_char * 11),
        ('ClientID', c_char * 11),
        ('ExchangeInstID', c_char * 31),
        ('TraderID', c_char * 21),
        ('InstallID', c_int),
        ('OrderSubmitStatus', c_char),
        ('NotifySequence', c_int),
        ('TradingDay', c_char * 9),
        ('SettlementID', c_int),
        ('OrderSysID', c_char * 21),
        ('OrderSource', c_char),
        ('OrderStatus', c_char),
        ('OrderType', c_char),
        ('VolumeTraded', c_int),
        ('VolumeTotal', c_int),
        ('InsertDate', c_char * 9),
        ('InsertTime', c_char * 9),
        ('ActiveTime', c_char * 9),
        ('SuspendTime', c_char * 9),
        ('UpdateTime', c_char * 9),
        ('CancelTime', c_char * 9),
        ('ActiveTraderID', c_char * 21),
        ('ClearingPartID', c_char * 11),
        ('SequenceNo', c_int),
        ('FrontID', c_int),
        ('SessionID', c_int),
        ('UserProductInfo', c_char * 11),
        ('StatusMsg', c_char * 81),
        ('UserForceClose', c_int),
        ('ActiveUserID', c_char * 16),
        ('BrokerOrderSeq', c_int),
        ('RelativeOrderSysID', c_char * 21),
        ('ZCETotalTradedVolume', c_int),
        ('IsSwapOrder', c_int),
        ('BranchID', c_char * 9),
        ('InvestUnitID', c_char * 17),
        ('AccountID', c_char * 13),
        ('CurrencyID', c_char * 4),
        ('IPAddress', c_char * 16),
        ('MacAddress', c_char * 21)
    ]

class CThostFtdcExchangeOrderField(Structure):
    _fields_ = [
        ('OrderPriceType', c_char),
        ('Direction', c_char),
        ('CombOffsetFlag', c_char * 5),
        ('CombHedgeFlag', c_char * 5),
        ('LimitPrice', c_double),
        ('VolumeTotalOriginal', c_int),
        ('TimeCondition', c_char),
        ('GTDDate', c_char * 9),
        ('VolumeCondition', c_char),
        ('MinVolume', c_int),
        ('ContingentCondition', c_char),
        ('StopPrice', c_double),
        ('ForceCloseReason', c_char),
        ('IsAutoSuspend', c_int),
        ('BusinessUnit', c_char * 21),
        ('RequestID', c_int),
        ('OrderLocalID', c_char * 13),
        ('ExchangeID', c_char * 9),
        ('ParticipantID', c_char * 11),
        ('ClientID', c_char * 11),
        ('ExchangeInstID', c_char * 31),
        ('TraderID', c_char * 21),
        ('InstallID', c_int),
        ('OrderSubmitStatus', c_char),
        ('NotifySequence', c_int),
        ('TradingDay', c_char * 9),
        ('SettlementID', c_int),
        ('OrderSysID', c_char * 21),
        ('OrderSource', c_char),
        ('OrderStatus', c_char),
        ('OrderType', c_char),
        ('VolumeTraded', c_int),
        ('VolumeTotal', c_int),
        ('InsertDate', c_char * 9),
        ('InsertTime', c_char * 9),
        ('ActiveTime', c_char * 9),
        ('SuspendTime', c_char * 9),
        ('UpdateTime', c_char * 9),
        ('CancelTime', c_char * 9),
        ('ActiveTraderID', c_char * 21),
        ('ClearingPartID', c_char * 11),
        ('SequenceNo', c_int),
        ('BranchID', c_char * 9),
        ('IPAddress', c_char * 16),
        ('MacAddress', c_char * 21)
    ]

class CThostFtdcExchangeOrderInsertErrorField(Structure):
    _fields_ = [
        ('ExchangeID', c_char * 9),
        ('ParticipantID', c_char * 11),
        ('TraderID', c_char * 21),
        ('InstallID', c_int),
        ('OrderLocalID', c_char * 13),
        ('ErrorID', c_int),
        ('ErrorMsg', c_char * 81)
    ]

class CThostFtdcInputOrderActionField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('InvestorID', c_char * 13),
        ('OrderActionRef', c_int),
        ('OrderRef', c_char * 13),
        ('RequestID', c_int),
        ('FrontID', c_int),
        ('SessionID', c_int),
        ('ExchangeID', c_char * 9),
        ('OrderSysID', c_char * 21),
        ('ActionFlag', c_char),
        ('LimitPrice', c_double),
        ('VolumeChange', c_int),
        ('UserID', c_char * 16),
        ('InstrumentID', c_char * 31),
        ('InvestUnitID', c_char * 17),
        ('IPAddress', c_char * 16),
        ('MacAddress', c_char * 21)
    ]

class CThostFtdcOrderActionField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('InvestorID', c_char * 13),
        ('OrderActionRef', c_int),
        ('OrderRef', c_char * 13),
        ('RequestID', c_int),
        ('FrontID', c_int),
        ('SessionID', c_int),
        ('ExchangeID', c_char * 9),
        ('OrderSysID', c_char * 21),
        ('ActionFlag', c_char),
        ('LimitPrice', c_double),
        ('VolumeChange', c_int),
        ('ActionDate', c_char * 9),
        ('ActionTime', c_char * 9),
        ('TraderID', c_char * 21),
        ('InstallID', c_int),
        ('OrderLocalID', c_char * 13),
        ('ActionLocalID', c_char * 13),
        ('ParticipantID', c_char * 11),
        ('ClientID', c_char * 11),
        ('BusinessUnit', c_char * 21),
        ('OrderActionStatus', c_char),
        ('UserID', c_char * 16),
        ('StatusMsg', c_char * 81),
        ('InstrumentID', c_char * 31),
        ('BranchID', c_char * 9),
        ('InvestUnitID', c_char * 17),
        ('IPAddress', c_char * 16),
        ('MacAddress', c_char * 21)
    ]

class CThostFtdcExchangeOrderActionField(Structure):
    _fields_ = [
        ('ExchangeID', c_char * 9),
        ('OrderSysID', c_char * 21),
        ('ActionFlag', c_char),
        ('LimitPrice', c_double),
        ('VolumeChange', c_int),
        ('ActionDate', c_char * 9),
        ('ActionTime', c_char * 9),
        ('TraderID', c_char * 21),
        ('InstallID', c_int),
        ('OrderLocalID', c_char * 13),
        ('ActionLocalID', c_char * 13),
        ('ParticipantID', c_char * 11),
        ('ClientID', c_char * 11),
        ('BusinessUnit', c_char * 21),
        ('OrderActionStatus', c_char),
        ('UserID', c_char * 16),
        ('BranchID', c_char * 9),
        ('IPAddress', c_char * 16),
        ('MacAddress', c_char * 21)
    ]

class CThostFtdcExchangeOrderActionErrorField(Structure):
    _fields_ = [
        ('ExchangeID', c_char * 9),
        ('OrderSysID', c_char * 21),
        ('TraderID', c_char * 21),
        ('InstallID', c_int),
        ('OrderLocalID', c_char * 13),
        ('ActionLocalID', c_char * 13),
        ('ErrorID', c_int),
        ('ErrorMsg', c_char * 81)
    ]

class CThostFtdcExchangeTradeField(Structure):
    _fields_ = [
        ('ExchangeID', c_char * 9),
        ('TradeID', c_char * 21),
        ('Direction', c_char),
        ('OrderSysID', c_char * 21),
        ('ParticipantID', c_char * 11),
        ('ClientID', c_char * 11),
        ('TradingRole', c_char),
        ('ExchangeInstID', c_char * 31),
        ('OffsetFlag', c_char),
        ('HedgeFlag', c_char),
        ('Price', c_double),
        ('Volume', c_int),
        ('TradeDate', c_char * 9),
        ('TradeTime', c_char * 9),
        ('TradeType', c_char),
        ('PriceSource', c_char),
        ('TraderID', c_char * 21),
        ('OrderLocalID', c_char * 13),
        ('ClearingPartID', c_char * 11),
        ('BusinessUnit', c_char * 21),
        ('SequenceNo', c_int),
        ('TradeSource', c_char)
    ]

class CThostFtdcTradeField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('InvestorID', c_char * 13),
        ('InstrumentID', c_char * 31),
        ('OrderRef', c_char * 13),
        ('UserID', c_char * 16),
        ('ExchangeID', c_char * 9),
        ('TradeID', c_char * 21),
        ('Direction', c_char),
        ('OrderSysID', c_char * 21),
        ('ParticipantID', c_char * 11),
        ('ClientID', c_char * 11),
        ('TradingRole', c_char),
        ('ExchangeInstID', c_char * 31),
        ('OffsetFlag', c_char),
        ('HedgeFlag', c_char),
        ('Price', c_double),
        ('Volume', c_int),
        ('TradeDate', c_char * 9),
        ('TradeTime', c_char * 9),
        ('TradeType', c_char),
        ('PriceSource', c_char),
        ('TraderID', c_char * 21),
        ('OrderLocalID', c_char * 13),
        ('ClearingPartID', c_char * 11),
        ('BusinessUnit', c_char * 21),
        ('SequenceNo', c_int),
        ('TradingDay', c_char * 9),
        ('SettlementID', c_int),
        ('BrokerOrderSeq', c_int),
        ('TradeSource', c_char)
    ]

class CThostFtdcUserSessionField(Structure):
    _fields_ = [
        ('FrontID', c_int),
        ('SessionID', c_int),
        ('BrokerID', c_char * 11),
        ('UserID', c_char * 16),
        ('LoginDate', c_char * 9),
        ('LoginTime', c_char * 9),
        ('IPAddress', c_char * 16),
        ('UserProductInfo', c_char * 11),
        ('InterfaceProductInfo', c_char * 11),
        ('ProtocolInfo', c_char * 11),
        ('MacAddress', c_char * 21),
        ('LoginRemark', c_char * 36)
    ]

class CThostFtdcQueryMaxOrderVolumeField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('InvestorID', c_char * 13),
        ('InstrumentID', c_char * 31),
        ('Direction', c_char),
        ('OffsetFlag', c_char),
        ('HedgeFlag', c_char),
        ('MaxVolume', c_int)
    ]

class CThostFtdcSettlementInfoConfirmField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('InvestorID', c_char * 13),
        ('ConfirmDate', c_char * 9),
        ('ConfirmTime', c_char * 9)
    ]

class CThostFtdcSyncDepositField(Structure):
    _fields_ = [
        ('DepositSeqNo', c_char * 15),
        ('BrokerID', c_char * 11),
        ('InvestorID', c_char * 13),
        ('Deposit', c_double),
        ('IsForce', c_int),
        ('CurrencyID', c_char * 4)
    ]

class CThostFtdcSyncFundMortgageField(Structure):
    _fields_ = [
        ('MortgageSeqNo', c_char * 15),
        ('BrokerID', c_char * 11),
        ('InvestorID', c_char * 13),
        ('FromCurrencyID', c_char * 4),
        ('MortgageAmount', c_double),
        ('ToCurrencyID', c_char * 4)
    ]

class CThostFtdcBrokerSyncField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11)
    ]

class CThostFtdcSyncingInvestorField(Structure):
    _fields_ = [
        ('InvestorID', c_char * 13),
        ('BrokerID', c_char * 11),
        ('InvestorGroupID', c_char * 13),
        ('InvestorName', c_char * 81),
        ('IdentifiedCardType', c_char),
        ('IdentifiedCardNo', c_char * 51),
        ('IsActive', c_int),
        ('Telephone', c_char * 41),
        ('Address', c_char * 101),
        ('OpenDate', c_char * 9),
        ('Mobile', c_char * 41),
        ('CommModelID', c_char * 13),
        ('MarginModelID', c_char * 13)
    ]

class CThostFtdcSyncingTradingCodeField(Structure):
    _fields_ = [
        ('InvestorID', c_char * 13),
        ('BrokerID', c_char * 11),
        ('ExchangeID', c_char * 9),
        ('ClientID', c_char * 11),
        ('IsActive', c_int),
        ('ClientIDType', c_char)
    ]

class CThostFtdcSyncingInvestorGroupField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('InvestorGroupID', c_char * 13),
        ('InvestorGroupName', c_char * 41)
    ]

class CThostFtdcSyncingTradingAccountField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('AccountID', c_char * 13),
        ('PreMortgage', c_double),
        ('PreCredit', c_double),
        ('PreDeposit', c_double),
        ('PreBalance', c_double),
        ('PreMargin', c_double),
        ('InterestBase', c_double),
        ('Interest', c_double),
        ('Deposit', c_double),
        ('Withdraw', c_double),
        ('FrozenMargin', c_double),
        ('FrozenCash', c_double),
        ('FrozenCommission', c_double),
        ('CurrMargin', c_double),
        ('CashIn', c_double),
        ('Commission', c_double),
        ('CloseProfit', c_double),
        ('PositionProfit', c_double),
        ('Balance', c_double),
        ('Available', c_double),
        ('WithdrawQuota', c_double),
        ('Reserve', c_double),
        ('TradingDay', c_char * 9),
        ('SettlementID', c_int),
        ('Credit', c_double),
        ('Mortgage', c_double),
        ('ExchangeMargin', c_double),
        ('DeliveryMargin', c_double),
        ('ExchangeDeliveryMargin', c_double),
        ('ReserveBalance', c_double),
        ('CurrencyID', c_char * 4),
        ('PreFundMortgageIn', c_double),
        ('PreFundMortgageOut', c_double),
        ('FundMortgageIn', c_double),
        ('FundMortgageOut', c_double),
        ('FundMortgageAvailable', c_double),
        ('MortgageableFund', c_double),
        ('SpecProductMargin', c_double),
        ('SpecProductFrozenMargin', c_double),
        ('SpecProductCommission', c_double),
        ('SpecProductFrozenCommission', c_double),
        ('SpecProductPositionProfit', c_double),
        ('SpecProductCloseProfit', c_double),
        ('SpecProductPositionProfitByAlg', c_double),
        ('SpecProductExchangeMargin', c_double)
    ]

class CThostFtdcSyncingInvestorPositionField(Structure):
    _fields_ = [
        ('InstrumentID', c_char * 31),
        ('BrokerID', c_char * 11),
        ('InvestorID', c_char * 13),
        ('PosiDirection', c_char),
        ('HedgeFlag', c_char),
        ('PositionDate', c_char),
        ('YdPosition', c_int),
        ('Position', c_int),
        ('LongFrozen', c_int),
        ('ShortFrozen', c_int),
        ('LongFrozenAmount', c_double),
        ('ShortFrozenAmount', c_double),
        ('OpenVolume', c_int),
        ('CloseVolume', c_int),
        ('OpenAmount', c_double),
        ('CloseAmount', c_double),
        ('PositionCost', c_double),
        ('PreMargin', c_double),
        ('UseMargin', c_double),
        ('FrozenMargin', c_double),
        ('FrozenCash', c_double),
        ('FrozenCommission', c_double),
        ('CashIn', c_double),
        ('Commission', c_double),
        ('CloseProfit', c_double),
        ('PositionProfit', c_double),
        ('PreSettlementPrice', c_double),
        ('SettlementPrice', c_double),
        ('TradingDay', c_char * 9),
        ('SettlementID', c_int),
        ('OpenCost', c_double),
        ('ExchangeMargin', c_double),
        ('CombPosition', c_int),
        ('CombLongFrozen', c_int),
        ('CombShortFrozen', c_int),
        ('CloseProfitByDate', c_double),
        ('CloseProfitByTrade', c_double),
        ('TodayPosition', c_int),
        ('MarginRateByMoney', c_double),
        ('MarginRateByVolume', c_double),
        ('StrikeFrozen', c_int),
        ('StrikeFrozenAmount', c_double),
        ('AbandonFrozen', c_int)
    ]

class CThostFtdcSyncingInstrumentMarginRateField(Structure):
    _fields_ = [
        ('InstrumentID', c_char * 31),
        ('InvestorRange', c_char),
        ('BrokerID', c_char * 11),
        ('InvestorID', c_char * 13),
        ('HedgeFlag', c_char),
        ('LongMarginRatioByMoney', c_double),
        ('LongMarginRatioByVolume', c_double),
        ('ShortMarginRatioByMoney', c_double),
        ('ShortMarginRatioByVolume', c_double),
        ('IsRelative', c_int)
    ]

class CThostFtdcSyncingInstrumentCommissionRateField(Structure):
    _fields_ = [
        ('InstrumentID', c_char * 31),
        ('InvestorRange', c_char),
        ('BrokerID', c_char * 11),
        ('InvestorID', c_char * 13),
        ('OpenRatioByMoney', c_double),
        ('OpenRatioByVolume', c_double),
        ('CloseRatioByMoney', c_double),
        ('CloseRatioByVolume', c_double),
        ('CloseTodayRatioByMoney', c_double),
        ('CloseTodayRatioByVolume', c_double)
    ]

class CThostFtdcSyncingInstrumentTradingRightField(Structure):
    _fields_ = [
        ('InstrumentID', c_char * 31),
        ('InvestorRange', c_char),
        ('BrokerID', c_char * 11),
        ('InvestorID', c_char * 13),
        ('TradingRight', c_char)
    ]

class CThostFtdcQryOrderField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('InvestorID', c_char * 13),
        ('InstrumentID', c_char * 31),
        ('ExchangeID', c_char * 9),
        ('OrderSysID', c_char * 21),
        ('InsertTimeStart', c_char * 9),
        ('InsertTimeEnd', c_char * 9)
    ]

class CThostFtdcQryTradeField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('InvestorID', c_char * 13),
        ('InstrumentID', c_char * 31),
        ('ExchangeID', c_char * 9),
        ('TradeID', c_char * 21),
        ('TradeTimeStart', c_char * 9),
        ('TradeTimeEnd', c_char * 9)
    ]

class CThostFtdcQryInvestorPositionField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('InvestorID', c_char * 13),
        ('InstrumentID', c_char * 31)
    ]

class CThostFtdcQryTradingAccountField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('InvestorID', c_char * 13),
        ('CurrencyID', c_char * 4)
    ]

class CThostFtdcQryInvestorField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('InvestorID', c_char * 13)
    ]

class CThostFtdcQryTradingCodeField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('InvestorID', c_char * 13),
        ('ExchangeID', c_char * 9),
        ('ClientID', c_char * 11),
        ('ClientIDType', c_char)
    ]

class CThostFtdcQryInvestorGroupField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11)
    ]

class CThostFtdcQryInstrumentMarginRateField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('InvestorID', c_char * 13),
        ('InstrumentID', c_char * 31),
        ('HedgeFlag', c_char)
    ]

class CThostFtdcQryInstrumentCommissionRateField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('InvestorID', c_char * 13),
        ('InstrumentID', c_char * 31)
    ]

class CThostFtdcQryInstrumentTradingRightField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('InvestorID', c_char * 13),
        ('InstrumentID', c_char * 31)
    ]

class CThostFtdcQryBrokerField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11)
    ]

class CThostFtdcQryTraderField(Structure):
    _fields_ = [
        ('ExchangeID', c_char * 9),
        ('ParticipantID', c_char * 11),
        ('TraderID', c_char * 21)
    ]

class CThostFtdcQrySuperUserFunctionField(Structure):
    _fields_ = [
        ('UserID', c_char * 16)
    ]

class CThostFtdcQryUserSessionField(Structure):
    _fields_ = [
        ('FrontID', c_int),
        ('SessionID', c_int),
        ('BrokerID', c_char * 11),
        ('UserID', c_char * 16)
    ]

class CThostFtdcQryPartBrokerField(Structure):
    _fields_ = [
        ('ExchangeID', c_char * 9),
        ('BrokerID', c_char * 11),
        ('ParticipantID', c_char * 11)
    ]

class CThostFtdcQryFrontStatusField(Structure):
    _fields_ = [
        ('FrontID', c_int)
    ]

class CThostFtdcQryExchangeOrderField(Structure):
    _fields_ = [
        ('ParticipantID', c_char * 11),
        ('ClientID', c_char * 11),
        ('ExchangeInstID', c_char * 31),
        ('ExchangeID', c_char * 9),
        ('TraderID', c_char * 21)
    ]

class CThostFtdcQryOrderActionField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('InvestorID', c_char * 13),
        ('ExchangeID', c_char * 9)
    ]

class CThostFtdcQryExchangeOrderActionField(Structure):
    _fields_ = [
        ('ParticipantID', c_char * 11),
        ('ClientID', c_char * 11),
        ('ExchangeID', c_char * 9),
        ('TraderID', c_char * 21)
    ]

class CThostFtdcQrySuperUserField(Structure):
    _fields_ = [
        ('UserID', c_char * 16)
    ]

class CThostFtdcQryExchangeField(Structure):
    _fields_ = [
        ('ExchangeID', c_char * 9)
    ]

class CThostFtdcQryProductField(Structure):
    _fields_ = [
        ('ProductID', c_char * 31),
        ('ProductClass', c_char)
    ]

class CThostFtdcQryInstrumentField(Structure):
    _fields_ = [
        ('InstrumentID', c_char * 31),
        ('ExchangeID', c_char * 9),
        ('ExchangeInstID', c_char * 31),
        ('ProductID', c_char * 31)
    ]

class CThostFtdcQryDepthMarketDataField(Structure):
    _fields_ = [
        ('InstrumentID', c_char * 31)
    ]

class CThostFtdcQryBrokerUserField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('UserID', c_char * 16)
    ]

class CThostFtdcQryBrokerUserFunctionField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('UserID', c_char * 16)
    ]

class CThostFtdcQryTraderOfferField(Structure):
    _fields_ = [
        ('ExchangeID', c_char * 9),
        ('ParticipantID', c_char * 11),
        ('TraderID', c_char * 21)
    ]

class CThostFtdcQrySyncDepositField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('DepositSeqNo', c_char * 15)
    ]

class CThostFtdcQrySettlementInfoField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('InvestorID', c_char * 13),
        ('TradingDay', c_char * 9)
    ]

class CThostFtdcQryExchangeMarginRateField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('InstrumentID', c_char * 31),
        ('HedgeFlag', c_char)
    ]

class CThostFtdcQryExchangeMarginRateAdjustField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('InstrumentID', c_char * 31),
        ('HedgeFlag', c_char)
    ]

class CThostFtdcQryExchangeRateField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('FromCurrencyID', c_char * 4),
        ('ToCurrencyID', c_char * 4)
    ]

class CThostFtdcQrySyncFundMortgageField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('MortgageSeqNo', c_char * 15)
    ]

class CThostFtdcQryHisOrderField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('InvestorID', c_char * 13),
        ('InstrumentID', c_char * 31),
        ('ExchangeID', c_char * 9),
        ('OrderSysID', c_char * 21),
        ('InsertTimeStart', c_char * 9),
        ('InsertTimeEnd', c_char * 9),
        ('TradingDay', c_char * 9),
        ('SettlementID', c_int)
    ]

class CThostFtdcOptionInstrMiniMarginField(Structure):
    _fields_ = [
        ('InstrumentID', c_char * 31),
        ('InvestorRange', c_char),
        ('BrokerID', c_char * 11),
        ('InvestorID', c_char * 13),
        ('MinMargin', c_double),
        ('ValueMethod', c_char),
        ('IsRelative', c_int)
    ]

class CThostFtdcOptionInstrMarginAdjustField(Structure):
    _fields_ = [
        ('InstrumentID', c_char * 31),
        ('InvestorRange', c_char),
        ('BrokerID', c_char * 11),
        ('InvestorID', c_char * 13),
        ('SShortMarginRatioByMoney', c_double),
        ('SShortMarginRatioByVolume', c_double),
        ('HShortMarginRatioByMoney', c_double),
        ('HShortMarginRatioByVolume', c_double),
        ('AShortMarginRatioByMoney', c_double),
        ('AShortMarginRatioByVolume', c_double),
        ('IsRelative', c_int),
        ('MShortMarginRatioByMoney', c_double),
        ('MShortMarginRatioByVolume', c_double)
    ]

class CThostFtdcOptionInstrCommRateField(Structure):
    _fields_ = [
        ('InstrumentID', c_char * 31),
        ('InvestorRange', c_char),
        ('BrokerID', c_char * 11),
        ('InvestorID', c_char * 13),
        ('OpenRatioByMoney', c_double),
        ('OpenRatioByVolume', c_double),
        ('CloseRatioByMoney', c_double),
        ('CloseRatioByVolume', c_double),
        ('CloseTodayRatioByMoney', c_double),
        ('CloseTodayRatioByVolume', c_double),
        ('StrikeRatioByMoney', c_double),
        ('StrikeRatioByVolume', c_double)
    ]

class CThostFtdcOptionInstrTradeCostField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('InvestorID', c_char * 13),
        ('InstrumentID', c_char * 31),
        ('HedgeFlag', c_char),
        ('FixedMargin', c_double),
        ('MiniMargin', c_double),
        ('Royalty', c_double),
        ('ExchFixedMargin', c_double),
        ('ExchMiniMargin', c_double)
    ]

class CThostFtdcQryOptionInstrTradeCostField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('InvestorID', c_char * 13),
        ('InstrumentID', c_char * 31),
        ('HedgeFlag', c_char),
        ('InputPrice', c_double),
        ('UnderlyingPrice', c_double)
    ]

class CThostFtdcQryOptionInstrCommRateField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('InvestorID', c_char * 13),
        ('InstrumentID', c_char * 31)
    ]

class CThostFtdcIndexPriceField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('InstrumentID', c_char * 31),
        ('ClosePrice', c_double)
    ]

class CThostFtdcInputExecOrderField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('InvestorID', c_char * 13),
        ('InstrumentID', c_char * 31),
        ('ExecOrderRef', c_char * 13),
        ('UserID', c_char * 16),
        ('Volume', c_int),
        ('RequestID', c_int),
        ('BusinessUnit', c_char * 21),
        ('OffsetFlag', c_char),
        ('HedgeFlag', c_char),
        ('ActionType', c_char),
        ('PosiDirection', c_char),
        ('ReservePositionFlag', c_char),
        ('CloseFlag', c_char),
        ('ExchangeID', c_char * 9),
        ('InvestUnitID', c_char * 17),
        ('AccountID', c_char * 13),
        ('CurrencyID', c_char * 4),
        ('ClientID', c_char * 11),
        ('IPAddress', c_char * 16),
        ('MacAddress', c_char * 21)
    ]

class CThostFtdcInputExecOrderActionField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('InvestorID', c_char * 13),
        ('ExecOrderActionRef', c_int),
        ('ExecOrderRef', c_char * 13),
        ('RequestID', c_int),
        ('FrontID', c_int),
        ('SessionID', c_int),
        ('ExchangeID', c_char * 9),
        ('ExecOrderSysID', c_char * 21),
        ('ActionFlag', c_char),
        ('UserID', c_char * 16),
        ('InstrumentID', c_char * 31),
        ('InvestUnitID', c_char * 17),
        ('IPAddress', c_char * 16),
        ('MacAddress', c_char * 21)
    ]

class CThostFtdcExecOrderField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('InvestorID', c_char * 13),
        ('InstrumentID', c_char * 31),
        ('ExecOrderRef', c_char * 13),
        ('UserID', c_char * 16),
        ('Volume', c_int),
        ('RequestID', c_int),
        ('BusinessUnit', c_char * 21),
        ('OffsetFlag', c_char),
        ('HedgeFlag', c_char),
        ('ActionType', c_char),
        ('PosiDirection', c_char),
        ('ReservePositionFlag', c_char),
        ('CloseFlag', c_char),
        ('ExecOrderLocalID', c_char * 13),
        ('ExchangeID', c_char * 9),
        ('ParticipantID', c_char * 11),
        ('ClientID', c_char * 11),
        ('ExchangeInstID', c_char * 31),
        ('TraderID', c_char * 21),
        ('InstallID', c_int),
        ('OrderSubmitStatus', c_char),
        ('NotifySequence', c_int),
        ('TradingDay', c_char * 9),
        ('SettlementID', c_int),
        ('ExecOrderSysID', c_char * 21),
        ('InsertDate', c_char * 9),
        ('InsertTime', c_char * 9),
        ('CancelTime', c_char * 9),
        ('ExecResult', c_char),
        ('ClearingPartID', c_char * 11),
        ('SequenceNo', c_int),
        ('FrontID', c_int),
        ('SessionID', c_int),
        ('UserProductInfo', c_char * 11),
        ('StatusMsg', c_char * 81),
        ('ActiveUserID', c_char * 16),
        ('BrokerExecOrderSeq', c_int),
        ('BranchID', c_char * 9),
        ('InvestUnitID', c_char * 17),
        ('AccountID', c_char * 13),
        ('CurrencyID', c_char * 4),
        ('IPAddress', c_char * 16),
        ('MacAddress', c_char * 21)
    ]

class CThostFtdcExecOrderActionField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('InvestorID', c_char * 13),
        ('ExecOrderActionRef', c_int),
        ('ExecOrderRef', c_char * 13),
        ('RequestID', c_int),
        ('FrontID', c_int),
        ('SessionID', c_int),
        ('ExchangeID', c_char * 9),
        ('ExecOrderSysID', c_char * 21),
        ('ActionFlag', c_char),
        ('ActionDate', c_char * 9),
        ('ActionTime', c_char * 9),
        ('TraderID', c_char * 21),
        ('InstallID', c_int),
        ('ExecOrderLocalID', c_char * 13),
        ('ActionLocalID', c_char * 13),
        ('ParticipantID', c_char * 11),
        ('ClientID', c_char * 11),
        ('BusinessUnit', c_char * 21),
        ('OrderActionStatus', c_char),
        ('UserID', c_char * 16),
        ('ActionType', c_char),
        ('StatusMsg', c_char * 81),
        ('InstrumentID', c_char * 31),
        ('BranchID', c_char * 9),
        ('InvestUnitID', c_char * 17),
        ('IPAddress', c_char * 16),
        ('MacAddress', c_char * 21)
    ]

class CThostFtdcQryExecOrderField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('InvestorID', c_char * 13),
        ('InstrumentID', c_char * 31),
        ('ExchangeID', c_char * 9),
        ('ExecOrderSysID', c_char * 21),
        ('InsertTimeStart', c_char * 9),
        ('InsertTimeEnd', c_char * 9)
    ]

class CThostFtdcExchangeExecOrderField(Structure):
    _fields_ = [
        ('Volume', c_int),
        ('RequestID', c_int),
        ('BusinessUnit', c_char * 21),
        ('OffsetFlag', c_char),
        ('HedgeFlag', c_char),
        ('ActionType', c_char),
        ('PosiDirection', c_char),
        ('ReservePositionFlag', c_char),
        ('CloseFlag', c_char),
        ('ExecOrderLocalID', c_char * 13),
        ('ExchangeID', c_char * 9),
        ('ParticipantID', c_char * 11),
        ('ClientID', c_char * 11),
        ('ExchangeInstID', c_char * 31),
        ('TraderID', c_char * 21),
        ('InstallID', c_int),
        ('OrderSubmitStatus', c_char),
        ('NotifySequence', c_int),
        ('TradingDay', c_char * 9),
        ('SettlementID', c_int),
        ('ExecOrderSysID', c_char * 21),
        ('InsertDate', c_char * 9),
        ('InsertTime', c_char * 9),
        ('CancelTime', c_char * 9),
        ('ExecResult', c_char),
        ('ClearingPartID', c_char * 11),
        ('SequenceNo', c_int),
        ('BranchID', c_char * 9),
        ('IPAddress', c_char * 16),
        ('MacAddress', c_char * 21)
    ]

class CThostFtdcQryExchangeExecOrderField(Structure):
    _fields_ = [
        ('ParticipantID', c_char * 11),
        ('ClientID', c_char * 11),
        ('ExchangeInstID', c_char * 31),
        ('ExchangeID', c_char * 9),
        ('TraderID', c_char * 21)
    ]

class CThostFtdcQryExecOrderActionField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('InvestorID', c_char * 13),
        ('ExchangeID', c_char * 9)
    ]

class CThostFtdcExchangeExecOrderActionField(Structure):
    _fields_ = [
        ('ExchangeID', c_char * 9),
        ('ExecOrderSysID', c_char * 21),
        ('ActionFlag', c_char),
        ('ActionDate', c_char * 9),
        ('ActionTime', c_char * 9),
        ('TraderID', c_char * 21),
        ('InstallID', c_int),
        ('ExecOrderLocalID', c_char * 13),
        ('ActionLocalID', c_char * 13),
        ('ParticipantID', c_char * 11),
        ('ClientID', c_char * 11),
        ('BusinessUnit', c_char * 21),
        ('OrderActionStatus', c_char),
        ('UserID', c_char * 16),
        ('ActionType', c_char),
        ('BranchID', c_char * 9),
        ('IPAddress', c_char * 16),
        ('MacAddress', c_char * 21)
    ]

class CThostFtdcQryExchangeExecOrderActionField(Structure):
    _fields_ = [
        ('ParticipantID', c_char * 11),
        ('ClientID', c_char * 11),
        ('ExchangeID', c_char * 9),
        ('TraderID', c_char * 21)
    ]

class CThostFtdcErrExecOrderField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('InvestorID', c_char * 13),
        ('InstrumentID', c_char * 31),
        ('ExecOrderRef', c_char * 13),
        ('UserID', c_char * 16),
        ('Volume', c_int),
        ('RequestID', c_int),
        ('BusinessUnit', c_char * 21),
        ('OffsetFlag', c_char),
        ('HedgeFlag', c_char),
        ('ActionType', c_char),
        ('PosiDirection', c_char),
        ('ReservePositionFlag', c_char),
        ('CloseFlag', c_char),
        ('ExchangeID', c_char * 9),
        ('InvestUnitID', c_char * 17),
        ('AccountID', c_char * 13),
        ('CurrencyID', c_char * 4),
        ('ClientID', c_char * 11),
        ('IPAddress', c_char * 16),
        ('MacAddress', c_char * 21),
        ('ErrorID', c_int),
        ('ErrorMsg', c_char * 81)
    ]

class CThostFtdcQryErrExecOrderField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('InvestorID', c_char * 13)
    ]

class CThostFtdcErrExecOrderActionField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('InvestorID', c_char * 13),
        ('ExecOrderActionRef', c_int),
        ('ExecOrderRef', c_char * 13),
        ('RequestID', c_int),
        ('FrontID', c_int),
        ('SessionID', c_int),
        ('ExchangeID', c_char * 9),
        ('ExecOrderSysID', c_char * 21),
        ('ActionFlag', c_char),
        ('UserID', c_char * 16),
        ('InstrumentID', c_char * 31),
        ('InvestUnitID', c_char * 17),
        ('IPAddress', c_char * 16),
        ('MacAddress', c_char * 21),
        ('ErrorID', c_int),
        ('ErrorMsg', c_char * 81)
    ]

class CThostFtdcQryErrExecOrderActionField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('InvestorID', c_char * 13)
    ]

class CThostFtdcOptionInstrTradingRightField(Structure):
    _fields_ = [
        ('InstrumentID', c_char * 31),
        ('InvestorRange', c_char),
        ('BrokerID', c_char * 11),
        ('InvestorID', c_char * 13),
        ('Direction', c_char),
        ('TradingRight', c_char)
    ]

class CThostFtdcQryOptionInstrTradingRightField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('InvestorID', c_char * 13),
        ('InstrumentID', c_char * 31),
        ('Direction', c_char)
    ]

class CThostFtdcInputForQuoteField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('InvestorID', c_char * 13),
        ('InstrumentID', c_char * 31),
        ('ForQuoteRef', c_char * 13),
        ('UserID', c_char * 16),
        ('ExchangeID', c_char * 9),
        ('InvestUnitID', c_char * 17),
        ('IPAddress', c_char * 16),
        ('MacAddress', c_char * 21)
    ]

class CThostFtdcForQuoteField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('InvestorID', c_char * 13),
        ('InstrumentID', c_char * 31),
        ('ForQuoteRef', c_char * 13),
        ('UserID', c_char * 16),
        ('ForQuoteLocalID', c_char * 13),
        ('ExchangeID', c_char * 9),
        ('ParticipantID', c_char * 11),
        ('ClientID', c_char * 11),
        ('ExchangeInstID', c_char * 31),
        ('TraderID', c_char * 21),
        ('InstallID', c_int),
        ('InsertDate', c_char * 9),
        ('InsertTime', c_char * 9),
        ('ForQuoteStatus', c_char),
        ('FrontID', c_int),
        ('SessionID', c_int),
        ('StatusMsg', c_char * 81),
        ('ActiveUserID', c_char * 16),
        ('BrokerForQutoSeq', c_int),
        ('InvestUnitID', c_char * 17),
        ('IPAddress', c_char * 16),
        ('MacAddress', c_char * 21)
    ]

class CThostFtdcQryForQuoteField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('InvestorID', c_char * 13),
        ('InstrumentID', c_char * 31),
        ('ExchangeID', c_char * 9),
        ('InsertTimeStart', c_char * 9),
        ('InsertTimeEnd', c_char * 9)
    ]

class CThostFtdcExchangeForQuoteField(Structure):
    _fields_ = [
        ('ForQuoteLocalID', c_char * 13),
        ('ExchangeID', c_char * 9),
        ('ParticipantID', c_char * 11),
        ('ClientID', c_char * 11),
        ('ExchangeInstID', c_char * 31),
        ('TraderID', c_char * 21),
        ('InstallID', c_int),
        ('InsertDate', c_char * 9),
        ('InsertTime', c_char * 9),
        ('ForQuoteStatus', c_char),
        ('IPAddress', c_char * 16),
        ('MacAddress', c_char * 21)
    ]

class CThostFtdcQryExchangeForQuoteField(Structure):
    _fields_ = [
        ('ParticipantID', c_char * 11),
        ('ClientID', c_char * 11),
        ('ExchangeInstID', c_char * 31),
        ('ExchangeID', c_char * 9),
        ('TraderID', c_char * 21)
    ]

class CThostFtdcInputQuoteField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('InvestorID', c_char * 13),
        ('InstrumentID', c_char * 31),
        ('QuoteRef', c_char * 13),
        ('UserID', c_char * 16),
        ('AskPrice', c_double),
        ('BidPrice', c_double),
        ('AskVolume', c_int),
        ('BidVolume', c_int),
        ('RequestID', c_int),
        ('BusinessUnit', c_char * 21),
        ('AskOffsetFlag', c_char),
        ('BidOffsetFlag', c_char),
        ('AskHedgeFlag', c_char),
        ('BidHedgeFlag', c_char),
        ('AskOrderRef', c_char * 13),
        ('BidOrderRef', c_char * 13),
        ('ForQuoteSysID', c_char * 21),
        ('ExchangeID', c_char * 9),
        ('InvestUnitID', c_char * 17),
        ('ClientID', c_char * 11),
        ('IPAddress', c_char * 16),
        ('MacAddress', c_char * 21)
    ]

class CThostFtdcInputQuoteActionField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('InvestorID', c_char * 13),
        ('QuoteActionRef', c_int),
        ('QuoteRef', c_char * 13),
        ('RequestID', c_int),
        ('FrontID', c_int),
        ('SessionID', c_int),
        ('ExchangeID', c_char * 9),
        ('QuoteSysID', c_char * 21),
        ('ActionFlag', c_char),
        ('UserID', c_char * 16),
        ('InstrumentID', c_char * 31),
        ('InvestUnitID', c_char * 17),
        ('ClientID', c_char * 11),
        ('IPAddress', c_char * 16),
        ('MacAddress', c_char * 21)
    ]

class CThostFtdcQuoteField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('InvestorID', c_char * 13),
        ('InstrumentID', c_char * 31),
        ('QuoteRef', c_char * 13),
        ('UserID', c_char * 16),
        ('AskPrice', c_double),
        ('BidPrice', c_double),
        ('AskVolume', c_int),
        ('BidVolume', c_int),
        ('RequestID', c_int),
        ('BusinessUnit', c_char * 21),
        ('AskOffsetFlag', c_char),
        ('BidOffsetFlag', c_char),
        ('AskHedgeFlag', c_char),
        ('BidHedgeFlag', c_char),
        ('QuoteLocalID', c_char * 13),
        ('ExchangeID', c_char * 9),
        ('ParticipantID', c_char * 11),
        ('ClientID', c_char * 11),
        ('ExchangeInstID', c_char * 31),
        ('TraderID', c_char * 21),
        ('InstallID', c_int),
        ('NotifySequence', c_int),
        ('OrderSubmitStatus', c_char),
        ('TradingDay', c_char * 9),
        ('SettlementID', c_int),
        ('QuoteSysID', c_char * 21),
        ('InsertDate', c_char * 9),
        ('InsertTime', c_char * 9),
        ('CancelTime', c_char * 9),
        ('QuoteStatus', c_char),
        ('ClearingPartID', c_char * 11),
        ('SequenceNo', c_int),
        ('AskOrderSysID', c_char * 21),
        ('BidOrderSysID', c_char * 21),
        ('FrontID', c_int),
        ('SessionID', c_int),
        ('UserProductInfo', c_char * 11),
        ('StatusMsg', c_char * 81),
        ('ActiveUserID', c_char * 16),
        ('BrokerQuoteSeq', c_int),
        ('AskOrderRef', c_char * 13),
        ('BidOrderRef', c_char * 13),
        ('ForQuoteSysID', c_char * 21),
        ('BranchID', c_char * 9),
        ('InvestUnitID', c_char * 17),
        ('AccountID', c_char * 13),
        ('CurrencyID', c_char * 4),
        ('IPAddress', c_char * 16),
        ('MacAddress', c_char * 21)
    ]

class CThostFtdcQuoteActionField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('InvestorID', c_char * 13),
        ('QuoteActionRef', c_int),
        ('QuoteRef', c_char * 13),
        ('RequestID', c_int),
        ('FrontID', c_int),
        ('SessionID', c_int),
        ('ExchangeID', c_char * 9),
        ('QuoteSysID', c_char * 21),
        ('ActionFlag', c_char),
        ('ActionDate', c_char * 9),
        ('ActionTime', c_char * 9),
        ('TraderID', c_char * 21),
        ('InstallID', c_int),
        ('QuoteLocalID', c_char * 13),
        ('ActionLocalID', c_char * 13),
        ('ParticipantID', c_char * 11),
        ('ClientID', c_char * 11),
        ('BusinessUnit', c_char * 21),
        ('OrderActionStatus', c_char),
        ('UserID', c_char * 16),
        ('StatusMsg', c_char * 81),
        ('InstrumentID', c_char * 31),
        ('BranchID', c_char * 9),
        ('InvestUnitID', c_char * 17),
        ('IPAddress', c_char * 16),
        ('MacAddress', c_char * 21)
    ]

class CThostFtdcQryQuoteField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('InvestorID', c_char * 13),
        ('InstrumentID', c_char * 31),
        ('ExchangeID', c_char * 9),
        ('QuoteSysID', c_char * 21),
        ('InsertTimeStart', c_char * 9),
        ('InsertTimeEnd', c_char * 9)
    ]

class CThostFtdcExchangeQuoteField(Structure):
    _fields_ = [
        ('AskPrice', c_double),
        ('BidPrice', c_double),
        ('AskVolume', c_int),
        ('BidVolume', c_int),
        ('RequestID', c_int),
        ('BusinessUnit', c_char * 21),
        ('AskOffsetFlag', c_char),
        ('BidOffsetFlag', c_char),
        ('AskHedgeFlag', c_char),
        ('BidHedgeFlag', c_char),
        ('QuoteLocalID', c_char * 13),
        ('ExchangeID', c_char * 9),
        ('ParticipantID', c_char * 11),
        ('ClientID', c_char * 11),
        ('ExchangeInstID', c_char * 31),
        ('TraderID', c_char * 21),
        ('InstallID', c_int),
        ('NotifySequence', c_int),
        ('OrderSubmitStatus', c_char),
        ('TradingDay', c_char * 9),
        ('SettlementID', c_int),
        ('QuoteSysID', c_char * 21),
        ('InsertDate', c_char * 9),
        ('InsertTime', c_char * 9),
        ('CancelTime', c_char * 9),
        ('QuoteStatus', c_char),
        ('ClearingPartID', c_char * 11),
        ('SequenceNo', c_int),
        ('AskOrderSysID', c_char * 21),
        ('BidOrderSysID', c_char * 21),
        ('ForQuoteSysID', c_char * 21),
        ('BranchID', c_char * 9),
        ('IPAddress', c_char * 16),
        ('MacAddress', c_char * 21)
    ]

class CThostFtdcQryExchangeQuoteField(Structure):
    _fields_ = [
        ('ParticipantID', c_char * 11),
        ('ClientID', c_char * 11),
        ('ExchangeInstID', c_char * 31),
        ('ExchangeID', c_char * 9),
        ('TraderID', c_char * 21)
    ]

class CThostFtdcQryQuoteActionField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('InvestorID', c_char * 13),
        ('ExchangeID', c_char * 9)
    ]

class CThostFtdcExchangeQuoteActionField(Structure):
    _fields_ = [
        ('ExchangeID', c_char * 9),
        ('QuoteSysID', c_char * 21),
        ('ActionFlag', c_char),
        ('ActionDate', c_char * 9),
        ('ActionTime', c_char * 9),
        ('TraderID', c_char * 21),
        ('InstallID', c_int),
        ('QuoteLocalID', c_char * 13),
        ('ActionLocalID', c_char * 13),
        ('ParticipantID', c_char * 11),
        ('ClientID', c_char * 11),
        ('BusinessUnit', c_char * 21),
        ('OrderActionStatus', c_char),
        ('UserID', c_char * 16),
        ('IPAddress', c_char * 16),
        ('MacAddress', c_char * 21)
    ]

class CThostFtdcQryExchangeQuoteActionField(Structure):
    _fields_ = [
        ('ParticipantID', c_char * 11),
        ('ClientID', c_char * 11),
        ('ExchangeID', c_char * 9),
        ('TraderID', c_char * 21)
    ]

class CThostFtdcOptionInstrDeltaField(Structure):
    _fields_ = [
        ('InstrumentID', c_char * 31),
        ('InvestorRange', c_char),
        ('BrokerID', c_char * 11),
        ('InvestorID', c_char * 13),
        ('Delta', c_double)
    ]

class CThostFtdcForQuoteRspField(Structure):
    _fields_ = [
        ('TradingDay', c_char * 9),
        ('InstrumentID', c_char * 31),
        ('ForQuoteSysID', c_char * 21),
        ('ForQuoteTime', c_char * 9),
        ('ActionDay', c_char * 9),
        ('ExchangeID', c_char * 9)
    ]

class CThostFtdcStrikeOffsetField(Structure):
    _fields_ = [
        ('InstrumentID', c_char * 31),
        ('InvestorRange', c_char),
        ('BrokerID', c_char * 11),
        ('InvestorID', c_char * 13),
        ('Offset', c_double),
        ('OffsetType', c_char)
    ]

class CThostFtdcQryStrikeOffsetField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('InvestorID', c_char * 13),
        ('InstrumentID', c_char * 31)
    ]

class CThostFtdcInputBatchOrderActionField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('InvestorID', c_char * 13),
        ('OrderActionRef', c_int),
        ('RequestID', c_int),
        ('FrontID', c_int),
        ('SessionID', c_int),
        ('ExchangeID', c_char * 9),
        ('UserID', c_char * 16),
        ('InvestUnitID', c_char * 17),
        ('IPAddress', c_char * 16),
        ('MacAddress', c_char * 21)
    ]

class CThostFtdcBatchOrderActionField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('InvestorID', c_char * 13),
        ('OrderActionRef', c_int),
        ('RequestID', c_int),
        ('FrontID', c_int),
        ('SessionID', c_int),
        ('ExchangeID', c_char * 9),
        ('ActionDate', c_char * 9),
        ('ActionTime', c_char * 9),
        ('TraderID', c_char * 21),
        ('InstallID', c_int),
        ('ActionLocalID', c_char * 13),
        ('ParticipantID', c_char * 11),
        ('ClientID', c_char * 11),
        ('BusinessUnit', c_char * 21),
        ('OrderActionStatus', c_char),
        ('UserID', c_char * 16),
        ('StatusMsg', c_char * 81),
        ('InvestUnitID', c_char * 17),
        ('IPAddress', c_char * 16),
        ('MacAddress', c_char * 21)
    ]

class CThostFtdcExchangeBatchOrderActionField(Structure):
    _fields_ = [
        ('ExchangeID', c_char * 9),
        ('ActionDate', c_char * 9),
        ('ActionTime', c_char * 9),
        ('TraderID', c_char * 21),
        ('InstallID', c_int),
        ('ActionLocalID', c_char * 13),
        ('ParticipantID', c_char * 11),
        ('ClientID', c_char * 11),
        ('BusinessUnit', c_char * 21),
        ('OrderActionStatus', c_char),
        ('UserID', c_char * 16),
        ('IPAddress', c_char * 16),
        ('MacAddress', c_char * 21)
    ]

class CThostFtdcQryBatchOrderActionField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('InvestorID', c_char * 13),
        ('ExchangeID', c_char * 9)
    ]

class CThostFtdcCombInstrumentGuardField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('InstrumentID', c_char * 31),
        ('GuarantRatio', c_double)
    ]

class CThostFtdcQryCombInstrumentGuardField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('InstrumentID', c_char * 31)
    ]

class CThostFtdcInputCombActionField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('InvestorID', c_char * 13),
        ('InstrumentID', c_char * 31),
        ('CombActionRef', c_char * 13),
        ('UserID', c_char * 16),
        ('Direction', c_char),
        ('Volume', c_int),
        ('CombDirection', c_char),
        ('HedgeFlag', c_char),
        ('ExchangeID', c_char * 9),
        ('IPAddress', c_char * 16),
        ('MacAddress', c_char * 21)
    ]

class CThostFtdcCombActionField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('InvestorID', c_char * 13),
        ('InstrumentID', c_char * 31),
        ('CombActionRef', c_char * 13),
        ('UserID', c_char * 16),
        ('Direction', c_char),
        ('Volume', c_int),
        ('CombDirection', c_char),
        ('HedgeFlag', c_char),
        ('ActionLocalID', c_char * 13),
        ('ExchangeID', c_char * 9),
        ('ParticipantID', c_char * 11),
        ('ClientID', c_char * 11),
        ('ExchangeInstID', c_char * 31),
        ('TraderID', c_char * 21),
        ('InstallID', c_int),
        ('ActionStatus', c_char),
        ('NotifySequence', c_int),
        ('TradingDay', c_char * 9),
        ('SettlementID', c_int),
        ('SequenceNo', c_int),
        ('FrontID', c_int),
        ('SessionID', c_int),
        ('UserProductInfo', c_char * 11),
        ('StatusMsg', c_char * 81),
        ('IPAddress', c_char * 16),
        ('MacAddress', c_char * 21)
    ]

class CThostFtdcQryCombActionField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('InvestorID', c_char * 13),
        ('InstrumentID', c_char * 31),
        ('ExchangeID', c_char * 9)
    ]

class CThostFtdcExchangeCombActionField(Structure):
    _fields_ = [
        ('Direction', c_char),
        ('Volume', c_int),
        ('CombDirection', c_char),
        ('HedgeFlag', c_char),
        ('ActionLocalID', c_char * 13),
        ('ExchangeID', c_char * 9),
        ('ParticipantID', c_char * 11),
        ('ClientID', c_char * 11),
        ('ExchangeInstID', c_char * 31),
        ('TraderID', c_char * 21),
        ('InstallID', c_int),
        ('ActionStatus', c_char),
        ('NotifySequence', c_int),
        ('TradingDay', c_char * 9),
        ('SettlementID', c_int),
        ('SequenceNo', c_int),
        ('IPAddress', c_char * 16),
        ('MacAddress', c_char * 21)
    ]

class CThostFtdcQryExchangeCombActionField(Structure):
    _fields_ = [
        ('ParticipantID', c_char * 11),
        ('ClientID', c_char * 11),
        ('ExchangeInstID', c_char * 31),
        ('ExchangeID', c_char * 9),
        ('TraderID', c_char * 21)
    ]

class CThostFtdcProductExchRateField(Structure):
    _fields_ = [
        ('ProductID', c_char * 31),
        ('QuoteCurrencyID', c_char * 4),
        ('ExchangeRate', c_double)
    ]

class CThostFtdcQryProductExchRateField(Structure):
    _fields_ = [
        ('ProductID', c_char * 31)
    ]

class CThostFtdcQryForQuoteParamField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('InstrumentID', c_char * 31),
        ('ExchangeID', c_char * 9)
    ]

class CThostFtdcForQuoteParamField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('InstrumentID', c_char * 31),
        ('ExchangeID', c_char * 9),
        ('LastPrice', c_double),
        ('PriceInterval', c_double)
    ]

class CThostFtdcMMOptionInstrCommRateField(Structure):
    _fields_ = [
        ('InstrumentID', c_char * 31),
        ('InvestorRange', c_char),
        ('BrokerID', c_char * 11),
        ('InvestorID', c_char * 13),
        ('OpenRatioByMoney', c_double),
        ('OpenRatioByVolume', c_double),
        ('CloseRatioByMoney', c_double),
        ('CloseRatioByVolume', c_double),
        ('CloseTodayRatioByMoney', c_double),
        ('CloseTodayRatioByVolume', c_double),
        ('StrikeRatioByMoney', c_double),
        ('StrikeRatioByVolume', c_double)
    ]

class CThostFtdcQryMMOptionInstrCommRateField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('InvestorID', c_char * 13),
        ('InstrumentID', c_char * 31)
    ]

class CThostFtdcMMInstrumentCommissionRateField(Structure):
    _fields_ = [
        ('InstrumentID', c_char * 31),
        ('InvestorRange', c_char),
        ('BrokerID', c_char * 11),
        ('InvestorID', c_char * 13),
        ('OpenRatioByMoney', c_double),
        ('OpenRatioByVolume', c_double),
        ('CloseRatioByMoney', c_double),
        ('CloseRatioByVolume', c_double),
        ('CloseTodayRatioByMoney', c_double),
        ('CloseTodayRatioByVolume', c_double)
    ]

class CThostFtdcQryMMInstrumentCommissionRateField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('InvestorID', c_char * 13),
        ('InstrumentID', c_char * 31)
    ]

class CThostFtdcInstrumentOrderCommRateField(Structure):
    _fields_ = [
        ('InstrumentID', c_char * 31),
        ('InvestorRange', c_char),
        ('BrokerID', c_char * 11),
        ('InvestorID', c_char * 13),
        ('HedgeFlag', c_char),
        ('OrderCommByVolume', c_double),
        ('OrderActionCommByVolume', c_double)
    ]

class CThostFtdcQryInstrumentOrderCommRateField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('InvestorID', c_char * 13),
        ('InstrumentID', c_char * 31)
    ]

class CThostFtdcMarketDataField(Structure):
    _fields_ = [
        ('TradingDay', c_char * 9),
        ('InstrumentID', c_char * 31),
        ('ExchangeID', c_char * 9),
        ('ExchangeInstID', c_char * 31),
        ('LastPrice', c_double),
        ('PreSettlementPrice', c_double),
        ('PreClosePrice', c_double),
        ('PreOpenInterest', c_double),
        ('OpenPrice', c_double),
        ('HighestPrice', c_double),
        ('LowestPrice', c_double),
        ('Volume', c_int),
        ('Turnover', c_double),
        ('OpenInterest', c_double),
        ('ClosePrice', c_double),
        ('SettlementPrice', c_double),
        ('UpperLimitPrice', c_double),
        ('LowerLimitPrice', c_double),
        ('PreDelta', c_double),
        ('CurrDelta', c_double),
        ('UpdateTime', c_char * 9),
        ('UpdateMillisec', c_int),
        ('ActionDay', c_char * 9)
    ]

class CThostFtdcMarketDataBaseField(Structure):
    _fields_ = [
        ('TradingDay', c_char * 9),
        ('PreSettlementPrice', c_double),
        ('PreClosePrice', c_double),
        ('PreOpenInterest', c_double),
        ('PreDelta', c_double)
    ]

class CThostFtdcMarketDataStaticField(Structure):
    _fields_ = [
        ('OpenPrice', c_double),
        ('HighestPrice', c_double),
        ('LowestPrice', c_double),
        ('ClosePrice', c_double),
        ('UpperLimitPrice', c_double),
        ('LowerLimitPrice', c_double),
        ('SettlementPrice', c_double),
        ('CurrDelta', c_double)
    ]

class CThostFtdcMarketDataLastMatchField(Structure):
    _fields_ = [
        ('LastPrice', c_double),
        ('Volume', c_int),
        ('Turnover', c_double),
        ('OpenInterest', c_double)
    ]

class CThostFtdcMarketDataBestPriceField(Structure):
    _fields_ = [
        ('BidPrice1', c_double),
        ('BidVolume1', c_int),
        ('AskPrice1', c_double),
        ('AskVolume1', c_int)
    ]

class CThostFtdcMarketDataBid23Field(Structure):
    _fields_ = [
        ('BidPrice2', c_double),
        ('BidVolume2', c_int),
        ('BidPrice3', c_double),
        ('BidVolume3', c_int)
    ]

class CThostFtdcMarketDataAsk23Field(Structure):
    _fields_ = [
        ('AskPrice2', c_double),
        ('AskVolume2', c_int),
        ('AskPrice3', c_double),
        ('AskVolume3', c_int)
    ]

class CThostFtdcMarketDataBid45Field(Structure):
    _fields_ = [
        ('BidPrice4', c_double),
        ('BidVolume4', c_int),
        ('BidPrice5', c_double),
        ('BidVolume5', c_int)
    ]

class CThostFtdcMarketDataAsk45Field(Structure):
    _fields_ = [
        ('AskPrice4', c_double),
        ('AskVolume4', c_int),
        ('AskPrice5', c_double),
        ('AskVolume5', c_int)
    ]

class CThostFtdcMarketDataUpdateTimeField(Structure):
    _fields_ = [
        ('InstrumentID', c_char * 31),
        ('UpdateTime', c_char * 9),
        ('UpdateMillisec', c_int),
        ('ActionDay', c_char * 9)
    ]

class CThostFtdcMarketDataExchangeField(Structure):
    _fields_ = [
        ('ExchangeID', c_char * 9)
    ]

class CThostFtdcSpecificInstrumentField(Structure):
    _fields_ = [
        ('InstrumentID', c_char * 31)
    ]

class CThostFtdcInstrumentStatusField(Structure):
    _fields_ = [
        ('ExchangeID', c_char * 9),
        ('ExchangeInstID', c_char * 31),
        ('SettlementGroupID', c_char * 9),
        ('InstrumentID', c_char * 31),
        ('InstrumentStatus', c_char),
        ('TradingSegmentSN', c_int),
        ('EnterTime', c_char * 9),
        ('EnterReason', c_char)
    ]

class CThostFtdcQryInstrumentStatusField(Structure):
    _fields_ = [
        ('ExchangeID', c_char * 9),
        ('ExchangeInstID', c_char * 31)
    ]

class CThostFtdcInvestorAccountField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('InvestorID', c_char * 13),
        ('AccountID', c_char * 13),
        ('CurrencyID', c_char * 4)
    ]

class CThostFtdcPositionProfitAlgorithmField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('AccountID', c_char * 13),
        ('Algorithm', c_char),
        ('Memo', c_char * 161),
        ('CurrencyID', c_char * 4)
    ]

class CThostFtdcDiscountField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('InvestorRange', c_char),
        ('InvestorID', c_char * 13),
        ('Discount', c_double)
    ]

class CThostFtdcQryTransferBankField(Structure):
    _fields_ = [
        ('BankID', c_char * 4),
        ('BankBrchID', c_char * 5)
    ]

class CThostFtdcTransferBankField(Structure):
    _fields_ = [
        ('BankID', c_char * 4),
        ('BankBrchID', c_char * 5),
        ('BankName', c_char * 101),
        ('IsActive', c_int)
    ]

class CThostFtdcQryInvestorPositionDetailField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('InvestorID', c_char * 13),
        ('InstrumentID', c_char * 31)
    ]

class CThostFtdcInvestorPositionDetailField(Structure):
    _fields_ = [
        ('InstrumentID', c_char * 31),
        ('BrokerID', c_char * 11),
        ('InvestorID', c_char * 13),
        ('HedgeFlag', c_char),
        ('Direction', c_char),
        ('OpenDate', c_char * 9),
        ('TradeID', c_char * 21),
        ('Volume', c_int),
        ('OpenPrice', c_double),
        ('TradingDay', c_char * 9),
        ('SettlementID', c_int),
        ('TradeType', c_char),
        ('CombInstrumentID', c_char * 31),
        ('ExchangeID', c_char * 9),
        ('CloseProfitByDate', c_double),
        ('CloseProfitByTrade', c_double),
        ('PositionProfitByDate', c_double),
        ('PositionProfitByTrade', c_double),
        ('Margin', c_double),
        ('ExchMargin', c_double),
        ('MarginRateByMoney', c_double),
        ('MarginRateByVolume', c_double),
        ('LastSettlementPrice', c_double),
        ('SettlementPrice', c_double),
        ('CloseVolume', c_int),
        ('CloseAmount', c_double)
    ]

class CThostFtdcTradingAccountPasswordField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('AccountID', c_char * 13),
        ('Password', c_char * 41),
        ('CurrencyID', c_char * 4)
    ]

class CThostFtdcMDTraderOfferField(Structure):
    _fields_ = [
        ('ExchangeID', c_char * 9),
        ('TraderID', c_char * 21),
        ('ParticipantID', c_char * 11),
        ('Password', c_char * 41),
        ('InstallID', c_int),
        ('OrderLocalID', c_char * 13),
        ('TraderConnectStatus', c_char),
        ('ConnectRequestDate', c_char * 9),
        ('ConnectRequestTime', c_char * 9),
        ('LastReportDate', c_char * 9),
        ('LastReportTime', c_char * 9),
        ('ConnectDate', c_char * 9),
        ('ConnectTime', c_char * 9),
        ('StartDate', c_char * 9),
        ('StartTime', c_char * 9),
        ('TradingDay', c_char * 9),
        ('BrokerID', c_char * 11),
        ('MaxTradeID', c_char * 21),
        ('MaxOrderMessageReference', c_char * 7)
    ]

class CThostFtdcQryMDTraderOfferField(Structure):
    _fields_ = [
        ('ExchangeID', c_char * 9),
        ('ParticipantID', c_char * 11),
        ('TraderID', c_char * 21)
    ]

class CThostFtdcQryNoticeField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11)
    ]

class CThostFtdcNoticeField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('Content', c_char * 501),
        ('SequenceLabel', c_char * 2)
    ]

class CThostFtdcUserRightField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('UserID', c_char * 16),
        ('UserRightType', c_char),
        ('IsForbidden', c_int)
    ]

class CThostFtdcQrySettlementInfoConfirmField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('InvestorID', c_char * 13)
    ]

class CThostFtdcLoadSettlementInfoField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11)
    ]

class CThostFtdcBrokerWithdrawAlgorithmField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('WithdrawAlgorithm', c_char),
        ('UsingRatio', c_double),
        ('IncludeCloseProfit', c_char),
        ('AllWithoutTrade', c_char),
        ('AvailIncludeCloseProfit', c_char),
        ('IsBrokerUserEvent', c_int),
        ('CurrencyID', c_char * 4),
        ('FundMortgageRatio', c_double),
        ('BalanceAlgorithm', c_char)
    ]

class CThostFtdcTradingAccountPasswordUpdateV1Field(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('InvestorID', c_char * 13),
        ('OldPassword', c_char * 41),
        ('NewPassword', c_char * 41)
    ]

class CThostFtdcTradingAccountPasswordUpdateField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('AccountID', c_char * 13),
        ('OldPassword', c_char * 41),
        ('NewPassword', c_char * 41),
        ('CurrencyID', c_char * 4)
    ]

class CThostFtdcQryCombinationLegField(Structure):
    _fields_ = [
        ('CombInstrumentID', c_char * 31),
        ('LegID', c_int),
        ('LegInstrumentID', c_char * 31)
    ]

class CThostFtdcQrySyncStatusField(Structure):
    _fields_ = [
        ('TradingDay', c_char * 9)
    ]

class CThostFtdcCombinationLegField(Structure):
    _fields_ = [
        ('CombInstrumentID', c_char * 31),
        ('LegID', c_int),
        ('LegInstrumentID', c_char * 31),
        ('Direction', c_char),
        ('LegMultiple', c_int),
        ('ImplyLevel', c_int)
    ]

class CThostFtdcSyncStatusField(Structure):
    _fields_ = [
        ('TradingDay', c_char * 9),
        ('DataSyncStatus', c_char)
    ]

class CThostFtdcQryLinkManField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('InvestorID', c_char * 13)
    ]

class CThostFtdcLinkManField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('InvestorID', c_char * 13),
        ('PersonType', c_char),
        ('IdentifiedCardType', c_char),
        ('IdentifiedCardNo', c_char * 51),
        ('PersonName', c_char * 81),
        ('Telephone', c_char * 41),
        ('Address', c_char * 101),
        ('ZipCode', c_char * 7),
        ('Priority', c_int),
        ('UOAZipCode', c_char * 11),
        ('PersonFullName', c_char * 101)
    ]

class CThostFtdcQryBrokerUserEventField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('UserID', c_char * 16),
        ('UserEventType', c_char)
    ]

class CThostFtdcBrokerUserEventField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('UserID', c_char * 16),
        ('UserEventType', c_char),
        ('EventSequenceNo', c_int),
        ('EventDate', c_char * 9),
        ('EventTime', c_char * 9),
        ('UserEventInfo', c_char * 1025),
        ('InvestorID', c_char * 13),
        ('InstrumentID', c_char * 31)
    ]

class CThostFtdcQryContractBankField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('BankID', c_char * 4),
        ('BankBrchID', c_char * 5)
    ]

class CThostFtdcContractBankField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('BankID', c_char * 4),
        ('BankBrchID', c_char * 5),
        ('BankName', c_char * 101)
    ]

class CThostFtdcInvestorPositionCombineDetailField(Structure):
    _fields_ = [
        ('TradingDay', c_char * 9),
        ('OpenDate', c_char * 9),
        ('ExchangeID', c_char * 9),
        ('SettlementID', c_int),
        ('BrokerID', c_char * 11),
        ('InvestorID', c_char * 13),
        ('ComTradeID', c_char * 21),
        ('TradeID', c_char * 21),
        ('InstrumentID', c_char * 31),
        ('HedgeFlag', c_char),
        ('Direction', c_char),
        ('TotalAmt', c_int),
        ('Margin', c_double),
        ('ExchMargin', c_double),
        ('MarginRateByMoney', c_double),
        ('MarginRateByVolume', c_double),
        ('LegID', c_int),
        ('LegMultiple', c_int),
        ('CombInstrumentID', c_char * 31),
        ('TradeGroupID', c_int)
    ]

class CThostFtdcParkedOrderField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('InvestorID', c_char * 13),
        ('InstrumentID', c_char * 31),
        ('OrderRef', c_char * 13),
        ('UserID', c_char * 16),
        ('OrderPriceType', c_char),
        ('Direction', c_char),
        ('CombOffsetFlag', c_char * 5),
        ('CombHedgeFlag', c_char * 5),
        ('LimitPrice', c_double),
        ('VolumeTotalOriginal', c_int),
        ('TimeCondition', c_char),
        ('GTDDate', c_char * 9),
        ('VolumeCondition', c_char),
        ('MinVolume', c_int),
        ('ContingentCondition', c_char),
        ('StopPrice', c_double),
        ('ForceCloseReason', c_char),
        ('IsAutoSuspend', c_int),
        ('BusinessUnit', c_char * 21),
        ('RequestID', c_int),
        ('UserForceClose', c_int),
        ('ExchangeID', c_char * 9),
        ('ParkedOrderID', c_char * 13),
        ('UserType', c_char),
        ('Status', c_char),
        ('ErrorID', c_int),
        ('ErrorMsg', c_char * 81),
        ('IsSwapOrder', c_int),
        ('AccountID', c_char * 13),
        ('CurrencyID', c_char * 4),
        ('ClientID', c_char * 11),
        ('InvestUnitID', c_char * 17),
        ('IPAddress', c_char * 16),
        ('MacAddress', c_char * 21)
    ]

class CThostFtdcParkedOrderActionField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('InvestorID', c_char * 13),
        ('OrderActionRef', c_int),
        ('OrderRef', c_char * 13),
        ('RequestID', c_int),
        ('FrontID', c_int),
        ('SessionID', c_int),
        ('ExchangeID', c_char * 9),
        ('OrderSysID', c_char * 21),
        ('ActionFlag', c_char),
        ('LimitPrice', c_double),
        ('VolumeChange', c_int),
        ('UserID', c_char * 16),
        ('InstrumentID', c_char * 31),
        ('ParkedOrderActionID', c_char * 13),
        ('UserType', c_char),
        ('Status', c_char),
        ('ErrorID', c_int),
        ('ErrorMsg', c_char * 81),
        ('InvestUnitID', c_char * 17),
        ('IPAddress', c_char * 16),
        ('MacAddress', c_char * 21)
    ]

class CThostFtdcQryParkedOrderField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('InvestorID', c_char * 13),
        ('InstrumentID', c_char * 31),
        ('ExchangeID', c_char * 9)
    ]

class CThostFtdcQryParkedOrderActionField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('InvestorID', c_char * 13),
        ('InstrumentID', c_char * 31),
        ('ExchangeID', c_char * 9)
    ]

class CThostFtdcRemoveParkedOrderField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('InvestorID', c_char * 13),
        ('ParkedOrderID', c_char * 13)
    ]

class CThostFtdcRemoveParkedOrderActionField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('InvestorID', c_char * 13),
        ('ParkedOrderActionID', c_char * 13)
    ]

class CThostFtdcInvestorWithdrawAlgorithmField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('InvestorRange', c_char),
        ('InvestorID', c_char * 13),
        ('UsingRatio', c_double),
        ('CurrencyID', c_char * 4),
        ('FundMortgageRatio', c_double)
    ]

class CThostFtdcQryInvestorPositionCombineDetailField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('InvestorID', c_char * 13),
        ('CombInstrumentID', c_char * 31)
    ]

class CThostFtdcMarketDataAveragePriceField(Structure):
    _fields_ = [
        ('AveragePrice', c_double)
    ]

class CThostFtdcVerifyInvestorPasswordField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('InvestorID', c_char * 13),
        ('Password', c_char * 41)
    ]

class CThostFtdcUserIPField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('UserID', c_char * 16),
        ('IPAddress', c_char * 16),
        ('IPMask', c_char * 16),
        ('MacAddress', c_char * 21)
    ]

class CThostFtdcTradingNoticeInfoField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('InvestorID', c_char * 13),
        ('SendTime', c_char * 9),
        ('FieldContent', c_char * 501),
        ('SequenceSeries', c_short),
        ('SequenceNo', c_int)
    ]

class CThostFtdcTradingNoticeField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('InvestorRange', c_char),
        ('InvestorID', c_char * 13),
        ('SequenceSeries', c_short),
        ('UserID', c_char * 16),
        ('SendTime', c_char * 9),
        ('SequenceNo', c_int),
        ('FieldContent', c_char * 501)
    ]

class CThostFtdcQryTradingNoticeField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('InvestorID', c_char * 13)
    ]

class CThostFtdcQryErrOrderField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('InvestorID', c_char * 13)
    ]

class CThostFtdcErrOrderField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('InvestorID', c_char * 13),
        ('InstrumentID', c_char * 31),
        ('OrderRef', c_char * 13),
        ('UserID', c_char * 16),
        ('OrderPriceType', c_char),
        ('Direction', c_char),
        ('CombOffsetFlag', c_char * 5),
        ('CombHedgeFlag', c_char * 5),
        ('LimitPrice', c_double),
        ('VolumeTotalOriginal', c_int),
        ('TimeCondition', c_char),
        ('GTDDate', c_char * 9),
        ('VolumeCondition', c_char),
        ('MinVolume', c_int),
        ('ContingentCondition', c_char),
        ('StopPrice', c_double),
        ('ForceCloseReason', c_char),
        ('IsAutoSuspend', c_int),
        ('BusinessUnit', c_char * 21),
        ('RequestID', c_int),
        ('UserForceClose', c_int),
        ('ErrorID', c_int),
        ('ErrorMsg', c_char * 81),
        ('IsSwapOrder', c_int),
        ('ExchangeID', c_char * 9),
        ('InvestUnitID', c_char * 17),
        ('AccountID', c_char * 13),
        ('CurrencyID', c_char * 4),
        ('ClientID', c_char * 11),
        ('IPAddress', c_char * 16),
        ('MacAddress', c_char * 21)
    ]

class CThostFtdcErrorConditionalOrderField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('InvestorID', c_char * 13),
        ('InstrumentID', c_char * 31),
        ('OrderRef', c_char * 13),
        ('UserID', c_char * 16),
        ('OrderPriceType', c_char),
        ('Direction', c_char),
        ('CombOffsetFlag', c_char * 5),
        ('CombHedgeFlag', c_char * 5),
        ('LimitPrice', c_double),
        ('VolumeTotalOriginal', c_int),
        ('TimeCondition', c_char),
        ('GTDDate', c_char * 9),
        ('VolumeCondition', c_char),
        ('MinVolume', c_int),
        ('ContingentCondition', c_char),
        ('StopPrice', c_double),
        ('ForceCloseReason', c_char),
        ('IsAutoSuspend', c_int),
        ('BusinessUnit', c_char * 21),
        ('RequestID', c_int),
        ('OrderLocalID', c_char * 13),
        ('ExchangeID', c_char * 9),
        ('ParticipantID', c_char * 11),
        ('ClientID', c_char * 11),
        ('ExchangeInstID', c_char * 31),
        ('TraderID', c_char * 21),
        ('InstallID', c_int),
        ('OrderSubmitStatus', c_char),
        ('NotifySequence', c_int),
        ('TradingDay', c_char * 9),
        ('SettlementID', c_int),
        ('OrderSysID', c_char * 21),
        ('OrderSource', c_char),
        ('OrderStatus', c_char),
        ('OrderType', c_char),
        ('VolumeTraded', c_int),
        ('VolumeTotal', c_int),
        ('InsertDate', c_char * 9),
        ('InsertTime', c_char * 9),
        ('ActiveTime', c_char * 9),
        ('SuspendTime', c_char * 9),
        ('UpdateTime', c_char * 9),
        ('CancelTime', c_char * 9),
        ('ActiveTraderID', c_char * 21),
        ('ClearingPartID', c_char * 11),
        ('SequenceNo', c_int),
        ('FrontID', c_int),
        ('SessionID', c_int),
        ('UserProductInfo', c_char * 11),
        ('StatusMsg', c_char * 81),
        ('UserForceClose', c_int),
        ('ActiveUserID', c_char * 16),
        ('BrokerOrderSeq', c_int),
        ('RelativeOrderSysID', c_char * 21),
        ('ZCETotalTradedVolume', c_int),
        ('ErrorID', c_int),
        ('ErrorMsg', c_char * 81),
        ('IsSwapOrder', c_int),
        ('BranchID', c_char * 9),
        ('InvestUnitID', c_char * 17),
        ('AccountID', c_char * 13),
        ('CurrencyID', c_char * 4),
        ('IPAddress', c_char * 16),
        ('MacAddress', c_char * 21)
    ]

class CThostFtdcQryErrOrderActionField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('InvestorID', c_char * 13)
    ]

class CThostFtdcErrOrderActionField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('InvestorID', c_char * 13),
        ('OrderActionRef', c_int),
        ('OrderRef', c_char * 13),
        ('RequestID', c_int),
        ('FrontID', c_int),
        ('SessionID', c_int),
        ('ExchangeID', c_char * 9),
        ('OrderSysID', c_char * 21),
        ('ActionFlag', c_char),
        ('LimitPrice', c_double),
        ('VolumeChange', c_int),
        ('ActionDate', c_char * 9),
        ('ActionTime', c_char * 9),
        ('TraderID', c_char * 21),
        ('InstallID', c_int),
        ('OrderLocalID', c_char * 13),
        ('ActionLocalID', c_char * 13),
        ('ParticipantID', c_char * 11),
        ('ClientID', c_char * 11),
        ('BusinessUnit', c_char * 21),
        ('OrderActionStatus', c_char),
        ('UserID', c_char * 16),
        ('StatusMsg', c_char * 81),
        ('InstrumentID', c_char * 31),
        ('BranchID', c_char * 9),
        ('InvestUnitID', c_char * 17),
        ('IPAddress', c_char * 16),
        ('MacAddress', c_char * 21),
        ('ErrorID', c_int),
        ('ErrorMsg', c_char * 81)
    ]

class CThostFtdcQryExchangeSequenceField(Structure):
    _fields_ = [
        ('ExchangeID', c_char * 9)
    ]

class CThostFtdcExchangeSequenceField(Structure):
    _fields_ = [
        ('ExchangeID', c_char * 9),
        ('SequenceNo', c_int),
        ('MarketStatus', c_char)
    ]

class CThostFtdcQueryMaxOrderVolumeWithPriceField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('InvestorID', c_char * 13),
        ('InstrumentID', c_char * 31),
        ('Direction', c_char),
        ('OffsetFlag', c_char),
        ('HedgeFlag', c_char),
        ('MaxVolume', c_int),
        ('Price', c_double)
    ]

class CThostFtdcQryBrokerTradingParamsField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('InvestorID', c_char * 13),
        ('CurrencyID', c_char * 4)
    ]

class CThostFtdcBrokerTradingParamsField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('InvestorID', c_char * 13),
        ('MarginPriceType', c_char),
        ('Algorithm', c_char),
        ('AvailIncludeCloseProfit', c_char),
        ('CurrencyID', c_char * 4),
        ('OptionRoyaltyPriceType', c_char)
    ]

class CThostFtdcQryBrokerTradingAlgosField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('ExchangeID', c_char * 9),
        ('InstrumentID', c_char * 31)
    ]

class CThostFtdcBrokerTradingAlgosField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('ExchangeID', c_char * 9),
        ('InstrumentID', c_char * 31),
        ('HandlePositionAlgoID', c_char),
        ('FindMarginRateAlgoID', c_char),
        ('HandleTradingAccountAlgoID', c_char)
    ]

class CThostFtdcQueryBrokerDepositField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('ExchangeID', c_char * 9)
    ]

class CThostFtdcBrokerDepositField(Structure):
    _fields_ = [
        ('TradingDay', c_char * 9),
        ('BrokerID', c_char * 11),
        ('ParticipantID', c_char * 11),
        ('ExchangeID', c_char * 9),
        ('PreBalance', c_double),
        ('CurrMargin', c_double),
        ('CloseProfit', c_double),
        ('Balance', c_double),
        ('Deposit', c_double),
        ('Withdraw', c_double),
        ('Available', c_double),
        ('Reserve', c_double),
        ('FrozenMargin', c_double)
    ]

class CThostFtdcQryCFMMCBrokerKeyField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11)
    ]

class CThostFtdcCFMMCBrokerKeyField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('ParticipantID', c_char * 11),
        ('CreateDate', c_char * 9),
        ('CreateTime', c_char * 9),
        ('KeyID', c_int),
        ('CurrentKey', c_char * 21),
        ('KeyKind', c_char)
    ]

class CThostFtdcCFMMCTradingAccountKeyField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('ParticipantID', c_char * 11),
        ('AccountID', c_char * 13),
        ('KeyID', c_int),
        ('CurrentKey', c_char * 21)
    ]

class CThostFtdcQryCFMMCTradingAccountKeyField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('InvestorID', c_char * 13)
    ]

class CThostFtdcBrokerUserOTPParamField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('UserID', c_char * 16),
        ('OTPVendorsID', c_char * 2),
        ('SerialNumber', c_char * 17),
        ('AuthKey', c_char * 41),
        ('LastDrift', c_int),
        ('LastSuccess', c_int),
        ('OTPType', c_char)
    ]

class CThostFtdcManualSyncBrokerUserOTPField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('UserID', c_char * 16),
        ('OTPType', c_char),
        ('FirstOTP', c_char * 41),
        ('SecondOTP', c_char * 41)
    ]

class CThostFtdcCommRateModelField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('CommModelID', c_char * 13),
        ('CommModelName', c_char * 161)
    ]

class CThostFtdcQryCommRateModelField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('CommModelID', c_char * 13)
    ]

class CThostFtdcMarginModelField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('MarginModelID', c_char * 13),
        ('MarginModelName', c_char * 161)
    ]

class CThostFtdcQryMarginModelField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('MarginModelID', c_char * 13)
    ]

class CThostFtdcEWarrantOffsetField(Structure):
    _fields_ = [
        ('TradingDay', c_char * 9),
        ('BrokerID', c_char * 11),
        ('InvestorID', c_char * 13),
        ('ExchangeID', c_char * 9),
        ('InstrumentID', c_char * 31),
        ('Direction', c_char),
        ('HedgeFlag', c_char),
        ('Volume', c_int)
    ]

class CThostFtdcQryEWarrantOffsetField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('InvestorID', c_char * 13),
        ('ExchangeID', c_char * 9),
        ('InstrumentID', c_char * 31)
    ]

class CThostFtdcQryInvestorProductGroupMarginField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('InvestorID', c_char * 13),
        ('ProductGroupID', c_char * 31),
        ('HedgeFlag', c_char)
    ]

class CThostFtdcInvestorProductGroupMarginField(Structure):
    _fields_ = [
        ('ProductGroupID', c_char * 31),
        ('BrokerID', c_char * 11),
        ('InvestorID', c_char * 13),
        ('TradingDay', c_char * 9),
        ('SettlementID', c_int),
        ('FrozenMargin', c_double),
        ('LongFrozenMargin', c_double),
        ('ShortFrozenMargin', c_double),
        ('UseMargin', c_double),
        ('LongUseMargin', c_double),
        ('ShortUseMargin', c_double),
        ('ExchMargin', c_double),
        ('LongExchMargin', c_double),
        ('ShortExchMargin', c_double),
        ('CloseProfit', c_double),
        ('FrozenCommission', c_double),
        ('Commission', c_double),
        ('FrozenCash', c_double),
        ('CashIn', c_double),
        ('PositionProfit', c_double),
        ('OffsetAmount', c_double),
        ('LongOffsetAmount', c_double),
        ('ShortOffsetAmount', c_double),
        ('ExchOffsetAmount', c_double),
        ('LongExchOffsetAmount', c_double),
        ('ShortExchOffsetAmount', c_double),
        ('HedgeFlag', c_char)
    ]

class CThostFtdcQueryCFMMCTradingAccountTokenField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('InvestorID', c_char * 13)
    ]

class CThostFtdcCFMMCTradingAccountTokenField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('ParticipantID', c_char * 11),
        ('AccountID', c_char * 13),
        ('KeyID', c_int),
        ('Token', c_char * 21)
    ]

class CThostFtdcQryProductGroupField(Structure):
    _fields_ = [
        ('ProductID', c_char * 31),
        ('ExchangeID', c_char * 9)
    ]

class CThostFtdcProductGroupField(Structure):
    _fields_ = [
        ('ProductID', c_char * 31),
        ('ExchangeID', c_char * 9),
        ('ProductGroupID', c_char * 31)
    ]

class CThostFtdcBulletinField(Structure):
    _fields_ = [
        ('ExchangeID', c_char * 9),
        ('TradingDay', c_char * 9),
        ('BulletinID', c_int),
        ('SequenceNo', c_int),
        ('NewsType', c_char * 3),
        ('NewsUrgency', c_char),
        ('SendTime', c_char * 9),
        ('Abstract', c_char * 81),
        ('ComeFrom', c_char * 21),
        ('Content', c_char * 501),
        ('URLLink', c_char * 201),
        ('MarketID', c_char * 31)
    ]

class CThostFtdcQryBulletinField(Structure):
    _fields_ = [
        ('ExchangeID', c_char * 9),
        ('BulletinID', c_int),
        ('SequenceNo', c_int),
        ('NewsType', c_char * 3),
        ('NewsUrgency', c_char)
    ]

class CThostFtdcReqOpenAccountField(Structure):
    _fields_ = [
        ('TradeCode', c_char * 7),
        ('BankID', c_char * 4),
        ('BankBranchID', c_char * 5),
        ('BrokerID', c_char * 11),
        ('BrokerBranchID', c_char * 31),
        ('TradeDate', c_char * 9),
        ('TradeTime', c_char * 9),
        ('BankSerial', c_char * 13),
        ('TradingDay', c_char * 9),
        ('PlateSerial', c_int),
        ('LastFragment', c_char),
        ('SessionID', c_int),
        ('CustomerName', c_char * 51),
        ('IdCardType', c_char),
        ('IdentifiedCardNo', c_char * 51),
        ('Gender', c_char),
        ('CountryCode', c_char * 21),
        ('CustType', c_char),
        ('Address', c_char * 101),
        ('ZipCode', c_char * 7),
        ('Telephone', c_char * 41),
        ('MobilePhone', c_char * 21),
        ('Fax', c_char * 41),
        ('EMail', c_char * 41),
        ('MoneyAccountStatus', c_char),
        ('BankAccount', c_char * 41),
        ('BankPassWord', c_char * 41),
        ('AccountID', c_char * 13),
        ('Password', c_char * 41),
        ('InstallID', c_int),
        ('VerifyCertNoFlag', c_char),
        ('CurrencyID', c_char * 4),
        ('CashExchangeCode', c_char),
        ('Digest', c_char * 36),
        ('BankAccType', c_char),
        ('DeviceID', c_char * 3),
        ('BankSecuAccType', c_char),
        ('BrokerIDByBank', c_char * 33),
        ('BankSecuAcc', c_char * 41),
        ('BankPwdFlag', c_char),
        ('SecuPwdFlag', c_char),
        ('OperNo', c_char * 17),
        ('TID', c_int),
        ('UserID', c_char * 16),
        ('LongCustomerName', c_char * 161)
    ]

class CThostFtdcReqCancelAccountField(Structure):
    _fields_ = [
        ('TradeCode', c_char * 7),
        ('BankID', c_char * 4),
        ('BankBranchID', c_char * 5),
        ('BrokerID', c_char * 11),
        ('BrokerBranchID', c_char * 31),
        ('TradeDate', c_char * 9),
        ('TradeTime', c_char * 9),
        ('BankSerial', c_char * 13),
        ('TradingDay', c_char * 9),
        ('PlateSerial', c_int),
        ('LastFragment', c_char),
        ('SessionID', c_int),
        ('CustomerName', c_char * 51),
        ('IdCardType', c_char),
        ('IdentifiedCardNo', c_char * 51),
        ('Gender', c_char),
        ('CountryCode', c_char * 21),
        ('CustType', c_char),
        ('Address', c_char * 101),
        ('ZipCode', c_char * 7),
        ('Telephone', c_char * 41),
        ('MobilePhone', c_char * 21),
        ('Fax', c_char * 41),
        ('EMail', c_char * 41),
        ('MoneyAccountStatus', c_char),
        ('BankAccount', c_char * 41),
        ('BankPassWord', c_char * 41),
        ('AccountID', c_char * 13),
        ('Password', c_char * 41),
        ('InstallID', c_int),
        ('VerifyCertNoFlag', c_char),
        ('CurrencyID', c_char * 4),
        ('CashExchangeCode', c_char),
        ('Digest', c_char * 36),
        ('BankAccType', c_char),
        ('DeviceID', c_char * 3),
        ('BankSecuAccType', c_char),
        ('BrokerIDByBank', c_char * 33),
        ('BankSecuAcc', c_char * 41),
        ('BankPwdFlag', c_char),
        ('SecuPwdFlag', c_char),
        ('OperNo', c_char * 17),
        ('TID', c_int),
        ('UserID', c_char * 16),
        ('LongCustomerName', c_char * 161)
    ]

class CThostFtdcReqChangeAccountField(Structure):
    _fields_ = [
        ('TradeCode', c_char * 7),
        ('BankID', c_char * 4),
        ('BankBranchID', c_char * 5),
        ('BrokerID', c_char * 11),
        ('BrokerBranchID', c_char * 31),
        ('TradeDate', c_char * 9),
        ('TradeTime', c_char * 9),
        ('BankSerial', c_char * 13),
        ('TradingDay', c_char * 9),
        ('PlateSerial', c_int),
        ('LastFragment', c_char),
        ('SessionID', c_int),
        ('CustomerName', c_char * 51),
        ('IdCardType', c_char),
        ('IdentifiedCardNo', c_char * 51),
        ('Gender', c_char),
        ('CountryCode', c_char * 21),
        ('CustType', c_char),
        ('Address', c_char * 101),
        ('ZipCode', c_char * 7),
        ('Telephone', c_char * 41),
        ('MobilePhone', c_char * 21),
        ('Fax', c_char * 41),
        ('EMail', c_char * 41),
        ('MoneyAccountStatus', c_char),
        ('BankAccount', c_char * 41),
        ('BankPassWord', c_char * 41),
        ('NewBankAccount', c_char * 41),
        ('NewBankPassWord', c_char * 41),
        ('AccountID', c_char * 13),
        ('Password', c_char * 41),
        ('BankAccType', c_char),
        ('InstallID', c_int),
        ('VerifyCertNoFlag', c_char),
        ('CurrencyID', c_char * 4),
        ('BrokerIDByBank', c_char * 33),
        ('BankPwdFlag', c_char),
        ('SecuPwdFlag', c_char),
        ('TID', c_int),
        ('Digest', c_char * 36),
        ('LongCustomerName', c_char * 161)
    ]

class CThostFtdcReqTransferField(Structure):
    _fields_ = [
        ('TradeCode', c_char * 7),
        ('BankID', c_char * 4),
        ('BankBranchID', c_char * 5),
        ('BrokerID', c_char * 11),
        ('BrokerBranchID', c_char * 31),
        ('TradeDate', c_char * 9),
        ('TradeTime', c_char * 9),
        ('BankSerial', c_char * 13),
        ('TradingDay', c_char * 9),
        ('PlateSerial', c_int),
        ('LastFragment', c_char),
        ('SessionID', c_int),
        ('CustomerName', c_char * 51),
        ('IdCardType', c_char),
        ('IdentifiedCardNo', c_char * 51),
        ('CustType', c_char),
        ('BankAccount', c_char * 41),
        ('BankPassWord', c_char * 41),
        ('AccountID', c_char * 13),
        ('Password', c_char * 41),
        ('InstallID', c_int),
        ('FutureSerial', c_int),
        ('UserID', c_char * 16),
        ('VerifyCertNoFlag', c_char),
        ('CurrencyID', c_char * 4),
        ('TradeAmount', c_double),
        ('FutureFetchAmount', c_double),
        ('FeePayFlag', c_char),
        ('CustFee', c_double),
        ('BrokerFee', c_double),
        ('Message', c_char * 129),
        ('Digest', c_char * 36),
        ('BankAccType', c_char),
        ('DeviceID', c_char * 3),
        ('BankSecuAccType', c_char),
        ('BrokerIDByBank', c_char * 33),
        ('BankSecuAcc', c_char * 41),
        ('BankPwdFlag', c_char),
        ('SecuPwdFlag', c_char),
        ('OperNo', c_char * 17),
        ('RequestID', c_int),
        ('TID', c_int),
        ('TransferStatus', c_char),
        ('LongCustomerName', c_char * 161)
    ]

class CThostFtdcRspTransferField(Structure):
    _fields_ = [
        ('TradeCode', c_char * 7),
        ('BankID', c_char * 4),
        ('BankBranchID', c_char * 5),
        ('BrokerID', c_char * 11),
        ('BrokerBranchID', c_char * 31),
        ('TradeDate', c_char * 9),
        ('TradeTime', c_char * 9),
        ('BankSerial', c_char * 13),
        ('TradingDay', c_char * 9),
        ('PlateSerial', c_int),
        ('LastFragment', c_char),
        ('SessionID', c_int),
        ('CustomerName', c_char * 51),
        ('IdCardType', c_char),
        ('IdentifiedCardNo', c_char * 51),
        ('CustType', c_char),
        ('BankAccount', c_char * 41),
        ('BankPassWord', c_char * 41),
        ('AccountID', c_char * 13),
        ('Password', c_char * 41),
        ('InstallID', c_int),
        ('FutureSerial', c_int),
        ('UserID', c_char * 16),
        ('VerifyCertNoFlag', c_char),
        ('CurrencyID', c_char * 4),
        ('TradeAmount', c_double),
        ('FutureFetchAmount', c_double),
        ('FeePayFlag', c_char),
        ('CustFee', c_double),
        ('BrokerFee', c_double),
        ('Message', c_char * 129),
        ('Digest', c_char * 36),
        ('BankAccType', c_char),
        ('DeviceID', c_char * 3),
        ('BankSecuAccType', c_char),
        ('BrokerIDByBank', c_char * 33),
        ('BankSecuAcc', c_char * 41),
        ('BankPwdFlag', c_char),
        ('SecuPwdFlag', c_char),
        ('OperNo', c_char * 17),
        ('RequestID', c_int),
        ('TID', c_int),
        ('TransferStatus', c_char),
        ('ErrorID', c_int),
        ('ErrorMsg', c_char * 81),
        ('LongCustomerName', c_char * 161)
    ]

class CThostFtdcReqRepealField(Structure):
    _fields_ = [
        ('RepealTimeInterval', c_int),
        ('RepealedTimes', c_int),
        ('BankRepealFlag', c_char),
        ('BrokerRepealFlag', c_char),
        ('PlateRepealSerial', c_int),
        ('BankRepealSerial', c_char * 13),
        ('FutureRepealSerial', c_int),
        ('TradeCode', c_char * 7),
        ('BankID', c_char * 4),
        ('BankBranchID', c_char * 5),
        ('BrokerID', c_char * 11),
        ('BrokerBranchID', c_char * 31),
        ('TradeDate', c_char * 9),
        ('TradeTime', c_char * 9),
        ('BankSerial', c_char * 13),
        ('TradingDay', c_char * 9),
        ('PlateSerial', c_int),
        ('LastFragment', c_char),
        ('SessionID', c_int),
        ('CustomerName', c_char * 51),
        ('IdCardType', c_char),
        ('IdentifiedCardNo', c_char * 51),
        ('CustType', c_char),
        ('BankAccount', c_char * 41),
        ('BankPassWord', c_char * 41),
        ('AccountID', c_char * 13),
        ('Password', c_char * 41),
        ('InstallID', c_int),
        ('FutureSerial', c_int),
        ('UserID', c_char * 16),
        ('VerifyCertNoFlag', c_char),
        ('CurrencyID', c_char * 4),
        ('TradeAmount', c_double),
        ('FutureFetchAmount', c_double),
        ('FeePayFlag', c_char),
        ('CustFee', c_double),
        ('BrokerFee', c_double),
        ('Message', c_char * 129),
        ('Digest', c_char * 36),
        ('BankAccType', c_char),
        ('DeviceID', c_char * 3),
        ('BankSecuAccType', c_char),
        ('BrokerIDByBank', c_char * 33),
        ('BankSecuAcc', c_char * 41),
        ('BankPwdFlag', c_char),
        ('SecuPwdFlag', c_char),
        ('OperNo', c_char * 17),
        ('RequestID', c_int),
        ('TID', c_int),
        ('TransferStatus', c_char),
        ('LongCustomerName', c_char * 161)
    ]

class CThostFtdcRspRepealField(Structure):
    _fields_ = [
        ('RepealTimeInterval', c_int),
        ('RepealedTimes', c_int),
        ('BankRepealFlag', c_char),
        ('BrokerRepealFlag', c_char),
        ('PlateRepealSerial', c_int),
        ('BankRepealSerial', c_char * 13),
        ('FutureRepealSerial', c_int),
        ('TradeCode', c_char * 7),
        ('BankID', c_char * 4),
        ('BankBranchID', c_char * 5),
        ('BrokerID', c_char * 11),
        ('BrokerBranchID', c_char * 31),
        ('TradeDate', c_char * 9),
        ('TradeTime', c_char * 9),
        ('BankSerial', c_char * 13),
        ('TradingDay', c_char * 9),
        ('PlateSerial', c_int),
        ('LastFragment', c_char),
        ('SessionID', c_int),
        ('CustomerName', c_char * 51),
        ('IdCardType', c_char),
        ('IdentifiedCardNo', c_char * 51),
        ('CustType', c_char),
        ('BankAccount', c_char * 41),
        ('BankPassWord', c_char * 41),
        ('AccountID', c_char * 13),
        ('Password', c_char * 41),
        ('InstallID', c_int),
        ('FutureSerial', c_int),
        ('UserID', c_char * 16),
        ('VerifyCertNoFlag', c_char),
        ('CurrencyID', c_char * 4),
        ('TradeAmount', c_double),
        ('FutureFetchAmount', c_double),
        ('FeePayFlag', c_char),
        ('CustFee', c_double),
        ('BrokerFee', c_double),
        ('Message', c_char * 129),
        ('Digest', c_char * 36),
        ('BankAccType', c_char),
        ('DeviceID', c_char * 3),
        ('BankSecuAccType', c_char),
        ('BrokerIDByBank', c_char * 33),
        ('BankSecuAcc', c_char * 41),
        ('BankPwdFlag', c_char),
        ('SecuPwdFlag', c_char),
        ('OperNo', c_char * 17),
        ('RequestID', c_int),
        ('TID', c_int),
        ('TransferStatus', c_char),
        ('ErrorID', c_int),
        ('ErrorMsg', c_char * 81),
        ('LongCustomerName', c_char * 161)
    ]

class CThostFtdcReqQueryAccountField(Structure):
    _fields_ = [
        ('TradeCode', c_char * 7),
        ('BankID', c_char * 4),
        ('BankBranchID', c_char * 5),
        ('BrokerID', c_char * 11),
        ('BrokerBranchID', c_char * 31),
        ('TradeDate', c_char * 9),
        ('TradeTime', c_char * 9),
        ('BankSerial', c_char * 13),
        ('TradingDay', c_char * 9),
        ('PlateSerial', c_int),
        ('LastFragment', c_char),
        ('SessionID', c_int),
        ('CustomerName', c_char * 51),
        ('IdCardType', c_char),
        ('IdentifiedCardNo', c_char * 51),
        ('CustType', c_char),
        ('BankAccount', c_char * 41),
        ('BankPassWord', c_char * 41),
        ('AccountID', c_char * 13),
        ('Password', c_char * 41),
        ('FutureSerial', c_int),
        ('InstallID', c_int),
        ('UserID', c_char * 16),
        ('VerifyCertNoFlag', c_char),
        ('CurrencyID', c_char * 4),
        ('Digest', c_char * 36),
        ('BankAccType', c_char),
        ('DeviceID', c_char * 3),
        ('BankSecuAccType', c_char),
        ('BrokerIDByBank', c_char * 33),
        ('BankSecuAcc', c_char * 41),
        ('BankPwdFlag', c_char),
        ('SecuPwdFlag', c_char),
        ('OperNo', c_char * 17),
        ('RequestID', c_int),
        ('TID', c_int),
        ('LongCustomerName', c_char * 161)
    ]

class CThostFtdcRspQueryAccountField(Structure):
    _fields_ = [
        ('TradeCode', c_char * 7),
        ('BankID', c_char * 4),
        ('BankBranchID', c_char * 5),
        ('BrokerID', c_char * 11),
        ('BrokerBranchID', c_char * 31),
        ('TradeDate', c_char * 9),
        ('TradeTime', c_char * 9),
        ('BankSerial', c_char * 13),
        ('TradingDay', c_char * 9),
        ('PlateSerial', c_int),
        ('LastFragment', c_char),
        ('SessionID', c_int),
        ('CustomerName', c_char * 51),
        ('IdCardType', c_char),
        ('IdentifiedCardNo', c_char * 51),
        ('CustType', c_char),
        ('BankAccount', c_char * 41),
        ('BankPassWord', c_char * 41),
        ('AccountID', c_char * 13),
        ('Password', c_char * 41),
        ('FutureSerial', c_int),
        ('InstallID', c_int),
        ('UserID', c_char * 16),
        ('VerifyCertNoFlag', c_char),
        ('CurrencyID', c_char * 4),
        ('Digest', c_char * 36),
        ('BankAccType', c_char),
        ('DeviceID', c_char * 3),
        ('BankSecuAccType', c_char),
        ('BrokerIDByBank', c_char * 33),
        ('BankSecuAcc', c_char * 41),
        ('BankPwdFlag', c_char),
        ('SecuPwdFlag', c_char),
        ('OperNo', c_char * 17),
        ('RequestID', c_int),
        ('TID', c_int),
        ('BankUseAmount', c_double),
        ('BankFetchAmount', c_double),
        ('LongCustomerName', c_char * 161)
    ]

class CThostFtdcFutureSignIOField(Structure):
    _fields_ = [
        ('TradeCode', c_char * 7),
        ('BankID', c_char * 4),
        ('BankBranchID', c_char * 5),
        ('BrokerID', c_char * 11),
        ('BrokerBranchID', c_char * 31),
        ('TradeDate', c_char * 9),
        ('TradeTime', c_char * 9),
        ('BankSerial', c_char * 13),
        ('TradingDay', c_char * 9),
        ('PlateSerial', c_int),
        ('LastFragment', c_char),
        ('SessionID', c_int),
        ('InstallID', c_int),
        ('UserID', c_char * 16),
        ('Digest', c_char * 36),
        ('CurrencyID', c_char * 4),
        ('DeviceID', c_char * 3),
        ('BrokerIDByBank', c_char * 33),
        ('OperNo', c_char * 17),
        ('RequestID', c_int),
        ('TID', c_int)
    ]

class CThostFtdcRspFutureSignInField(Structure):
    _fields_ = [
        ('TradeCode', c_char * 7),
        ('BankID', c_char * 4),
        ('BankBranchID', c_char * 5),
        ('BrokerID', c_char * 11),
        ('BrokerBranchID', c_char * 31),
        ('TradeDate', c_char * 9),
        ('TradeTime', c_char * 9),
        ('BankSerial', c_char * 13),
        ('TradingDay', c_char * 9),
        ('PlateSerial', c_int),
        ('LastFragment', c_char),
        ('SessionID', c_int),
        ('InstallID', c_int),
        ('UserID', c_char * 16),
        ('Digest', c_char * 36),
        ('CurrencyID', c_char * 4),
        ('DeviceID', c_char * 3),
        ('BrokerIDByBank', c_char * 33),
        ('OperNo', c_char * 17),
        ('RequestID', c_int),
        ('TID', c_int),
        ('ErrorID', c_int),
        ('ErrorMsg', c_char * 81),
        ('PinKey', c_char * 129),
        ('MacKey', c_char * 129)
    ]

class CThostFtdcReqFutureSignOutField(Structure):
    _fields_ = [
        ('TradeCode', c_char * 7),
        ('BankID', c_char * 4),
        ('BankBranchID', c_char * 5),
        ('BrokerID', c_char * 11),
        ('BrokerBranchID', c_char * 31),
        ('TradeDate', c_char * 9),
        ('TradeTime', c_char * 9),
        ('BankSerial', c_char * 13),
        ('TradingDay', c_char * 9),
        ('PlateSerial', c_int),
        ('LastFragment', c_char),
        ('SessionID', c_int),
        ('InstallID', c_int),
        ('UserID', c_char * 16),
        ('Digest', c_char * 36),
        ('CurrencyID', c_char * 4),
        ('DeviceID', c_char * 3),
        ('BrokerIDByBank', c_char * 33),
        ('OperNo', c_char * 17),
        ('RequestID', c_int),
        ('TID', c_int)
    ]

class CThostFtdcRspFutureSignOutField(Structure):
    _fields_ = [
        ('TradeCode', c_char * 7),
        ('BankID', c_char * 4),
        ('BankBranchID', c_char * 5),
        ('BrokerID', c_char * 11),
        ('BrokerBranchID', c_char * 31),
        ('TradeDate', c_char * 9),
        ('TradeTime', c_char * 9),
        ('BankSerial', c_char * 13),
        ('TradingDay', c_char * 9),
        ('PlateSerial', c_int),
        ('LastFragment', c_char),
        ('SessionID', c_int),
        ('InstallID', c_int),
        ('UserID', c_char * 16),
        ('Digest', c_char * 36),
        ('CurrencyID', c_char * 4),
        ('DeviceID', c_char * 3),
        ('BrokerIDByBank', c_char * 33),
        ('OperNo', c_char * 17),
        ('RequestID', c_int),
        ('TID', c_int),
        ('ErrorID', c_int),
        ('ErrorMsg', c_char * 81)
    ]

class CThostFtdcReqQueryTradeResultBySerialField(Structure):
    _fields_ = [
        ('TradeCode', c_char * 7),
        ('BankID', c_char * 4),
        ('BankBranchID', c_char * 5),
        ('BrokerID', c_char * 11),
        ('BrokerBranchID', c_char * 31),
        ('TradeDate', c_char * 9),
        ('TradeTime', c_char * 9),
        ('BankSerial', c_char * 13),
        ('TradingDay', c_char * 9),
        ('PlateSerial', c_int),
        ('LastFragment', c_char),
        ('SessionID', c_int),
        ('Reference', c_int),
        ('RefrenceIssureType', c_char),
        ('RefrenceIssure', c_char * 36),
        ('CustomerName', c_char * 51),
        ('IdCardType', c_char),
        ('IdentifiedCardNo', c_char * 51),
        ('CustType', c_char),
        ('BankAccount', c_char * 41),
        ('BankPassWord', c_char * 41),
        ('AccountID', c_char * 13),
        ('Password', c_char * 41),
        ('CurrencyID', c_char * 4),
        ('TradeAmount', c_double),
        ('Digest', c_char * 36),
        ('LongCustomerName', c_char * 161)
    ]

class CThostFtdcRspQueryTradeResultBySerialField(Structure):
    _fields_ = [
        ('TradeCode', c_char * 7),
        ('BankID', c_char * 4),
        ('BankBranchID', c_char * 5),
        ('BrokerID', c_char * 11),
        ('BrokerBranchID', c_char * 31),
        ('TradeDate', c_char * 9),
        ('TradeTime', c_char * 9),
        ('BankSerial', c_char * 13),
        ('TradingDay', c_char * 9),
        ('PlateSerial', c_int),
        ('LastFragment', c_char),
        ('SessionID', c_int),
        ('ErrorID', c_int),
        ('ErrorMsg', c_char * 81),
        ('Reference', c_int),
        ('RefrenceIssureType', c_char),
        ('RefrenceIssure', c_char * 36),
        ('OriginReturnCode', c_char * 7),
        ('OriginDescrInfoForReturnCode', c_char * 129),
        ('BankAccount', c_char * 41),
        ('BankPassWord', c_char * 41),
        ('AccountID', c_char * 13),
        ('Password', c_char * 41),
        ('CurrencyID', c_char * 4),
        ('TradeAmount', c_double),
        ('Digest', c_char * 36)
    ]

class CThostFtdcReqDayEndFileReadyField(Structure):
    _fields_ = [
        ('TradeCode', c_char * 7),
        ('BankID', c_char * 4),
        ('BankBranchID', c_char * 5),
        ('BrokerID', c_char * 11),
        ('BrokerBranchID', c_char * 31),
        ('TradeDate', c_char * 9),
        ('TradeTime', c_char * 9),
        ('BankSerial', c_char * 13),
        ('TradingDay', c_char * 9),
        ('PlateSerial', c_int),
        ('LastFragment', c_char),
        ('SessionID', c_int),
        ('FileBusinessCode', c_char),
        ('Digest', c_char * 36)
    ]

class CThostFtdcReturnResultField(Structure):
    _fields_ = [
        ('ReturnCode', c_char * 7),
        ('DescrInfoForReturnCode', c_char * 129)
    ]

class CThostFtdcVerifyFuturePasswordField(Structure):
    _fields_ = [
        ('TradeCode', c_char * 7),
        ('BankID', c_char * 4),
        ('BankBranchID', c_char * 5),
        ('BrokerID', c_char * 11),
        ('BrokerBranchID', c_char * 31),
        ('TradeDate', c_char * 9),
        ('TradeTime', c_char * 9),
        ('BankSerial', c_char * 13),
        ('TradingDay', c_char * 9),
        ('PlateSerial', c_int),
        ('LastFragment', c_char),
        ('SessionID', c_int),
        ('AccountID', c_char * 13),
        ('Password', c_char * 41),
        ('BankAccount', c_char * 41),
        ('BankPassWord', c_char * 41),
        ('InstallID', c_int),
        ('TID', c_int),
        ('CurrencyID', c_char * 4)
    ]

class CThostFtdcVerifyCustInfoField(Structure):
    _fields_ = [
        ('CustomerName', c_char * 51),
        ('IdCardType', c_char),
        ('IdentifiedCardNo', c_char * 51),
        ('CustType', c_char),
        ('LongCustomerName', c_char * 161)
    ]

class CThostFtdcVerifyFuturePasswordAndCustInfoField(Structure):
    _fields_ = [
        ('CustomerName', c_char * 51),
        ('IdCardType', c_char),
        ('IdentifiedCardNo', c_char * 51),
        ('CustType', c_char),
        ('AccountID', c_char * 13),
        ('Password', c_char * 41),
        ('CurrencyID', c_char * 4),
        ('LongCustomerName', c_char * 161)
    ]

class CThostFtdcDepositResultInformField(Structure):
    _fields_ = [
        ('DepositSeqNo', c_char * 15),
        ('BrokerID', c_char * 11),
        ('InvestorID', c_char * 13),
        ('Deposit', c_double),
        ('RequestID', c_int),
        ('ReturnCode', c_char * 7),
        ('DescrInfoForReturnCode', c_char * 129)
    ]

class CThostFtdcReqSyncKeyField(Structure):
    _fields_ = [
        ('TradeCode', c_char * 7),
        ('BankID', c_char * 4),
        ('BankBranchID', c_char * 5),
        ('BrokerID', c_char * 11),
        ('BrokerBranchID', c_char * 31),
        ('TradeDate', c_char * 9),
        ('TradeTime', c_char * 9),
        ('BankSerial', c_char * 13),
        ('TradingDay', c_char * 9),
        ('PlateSerial', c_int),
        ('LastFragment', c_char),
        ('SessionID', c_int),
        ('InstallID', c_int),
        ('UserID', c_char * 16),
        ('Message', c_char * 129),
        ('DeviceID', c_char * 3),
        ('BrokerIDByBank', c_char * 33),
        ('OperNo', c_char * 17),
        ('RequestID', c_int),
        ('TID', c_int)
    ]

class CThostFtdcRspSyncKeyField(Structure):
    _fields_ = [
        ('TradeCode', c_char * 7),
        ('BankID', c_char * 4),
        ('BankBranchID', c_char * 5),
        ('BrokerID', c_char * 11),
        ('BrokerBranchID', c_char * 31),
        ('TradeDate', c_char * 9),
        ('TradeTime', c_char * 9),
        ('BankSerial', c_char * 13),
        ('TradingDay', c_char * 9),
        ('PlateSerial', c_int),
        ('LastFragment', c_char),
        ('SessionID', c_int),
        ('InstallID', c_int),
        ('UserID', c_char * 16),
        ('Message', c_char * 129),
        ('DeviceID', c_char * 3),
        ('BrokerIDByBank', c_char * 33),
        ('OperNo', c_char * 17),
        ('RequestID', c_int),
        ('TID', c_int),
        ('ErrorID', c_int),
        ('ErrorMsg', c_char * 81)
    ]

class CThostFtdcNotifyQueryAccountField(Structure):
    _fields_ = [
        ('TradeCode', c_char * 7),
        ('BankID', c_char * 4),
        ('BankBranchID', c_char * 5),
        ('BrokerID', c_char * 11),
        ('BrokerBranchID', c_char * 31),
        ('TradeDate', c_char * 9),
        ('TradeTime', c_char * 9),
        ('BankSerial', c_char * 13),
        ('TradingDay', c_char * 9),
        ('PlateSerial', c_int),
        ('LastFragment', c_char),
        ('SessionID', c_int),
        ('CustomerName', c_char * 51),
        ('IdCardType', c_char),
        ('IdentifiedCardNo', c_char * 51),
        ('CustType', c_char),
        ('BankAccount', c_char * 41),
        ('BankPassWord', c_char * 41),
        ('AccountID', c_char * 13),
        ('Password', c_char * 41),
        ('FutureSerial', c_int),
        ('InstallID', c_int),
        ('UserID', c_char * 16),
        ('VerifyCertNoFlag', c_char),
        ('CurrencyID', c_char * 4),
        ('Digest', c_char * 36),
        ('BankAccType', c_char),
        ('DeviceID', c_char * 3),
        ('BankSecuAccType', c_char),
        ('BrokerIDByBank', c_char * 33),
        ('BankSecuAcc', c_char * 41),
        ('BankPwdFlag', c_char),
        ('SecuPwdFlag', c_char),
        ('OperNo', c_char * 17),
        ('RequestID', c_int),
        ('TID', c_int),
        ('BankUseAmount', c_double),
        ('BankFetchAmount', c_double),
        ('ErrorID', c_int),
        ('ErrorMsg', c_char * 81),
        ('LongCustomerName', c_char * 161)
    ]

class CThostFtdcTransferSerialField(Structure):
    _fields_ = [
        ('PlateSerial', c_int),
        ('TradeDate', c_char * 9),
        ('TradingDay', c_char * 9),
        ('TradeTime', c_char * 9),
        ('TradeCode', c_char * 7),
        ('SessionID', c_int),
        ('BankID', c_char * 4),
        ('BankBranchID', c_char * 5),
        ('BankAccType', c_char),
        ('BankAccount', c_char * 41),
        ('BankSerial', c_char * 13),
        ('BrokerID', c_char * 11),
        ('BrokerBranchID', c_char * 31),
        ('FutureAccType', c_char),
        ('AccountID', c_char * 13),
        ('InvestorID', c_char * 13),
        ('FutureSerial', c_int),
        ('IdCardType', c_char),
        ('IdentifiedCardNo', c_char * 51),
        ('CurrencyID', c_char * 4),
        ('TradeAmount', c_double),
        ('CustFee', c_double),
        ('BrokerFee', c_double),
        ('AvailabilityFlag', c_char),
        ('OperatorCode', c_char * 17),
        ('BankNewAccount', c_char * 41),
        ('ErrorID', c_int),
        ('ErrorMsg', c_char * 81)
    ]

class CThostFtdcQryTransferSerialField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('AccountID', c_char * 13),
        ('BankID', c_char * 4),
        ('CurrencyID', c_char * 4)
    ]

class CThostFtdcNotifyFutureSignInField(Structure):
    _fields_ = [
        ('TradeCode', c_char * 7),
        ('BankID', c_char * 4),
        ('BankBranchID', c_char * 5),
        ('BrokerID', c_char * 11),
        ('BrokerBranchID', c_char * 31),
        ('TradeDate', c_char * 9),
        ('TradeTime', c_char * 9),
        ('BankSerial', c_char * 13),
        ('TradingDay', c_char * 9),
        ('PlateSerial', c_int),
        ('LastFragment', c_char),
        ('SessionID', c_int),
        ('InstallID', c_int),
        ('UserID', c_char * 16),
        ('Digest', c_char * 36),
        ('CurrencyID', c_char * 4),
        ('DeviceID', c_char * 3),
        ('BrokerIDByBank', c_char * 33),
        ('OperNo', c_char * 17),
        ('RequestID', c_int),
        ('TID', c_int),
        ('ErrorID', c_int),
        ('ErrorMsg', c_char * 81),
        ('PinKey', c_char * 129),
        ('MacKey', c_char * 129)
    ]

class CThostFtdcNotifyFutureSignOutField(Structure):
    _fields_ = [
        ('TradeCode', c_char * 7),
        ('BankID', c_char * 4),
        ('BankBranchID', c_char * 5),
        ('BrokerID', c_char * 11),
        ('BrokerBranchID', c_char * 31),
        ('TradeDate', c_char * 9),
        ('TradeTime', c_char * 9),
        ('BankSerial', c_char * 13),
        ('TradingDay', c_char * 9),
        ('PlateSerial', c_int),
        ('LastFragment', c_char),
        ('SessionID', c_int),
        ('InstallID', c_int),
        ('UserID', c_char * 16),
        ('Digest', c_char * 36),
        ('CurrencyID', c_char * 4),
        ('DeviceID', c_char * 3),
        ('BrokerIDByBank', c_char * 33),
        ('OperNo', c_char * 17),
        ('RequestID', c_int),
        ('TID', c_int),
        ('ErrorID', c_int),
        ('ErrorMsg', c_char * 81)
    ]

class CThostFtdcNotifySyncKeyField(Structure):
    _fields_ = [
        ('TradeCode', c_char * 7),
        ('BankID', c_char * 4),
        ('BankBranchID', c_char * 5),
        ('BrokerID', c_char * 11),
        ('BrokerBranchID', c_char * 31),
        ('TradeDate', c_char * 9),
        ('TradeTime', c_char * 9),
        ('BankSerial', c_char * 13),
        ('TradingDay', c_char * 9),
        ('PlateSerial', c_int),
        ('LastFragment', c_char),
        ('SessionID', c_int),
        ('InstallID', c_int),
        ('UserID', c_char * 16),
        ('Message', c_char * 129),
        ('DeviceID', c_char * 3),
        ('BrokerIDByBank', c_char * 33),
        ('OperNo', c_char * 17),
        ('RequestID', c_int),
        ('TID', c_int),
        ('ErrorID', c_int),
        ('ErrorMsg', c_char * 81)
    ]

class CThostFtdcQryAccountregisterField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('AccountID', c_char * 13),
        ('BankID', c_char * 4),
        ('BankBranchID', c_char * 5),
        ('CurrencyID', c_char * 4)
    ]

class CThostFtdcAccountregisterField(Structure):
    _fields_ = [
        ('TradeDay', c_char * 9),
        ('BankID', c_char * 4),
        ('BankBranchID', c_char * 5),
        ('BankAccount', c_char * 41),
        ('BrokerID', c_char * 11),
        ('BrokerBranchID', c_char * 31),
        ('AccountID', c_char * 13),
        ('IdCardType', c_char),
        ('IdentifiedCardNo', c_char * 51),
        ('CustomerName', c_char * 51),
        ('CurrencyID', c_char * 4),
        ('OpenOrDestroy', c_char),
        ('RegDate', c_char * 9),
        ('OutDate', c_char * 9),
        ('TID', c_int),
        ('CustType', c_char),
        ('BankAccType', c_char),
        ('LongCustomerName', c_char * 161)
    ]

class CThostFtdcOpenAccountField(Structure):
    _fields_ = [
        ('TradeCode', c_char * 7),
        ('BankID', c_char * 4),
        ('BankBranchID', c_char * 5),
        ('BrokerID', c_char * 11),
        ('BrokerBranchID', c_char * 31),
        ('TradeDate', c_char * 9),
        ('TradeTime', c_char * 9),
        ('BankSerial', c_char * 13),
        ('TradingDay', c_char * 9),
        ('PlateSerial', c_int),
        ('LastFragment', c_char),
        ('SessionID', c_int),
        ('CustomerName', c_char * 51),
        ('IdCardType', c_char),
        ('IdentifiedCardNo', c_char * 51),
        ('Gender', c_char),
        ('CountryCode', c_char * 21),
        ('CustType', c_char),
        ('Address', c_char * 101),
        ('ZipCode', c_char * 7),
        ('Telephone', c_char * 41),
        ('MobilePhone', c_char * 21),
        ('Fax', c_char * 41),
        ('EMail', c_char * 41),
        ('MoneyAccountStatus', c_char),
        ('BankAccount', c_char * 41),
        ('BankPassWord', c_char * 41),
        ('AccountID', c_char * 13),
        ('Password', c_char * 41),
        ('InstallID', c_int),
        ('VerifyCertNoFlag', c_char),
        ('CurrencyID', c_char * 4),
        ('CashExchangeCode', c_char),
        ('Digest', c_char * 36),
        ('BankAccType', c_char),
        ('DeviceID', c_char * 3),
        ('BankSecuAccType', c_char),
        ('BrokerIDByBank', c_char * 33),
        ('BankSecuAcc', c_char * 41),
        ('BankPwdFlag', c_char),
        ('SecuPwdFlag', c_char),
        ('OperNo', c_char * 17),
        ('TID', c_int),
        ('UserID', c_char * 16),
        ('ErrorID', c_int),
        ('ErrorMsg', c_char * 81),
        ('LongCustomerName', c_char * 161)
    ]

class CThostFtdcCancelAccountField(Structure):
    _fields_ = [
        ('TradeCode', c_char * 7),
        ('BankID', c_char * 4),
        ('BankBranchID', c_char * 5),
        ('BrokerID', c_char * 11),
        ('BrokerBranchID', c_char * 31),
        ('TradeDate', c_char * 9),
        ('TradeTime', c_char * 9),
        ('BankSerial', c_char * 13),
        ('TradingDay', c_char * 9),
        ('PlateSerial', c_int),
        ('LastFragment', c_char),
        ('SessionID', c_int),
        ('CustomerName', c_char * 51),
        ('IdCardType', c_char),
        ('IdentifiedCardNo', c_char * 51),
        ('Gender', c_char),
        ('CountryCode', c_char * 21),
        ('CustType', c_char),
        ('Address', c_char * 101),
        ('ZipCode', c_char * 7),
        ('Telephone', c_char * 41),
        ('MobilePhone', c_char * 21),
        ('Fax', c_char * 41),
        ('EMail', c_char * 41),
        ('MoneyAccountStatus', c_char),
        ('BankAccount', c_char * 41),
        ('BankPassWord', c_char * 41),
        ('AccountID', c_char * 13),
        ('Password', c_char * 41),
        ('InstallID', c_int),
        ('VerifyCertNoFlag', c_char),
        ('CurrencyID', c_char * 4),
        ('CashExchangeCode', c_char),
        ('Digest', c_char * 36),
        ('BankAccType', c_char),
        ('DeviceID', c_char * 3),
        ('BankSecuAccType', c_char),
        ('BrokerIDByBank', c_char * 33),
        ('BankSecuAcc', c_char * 41),
        ('BankPwdFlag', c_char),
        ('SecuPwdFlag', c_char),
        ('OperNo', c_char * 17),
        ('TID', c_int),
        ('UserID', c_char * 16),
        ('ErrorID', c_int),
        ('ErrorMsg', c_char * 81),
        ('LongCustomerName', c_char * 161)
    ]

class CThostFtdcChangeAccountField(Structure):
    _fields_ = [
        ('TradeCode', c_char * 7),
        ('BankID', c_char * 4),
        ('BankBranchID', c_char * 5),
        ('BrokerID', c_char * 11),
        ('BrokerBranchID', c_char * 31),
        ('TradeDate', c_char * 9),
        ('TradeTime', c_char * 9),
        ('BankSerial', c_char * 13),
        ('TradingDay', c_char * 9),
        ('PlateSerial', c_int),
        ('LastFragment', c_char),
        ('SessionID', c_int),
        ('CustomerName', c_char * 51),
        ('IdCardType', c_char),
        ('IdentifiedCardNo', c_char * 51),
        ('Gender', c_char),
        ('CountryCode', c_char * 21),
        ('CustType', c_char),
        ('Address', c_char * 101),
        ('ZipCode', c_char * 7),
        ('Telephone', c_char * 41),
        ('MobilePhone', c_char * 21),
        ('Fax', c_char * 41),
        ('EMail', c_char * 41),
        ('MoneyAccountStatus', c_char),
        ('BankAccount', c_char * 41),
        ('BankPassWord', c_char * 41),
        ('NewBankAccount', c_char * 41),
        ('NewBankPassWord', c_char * 41),
        ('AccountID', c_char * 13),
        ('Password', c_char * 41),
        ('BankAccType', c_char),
        ('InstallID', c_int),
        ('VerifyCertNoFlag', c_char),
        ('CurrencyID', c_char * 4),
        ('BrokerIDByBank', c_char * 33),
        ('BankPwdFlag', c_char),
        ('SecuPwdFlag', c_char),
        ('TID', c_int),
        ('Digest', c_char * 36),
        ('ErrorID', c_int),
        ('ErrorMsg', c_char * 81),
        ('LongCustomerName', c_char * 161)
    ]

class CThostFtdcSecAgentACIDMapField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('UserID', c_char * 16),
        ('AccountID', c_char * 13),
        ('CurrencyID', c_char * 4),
        ('BrokerSecAgentID', c_char * 13)
    ]

class CThostFtdcQrySecAgentACIDMapField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('UserID', c_char * 16),
        ('AccountID', c_char * 13),
        ('CurrencyID', c_char * 4)
    ]

class CThostFtdcUserRightsAssignField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('UserID', c_char * 16),
        ('DRIdentityID', c_int)
    ]

class CThostFtdcBrokerUserRightAssignField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('DRIdentityID', c_int),
        ('Tradeable', c_int)
    ]

class CThostFtdcDRTransferField(Structure):
    _fields_ = [
        ('OrigDRIdentityID', c_int),
        ('DestDRIdentityID', c_int),
        ('OrigBrokerID', c_char * 11),
        ('DestBrokerID', c_char * 11)
    ]

class CThostFtdcFensUserInfoField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('UserID', c_char * 16),
        ('LoginMode', c_char)
    ]

class CThostFtdcCurrTransferIdentityField(Structure):
    _fields_ = [
        ('IdentityID', c_int)
    ]

class CThostFtdcLoginForbiddenUserField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('UserID', c_char * 16),
        ('IPAddress', c_char * 16)
    ]

class CThostFtdcQryLoginForbiddenUserField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('UserID', c_char * 16)
    ]

class CThostFtdcMulticastGroupInfoField(Structure):
    _fields_ = [
        ('GroupIP', c_char * 16),
        ('GroupPort', c_int),
        ('SourceIP', c_char * 16)
    ]

class CThostFtdcTradingAccountReserveField(Structure):
    _fields_ = [
        ('BrokerID', c_char * 11),
        ('AccountID', c_char * 13),
        ('Reserve', c_double),
        ('CurrencyID', c_char * 4)
    ]

class CThostFtdcReserveOpenAccountConfirmField(Structure):
    _fields_ = [
        ('TradeCode', c_char * 7),
        ('BankID', c_char * 4),
        ('BankBranchID', c_char * 5),
        ('BrokerID', c_char * 11),
        ('BrokerBranchID', c_char * 31),
        ('TradeDate', c_char * 9),
        ('TradeTime', c_char * 9),
        ('BankSerial', c_char * 13),
        ('TradingDay', c_char * 9),
        ('PlateSerial', c_int),
        ('LastFragment', c_char),
        ('SessionID', c_int),
        ('CustomerName', c_char * 161),
        ('IdCardType', c_char),
        ('IdentifiedCardNo', c_char * 51),
        ('Gender', c_char),
        ('CountryCode', c_char * 21),
        ('CustType', c_char),
        ('Address', c_char * 101),
        ('ZipCode', c_char * 7),
        ('Telephone', c_char * 41),
        ('MobilePhone', c_char * 21),
        ('Fax', c_char * 41),
        ('EMail', c_char * 41),
        ('MoneyAccountStatus', c_char),
        ('BankAccount', c_char * 41),
        ('BankPassWord', c_char * 41),
        ('InstallID', c_int),
        ('VerifyCertNoFlag', c_char),
        ('CurrencyID', c_char * 4),
        ('Digest', c_char * 36),
        ('BankAccType', c_char),
        ('BrokerIDByBank', c_char * 33),
        ('TID', c_int),
        ('AccountID', c_char * 13),
        ('Password', c_char * 41),
        ('BankReserveOpenSeq', c_char * 13),
        ('BookDate', c_char * 9),
        ('BookPsw', c_char * 41),
        ('ErrorID', c_int),
        ('ErrorMsg', c_char * 81)
    ]

class CThostFtdcReserveOpenAccountField(Structure):
    _fields_ = [
        ('TradeCode', c_char * 7),
        ('BankID', c_char * 4),
        ('BankBranchID', c_char * 5),
        ('BrokerID', c_char * 11),
        ('BrokerBranchID', c_char * 31),
        ('TradeDate', c_char * 9),
        ('TradeTime', c_char * 9),
        ('BankSerial', c_char * 13),
        ('TradingDay', c_char * 9),
        ('PlateSerial', c_int),
        ('LastFragment', c_char),
        ('SessionID', c_int),
        ('CustomerName', c_char * 161),
        ('IdCardType', c_char),
        ('IdentifiedCardNo', c_char * 51),
        ('Gender', c_char),
        ('CountryCode', c_char * 21),
        ('CustType', c_char),
        ('Address', c_char * 101),
        ('ZipCode', c_char * 7),
        ('Telephone', c_char * 41),
        ('MobilePhone', c_char * 21),
        ('Fax', c_char * 41),
        ('EMail', c_char * 41),
        ('MoneyAccountStatus', c_char),
        ('BankAccount', c_char * 41),
        ('BankPassWord', c_char * 41),
        ('InstallID', c_int),
        ('VerifyCertNoFlag', c_char),
        ('CurrencyID', c_char * 4),
        ('Digest', c_char * 36),
        ('BankAccType', c_char),
        ('BrokerIDByBank', c_char * 33),
        ('TID', c_int),
        ('ReserveOpenAccStas', c_char),
        ('ErrorID', c_int),
        ('ErrorMsg', c_char * 81)
    ]

