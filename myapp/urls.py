from django.urls import path 
from . import views 
app_name = 'myapp' 
urlpatterns = [ path('', views.index1, name='index'),
                path('about/<int:year>/<int:month>/', views.about, name='about'),
                 path('<int:type_no>/', views.detail, name='item_detail'),
                  path('hello-fbv/', views.hello_fbv, name='hello_fbv'),
                   path('hello-cbv/', views.HelloCBV.as_view(), name='hello_cbv'),
                ]