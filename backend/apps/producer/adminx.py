#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: liyao
@license: Apache Licence 
@contact: yli@posbao.net
@site: http://www.piowind.com/
@software: PyCharm
@file: adminx.py
@time: 2017/7/4 17:04
"""
import xadmin
from xadmin import views
from producer.models import Result, Instrument

from producer.models import ResultColumns


class ResultSetting(object):
    # enable_themes = True
    # use_bootswatch = True
    search_field = ['owner',]
    list_filter = ['owner','instrument',]
    list_display = ['owner','instrument','corediameter','claddiameter','coreroundness','cladroundness','concentricity']

    list_per_page = 10
    ordering = ['-id']


class InstrumentSetting(object):
    list_display = ["serialsnumber","instrumenttype"]
    ordering = ['-id']



# class GlobalSettings(object):
#     site_title = "慕学生鲜后台"
#     site_footer = "mxshop"
#     # menu_style = "accordion"
#
#
# class VerifyCodeAdmin(object):
#     list_display = ['code', 'mobile', "add_time"]
# class ResultAdmin(object):

class ViewColumnSetting(object):
    list_display = ['name','key']

xadmin.site.register(ResultColumns, ViewColumnSetting)

xadmin.site.register(Result, ResultSetting)
xadmin.site.register(Instrument, InstrumentSetting)

