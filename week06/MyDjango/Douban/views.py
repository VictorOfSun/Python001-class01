from django.shortcuts import render

# Create your views here.
from .models import Comment
from django.db.models import Avg

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


def select_short(request):
    if request.method == 'POST':
        name = request.POST.get('short')
        shorts = Comment.objects.filter(content__icontains = name)
    return render(request, 'result.html', locals())


