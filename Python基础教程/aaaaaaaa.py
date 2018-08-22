#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
Created on 20180421    @author: ices
'''
# Function:
#      A. Analyse NE log and return analysed result and detail information
#      B. All result informaion data structure as Json format ,one example as below
#          {
#             "log_integrity_states": 0,      //0,1 ,checking log integrity
#             "analysis_states": "finished",  //finished|error , checking log analysis finished without exception
#             "item_analysed_detail": {"normal_detail_info": {"WDU-00": "WO-BU"}, "abnormal_detail_info": {"WDU-01": "ID-BU"}},  //analysis result detail
#             "item_analysed_result": "abnormal"     //normal|abnormal|unknown analysis result
#           }

import re
import json
import traceback
import sys
import os

# step 1: change ne command & prompt
commandChecked = r"时间"
nePrompt = r"$"  # nokia atca


# nePrompt = r"$|#" # linux

# step 2: analysis logic
def kpiAnalysis(loginfo):
    # print loginfo
    normal = []  # compliance data
    abnormal = []  # unsatisfactory data

    for item in (re.findall(r"\S+ +\S+,\d+,\"(HKCG\d+BHW)/业务模块:模块名=R9\",可信,\d+,(\d+)", loginfo, re.DOTALL)):
        print item,item[1]
        tmp_item_str = '%s' % (item[0])
        if (int(item[1]) >= 0):
            normal.append((tmp_item_str, str(item[1])))
        else:
            abnormal.append((tmp_item_str, str(item[1])))
    return normal, abnormal


# !!! do not change analyse function code
def analyseLogs(*file):
    result_data = {
        'log_integrity_states': 1,  # 0|1: cmd execute state(0 succ)
        'analysis_states': "error",  # normal|abnormal|unknown: analyse result
        'item_analysed_result': "unknown",  # abnormal|abnormal: task checking result
        'item_analysed_detail': {"normal_detail_info": {}, "abnormal_detail_info": {}}
    # ok(normal data)|error(abnormal data)
    }
    correct_data = []
    error_data = []
    try:
        f = open(file[0], "r")
        content = f.read().decode('gbk')
        content = content.encode("utf-8", 'ignore')
        f.close()
        # print 'content= ',content
        # find command has executed
        log = re.search("%s(.+?)%s" % (commandChecked, nePrompt), content, re.S)
        if log:
            result_data['log_integrity_states'] = 0
            correct_data, error_data = kpiAnalysis(log.group(1))
    except Exception as e:
        print e

    # if data&error variable has data, analyse "finished" ,else is "error"
    if (len(error_data) > 0 or len(correct_data) > 0):
        result_data['item_analysed_detail']['normal_detail_info'] = dict(correct_data)
        result_data['item_analysed_detail']['abnormal_detail_info'] = dict(error_data)
        result_data['item_analysed_result'] = "abnormal"
        result_data['analysis_states'] = "finished"
        # if error variable has not data,service "ok"
        if (len(error_data) == 0):
            result_data['item_analysed_result'] = "normal"

    # return json format
    return json.dumps(result_data)


def jmain(*file):
    return analyseLogs(*file)

# step 3: remove below code
# because analysis engine will be auto add this code
if __name__=="__main__":
    print(jmain(r'C:\Users\JETLi\Desktop\111\hainan_python\pmresult_60_201807110700_201807110800_CG-1HuaDan-2JieShouSuDu.csv'))
