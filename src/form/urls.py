from django.urls import path

from form.api import views

urlpatterns = [
    path('form/', views.FormViewSet.as_view({'post': 'create', 'get': 'list'})),
    path('dropdown/', views.DropDownViewSet.as_view({'post': 'create', 'get': 'list'}))
]
