#encoding=utf-8
from django.shortcuts import render,redirect
from .models import playinfo,classinfo,User
from .forms import LoginForm,zhuceForm,baomingForm
from django.template.loader import get_template
from datetime import datetime
from django.http import HttpResponse
from django.template import RequestContext
# Create your views here.
def login(request):
    if request.method=='POST':
        login_form=LoginForm(request.POST)
        if login_form.is_valid():      #检查输入是否正确
            login_name=request.POST['username'].strip() #获取用户输入的值
            login_password=request.POST['password']
            try:
               user=User.objects.get(name=login_name)
               if user.password==login_password:
                   response=redirect('/')
                   request.session['username']=user.name   #设置session
                   request.session.set_expiry(0)
                   return redirect('/')
               else:
                    message="密码错误,请检查一次"
            except:
                message="用户不存在,请先注册"
        else:
            message="请检查输入的字段内容"
    else:
        login_form=LoginForm()  #产生一个新的窗体实例

    template=get_template('login.html')
    request_context=RequestContext(request)
    request_context.push(locals())
    html=template.render(request_context)
    return HttpResponse(html)
def logout(request):
    del request.session['username']
    response=redirect('/')
    message='注销成功!'
    return response
def zhuce(request):
    if request.method=='POST':
        zhuce_form=zhuceForm(request.POST)
        if zhuce_form.is_valid():      #检查输入是否正确
                zhuce_name=request.POST['username'].strip() #获取用户输入的值
                zhuce_password=request.POST['password']
                zhuce_password2=request.POST['password2']
                user=User.objects.values('name')
                if zhuce_name in user:
                    message="该用户名已存在"
                else:
                   if zhuce_password==zhuce_password2:
                      User.objects.create(name=zhuce_name,password=zhuce_password,enabled=False)
                      response=redirect('/login')
                      return redirect('/login')
                   else:
                     message="密码不一致,请重新输入"
        else:
            message="请检查输入的字段内容"
    else:
        zhuce_form=zhuceForm()  #产生一个新的窗体实例

    template=get_template('zhuce.html')
    request_context=RequestContext(request)
    request_context.push(locals())
    html=template.render(request_context)
    return HttpResponse(html)

def playif(request,pid=None,del_pass=None):
    if 'username' in request.session:
        username=request.session['username']
        if 'admin' in username:
            template=get_template('index.html')
            list = playinfo.objects.all()
            html=template.render(locals())
            return HttpResponse(html)
        else:
            if request.method=='POST':
                baoming_form=baomingForm(request.POST)
                if baoming_form.is_valid():      #检查输入是否正确
                      baoming_no=baoming_form.cleaned_data['playerno']
                      baoming_name=baoming_form.cleaned_data['playername'].strip() #获取用户输入的值
                      baoming_class=baoming_form.cleaned_data['class1']
                      baoming_xiangmu=baoming_form.cleaned_data['xiangmu']
                      user=playinfo.objects.values('playno')
                      if baoming_no in user:
                           message="该id已存在"
                      else:
                            try:
                              insert=playinfo.objects.create(playno=baoming_no,playname=baoming_name,class1=baoming_class,xiangmu=baoming_xiangmu)
                              insert.save()
                              message="报名成功!"
                            except:
                              message="报名失败!"
                else:
                         message="请检查输入的字段内容"
            else:
                baoming_form=baomingForm()  #产生一个新的窗体实例
            template=get_template('index.html')
            request_context=RequestContext(request)
            request_context.push(locals())
            html=template.render(request_context)
            return HttpResponse(html)
    else:
        return redirect('/login/')
        message="你还未登录,请先登录!"
def luruscore(request):
    if 'username' in request.session:
        username=request.session['username']
    template=get_template('score.html')
    list = playinfo.objects.all().order_by('xiangmu')
    html=template.render(locals())
    return HttpResponse(html)
def tijiao(request):
    if 'username' in request.session:
        username=request.session['username']
    list_0=request.GET.getlist('score')
    template=get_template('score.html')
    list = playinfo.objects.all().order_by('xiangmu')
    i=0
    for var in list:
        playinfo.objects.filter(playno=var.playno).update(mingci=list_0[i])
        i=i+1
    message="update success!"
    html=template.render(locals())
    return HttpResponse(html)
def chaxun(request):
    if 'username' in request.session:
        username=request.session['username']
    template=get_template('chaxun.html')
    html=template.render(locals())
    return HttpResponse(html)
def chaxun1(request):
    if 'username' in request.session:
        username=request.session['username']
    template=get_template('chaxun.html')
    chaxun1=request.GET['chaxun1']
    list=playinfo.objects.filter(playno=chaxun1)
    for var in list:
        message1="该运动员所参加的项目是:"+var.xiangmu.encode("utf-8")+", 该运动员排名:"+var.mingci.encode("utf-8")
    message=message1
    html=template.render(locals())
    return HttpResponse(html)

def chaxun2(request):
    if 'username' in request.session:
        username=request.session['username']
    template=get_template('chaxun.html')
    chaxun2=request.GET['chaxun2']
    obj=playinfo.objects.values('class1').distinct()             #录入classinfo表
    obj1=classinfo.objects.values('class1').distinct()
    count=obj.count()
    for class0 in range(1,count+1):
        list=playinfo.objects.filter(class1=class0)
        score=0
        list2={'class1':str(class0)}
        for var in list:
             if var.mingci=="1":
                 score=score+10;
             elif var.mingci=="2":
                 score=score+5;
             elif var.mingci=="3":
                 score=score+1;
             else:
                 score=score+0;
        if list2 in obj1:
            break
        classinfo.objects.create(class1=class0,score=score)
    list3=classinfo.objects.all().order_by('-score')
    i=0                   #总分排序,返回名次
    for line in list3:
        i=i+1
        if str(line.class1)==chaxun2:
           message2=i
           break
        else:
           continue
    list1=classinfo.objects.filter(class1=chaxun2)
    for score in list1:
        message1=score.score
    message="该班总分为:"+message1.encode("utf-8")+",排名:"+str(message2)
    html=template.render(locals())
    return HttpResponse(html)
def chaxun3(request):
    if 'username' in request.session:
        username=request.session['username']
    template=get_template('chaxun.html')
    chaxun3=request.GET['chaxun3']
    list_4=playinfo.objects.filter(xiangmu=chaxun3).order_by('mingci')
    #message="姓名:"+message0.encode("utf-8")+",名次:"+message1.encode("utf-8")
    html=template.render(locals())
    return HttpResponse(html)
def chaxun4(request):
    if 'username' in request.session:
        username=request.session['username']
    template=get_template('chaxun4.html')
    list=classinfo.objects.all().order_by('-score')
    html=template.render(locals())
    return HttpResponse(html)

