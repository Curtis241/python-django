from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Post, Category
from .forms import PostForm, EditForm


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ["-post_date"]

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        category_names = Category.objects.all()
        context['category_list'] = category_names
        return context

# def CategoryView(request, cats):
#     category_posts = Post.objects.filter(category=cats)
#     return render(request, 'categories.html', {'cats': cats, 'category_posts': category_posts})


class PostCategoryView(ListView):
    model = Post
    template_name = 'categories.html'

    def get_queryset(self):
        category_name = self.kwargs.get('category')
        return Post.objects.filter(category=str(category_name).replace('-', ' '))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostCategoryView, self).get_context_data(**kwargs)
        context['category_name'] = str(self.kwargs.get('category')).replace('-', ' ')
        return context


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'


class AddPostView(CreateView):
    model = Post
    template_name = 'add_post.html'
    form_class = PostForm


class AddCategoryView(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = '__all__'


class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
