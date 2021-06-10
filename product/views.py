from product.models import Product
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.models import User
from .models import Product
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
import face_recognition
import cv2 
import os
from PIL import Image
from .face2 import func

 
# class PostListView(ListView):
#     model = Product
#     template_name = 'product/home.html'

class PostListView(ListView):
    model = Product
    template_name = 'product/home.html'
    context_object_name = 'products'

class PostDetailView(DetailView):
	model = Product


def buy(request, *args, **kwargs):
	# print(kwargs['pk'])
	# print(Product.objects.get(pk = 1))
	x =  kwargs['pk']
	context = {
        'prod': Product.objects.get(pk = kwargs['pk'])
    }

	if request.method == 'POST':
		if func(request.user.profile.image.url):
			messages.success(request, f'ORDER PLACED SUCCESFULLY! THANK YOU')
			return redirect('product-home')
		else:
			messages.error(request, f'FACE MATCHING FAILED. TRY AGAIN')
			return redirect('buy-page', pk = x)
	# else:
	# 	print("GET")

	return render(request, 'product/buy.html', context)

# class buyView(LoginRequiredMixin, DetailView):
# 	model = Product
# 	template_name = 'product/buy.html'

# 	def authenticate




def about(request):
    return render(request, 'product/about.html')