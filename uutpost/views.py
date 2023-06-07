from django.shortcuts import render, redirect
from .models import Address
from .forms import AddAddress
from django.http import HttpResponse


def address_list(request):
    addresses = Address.objects.all()
    return render(request, 'uutpost/addresses_list.html', {'adresses': addresses})

# def address_new(request):
#     if request.method == "POST":
#         form = (request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.save()
#             return redirect('post_detail', pk=post.pk)
#     else:
#         form = PostForm()
#         return render(request, 'blog/post_edit.html', {'form': form})
#
#     def post_detail(request):
#         return HttpResponse('cover uploaded')
