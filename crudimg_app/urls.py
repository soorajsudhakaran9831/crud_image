from django.urls import path,include
from . import views
urlpatterns = [
     path('',views.add,name='add'),
     path('add_product',views.add_product,name='add_product'),
     path('show_products',views.show_products,name='show_products'),
     path('editpage/<int:pk>',views.editpage,name='editpage'),
     path('edit_products/<int:pk>',views.edit_products,name='edit_products'),
     path('deletepage/<int:pk>',views.deletepage,name='deletepage'),
  ]