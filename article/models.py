from django.db import models
from django.utils import timezone


class ArticlePost(models.Model):
    author = models.ForeignKey("userprofile.UserProfile", on_delete=models.CASCADE)  # 文章作者，on_delete用于指定数据删除的方式
    title = models.CharField(max_length=100)  # 文章标题，models.CharField为字符串字段，用于保存较短的字符串
    body = models.TextField()  # 文章正文，TextField用于保存大量文本
    created = models.DateTimeField(default=timezone.now)  # 文章创建时间，default=timezone.now指定在创建数据时默认写入当前的时间
    updated = models.DateTimeField(auto_now=True)  # 文章更新时间，auto_now=True指定每次数据更新时自动写入当前时间

    class Meta:  # 内部类，用于定义元数据
        ordering = ('-created',)  # ordering指定模型返回的数据的排列顺序，'-created' 表明数据应该以文章创建时间倒序排列，负号标识倒序

    def __str__(self):  # 定义当调用对象的 str() 方法时的返回值内容
        return self.title
