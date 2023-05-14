from django.urls import path, include

from . import views

app_name = 'api'

urlpatterns = [
    #path('', views.IndexView.as_view()),
    path('categoria', views.CategoriaView.as_view()),
    path('producto', views.ProductoView.as_view()),
    path('categoria/<int:pk>/', views.CategoriaDetailView.as_view()),
    path('producto/<int:pk>/', views.ProductoDetailView.as_view()),
]

# from rest_framework.routers import DefaultRouter
# router = DefaulRouter()
# router.register(r'producto', view.ProductoViewSet, basename='producto')
# path('admin/', include(router.urls)),

