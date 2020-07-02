from django.views.generic import ListView, DetailView, View, TemplateView

from product import models


class Categories:
    def get_categories(self):
        return models.Category.objects.all()

    extra_context = {
        'cores': models.LaptopCore.objects.all(),
        'colors': models.LaptopColor.objects.all(),
        'diagonals': models.LaptopScreenDiagonal.objects.all(),
        'refresh_rates': models.LaptopRefreshRate.objects.all(),
        'oss': models.LaptopOS.objects.all(),
        'rams': models.LaptopRAM.objects.all(),
        'ram_types': models.LaptopRAMType.objects.all(),
        'storages': models.LaptopStorage.objects.all(),
        'storage_sizes': models.LaptopStorageSize.objects.all(),
        'storage_types': models.LaptopStorageType.objects.all()
    }


class MainPageView(Categories, TemplateView):
    template_name = 'layout/basic.html'


class LaptopListView(Categories, ListView):
    model = models.Laptop
    template_name = 'catalog/product_list.html'
    context_object_name = 'laptops'
    queryset = models.Laptop.objects.filter(available=True)


class FilterProductView(Categories, ListView):
    template_name = 'catalog/product_list.html'
    context_object_name = 'laptops'

    def get_queryset(self):
        get = self.request.GET
        queryset = models.Laptop.objects.all()
        if 'ram' in get:
            queryset = queryset.filter(ram__name__in=get.getlist('ram'))
        if 'refresh_rate' in get:
            queryset = queryset.filter(refresh_rate__value__in=get.getlist('refresh_rate'))
        if 'diagonal' in get:
            queryset = queryset.filter(diagonal__value__in=get.getlist('diagonal'))
        if 'os' in get:
            queryset = queryset.filter(os__name__in=get.getlist('os'))
        if 'core' in get:
            queryset = queryset.filter(core__name__in=get.getlist('core'))
        return queryset


class LaptopDetailView(Categories, DetailView):
    model = models.Laptop
    template_name = 'catalog/product_detail.html'
    slug_field = 'url'
    slug_url_kwarg = 'url'
