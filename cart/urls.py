from django.urls import path

from . import views

urlpatterns = (
    path('detail/', views.cart_detail, name='detail'),
    path('add/<int:id>/', views.cart_add, name='add'),
    path('remove/<int:id>/', views.cart_remove, name='remove'),
    path('clear/', views.cart_clear, name='clear'),
)
