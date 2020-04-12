from .models import Post
from django.views.generic import ListView,CreateView,TemplateView,FormView,DetailView
from django.urls import reverse_lazy
from .forms import ClaimForm, PostForm
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.shortcuts import redirect
from django.urls import reverse

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
class PostCreateFormView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post/post_create_form.html'
    success_url = reverse_lazy('post:post_top')

    
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
    success_url = reverse_lazy('post:post_top')
    template_name = 'post/post_form.html'

    def form_valid(self, form):
        subject = 'クレームが入りました。'
        message = render_to_string('mail.txt',form.cleaned_data,self.request)
        from_email = 'shoutaro0726@gmail.com'
        recipient_list = ['shoutaro0726@gmail.com']
        send_mail(subject, message, from_email, recipient_list)
        return redirect('post:post_top')
    





    


