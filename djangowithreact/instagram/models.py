from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Post(models.Model):
    message = models.TextField()
    photo = models.ImageField(blank=True, upload_to='instagram/post')
    is_public = models.BooleanField(default=False, verbose_name='공개 여부')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.message}"

    class Meta:
        ordering = ['-id']

    def message_length(self):
        return f"{len(self.message)} 글자"

# 필드명은 snake case 로 작성
class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               limit_choices_to={'is_public': True})
    post = models.ForeignKey(Post, on_delete=models.CASCADE) # post_id 필드가 생성된다.
    # post = models.ForeignKey('instagram.Post', on_delete=models.CASCADE) # 이 방법은, 다른 모델의 데이터를 가져올때 사용.
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)