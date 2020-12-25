from . forms import *
from . models import *
from django.shortcuts import render
from django.contrib.auth.models import User as authUser
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.http import HttpResponse,JsonResponse
# from rest_framework import compat
from django.views import View
from django.db.models import Q 
# from rest_framework.response import Response 
# from rest_framework import status 
# from rest_framework.views import APIView
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import json

# @login_required(login_url="/login/")
def home(request):
	form = foodForm(request.POST)
	cate = foodCategory.objects.values()
	attri = foodAttribute.objects.values()
	FoodItemdata = foodItem.objects.values()
	context = {'category':cate,'attribute':attri,'foodItem':FoodItemdata}

	if 'price' in request.GET:
		min_price = request.GET.get('min_price')
		max_price = request.GET.get('max_price')
		FoodItemdata = foodItem.objects.filter(price__range=(min_price, max_price))
		context = {'category':cate,'attribute':attri,'foodItem':FoodItemdata}
		return render(request, 'home.html',context)

	if "searchData" in request.GET:
		search_query = request.GET.get('search', None)
		FoodItemdata = foodItem.objects.filter(Q(item=search_query) | Q(attribute__attribute=search_query) | Q(category__category=search_query))
		context = {'category':cate,'attribute':attri,'foodItem':FoodItemdata}
		return render(request, 'home.html',context)

	if "search" in request.POST:
		foodAttri = request.POST.get("attribute")
		foodCate = request.POST.get("category")
		print("See Data",foodAttri,foodCate)
		if (foodAttri == 'None' and foodCate == 'None'):
			FoodItemdata = foodItem.objects.values('item')
			context = {'foodItem':FoodItemdata,'category':cate,'attribute':attri}
			return render(request, 'home.html',context)
		if (foodAttri == 'None'):
			FoodItemdata = foodItem.objects.filter(category__category=foodCate)
			context = {'foodItem':FoodItemdata,'category':cate,'attribute':attri}
			return render(request, 'home.html',context)
		elif (foodCate == 'None'):
			FoodItemdata = foodItem.objects.filter(attribute__attribute=foodAttri)
			context = {'foodItem':FoodItemdata,'category':cate,'attribute':attri}
			return render(request, 'home.html',context)
		else:
			FoodItemdata = foodItem.objects.filter(attribute__attribute=foodAttri,category__category=foodCate)
			context = {'foodItem':FoodItemdata,'category':cate,'attribute':attri}
			return render(request, 'home.html',context)
	return render(request, 'home.html',context)


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})


# from django.conf import settings 
# from django.core.mail import send_mail
# def home(request):
# 	form = foodForm(request.POST)
# 	data = foodCategory.objects.values()
# 	context = {'data':data,'form':form}
# 	email_from = settings.EMAIL_HOST_USER 
# 	recipient_list = ['milkyrajpoot@gmail.com',]
# 	send_mail('subject', 'body of the message', email_from, recipient_list)
# 	return render(request, 'home.html',context)