from .models import Post
from django.views.generic import ListView,CreateView,TemplateView
from django.urls import reverse_lazy

"""
トップページ
"""
class PostTopListView(ListView):
    model = Post
    template_name = 'post/post_list.html'
    paginate_by = 5

"""
投稿ページ
"""
class PostFormView(CreateView):
    model = Post
    template_name = 'post/post_form.html'
    fields = ('name','naiyou')
    success_url = reverse_lazy('post_top')

"""
使い方のページ
"""
class PostUseView(TemplateView):
    template_name = 'post/post_use.html'






    


