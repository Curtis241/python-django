from django import forms

from .models import Post, Category

choices = Category.objects.all().values_list('name', 'name')

choice_list = list()
for choice in choices:
    choice_list.append(choice)


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'title_tag', 'author', 'category', 'body']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={"class": "form-control"}),
            'author': forms.Select(attrs={"class": "form-control"}),
            'category': forms.Select(choices=choices, attrs={"class": "form-control"}),
            'body': forms.Textarea(attrs={"class": "form-control"})
        }


class EditForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'title_tag', 'author', 'category', 'body']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={"class": "form-control"}),
            'category': forms.Select(choices=choices, attrs={"class": "form-control"}),
            'body': forms.Textarea(attrs={"class": "form-control"})
        }
