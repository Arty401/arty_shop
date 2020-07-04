from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.LaptopListView.as_view(), name='list'),
    path('catalog/search/', views.SearchProductView.as_view(), name='search'),
    path('catalog/filter/', views.FilterProductView.as_view(), name='by_category'),
    path('catalog/detail/<int:id>/<slug:url>/', views.LaptopDetailView.as_view(), name='detail'),
]
