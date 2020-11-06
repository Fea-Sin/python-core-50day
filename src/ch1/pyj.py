#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2020/11/6 5:12 下午
# @Author : FEASIN

"""
花旗骰
通过摇两粒骰子获得点数进行游戏，规则：
玩家第一次摇出7点或11点，玩家胜
玩家第一次摇出2点、3点或12点，庄家胜
玩家如果摇出其他点数则继续
如果玩家摇出7点，庄家胜
如果玩家摇出了第一次摇的点数，玩家胜
其他点数继续，直至分出胜负

version 0.1
"""

# 设定游戏开始时玩家有1000元

from random import randint

money = 1000
while money > 0:
    print(f'你的总资产为：{money}元')
    go_on = False
    num = 0
    # 下注金额必须大于0小于等于玩家总资产
    while True:
        if money < 0:
            break
        debt =int(input('请下注：'))
        if debt < 0:
            break
        # 第一次摇骰子
        first = randint(1, 6) + randint(1, 6)
        num += 1
        print(f'\nSTEP-ONE玩家摇出了{first}点')
        if first == 7 or first == 11:
            money += debt
            print('玩家胜!\n')
            print(f'此时你还有金钱{money}')
        elif first == 2 or first == 3 or first == 12:
            money -= debt
            print('庄家胜!\n')
            print(f'此时你还有金钱{money}')
        else: go_on = True

        # 第一次没有分出胜负
        while go_on:
            go_on = False
            current = randint(1, 6) + randint(1, 6)
            num += 1
            print(f'STEP-TWO玩家摇出了{current}点')
            if current == 7:
                print('庄家胜!\n')
                money -= debt
                print(f'此时你还有金钱{money}')
            elif current == first:
                print('玩家利\n!')
                money += debt
                print(f'此时你还有金钱{money}')
            else:
                go_on = True

print(f'你破产了，游戏结束，一共玩了{num}次')
print(f'最后你负债{money}')






