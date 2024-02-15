from django.shortcuts import redirect, render
from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import TemplateView,ListView,DetailView,CreateView,DeleteView,UpdateView
from whitebox.forms import CommentCreateForm
from whitebox.models import App, Comment
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.contrib.auth import logout

# Create your views here.
class HelloClass(TemplateView):
    template_name='index2.html'

class WhiteboxList(ListView):
    template_name='whitebox/whitebox_list.html'
    model=App

class WhiteboxDetail(LoginRequiredMixin,DetailView):
    template_name='whitebox/whitebox_detail.html'
    model=App

class WhiteboxCreate(LoginRequiredMixin,CreateView):
    template_name='whitebox/whitebox_create.html'
    model=App
    fields=('title','text','degree')
    success_url=reverse_lazy('whitebox:whitebox-list')

    def form_valid(self,form):
        form.instance.user=self.request.user
        return super().form_valid(form)

class WhiteboxDelete(LoginRequiredMixin,DeleteView):
    template_name='whitebox/whitebox_delete.html'
    model=App
    success_url=reverse_lazy('whitebox:whitebox-list')

    def get_object(self,queryset=None):
        data=super().get_object(queryset)

        if data.user != self.request.user:
            raise PermissionDenied
        return data

class WhiteboxUpdate(LoginRequiredMixin,UpdateView):
    template_name='whitebox/whitebox_update.html'
    model=App
    fields=('title','text','degree')
    success_url=reverse_lazy('whitebox:whitebox-list')

    def get_object(self,queryset=None):
        data=super().get_object(queryset)

        if data.user != self.request.user:
            raise PermissionDenied
        return data

class CommentCreate(CreateView):
    template_name='whitebox/comment_create.html'
    model=Comment
    form_class=CommentCreateForm
    def form_valid(self,form):
        post_pk=self.kwargs['key']
        post=get_object_or_404(App,pk=post_pk)
        comment=form.save(commit=False)
        comment.target=post
        comment.username=self.request.user
        comment.save()
        return redirect('whitebox:whitebox-detail',pk=post_pk)
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['whitebox']=get_object_or_404(App,pk=self.kwargs['key'])
        return context

def WhiteboxView(request):
    return render(request, 'whitebox/WHITEBOX.html')

def Howaito(request):
    return render(request, 'whitebox/howaito.html')

def Rio(request):
    return render(request, 'whitebox/rio.html')

def Aka(request):
    return render(request, 'whitebox/aka.html')

def Tedhi(request):
    return render(request, 'whitebox/teddy.html')

def Coco(request):
    return render(request, 'whitebox/coco.html')

def Wiru(request):
    return render(request, 'whitebox/will.html')
