# -*- coding: utf-8 -*-

class BuyGoods(object):


    def __init__(self, budget, goods_price_list):
        '''设置预算, 和物品的价格'''
        self.budget = budget
        # 要买的物品
        self.goods_price_list = goods_price_list

    def process_goods(self):
        self.goods_price_list.pop()

    def analize(self):
        '''处理分析'''
        cost = sum(self.goods_price_list)
        if cost <= self.budget:
            print('购买的物品的相应价格为{0}，可购买的物品总数为{1}'.format(self.goods_price_list, len(self.goods_price_list)))
            
        else:
            cost = self.process_goods()
            self.analize()

def main():
    # 设置预算
    budget = int(input('请输入预算:'))
    # 要买的物品
    goods_price = input('请输入要买物品的价格,用空格分开:')
    goods_price_list = sorted([int(i) for i in goods_price.split()])
    
    # 分析出购买物品的列表
    goods = BuyGoods(budget, goods_price_list)
    goods.analize()


if __name__ == '__main__':
    main()


