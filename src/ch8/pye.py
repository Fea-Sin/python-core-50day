#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2020/11/12 4:45 下午
# @Author : FEASIN

"""
扑克游戏

version 0.1
"""

from enum import Enum
import random

class Suite(Enum):
    """花色（枚举）"""
    SPADE, HEART, CLUB, DIAMOND = range(4)

# Python中的枚举是可迭代类型
# for suite in Suite:
#     print(f'{suite}: {suite.value}')

class Card:
    """牌"""
    def __init__(self, suite, face):
        self.suite = suite
        self.face = face

    def __repr__(self):
        suites = '♠♥♣♦'
        faces = ['', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        # 根据牌的花色和点数取到对应的字符
        return f'{suites[self.suite.value]}{faces[self.face]}'

    def __lt__(self, other):
        return self.face < other.face

card1 = Card(Suite.SPADE, 5-1)
card2 = Card(Suite.HEART, 13-1)
# print('黑桃5', card1)
# print('红心k', card2)


class Poker:
    """扑克"""

    def __init__(self):
        self.cards = [Card(suite, face) for suite in Suite for face in range(1, 14)]
        # current 表示发牌位置
        self.current = 0

    def shuffle(self):
        """洗牌"""
        random.shuffle(self.cards)

    def deal(self):
        """发牌"""
        card = self.cards[self.current]
        self.current += 1
        return card

    @property
    def has_next(self):
        """还有没有牌可以发"""
        return self.current < len(self.cards)

# 测试扑克类
poker = Poker()
poker.shuffle()
# print('所有牌面-->', poker.cards)

class Player:
    """玩家"""
    def __init__(self, name):
        self.name = name
        self.poker = []

    def get_one(self, card):
        """摸牌"""
        self.poker.append(card)

    def arrange(self):
        self.poker.sort()
        self.poker.reverse()

    def __repr__(self):
        return f'玩家信息：{self.name}，扑克牌：{self.poker}'

# 测试玩家
play1 = Player('聂卫平')
# print(play1)

players = [Player('东邪'), Player('西毒'), Player('南帝'), Player('北丐')]

# 发牌
for _ in range(13):
    for player in players:
        player.get_one(poker.deal())

for player in players:
    player.arrange()
    print(player, end='\n')





