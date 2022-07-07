from django.db import models

# Create your models here.

from django.db import models #这里引用了一个model 的class
from django.utils import timezone

#此处定义的models.Model，实际上是对models的一个继承
class Post(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title = models.CharField(max_length = 200 ) #定义标题最长长度是200
    text = models.TextField()
    created_date = models.DateTimeField(default = timezone.now)
    published_date = models.DateTimeField(blank = True,null=True)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()
     
    
    def __str__(self):
        return self.title