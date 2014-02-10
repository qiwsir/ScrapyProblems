#!/usr/bin/env python
#coding:utf-8

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

#题目有关
class ProblemsItem(Item):
    # define the fields for your item here like:
    # name = Field()
    
    #题干
    pro_question = Field(default = 0)
    #选项
    pro_item = Field(default = 0)
    #考点
    pro_check = Field(default = 0)
    #专题/题型
    pro_type = Field(default = 0)
    #分析
    pro_analysis = Field(default = 0)
    #解答
    pro_answer = Field(default = 0)
    #点评
    pro_comment = Field(default = 0)

#章节有关
class SectionsItem(Item):
    #第一级
    sec_chapter1 = Field(default = 0)
    #第二级
    sec_chapter2 = Field(default = 0)
    #第三级
    sec_chapter3 = Field(default = 0)
