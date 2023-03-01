from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
import random
from cafe.models import Product, Category
from datetime import datetime

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


    js = 'window.alert(this.innerHTML)'

    style = '''
        <style>
            table{
                width: 100%;
                border: 3px green solid;
            }
            td{
                border: 1px gray solid;
                text-align: center;
            }
        </style>
    '''

    product = Product.objects.all()
    table = "<tr><td>Product No</td><td>Product Name</td><td>Product Price</td><td>Product Size</td></tr>"
    for p in product:
        table += f'<tr><td>{p.pid}</td><td onclick={js}>{p.name}</td><td>{p.price}</td><td>{p.size}</td></tr>'

    html = f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
        {style}
    </head>
    <body>
        <table>{table}</table>
    </body>
    </html>
    '''

    return HttpResponse(html)

def coffe7(request):

    js = 'window.alert(this.innerHTML)'

    style = '''
        <style>
            table{
                width: 100%;
                border: 3px green solid;
            }
            td{
                border: 1px gray solid;
                text-align: center;
            }
        </style>
    '''

    category = Category.objects.all()
    table = "<tr><td>Product No</td><td>Product Name</td></tr>"
    for c in category:
        table += f'<tr><td>{c.cid}</td><td onclick={js}>{c.name}</td></tr>'

    html = f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
        {style}
    </head>
    <body>
        <table>{table}</table>
    </body>
    </html>
    '''

    return HttpResponse(html)



def coffe8(request):

    product = Product.objects.all()
    template = get_template('coffee/coffee8.html')
    template = template.render({'product': product})
    return HttpResponse(template)    

def coffe9(request, pid):

    product = Product.objects.get(pid=pid)
    template = get_template('coffee/coffee9.html')
    template = template.render({'product': product})
    return HttpResponse(template)    

def coffe10(request):
    return render(request, 'coffee/coffee10.html')

def coffe11(request):

    coffee = [
        {'image': 'arabica.png', 'name': 'Arabica'},
        {'image': 'liberia.png', 'name': 'Liberia'},
        {'image': 'robusta.png', 'name': 'Robusta'},
        ]
    sec = datetime.now().second
    
    template = get_template('coffee/coffee11.html')
    template = template.render(locals())
    return HttpResponse(template)    
