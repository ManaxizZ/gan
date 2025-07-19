from django.contrib import admin
from .models import Size, Category, \
    ClothingItem, ClothingItemSize


class ClothingItemSizeInline(admin.TabularInline): # Поле для дополнительных размеров
    model = ClothingItemSize
    extra = 4 # Сколько зарание прогруженных форм


    @admin.register(Size)
    class SizeAdmin(admin.ModelAdmin):
        list_display = ('name',) # Задать поля
        search_fields = ('name',) # Задать поля - Поиск по моделям

    @admin.register(Category)
    class CategoryAdmin(admin.ModelAdmin):
        list_display = ('name', 'slug') # Задать поля
        prepopulated_fields = {'slug': ('name',)} # Автозаполнение
        search_fields = ('name',) # Задать поля - Поиск по моделям



@admin.register(ClothingItem)
class ClothingItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 
                    'available', 'price', 'discount',
                    'created_at', 'updated_at')
    list_filter = ('available', 'category',)
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('-created_at',)
    inlines = [ClothingItemSizeInline]