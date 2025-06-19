from django.urls import path
from catalog.apps import CatalogConfig

from catalog.views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView, \
    ContactsView, CategoryListView, CategoryProductsView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('products/create/', ProductCreateView.as_view(), name='product_create'),
    path('products/update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('products/delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('category/', CategoryListView.as_view(), name='category_list'),
    path('category/<slug:category_slug>/', CategoryProductsView.as_view(), name='category_products'),
]
