# posts/views.py
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post, Group, User
from .forms import PostForm
from django.shortcuts import redirect


@login_required
def index(request):
    post_list = Post.objects.all().order_by('-pub_date')
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    post_list = group.posts.all().order_by('-pub_date')
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'group': group,
        'page_obj': page_obj,
    }
    return render(request, 'posts/group_list.html', context)


def show_base_template(request):
    template = 'base.html'
    return render(request, template)


@login_required
def profile(request, username):
    post_author = get_object_or_404(User, username=username)
    post_list = post_author.posts.all().order_by('-pub_date')
    post_count = post_author.posts.count()
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'username': username,
        'post_count': post_count,
    }
    return render(request, 'posts/profile.html', context)


@login_required
def post_detail(request, post_id):
    this_post = get_object_or_404(Post, id=post_id)
    author_post_count = this_post.author.posts.count()
    context = {
        'this_post': this_post,
        'author_post_count': author_post_count,
    }
    return render(request, 'posts/post_detail.html', context)


@login_required
def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        return redirect('posts:profile', post.author)
    context = {
        'form': form,
        'is_edit': False,
    }
    return render(request, 'posts/create_post.html', context)


@login_required
def post_edit(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    user = request.user
    author = post.author
    if author != user:
        return redirect('posts:post_detail', post_id)
    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        post = form.save(commit=False)
        post.save()
        return redirect('posts:post_detail', post_id)
    context = {
        'form': form,
        'post_id': post_id,
        'is_edit': True,
        'post': post,
    }
    return render(request, 'posts/create_post.html', context)
