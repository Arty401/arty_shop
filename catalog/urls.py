from django.urls import path

from . import views

app_name = 'catalog'

urlpatterns = (
    path('', views.LaptopListView.as_view(), name='list'),
    path('catalog/filter/', views.FilterProductView.as_view(), name='by_category'),
    path('catalog/detail/<int:id>/<slug:url>/', views.LaptopDetailView.as_view(), name='detail'),
)
