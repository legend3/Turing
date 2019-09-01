# -*-coding:utf8-*-
from pymongo import MongoClient
import json
from bson import ObjectId
# conn = MongoClient('192.168.0.96', 27017)
# db = conn.audit
# db.authenticate("audit", "123@Audit")


def NumberLong(n_str):
    return int(n_str)



def start_mongo_config(host):
    host1=host.split(":")[0]

    conn = MongoClient(host1, 27017)
    db = conn.audit


    db.authenticate("audit", "123@Audit")

    manualRiskRule = db.manualRiskRule
    apiConfig = db.apiConfig
    userResolveConfig=db.userResolveConfig
    rule_config=[
{
    "_id" : "0931F0CB0B7C816EFFCB8BCF288F9363",
    "enable" : 1,
    "varList" : [
        "$isNewIp$"
    ],
    "ruleName" : "IP异常",
    "objType" : "apiUserDateStat",
    "evalExprs" : [
        {
            "left" : "isNewIp",
            "operation" : "==",
            "right" : "True",
            "rightType" : "Boolean",
            "expression" : "$isNewIp$==True"
        }
    ],
    "_class" : "com.quanzhi.audit_core.model.web.ManualRiskRule",
    "apiList" : [
        "5b7e2d15659cfe27b146b066",
        "5b7e2d15659cfe27b146b067",
        "5b7fb4137f81566e30216f63"
    ],
    "remark" : "",
    "isAllApiList" : 0,
    "riskLevel" : 1,
    "delFlag" : 0,
    "isDefined" : 0,
    "msgExpl" : "1"
}

,
{
    "_id" : "3AD228208017ED54046B643151179362",
    "enable" : 1.0,
    "varList" : [
        "$isLabelVisitMoreOffUserProfile$"
    ],
    "ruleName" : "获取敏感数据量大幅偏移基线",
    "objType" : "apiUserDateStat",
    "evalExprs" : [
        {
            "left" : "isLabelVisitMoreOffUserProfile",
            "operation" : "==",
            "right" : "True",
            "rightType" : "Boolean",
            "expression" : "$isLabelVisitMoreOffUserProfile$==True"
        }
    ],
    "_class" : "com.quanzhi.audit_core.model.web.ManualRiskRule",
    "apiList" : [
        "5b7e2d15659cfe27b146b066",
        "5b7e2d15659cfe27b146b067",
        "5b7fb4137f81566e30216f63"
    ],
    "remark" : "",
    "isAllApiList" : 0,
    "riskLevel" : 1.0,
    "delFlag" : 0.0,
    "isDefined" : 0.0,
    "msgExpl" : "1"
}

,
{
    "_id" : "1D07059AC43C19C2C859F761EAF799A4",
    "enable" : 1.0,
    "varList" : [
        "$reqFreqOffApiProfile$"
    ],
    "ruleName" : "请求频次偏移基线",
    "objType" : "apiUserDateStat",
    "evalExprs" : [
        {
            "left" : "reqFreqOffApiProfile",
            "operation" : "==",
            "right" : "True",
            "rightType" : "Boolean",
            "expression" : "$reqFreqOffApiProfile$==True"
        }
    ],
    "_class" : "com.quanzhi.audit_core.model.web.ManualRiskRule",
    "apiList" : [
        "5b7e2d15659cfe27b146b066",
        "5b7e2d15659cfe27b146b067",
        "5b7fb4137f81566e30216f63"
    ],
    "remark" : "",
    "isAllApiList" : 0,
    "riskLevel" : 1.0,
    "delFlag" : 0.0,
    "isDefined" : 0.0,
    "msgExpl" : "1"
}

,
{
    "_id" : "6BAA3C494FD6EFB4A573FAC2FBE820E4",
    "enable" : 1.0,
    "varList" : [
        "$isAbnormalPerVisit$"
    ],
    "ruleName" : "周期性访问风险",
    "objType" : "apiUserDateStat",
    "evalExprs" : [
        {
            "operation" : "==",
            "right" : "True",
            "expression" : "$isAbnormalPerVisit$==True",
            "rightType" : "Boolean",
            "left" : "isAbnormalPerVisit"
        }
    ],
    "_class" : "com.quanzhi.audit_core.model.web.ManualRiskRule",
    "apiList" : [
        "5b7e2d15659cfe27b146b066",
        "5b7e2d15659cfe27b146b067",
        "5b7fb4137f81566e30216f63"
    ],
    "remark" : "",
    "isAllApiList" : 0,
    "riskLevel" : 1.0,
    "delFlag" : 0.0,
    "isDefined" : 0.0,
    "msgExpl" : "1"
}

,
{
    "_id" : "0FA497343363699C051BB99FDD2B1FFB",
    "enable" : 1.0,
    "varList" : [
        "$isAbnormalUa$"
    ],
    "ruleName" : "请求使用浏览器头异常",
    "objType" : "apiUserDateStat",
    "evalExprs" : [
        {
            "operation" : "==",
            "right" : "True",
            "expression" : "$isAbnormalUa$==True",
            "rightType" : "Boolean",
            "left" : "isAbnormalUa"
        }
    ],
    "_class" : "com.quanzhi.audit_core.model.web.ManualRiskRule",
    "apiList" :[
        "5b7e2d15659cfe27b146b066",
        "5b7e2d15659cfe27b146b067",
        "5b7fb4137f81566e30216f63"
    ],
    "remark" : "",
    "isAllApiList" : 0,
    "riskLevel" : 1.0,
    "delFlag" : 0.0,
    "isDefined" : 0.0,
    "msgExpl" : "1"
}

,
{
    "_id" : "4E147A22085DC574CFC5FC22DF22D90E",
    "enable" : 1.0,
    "varList" : [
        "$reqPathOffApiProfile$"
    ],
    "ruleName" : "请求路径异常",
    "objType" : "apiUserDateStat",
    "evalExprs" : [
        {
            "left" : "reqPathOffApiProfile",
            "operation" : "==",
            "right" : "True",
            "rightType" : "Boolean",
            "expression" : "$reqPathOffApiProfile$==True"
        }
    ],
    "_class" : "com.quanzhi.audit_core.model.web.ManualRiskRule",
    "apiList" : [
        "5b7e2d15659cfe27b146b066",
        "5b7e2d15659cfe27b146b067",
        "5b7fb4137f81566e30216f63"
    ],
    "remark" : "",
    "isAllApiList" : 0,
    "riskLevel" : 1.0,
    "delFlag" : 0.0,
    "isDefined" : 0.0,
    "msgExpl" : "1"
}

,
{
    "_id" : "DD02720D1D8C15A1D8E9A80F0D9E7039",
    "enable" : 1.0,
    "varList" : [
        "$singleReqOffApiProfile$"
    ],
    "ruleName" : "单次请求数据量风险",
    "objType" : "apiUserDateStat",
    "evalExprs" : [
        {
            "left" : "singleReqOffApiProfile",
            "operation" : "==",
            "right" : "True",
            "rightType" : "Boolean",
            "expression" : "$singleReqOffApiProfile$==True"
        }
    ],
    "_class" : "com.quanzhi.audit_core.model.web.ManualRiskRule",
    "apiList" : [
        "5b7e2d15659cfe27b146b066",
        "5b7e2d15659cfe27b146b067",
        "5b7fb4137f81566e30216f63"
    ],
    "remark" : "",
    "isAllApiList" : 0,
    "riskLevel" : 1.0,
    "delFlag" : 0.0,
    "isDefined" : 0.0,
    "msgExpl" : "1"
}

,
{
    "_id" : "C02E317974F44C9C32FB3B603E057214",
    "enable" : 1.0,
    "varList" : [
        "$sameIpMultiAcc$"
    ],
    "ruleName" : "账号混用机器风险",
    "objType" : "apiUserDateStat",
    "evalExprs" : [
        {
            "left" : "sameIpMultiAcc",
            "operation" : "==",
            "right" : "True",
            "rightType" : "Boolean",
            "expression" : "$sameIpMultiAcc$==True"
        }
    ],
    "_class" : "com.quanzhi.audit_core.model.web.ManualRiskRule",
    "apiList" : [
        "5b7e2d15659cfe27b146b066",
        "5b7e2d15659cfe27b146b067",
        "5b7fb4137f81566e30216f63"
    ],
    "remark" : "",
    "isAllApiList" : 0,
    "riskLevel" : 1.0,
    "delFlag" : 1.0,
    "isDefined" : 0.0,
    "msgExpl" : "1"
}

,
{
    "_id" : "6927D0708B05991BB235C4E6B54EFD15",
    "enable" : 1.0,
    "varList" : [
        "$isAbnormalCookie$"
    ],
    "ruleName" : "Cookie盗用",
    "objType" : "apiIpDateStat",
    "evalExprs" : [
        {
            "left" : "isAbnormalCookie",
            "operation" : "==",
            "right" : "True",
            "rightType" : "Boolean",
            "expression" : "$isAbnormalCookie$==True"
        }
    ],
    "_class" : "com.quanzhi.audit_core.model.web.ManualRiskRule",
    "apiList" : [
        "5b7e2d15659cfe27b146b066",
        "5b7e2d15659cfe27b146b067",
        "5b7fb4137f81566e30216f63"
    ],
    "remark" : "",
    "isAllApiList" : 0,
    "riskLevel" : 1.0,
    "delFlag" : 0.0,
    "isDefined" : 0.0,
    "msgExpl" : "1"
}

,
{
    "_id" : "2FBED01EF04644FE34B3512AA145F344",
    "enable" : 1,
    "varList" : [
        "$isAbnormalLoginBaoliPojie$"
    ],
    "ruleName" : "账号暴力破解",
    "objType" : "apiUserDateStat",
    "evalExprs" : [
        {
            "left" : "isAbnormalLoginBaoliPojie",
            "operation" : "==",
            "right" : "True",
            "rightType" : "Boolean",
            "expression" : "$isAbnormalLoginBaoliPojie$==True"
        }
    ],
    "_class" : "com.quanzhi.audit_core.model.web.ManualRiskRule",
    "apiList" : [
        "5b7e2d15659cfe27b146b068"
    ],
    "remark" : "",
    "isAllApiList" : 0,
    "riskLevel" : 1,
    "delFlag" : 0,
    "isDefined" : 0,
    "msgExpl" : "1"
}

,
{
    "_id" : "61BD24DD0D7F9FC099875D403FD00C44",
    "enable" : 1.0,
    "varList" : [
        "$isAbnormalLoginShuaku$"
    ],
    "ruleName" : "刷库",
    "objType" : "apiIpDateStat",
    "evalExprs" : [
        {
            "left" : "isAbnormalLoginShuaku",
            "operation" : "==",
            "right" : "True",
            "rightType" : "Boolean",
            "expression" : "$isAbnormalLoginShuaku$==True"
        }
    ],
    "_class" : "com.quanzhi.audit_core.model.web.ManualRiskRule",
    "apiList" : ["5b7e2d15659cfe27b146b068"],
    "remark" : "",
    "isAllApiList" : 0,
    "riskLevel" : 1.0,
    "delFlag" : 0.0,
    "isDefined" : 0.0,
    "msgExpl" : "1"
}

,
{
    "_id" : "0979DF91FAA7187EDCD1A92A1417A453",
    "enable" : 1.0,
    "varList" : [
        "$reqTimeOffApiProfile$"
    ],
    "ruleName" : "访问时间异常",
    "objType" : "apiUserDateStat",
    "evalExprs" : [
        {
            "left" : "reqTimeOffApiProfile",
            "operation" : "==",
            "right" : "True",
            "rightType" : "Boolean",
            "expression" : "$reqTimeOffApiProfile$==True"
        }
    ],
    "_class" : "com.quanzhi.audit_core.model.web.ManualRiskRule",
    "apiList" : [
        "5b7e2d15659cfe27b146b066",
        "5b7e2d15659cfe27b146b067",
        "5b7fb4137f81566e30216f63"
    ],
    "remark" : "",
    "isAllApiList" : 0,
    "riskLevel" : 1.0,
    "delFlag" : 0.0,
    "isDefined" : 0.0,
    "msgExpl" : "1"
}

,
{
    "_id" : "9829C48166E9D22811C28D9462BD951F",
    "_class" : "com.quanzhi.audit_core.model.web.ManualRiskRule",
    "ruleName" : "账号接口请求次数大幅偏移账号基线",
    "objType" : "apiUserDateStat",
    "riskLevel" : 1,
    "varList" : [
        "$isDateVisitMoreOffUserProfile$"
    ],
    "evalExprs" : [
        {
            "left" : "isDateVisitMoreOffUserProfile",
            "operation" : "==",
            "right" : "True",
            "rightType" : "Boolean",
            "expression" : "$isDateVisitMoreOffUserProfile$==True"
        }
    ],
    "msgExpl" : "1",
    "remark" : "",
    "enable" : 1,
    "isDefined" : 0,
    "delFlag" : 0,
    "apiList" : [
        "5b7e2d15659cfe27b146b066",
        "5b7e2d15659cfe27b146b067",
        "5b7fb4137f81566e30216f63"
    ],
    "isAllApiList" : 0
}]
    api_configs=[{
    "_id" : ObjectId("5b7e2d15659cfe27b146b066"),
        "addTime": NumberLong(1534156634362),
        "apiStatus": 5,
        "describe": "",
        "host": "10.2.30.161",
        "keepRspFlag": 0,
        "labels": [
            "手机号",
            "身份证号码",
            "银行卡号",
            "电子邮箱"
        ],
        "name": "客户数据列表",
        "onlineTime": NumberLong(1535899181766),
        "placeholderFlag": 0,
        "response": [
            {
                "type": "json",
                "when": {},
                "data": [
                    {
                        "path": ".data[:-1].phone",
                        "labels": [
                            "手机号"
                        ],
                        "sourceExtractor": "",
                        "isComment": 0,
                        "pathConfig": {
                            "cut": {},
                            "uncut": {
                                "手机号": 0
                            }
                        },
                        "isExtract": 0
                    },
                    {
                        "path": ".data[:-1].card",
                        "labels": [
                            "银行卡号"
                        ],
                        "sourceExtractor": "",
                        "isComment": 0,
                        "pathConfig": {
                            "cut": {},
                            "uncut": {
                                "银行卡号": 0
                            }
                        },
                        "isExtract": 0
                    },
                    {
                        "path": ".data[:-1].email",
                        "labels": [
                            "电子邮箱"
                        ],
                        "sourceExtractor": "",
                        "isComment": 0,
                        "pathConfig": {
                            "cut": {},
                            "uncut": {
                                "电子邮箱": 0
                            }
                        },
                        "isExtract": 0
                    },
                    {
                        "path": ".data[:-1].pid",
                        "labels": [
                            "身份证号码"
                        ],
                        "sourceExtractor": "",
                        "isComment": 0,
                        "pathConfig": {
                            "cut": {},
                            "uncut": {
                                "身份证号码": 0
                            }
                        },
                        "isExtract": 0
                    }
                ]
            }
        ],
        "sensiApiId": "432ee014ba90a4d81022b18fbe8ab9fa",
        "sensiFlag": 0,
        "updateTime": NumberLong(1535899181766),
        "url": "http://www.cdplatform.com/bss/ncrm/ncustomer/customerListTable/json/getCustomerListData.sdo",
    "userResolveId" : "5b83c8d4bfb1dbfd5d3998c5"
}


,
{
    "_id" : ObjectId("5b7e2d15659cfe27b146b067"),
    "addTime": NumberLong(1534156687232),
    "apiStatus": 5,
    "describe": "",
    "host": "10.2.30.161",
    "keepRspFlag": 0,
    "labels": [
        "手机号",
        "身份证号码",
        "银行卡号",
        "电子邮箱"
    ],
    "name": "客户数据详情",
    "onlineTime": NumberLong(1535898376975),
    "placeholderFlag": 0,
    "response": [
        {
            "type": "json",
            "when": {},
            "data": [
                {
                    "path": ".data.phone",
                    "labels": [
                        "手机号"
                    ],
                    "sourceExtractor": "",
                    "isComment": 0,
                    "pathConfig": {
                        "cut": {},
                        "uncut": {
                            "手机号": 0
                        }
                    },
                    "isExtract": 0
                },
                {
                    "path": ".data.card",
                    "labels": [
                        "银行卡号"
                    ],
                    "sourceExtractor": "",
                    "isComment": 0,
                    "pathConfig": {
                        "cut": {},
                        "uncut": {
                            "银行卡号": 0
                        }
                    },
                    "isExtract": 0
                },
                {
                    "path": ".data.email",
                    "labels": [
                        "电子邮箱"
                    ],
                    "sourceExtractor": "",
                    "isComment": 0,
                    "pathConfig": {
                        "cut": {},
                        "uncut": {
                            "电子邮箱": 0
                        }
                    },
                    "isExtract": 0
                },
                {
                    "path": ".data.pid",
                    "labels": [
                        "身份证号码"
                    ],
                    "sourceExtractor": "",
                    "isComment": 0,
                    "pathConfig": {
                        "cut": {},
                        "uncut": {
                            "身份证号码": 0
                        }
                    }
                }
            ]
        }
    ],
    "sensiApiId": "8cae2bb1f4775bce9344d95f19bb9f3b",
    "sensiFlag": 0,
    "updateTime": NumberLong(1535898376975),
    "url": "http://www.cdplatform.com/bss/ncrm/ncustomer/nPanorama/profiling/json/datas.sdo",
    "userResolveId" : "5b83c901bfb1dbfd5d3998c8"
}
,
{
    "_id" : ObjectId("5b7e2d15659cfe27b146b068"),
    "addTime" : NumberLong(1534157999765),
    "apiStatus" : 5,
    "describe" : "",
    "host" : "10.2.30.161",
    "keepRspFlag" : 0,
    "labels" : [],
    "name" : "登陆接口",
    "onlineTime" : NumberLong(1535363362701),
    "placeholderFlag" : 0,
    "response" : [
        {
            "type" : "json",
            "when" : {},
            "data" : []
        }
    ],
    "sensiApiId" : "",
    "sensiFlag" : 0,
    "updateTime" : NumberLong(1535363362701),
    "url" : "http://www.cdplatform.com/login.do",
    "userResolveId" : "5b83c922bfb1dbfd5d3998cb"
}
,
{
    "_id" : ObjectId("5b7fb4137f81566e30216f63"),
    "addTime" : NumberLong(1535095827521),
    "apiStatus" : 5,
    "describe" : "",
    "host" : "10.2.30.161",
    "keepRspFlag" : 0,
    "labels" : [
        "身份证号码",
        "银行卡号",
        "电子邮箱",
        "护照"
    ],
    "name" : "客户海外消费数据详情",
    "onlineTime" : NumberLong(1535363253019),
    "placeholderFlag" : 0,
    "response" : [
        {
            "type" : "html",
            "when" : {},
            "data" : [
                {
                    "path" : "html>body>.container-narrow>.masthead>.btn-group>.dropdown-menu>li>a",
                    "labels" : [
                        "电子邮箱"
                    ],
                    "sourceExtractor" : "",
                    "isComment" : 0,
                    "pathConfig" : {
                        "cut" : {},
                        "uncut" : {
                            "电子邮箱" : 0
                        }
                    },
                    "isExtract" : 0
                },
                {
                    "path" : "#share-home-modal>.modal-body>p",
                    "labels" : [
                        "身份证号码",
                        "银行卡号",
                        "护照"
                    ],
                    "sourceExtractor" : "",
                    "isComment" : 0,
                    "pathConfig" : {
                        "cut" : {},
                        "uncut" : {
                            "身份证号码" : 0,
                            "银行卡号" : 0,
                            "护照" : 0
                        }
                    },
                    "isExtract" : 0
                }
            ]
        }
    ],
    "sensiApiId" : "274248e70b8a6b8aaa5416f844e0d39c",
    "sensiFlag" : 0,
    "updateTime" : NumberLong(1535363253019),
    "url" : "http://www.cdplatform.com/bss/ncrm/ncustomer/shop/abroad/html/datas.sdo",
    "userResolveId" : "5b83c8b4bfb1dbfd5d3998c0"
}]


    user_info=[{
    "_id" : ObjectId("5b83c8b4bfb1dbfd5d3998c0"),
    "_class" : "com.quanzhi.audit_core.beta131common.model.UserResolveConfig",
    "name" : "自动生成_1535363252933",
    "resolveType" : 1,
    "currentUserNameParser" : {
        "pathLocation" : 2,
        "path" : "$.UserID",
        "pathType" : 1,
        "score" : 99.0,
        "udf" : "",
        "key" : "UserID"
    },
    "requestStatus" : "200",
    "createTime" : NumberLong(1535363252933)
}
,
{
    "_id" : ObjectId("5b83c8d0bfb1dbfd5d3998c4"),
    "_class" : "com.quanzhi.audit_core.beta131common.model.UserResolveConfig",
    "name" : "自动生成_1535363280358",
    "resolveType" : 1,
    "currentUserNameParser" : {
        "pathLocation" : 2,
        "path" : "$.UserID",
        "pathType" : 1,
        "score" : 99.0,
        "udf" : "",
        "key" : "UserID"
    },
    "requestStatus" : "200",
    "createTime" : NumberLong(1535363280358)
}
,
{
    "_id" : ObjectId("5b83c8d4bfb1dbfd5d3998c5"),
    "_class" : "com.quanzhi.audit_core.beta131common.model.UserResolveConfig",
    "name" : "自动生成_1535363284969",
    "resolveType" : 1,
    "currentUserNameParser" : {
        "pathLocation" : 2,
        "path" : "$.UserID",
        "pathType" : 1,
        "score" : 99.0,
        "udf" : "",
        "key" : "UserID"
    },
    "requestStatus" : "200",
    "createTime" : NumberLong(1535363284969)
}
,
{
    "_id" : ObjectId("5b83c901bfb1dbfd5d3998c8"),
    "_class" : "com.quanzhi.audit_core.beta131common.model.UserResolveConfig",
    "name" : "自动生成_1535363329579",
    "resolveType" : 1,
    "currentUserNameParser" : {
        "pathLocation" : 2,
        "path" : "$.UserID",
        "pathType" : 1,
        "score" : 99.0,
        "udf" : "",
        "key" : "UserID"
    },
    "requestStatus" : "200",
    "createTime" : NumberLong(1535363329579)
}
,
{
    "_id" : ObjectId("5b83c922bfb1dbfd5d3998cb"),
    "_class" : "com.quanzhi.audit_core.beta131common.model.UserResolveConfig",
    "name" : "自动生成_1535363362680",
    "resolveType" : 1,
    "currentUserNameParser" : {
        "pathLocation" : 2,
        "path" : "$.UserID",
        "pathType" : 1,
        "score" : 99.0,
        "udf" : "",
        "key" : "UserID"
    },
    "requestStatus" : "200",
    "createTime" : NumberLong(1535363362680)
}]





    for each in api_configs:
        apiConfig.save(each)

    for e in user_info:
        userResolveConfig.save(e)

    # if manualRiskRule:
    #     manualRiskRule.drop()

    # for ea in rule_config:
    #     manualRiskRule.save(ea)












