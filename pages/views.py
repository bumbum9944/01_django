from django.shortcuts import render
import random
import datetime
# Create your views here.
def index(request):
    return render(request, 'index.html')

def dinner(request):
    menu = ['중식', '한식', '양식']
    pick = random.choice(menu)

    context = {
        'pick': pick,
        'menu': menu,
    }
    return render(request, 'dinner.html', context)

def images(request):
    return render(request, 'images.html')


def greeting(request, name):
    context = {
        'name': name
    }
    return render(request, 'greeting.html', context)

def cube(request, num):
    cubic = num ** 3
    context = {
        'num': num,
        'cubic': cubic,
    }
    return render(request, 'cube.html', context)

def mul(request, num, mu):
    multi = num * mu
    context = {
        'num': num,
        'mu': mu,
        'multi': multi
    }
    return render(request, 'mul.html', context)

def dtl(request):
    menus = ['한식', '중식', '양식', '일식']
    sentences = 'KSSLDKJFOEEOEOEODKSJLSJF;WEIJA;LSDFJWEOJOANVA'
    messages = {
        'apple': '사과',
        'banana': '바나나',
        'peach': '복숭아',
    }
    now = datetime.datetime.now()
    empty = []

    context = {
        'now': now,
        'messages': messages,
        'sentences': sentences,
        'menus': menus,
        'empty': empty,
    }

    return render(request, 'dtl.html', context)

def christmas(request):
    now = datetime.datetime.now()
    nowdate = now.strftime('%m-%d')
    christmas = '12-25'

    context = {
        'nowdate': nowdate,
        'christmas': christmas,
    }

    return render(request, 'christmas.html', context)
    