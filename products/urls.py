from django.urls import path
from . import views

urlpatterns = [

    path('add_product', views.AddProduct.as_view(), name="add_product"),
    path('update/<slug:slug>', views.UpdateProduct.as_view(), name="update_product"),
    path('<slug:slug>/delete', views.DeleteProduct.as_view(), name="delete_product"),
    path('', views.product_list, name="products"),
    path('<slug:slug>', views.product_detail, name="detail"),
]
