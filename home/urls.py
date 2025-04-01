from django.contrib import admin
from django.urls import path
from home import views
from django.conf import settings
from django.conf.urls.static import static
# from home.views import upload_file

urlpatterns = [
    path("",views.index, name='home'),
    path("contact",views.contact, name='contact')
    # path("media/",upload_file, name='media')
]

# if settings.DEBUG:
#     urlpatterns+=static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)