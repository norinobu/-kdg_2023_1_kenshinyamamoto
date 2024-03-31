from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Syoukai,Article
from .forms import CommentForm  # 追加

class ListSyoukaiView(ListView):
    template_name = 'syoukai/index.html'
    model = Syoukai

class AboutSyoukaiView(ListView):
    template_name = 'syoukai/about.html'
    model = Syoukai

class GallerySyoukaiView(ListView):
    template_name = 'syoukai/gallery.html'
    model = Syoukai

class LinkSyoukaiView(ListView):
    template_name = 'syoukai/link.html'
    model = Syoukai


class CommentSyoukaiView(DetailView):
    model = Syoukai
    template_name = 'syoukai/index.html'  # コメントを表示するためのテンプレートを指定

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()  # コメント作成フォームを渡す
        return context

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            article = self.get_object()
            comment = form.save(commit=False)
            comment.article = article
            comment.save()
            return redirect('syoukai:detail', pk=article.pk)
        else:
            return self.render_to_response(self.get_context_data(form=form))


#class CommentSyoukaiView(ListView):
    #model = Article
 
    # 追加
    #def get_context_data(self, **kwargs):
        #context = super().get_context_data(**kwargs)
        # テンプレートにコメント作成フォームを渡す
        #context['comment_form'] = CommentForm
 
        #return context
 
# 中略
 
#class CommentSyoukaiView(ListView):
    #model = Comment
    #form_class = CommentForm
 
    #格納する値をチェック
    #def form_valid(self, form):
        #form.instance.author = self.request.user
        #article_pk = self.kwargs.get('pk')
        #article = get_object_or_404(Article, pk=article_pk)
 
        #comment = form.save(commit=False)
        #comment.target = article
        #comment.save()
 
        #return redirect('syoukai:detail', pk=article_pk)
# Create your views here.