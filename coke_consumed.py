# -*- coding: utf-8 -*-
#Define resources
_initial_money = 10
_initial_bottle = 0
_initial_top = 0

#Define exchange rate
_rate_money = 2
_rate_bottle = 2
_rate_top = 4

#Define current status
money = _initial_money
bottle = _initial_bottle
top = _initial_top

#Define result
consumed = 0

#Function print process
def processPrint(case):
    if case is 0:
        print "轉換率：\t", "錢(", _rate_money, ")\t", "瓶(", _rate_bottle, ")\t", "蓋(", _rate_top, ")"
        print "初始資源:\t", "錢(", money, ")\t", "瓶(", bottle, ")\t", "蓋(", top, ")\n"
    if case is 1:
        print "錢: ", money, "\t瓶: ", bottle, "\t蓋: ", top, "\t飲左: ", consumed
    if case is 2:
        print "\n結果飲左： ", consumed
    
#Exchange process
def exchangeProcess():
    global money, bottle, top, consumed
    processPrint(0)
    stop = False
    while not stop:
        if money >= _rate_money:
            transfer = money - (money % _rate_money)
            money -= transfer
            bottle += transfer / _rate_money
            top += transfer / _rate_money
            processPrint(1)
        if bottle >= _rate_bottle:
            transfer = bottle - (bottle % _rate_bottle)
            bottle -= transfer
            consumed += transfer            
            bottle += transfer / _rate_bottle
            top += transfer / _rate_bottle
            processPrint(1)
        if top >= _rate_top:
            transfer = top - (top % _rate_top)
            top -= transfer
            bottle += transfer / _rate_top
            top += transfer / _rate_top
            processPrint(1)
        if money < _rate_money and bottle < _rate_bottle and top < _rate_top:
            transfer = bottle
            bottle -= transfer
            consumed += transfer
            processPrint(1)
            stop = True
    processPrint(2)
    
exchangeProcess()
