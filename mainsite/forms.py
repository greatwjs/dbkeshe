# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2018-04-26 00:19:44
# @Last Modified by:   Marte
# @Last Modified time: 2018-04-26 21:34:28
from django import forms
class  LoginForm(forms.Form):
    username=forms.CharField(label='姓名',max_length=10)
    password=forms.CharField(label='密码',widget=forms.PasswordInput())
class zhuceForm(forms.Form):
    username=forms.CharField(label='你的姓名',max_length=10)
    password=forms.CharField(label='输入密码',widget=forms.PasswordInput())
    password2=forms.CharField(label='确认密码',widget=forms.PasswordInput())
class baomingForm(forms.Form):
    CLASS=[
    ['1','1'],
    ['2','2'],
    ['3','3'],
    ['4','4'],
    ['5','5'],
    ]
    SPORT=[
    ['长跑','长跑'],
    ['跳高','跳高'],
    ['跳远','跳远'],
    ['短跑','短跑'],
    ]
    playerno=forms.CharField(label='编号',max_length=10)
    playername=forms.CharField(label='姓名',max_length=10)
    class1=forms.ChoiceField(label='班级',choices=CLASS)
    xiangmu=forms.ChoiceField(label='项目',choices=SPORT)

