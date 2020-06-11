from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = "store_backend"

urlpatterns = [
    path('', views.login, name='login'),
    path('sign_up/', views.sign_up, name='sign_up'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)