from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from blogs.models import Blog, Comment
from blogs.forms import BlogForm, CommentForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.db.models import Q 
# Create your views here.

class ListBlog(ListView):

    model = Blog

    def get_queryset(self): # new
        query = self.request.GET.get('search_key')
        if query==None:
            object_list = Blog.objects.all()
        else:
            object_list = Blog.objects.filter(Q(article__icontains=query))
        return object_list

class DetailBlog(LoginRequiredMixin, DetailView, CreateView):

    login_url = '/accounts/user/login/'
    template_name = 'blogs/blog_detail.html'
    model = Blog
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        context = super(DetailBlog, self).get_context_data(**kwargs)
        context['form'] = self.get_form()
        context['comments'] = Comment.objects.filter(blog_id=self.object.id)
        return context

    def form_valid(self, form):
        self.object = self.get_object()
        form.save(self.request.user.username, self.object.id)
        return super(DetailBlog, self).form_valid(form)




class CreatePost(LoginRequiredMixin, CreateView):

    login_url = '/accounts/user/login/'
    form_class = BlogForm
    template_name = 'blogs/blog_form.html'

    
    def form_valid(self, form):
        form.save(self.request.user.username)
        return super(CreatePost, self).form_valid(form)


class EditPost(LoginRequiredMixin, UpdateView):
 
    login_url = '/accounts/user/login/'
    form_class = BlogForm
    template_name = 'blogs/blog_form.html'
    model = Blog

    def form_valid(self, form):
        if form.user_privileges(self.request.user.username):
            return super(EditPost, self).form_valid(form)
        else:
            return super(EditPost, self).form_invalid(form)


class DeletePost(LoginRequiredMixin, DeleteView):
 
    login_url = '/accounts/user/login/'
    model = Blog

    def get_success_url(self):
        return reverse('blogs')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.request.user.username != self.object.author:
            raise PermissionDenied
        return super(DeletePost, self).dispatch(
            request, *args, **kwargs)




class EditComment(LoginRequiredMixin, UpdateView):

    login_url = '/accounts/user/login/'
    form_class = CommentForm
    model = Comment

    def form_valid(self, form):
        if form.user_privileges(self.request.user.username):
            return super(EditComment, self).form_valid(form)
        else:
            return super(EditComment, self).form_invalid(form)




class DeleteComment(LoginRequiredMixin, DeleteView):

    login_url = '/accounts/user/login/'
    model = Comment

    def get_success_url(self):
        self.object = self.get_object()
        return reverse('blog_detail', args=[self.object.blog_id])

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.request.user.username != self.object.author:
            raise PermissionDenied
        return super(DeleteComment, self).dispatch(
            request, *args, **kwargs)


