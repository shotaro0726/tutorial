from .models import Post
from django.views.generic import ListView,CreateView,TemplateView,FormView,DetailView
from django.urls import reverse_lazy
from .forms import ClaimForm

"""
トップページ
"""
class PostTopListView(ListView):
    model = Post
    paginate_by = 5

"""
詳細画面
"""
class PostDetailView(DetailView):
    model = Post
    template_name = 'post/post_detail.html'


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

""" 
検索フォーム
"""
class PostSearchView(FormView):
    pass

"""
クレーム欄
"""
class PostClaimView(FormView):
    form_class = ClaimForm
    template_name = 'post/post_form.html'



    


