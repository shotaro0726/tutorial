from .models import Post
from django.views.generic import ListView,CreateView,TemplateView,FormView,DetailView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .forms import ClaimForm, PostForm
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.shortcuts import redirect
from django.urls import reverse
from django.db.models import Q

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
編集
"""
class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'post/post_create_form.html'
    success_url = reverse_lazy('post:post_top')

"""
削除
"""
class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('post:post_top')
    
"""
投稿ページ
"""
class PostCreateFormView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post/post_create_form.html'
    success_url = reverse_lazy('post:post_top')

""" 
検索フォーム
"""
class PostSearchView(ListView):
    model = Post
    paginate_by = 5
    template_name = 'post/post_search_form.html'

    def get_queryset(self):
        queryset = Post.objects.all()
        keyword = self.request.GET.get('keyword')
        if keyword:
            queryset = queryset.filter(Q(name__icontains=keyword) | Q(naiyou__icontains=keyword))
        return queryset

"""
クレーム欄
"""
class PostClaimView(FormView):
    form_class = ClaimForm
    success_url = reverse_lazy('post:post_top')
    template_name = 'post/post_form.html'

    def form_valid(self, form):
        subject = 'クレームが入りました。'
        message = render_to_string('mail/mail.txt',form.cleaned_data,self.request)
        from_email = 'shoutaro0726@gmail.com' #任意のメールアドレス
        recipient_list = ['shoutaro0726@gmail.com'] #任意のメールアドレス
        send_mail(subject, message, from_email, recipient_list)
        return redirect('post:post_top')
    





    


