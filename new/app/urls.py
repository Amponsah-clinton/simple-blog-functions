from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('form/', views.formpage, name='form'),
    path('details', views.details, name='details'),
    path('view/<int:pk>', views.viewpage, name='views'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('update/<int:id>', views.Update, name='update'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
