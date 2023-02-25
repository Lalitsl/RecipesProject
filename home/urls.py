

from django.urls import path
from .views import Home
from django.conf import settings
from django.conf.urls.static import static
# from . import views

urlpatterns = [
    path('',Home.as_view(),name="home"),
    # path('',views.home),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
