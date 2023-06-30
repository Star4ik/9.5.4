from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum
from django.urls import reverse


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    rate = models.IntegerField(default=0)

    def update_rating(self):
        author_rate_posts = Post.objects.filter(author=self).aggregate(Sum('rate'))['rate__sum'] * 3
        author_rate_comments = Comment.objects.filter(user=self.user).aggregate(Sum('rate'))['rate__sum']
        all_rate_comments = Comment.objects.filter(post__author__user=self.user).aggregate(Sum('rate'))['rate__sum']

        self.rate = author_rate_posts + author_rate_comments + all_rate_comments
        self.save()

    def __str__(self) -> str:
        return f'{self.user}'


class Category(models.Model):
    category_name = models.CharField(max_length=255, unique=True)


class Post(models.Model):
    article = "A"
    new = "N"

    CHOICES = (
        (article, 'Статья'),
        (new, 'Новость'),
    )
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    post_type = models.CharField(max_length=1, choices=CHOICES, default=article)
    time = models.DateTimeField(auto_now_add=True)
    post_category = models.ManyToManyField(Category, through="PostCategory")
    header = models.CharField(max_length=55)
    text = models.CharField(max_length=1024)
    rate = models.IntegerField(default=0)

    def like(self):
        self.rate += 1
        self.save()

    def dislike(self):
        self.rate -= 1
        self.save()

    def preview(self):
        preview_text = self.text
        return preview_text[0:125] + '...' if len(self.text) > 125 else self.text

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

    def __str__(self):
        return self.header.title()


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    time = models.DateTimeField(auto_now_add=True)
    rate = models.IntegerField(default=0)

    def like(self):
        self.rate += 1
        self.save()

    def dislike(self):
        self.rate -= 1
        self.save()
