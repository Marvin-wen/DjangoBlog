import markdown
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ArticlePostForm
from .models import ArticlePost


def article_list(request):
    articles = ArticlePost.objects.all()  # 获取所有的数据对象
    context = {'articles': articles}  # 传递给模板的上下文
    return render(request, "article/list.html", context)  # render函数的作用是结合模板和上下文，并返回渲染后的HttpResponse对象


def article_detail(request, id):
    article = ArticlePost.objects.get(id=id)
    # 将markdown语法渲染成html样式
    article.body = markdown.markdown(article.body,
                                     extensions=[
                                         'markdown.extensions.extra',   # 包含 缩写、表格等常用扩展
                                         'markdown.extensions.codehilite',  # 语法高亮扩展
                                     ])
    context = {'article': article}
    return render(request, "article/detail.html", context)


@login_required(login_url='userprofile:login')
def article_create(request):
    if request.method == "GET":
        article_post_form = ArticlePostForm()
        context = {"article_post_form": article_post_form}
        return render(request, "article/create.html", context)
    else:
        article_post_form = ArticlePostForm(data=request.POST)
        if article_post_form.is_valid():
            new_article = article_post_form.save(commit=False)
            new_article.author = request.user
            new_article.save()
            return redirect("article:article-list")
        else:
            return HttpResponse("表单填写有误，请重新填写！")


def article_delete(request, id):
    if request.method == "GET":
        article = ArticlePost.objects.get(id=id)
        if article.author.id == request.user.id:
            article.delete()
            return redirect("article:article-list")
        else:
            return HttpResponse('你没有权限删除这篇文章！')


def article_update(request, id):
    article = ArticlePost.objects.get(id=id)
    if request.method == "GET":
        context = {"article": article}
        return render(request, "article/update.html", context)
    else:
        article_post_form = ArticlePostForm(data=request.POST)
        if article_post_form.is_valid():
            if article.author.id == request.user.id:
                article.title = request.POST['title']
                article.body = request.POST['body']
                article.save()
                return redirect("article:article-detail", id=id)
            else:
                return HttpResponse('你无权修改这篇文章！')
        else:
            return HttpResponse("表单内容有误，请重新填写！")
