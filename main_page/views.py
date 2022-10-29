from django.shortcuts import render , redirect
from django.http import HttpResponse
import  telebot
bot =  telebot.TeleBot('5418418159:AAF8-qcAEiZ1X7w1H1UiWrJ9OpRUPl5c-8c')
from . import models
# Create your views here.
def home_page(request):
    all_categories = models.Category.objects.all()
    return render(request, 'index.html',
                  {'all_categories': all_categories})
# Полчить все товарыти выврд их на front
def get_all_products(request):
    all_products = models.Product.objects.all() #Получить  все

    return render(request,'ind2.html',{
        'all_products': all_products})

def get_all_categories(request):
    all_categories = models.Category.objects.all()
    return render(request, 'index.html',
                  {'all_categories': all_categories})

# Получение конкретного товара
def get_exact_product(request , pk):
    current_product = models.Product.objects.get(id=pk)

    return render(request,'ind3.html', {'current_product': current_product})

def get_exact_category(request, bla):

    current_category = models.Category.objects.get(id=bla)#Пл=олучаем данную категорию

    category_products = models.Product.objects.filter(product_category=current_category)#выводим продукты

    return  render(request, 'ind4.html',)

def search_exact_product(request):
    if request.method == 'POST':
        get_product = request.POST.get('search_product')
        try:
            models.Product.objects.get(product_name=get_product)

            return redirect(f'/product/{get_product}')
        except:
            return redirect('/')

def add_product_to_user_cart(request, pk):
    if request.method == 'POST':
        checker = models.Product.objects.get(id=pk)
        if checker.product_count >= int(request.POST.get('pr_count')):
            models.UserCart.objects.create(user_id=request.user.id,
                                           user_product=checker,
                                           user_product_quantity=int(request.POST.get('pr_count'))).save()

            return redirect('/products')

        else:
            return redirect(f'/product/{checker.product_name}')

def user_cart(request):
    cart= models.UserCart.objects.filter(user_id=request.user.id)
    return render(request,'cart.html',{
        'user_cart': cart
    })

def delete_exact_user_cart(request,pk):
    product_to_delete = models.Product.objects.get(id=pk)

    models.UserCart.objects.filter(user_id=request.user.id, user_product=product_to_delete).delete()

    return redirect('/user_cart')

def checkout_page(request):

    user_cart = models.UserCart.objects.filter(user_id=request.user.id)
    message = 'НОвый заказ:\n'
    itog = 0
    for i in user_cart:
        message += f'{i.user_product.product_name} : {i.user_product_quantity} шт : {round(i.user_product_quantity*i.user_product.product_price)} сум\n'
        itog  += i.user_product_quantity*i.user_product.product_price
    message += f'НА общую сумму в {itog} sum'
    bot.send_message(5003852709, message)
    models.UserCart.objects.filter(user_id=request.user.id).delete()
    return render(request, 'cart.html')
