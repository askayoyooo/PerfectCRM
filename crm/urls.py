from django.urls import path
from crm import views

urlpatterns = [
    path('', views.index, name="sales_index"),
    path('student', views.stu_index, name="stu_index"),
    path('customer', views.customer_list, name="customer_list"),

]
