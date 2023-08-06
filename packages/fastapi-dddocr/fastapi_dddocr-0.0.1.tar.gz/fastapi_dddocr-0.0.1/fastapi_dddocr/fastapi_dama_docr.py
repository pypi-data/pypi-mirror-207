#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   fastapi_dama.py
@Time    :   2021/10/26 11:33:14
@Author  :   jixn
@Version :   1.0
这是一个见的验证码识别
'''

from starlette.middleware.cors import CORSMiddleware
from fastapi import FastAPI,Request,Query
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
import uvicorn
import os
import base64
import re
import ddddocr


# iptable = db["ip_table"]

app = FastAPI() # 创建 api 对象
# 设置允许访问的域名
origins = ["*"]  # 也可以设置为"*"，即为所有。

# 设置跨域传参
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # 设置允许的origins来源
    allow_credentials=True,
    allow_methods=["*"],  # 设置允许跨域的http方法，比如 get、post、put等。
    allow_headers=["*"])  # 允许跨域的headers，可以用来鉴别来源等作用。


class Item(BaseModel):
    imgbase64 : str
    code_function : str

class CodeFunction(object):
    def code_function1(self,imgbyte):
        print(1)
        ocr = ddddocr.DdddOcr()
        return re.sub('[\u4e00-\u9fa5]', '', ocr.classification(imgbyte))

    def run(self,code_function,imgbase64):
        imgbyte = base64.b64decode(imgbase64)
        res = eval("self."+code_function)(imgbyte)
        r_json = {}
        r_json["data"] = {}
        r_json["data"]["recognition"] = res
        print(r_json)
        return r_json

@app.get("/") # 根路由
def root(request:Request):
    print(request.client.host)
    # iptable.find({})
    return {"武汉": "加油！！！"}

@app.post("/api/dama")
def getproxy(request:Request,_data:Item):
    macip = str(request.client.host)
    print(f"当前ip: {macip}")
    
    _data = jsonable_encoder(_data)
    print(f"_data: {_data}")
    imgbase64 = _data.get("imgbase64")
    code_function =  _data.get("code_function")

    # 进行打码
    item = {}
    if imgbase64:
        if code_function:
            codefun = CodeFunction()
            r_json = codefun.run(code_function,imgbase64)
        else:
            return 'code_function 为空'
        try:
            item["state"] = 1
            item["recognition"] = r_json["data"]["recognition"]
        except Exception as e:
            item["state"] = -1
            item["remark"] = str(e)
            item["response"] = r_json
    else:
        item["state"] = -1
        item["remark"] = '图片为空!!!'
    return item

def run():
    name_app = os.path.basename(__file__)[0:-3]
    uvicorn.run(f'{name_app}:app', host="0.0.0.0", port=12135, reload=True)

if __name__ == "__main__":
    run()
