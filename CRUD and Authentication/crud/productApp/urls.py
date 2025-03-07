from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('record/<int:pk>', views.customer_product, name='record'),
    path('delete_record/<int:pk>', views.delete_product, name='delete_record'),
    path('add_product/', views.add_product, name='add_product'),
    path('update_record/<int:pk>', views.update_product, name='update_record')
]