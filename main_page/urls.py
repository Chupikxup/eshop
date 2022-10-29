from django.urls import path
from . import views


# для отображения фоток


urlpatterns = [
    path('', views.home_page),
    path('products',views.get_all_products),
    path('categories',views.get_all_categories),
    path('product/<int:pk>', views.get_exact_product),
    path('category/<int:bla>',views.get_exact_category),
    path('search', views.search_exact_product),
    path('add_to_cart/<int:pk>', views.add_product_to_user_cart),
    path('user_cart', views.user_cart),
    path('delete_product/<int:pk>',views.delete_exact_user_cart),
    path('checkout', views.checkout_page)

]


