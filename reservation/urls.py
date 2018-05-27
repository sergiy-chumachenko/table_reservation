from django.conf.urls import url
from .views import CreateOrder, thanks, checkdate

app_name = 'reservation'
urlpatterns = [
    url(r'^ajax/checkdate', checkdate, name='checkdate'),
    url(r'^thanks$', thanks, name='thanks'),
    url(r'^', CreateOrder.as_view(), name='add_order'),

]
