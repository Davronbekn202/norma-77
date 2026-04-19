from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContactForm, PostForm
from .models import Product, Post
from .utils import is_teacher_or_admin


@permission_required('firstapp.add_product', raise_exception=False)
def product_create(request):
    if not request.user.has_perm('firstapp.add_product'):
        return HttpResponse("Sizda ruxsat yo‘q")

    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        Product.objects.create(name=name, price=price)
        return redirect('success')

    return render(request, 'products.html')

def noproduct(request):
    return render(request,'nopermission')

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})


def success_view(request):
    info = Product.objects.all()
    return render(request, 'success.html',{"forms":info})

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'success.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'posting/post_detail.html', {'post': post})


@login_required
def post_create(request):
    if not is_teacher_or_admin(request.user):
        return redirect('post_list')

    form = PostForm(request.POST or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        return redirect('post_list')

    return render(request, 'posting/post_form.html', {'form': form})


@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.user != post.author and request.user.role != 'admin':
        return redirect('post_list')

    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('post_detail', pk=post.pk)

    return render(request, 'posting/post_form.html', {'form': form})


@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.user != post.author and request.user.role != 'admin':
        return redirect('post_list')

    post.delete()
    return redirect('post_list')