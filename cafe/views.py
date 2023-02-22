from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
import random
from cafe.models import Product

# Create your views here.
def index(request):
    return render(request, 'index.html')

def coffee(request):
    return render(request, 'coffee/coffee.html')

def slogan(request):
    return HttpResponse('在忙也要很你喝一杯咖啡')

def index2(request):
    reponse = HttpResponse()
    reponse.write('<h1>Title</h1>')
    reponse.write('<hr>')
    reponse.write('Hi~')
    reponse.write('<a href="/coffee/">最新消息</a>')
    return reponse


def tea(request):
    return render(request, 'tea/tea.html')

def coffe1(request):
    return render(request, 'coffee/coffee1.html')

def coffe2(request):
    return render(request, 'coffee/coffee2.html')

def coffe3(request):
    return render(request, 'coffee/coffee3.html', {'name': 'coffee', 'price': 5, 'qty': 10})

def coffe4(request):
    title = 'Cherry Caffe'
    item = {
        'name': 'robusta',
        'price': 115,
    }
    return render(request, 'coffee/coffee4.html', locals())

def coffe5(request):

    template = get_template('coffee/coffee5.html')
    randItems = ['a_coffee', 'b_coffee', 'c_coffee']
    template = template.render({'content': random.choice(randItems)})
    return HttpResponse(template)


def coffe6(request):

    product = Product.objects.all()
    table = "<tr><td>Product No</td><td>Product Name</td><td>Product Price</td><td>Product Size</td></tr>"
    for p in product:
        table += f'<tr><td>{p.pid}</td><td>{p.name}</td><td>{p.price}</td><td>{p.size}</td></tr>'

    html = f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    <body>
        <table>{table}</table>
    </body>
    </html>
    '''

    return HttpResponse(html)