from django.urls import path

from main_page.api import views

urlpatterns = [
    path('card/', views.CardViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('card/<int:pk>', views.CardViewSet.as_view({'put': 'update'})),
]
