#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests

def getjson():
    return __import__("json").loads(requests.get("http://rdp.unipad.kr/store/getList.php").text)

def getdata():
    data = getjson()
    totalc = data['totalCount']
    packs = list()

    for pack in data['list']:
        packs.append(pack)

    """
    code
    isAutoPlay
    title
    isLED
    producerName
    downloadCount
    """
    ret = list()
    for d in packs:
        ret.append("%-40s | %-10s | %s" % (d['title'], d['downloadCount'], d['producerName']))
    ret.append("totalCount : %s" % totalc)
    return ret

def updatevalue():
	text = ""
	for l in getdata():
		text = text + l + "\n"
	lb.config(text=text, justify="left", font = ('굴림체', 10))


	

from tkinter import *
root=Tk()
lb = Label(root); lb.pack(anchor = "w")
data = getdata()

while(1):
    updatevalue()
    root.update() 
#    __import__("time").sleep(2)
