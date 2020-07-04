from django.contrib import admin

from .models import Category, Laptop, LaptopRAMType, LaptopStorage, LaptopStorageSize, LaptopStorageType, LaptopOS, \
    LaptopRAM, LaptopCore, LaptopColor, LaptopRefreshRate, LaptopScreenDiagonal


@admin.register(Laptop)
class LaptopAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'price', 'available', 'created', 'updated')
    list_filter = ('available', 'created', 'updated')
    list_editable = ('available', 'price')
    prepopulated_fields = {'url': ('title',)}
    fieldsets = (
        (None, {
            'fields': ('title', 'short_description', 'description', 'url', 'price', 'available')
        }),
        ('Характеристики', {
            'fields': ('core', 'ram', 'os', 'storage', 'refresh_rate', 'diagonal', 'color')
        }),
    )


@admin.register(LaptopRAMType)
class LaptopRAMTypeAdmin(admin.ModelAdmin):
    list_display = ('ram_type',)


@admin.register(LaptopStorage)
class LaptopStorageAdmin(admin.ModelAdmin):
    list_display = ('name', 'storage_type', 'storage_size')


@admin.register(LaptopStorageSize)
class LaptopStorageSizeAdmin(admin.ModelAdmin):
    list_display = ('size',)


@admin.register(LaptopStorageType)
class LaptopStorageTypeAdmin(admin.ModelAdmin):
    list_display = ('storage_type',)


@admin.register(LaptopOS)
class LaptopOSAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(LaptopRAM)
class LaptopRAMAdmin(admin.ModelAdmin):
    list_display = ('value', 'ram_type')
    prepopulated_fields = {'name': ('value', 'ram_type')}


@admin.register(LaptopCore)
class LaptopCoreAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(LaptopColor)
class LaptopColorAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(LaptopRefreshRate)
class LaptopRefreshRateAdmin(admin.ModelAdmin):
    list_display = ('value',)


@admin.register(LaptopScreenDiagonal)
class LaptopScreenDiagonalAdmin(admin.ModelAdmin):
    list_display = ('value',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')
    prepopulated_fields = {'url': ('name',)}
