from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.
from django.http import HttpResponse

# Create your views here.
from .models import Comment
from django.db.models import Avg

# form表单
from .form import LoginForm
from django.contrib.auth import authenticate, login


# 影评首页
def movies_short(request):
    ###  从models取数据传给template  ###
    shorts = Comment.objects.all()
    # 评论数量
    counter = Comment.objects.all().count()

    # 平均星级
    # star_value = T1.objects.values('n_star')
    star_avg =f" {Comment.objects.aggregate(Avg('star'))['star__avg']:0.1f} "

    # return render(request, 'douban.html', locals())
    return render(request, 'result.html', locals())


# 短评搜索
def select_short(request):
    if request.method == 'POST':
        name = request.POST.get('short')
        shorts = Comment.objects.filter(content__icontains = name)
    return render(request, 'result.html', locals())


# 登录函数
def login1(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            # 读取表单的返回值
            cd = login_form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user:
                # 登陆用户
                login(request, user)
                return redirect('movies_short')
            else:
                return HttpResponse('用户密码错误')

    # GET
    if request.method == "GET":
        login_form = LoginForm()
        return render(request, 'form.html', {'form': login_form})
