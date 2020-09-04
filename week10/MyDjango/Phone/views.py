from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.
from django.http import HttpResponse

# Create your views here.
from .models import Soda, Phone, PhoneCo
from django.db.models import Avg

# form表单
from .form import LoginForm
from django.contrib.auth import authenticate, login
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# 前十排名手机获取
def get_phone():
    phones = Phone.objects.all().order_by('-id')[:10]
    return phones


def get_pages(request, shorts):
    paginator = Paginator(shorts, 10)  # 每页10条
    page = request.GET.get('page')
    try:
        shorts = paginator.page(page)  # contacts为Page对象！
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        shorts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        shorts = paginator.page(paginator.num_pages)
    return shorts


def phones_index(request):
    phones = Phone.objects.all().order_by('-id')[:10]
    print(phones[0].name)
    return redirect('phones_short', name=phones[0].name)


# 评论
def phones_short(request, name):
    phones = get_phone()

    # 从models取数据传给template
    shorts = PhoneCo.objects.filter(name=name)

    # 方便搜索时候直接在url中加入当前手机名称
    phone_name = name

    # 获取翻页对象
    shorts = get_pages(request, shorts)

    # 评论数量
    counter = PhoneCo.objects.filter(name=name).count()

    # 情感倾向
    sent_avg =f" {PhoneCo.objects.filter(name=name).aggregate(Avg('sentiment'))['sentiment__avg']:0.2f} "

    # 正向数量
    queryset = PhoneCo.objects.filter(name=name).values('sentiment')
    condtions = {'sentiment__gte': 0.5}
    plus = queryset.filter(**condtions).count()

    # 负向数量
    queryset = PhoneCo.objects.filter(name=name).values('sentiment')
    condtions = {'sentiment__lt': 0.5}
    minus = queryset.filter(**condtions).count()

    return render(request, 'result.html', locals())


# 短评搜索
def select_short(request, name):
    phones = get_phone()
    phone_name = name

    if request.method == 'POST':
        if request.POST.get('choice') == 'comment':
            choice = 'comment'
            res = request.POST.get('short')
            shorts = PhoneCo.objects.filter(comment__icontains=res)
        else:
            choice = 'time'
            res = request.POST.get('short')
            shorts = PhoneCo.objects.filter(time__icontains=res)

    else:
        choice = request.GET.get('choice')
        res = request.GET.get('res')
        print(choice)
        print(res)
        if choice == 'comment':
            shorts = PhoneCo.objects.filter(comment__icontains=res)
        else:
            shorts = PhoneCo.objects.filter(time__icontains=res)

    # 获取翻页对象
    shorts = get_pages(request, shorts)

    # 评论数量
    counter = PhoneCo.objects.filter(name=name).count()

    # 情感倾向
    sent_avg = f" {PhoneCo.objects.filter(name=name).aggregate(Avg('sentiment'))['sentiment__avg']:0.2f} "

    # 正向数量
    queryset = PhoneCo.objects.filter(name=name).values('sentiment')
    condtions = {'sentiment__gte': 0.5}
    plus = queryset.filter(**condtions).count()

    # 负向数量
    queryset = PhoneCo.objects.filter(name=name).values('sentiment')
    condtions = {'sentiment__lt': 0.5}
    minus = queryset.filter(**condtions).count()

    return render(request, 'result.html', locals())


# 登录函数
def login1(request):
    if request.method == 'POST':
        phones = get_phone()

        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            # 读取表单的返回值
            cd = login_form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user:
                # 登陆用户
                login(request, user)
                return redirect('phones_short')
            else:
                return HttpResponse('用户密码错误')

    # GET
    if request.method == "GET":
        login_form = LoginForm()
        return render(request, 'form.html', {'form': login_form})
