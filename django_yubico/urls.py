from django.conf.urls import url

from django_yubico.views import login, password

urlpatterns = [
    url(r'^login', login, name='yubico_django_login'),
    url(r'^password', password, name='yubico_django_password'),
]
