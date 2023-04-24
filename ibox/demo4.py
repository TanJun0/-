# -*- coding: utf-8 -*-
import base64
import io
import json
import sys
import time
import execjs
import requests
from Crypto.Cipher import AES
import base64
from subprocess import Popen, PIPE
import six
headers = {
    'Accept': '*/*',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
'Cache-Control': 'no-cache',
'Connection': 'keep-alive',
'Content-Type': 'application/octet-stream',
'Host': 'web-001.cloud.servicewechat.com',
'Origin': 'https://www.ibox.art',
'Pragma': 'no-cache',
'Referer': 'https://www.ibox.art/',
'sec-ch-ua': '"Chromium";v="112", "Microsoft Edge";v="112", "Not:A-Brand";v="99"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': "Windows",
'Sec-Fetch-Dest': 'empty',
'Sec-Fetch-Mode': 'cors',
'Sec-Fetch-Site': 'cross-site',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.48'
}


url = 'https://web-001.cloud.servicewechat.com/wxa-qbase/jsoperatewxdata'

data = {
    "appid": "wxb5b2c81edbd4cf69",
    "data": {
        "qbase_api_name": "tcbapi_get_service_info",
        "qbase_req": "{\"client_random\":\"0.6798140972225728_1682272929302\",\"system\":\"\"}",
        "qbase_options": {
            "identityless": True,
            "resourceAppid": "wxb5b2c81edbd4cf69",
            "resourceEnv": "ibox-3gldlr1u1a8322d4",
            "config": {
                "database": {
                    "realtime": {
                        "maxReconnect": 5,
                        "reconnectInterval": 5000,
                        "totalConnectionTimeout": None
                    }
                }
            },
            "appid": "wxb5b2c81edbd4cf69",
            "env": "ibox-3gldlr1u1a8322d4"
        },
        "qbase_meta": {
            "session_id": "1682272929312",
            "sdk_version": "wx-web-sdk/WEBDOMAIN_1.0.0 (1655460325000)",
            "filter_user_info": False
        },
        "cli_req_id": str(int(time.time() * 1000))
    }
}
res = requests.post(url, data=json.dumps(data), headers=headers).json()
res_data = json.loads(res['data'])
token = res_data['token']
i_timestamp = res_data['timestamp']
key = res_data['key']
url = res_data['service_url']
print(url)
page = '1'  #页码
E = {
    "X-WX-ENCRYPTION-VERSION": '2',
    "X-WX-ENCRYPTION-TIMESTAMP": str(i_timestamp),
    "X-WX-COMPRESSION": "snappy",
    "X-WX-USER-TIMEOUT": '30000',
    "X-WX-LIB-BUILD-TS": '1655460325335',      
    "X-WX-RESPONSE-CONTENT-ACCEPT-ENCODING": "PB, JSON",
    "Content-Type": "application/octet-stream",
    "X-WX-REQUEST-CONTENT-ENCODING": "JSON"
}
# data = js.call('get_data', key,page)

call_id = "0.6449158999616627_1682271784120" 
#+ str(int(time.time() * 1000))
urlx='https://web-001.cloud.servicewechat.com/wxa-qbase/report?token='+token
response = requests.post(
    urlx,
    headers=headers,
)
headers.update(E)
def _exec_with_pipe(self, source):
    cmd = self._runtime._binary()

    p = None
    try:
        p = Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=PIPE, cwd=self._cwd, universal_newlines=True, encoding='utf-8')
        input = self._compile(source)
        if six.PY2:
            input = input.encode(sys.getfilesystemencoding())
        stdoutdata, stderrdata = p.communicate(input=input)
        ret = p.wait()
    finally:
        del p

    self._fail_on_non_zero_status(ret, stdoutdata, stderrdata)
    return stdoutdata
# for i in range(10):
execjs.ExternalRuntime.Context._exec_with_pipe = _exec_with_pipe
data = execjs.compile(open('demo\demo4.js','r',encoding='utf-8').read()).call('get_data',key,url,headers)
import base64

data = base64.b64decode(data)
response = requests.post(
    url,
    headers=headers,
    data=data,
).content
# # 将二进制数据转换为 base64 编码格式的字符串
base64_data = base64.b64encode(response).decode('utf-8')
# 将 JSON 字符串打印到控制台，供 JavaScript 使用
data=execjs.compile(open('demo\demo4.js','r',encoding='utf-8').read()).call('decrypt',base64_data,key)
print(data)
