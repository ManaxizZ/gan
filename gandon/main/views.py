from django.views.generic import ListView, DeleteView
from .models import ClothingItem, Category, Size
from django.db.models import Q


class CatalogView(ListView):
    modeles = ClothingItem 
    template_name = 'main/product/list.html' # Имя шаблона на стороне бекенда
    context_object_name = 'cloting_items' # То как называются предметы (Шаблон для товаров)


    def get_queryset(self):
        queryset = super().get_queryset()
        category_slugs = self.request.GET.getlist('category') # Фильтрация по категориям
        size_names = self.request.GET.getlist('size') # Все значения таблицы размеров
        min_price = self.request.GET.getlist('min_prise') # Ползунки цен для товара (Минемальная цена)
        max_price = self.request.GET.getlist('max_prise') # Ползунки цен для товара (Максимальная цена)
        
        if category_slugs: 
            queryset = queryset.filter(category__slugs__in=category_slugs)

        if size_names # Проверка выбрана ли фильтрация и размеров
            queryset = queryset.filter(
                Q(size__names__in=size_names) & Q(sizes__clothingitemsize__available=True) # Проверка доступен ли размер
            )

            if min_price:
                queryset = queryset.filter(price__gte=min_price)
            if min_price:
                queryset = queryset.filter(price__lte=max_price)
        return queryset
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categores'] = Category.objects.all()
        context['sizes'] = Size.objects.all()
        context['selected_categories'] = self.request.GET.getlist('category')
        context['selected_sizes'] = self.request.GET.getlist('size')
        context['min_price'] = self.request.GET.get('min_price', '') 
        context['max_price'] = self.request.GET.get('max_price', '') 

        return context 
    
    class ClothingItemDetailView(DeleteView)
        model = ClothingItem
        template_name = 'main/product/detail.html'
        context_object_name = 'clothing_item'
        slug_field = 'slug'
        slug_url_kwarg = 'slug'
    
