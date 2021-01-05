from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')

    def add_row(self, name):
        if not Category.objects.filter(name=name):
            Category.objects.create(name=name)
            return True

    def load_data(self):
        rows = list()
        rows.append(self.add_row("uncategorized"))
        rows.append(self.add_row("coding"))
        rows.append(self.add_row("sports"))
        rows.append(self.add_row("entertainment"))
        return all(rows)


class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255, default='uncategorized')

    def __str__(self):
        return f"{self.title} | {self.author}"

    def get_absolute_url(self):
        return reverse('article_details', args=(str(self.id)))




