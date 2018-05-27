from django.core import serializers
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import HttpResponse
from django.views.generic.edit import FormView
from django.http import JsonResponse

from datetime import datetime

from .forms import OrderForm
from .models import Order, Table


def thanks(request):
    return HttpResponse('Thank You for Your Order!')


class CreateOrder(FormView):
    template_name = 'reservation/form.html'
    form_class = OrderForm
    success_url = '/thanks'

    def get_context_data(self, **kwargs):
        context = super(CreateOrder, self).get_context_data(**kwargs)
        tables = Table.objects.all().order_by('table_id')
        context['orders'], context['tables'] = Order.objects.all(), tables,
        size = [i for i in range(1, 7)]
        context['x_coordinates'], context['y_coordinates'] = size, size
        scheme = [[] for s in range(len(size))]
        for x in context['x_coordinates']:
            for y in context['y_coordinates']:
                flag = 0
                for table in tables:
                    if table.x_coordinate == x and table.y_coordinate == y and flag == 0:
                        scheme[x-1].append(table)
                        flag = 1
                else:
                    if flag != 1:
                        scheme[x-1].append(0)
        context['scheme'] = scheme
        return context

    def form_valid(self, form):
        order = Order.objects.create(
            table_id=form.cleaned_data['table_id'],
            first_name=form.cleaned_data['first_name'],
            last_name=form.cleaned_data['last_name'],
            email=form.cleaned_data['email'],
            date=form.cleaned_data['order_date']
        )
        send_mail('Confirmation',
                  'Your reservation is confirmed!',
                  settings.EMAIL_HOST_USER,
                  [order.email])
        return super(CreateOrder, self).form_valid(form)


def checkdate(request):
    if request.method == 'POST' and request.is_ajax():
        date = datetime.strptime(request.POST.get('date'), '%m/%d/%Y').strftime('%Y-%m-%d')
        all_tables = [t for t in Table.objects.all()]
        reserved_tables = Order.objects.filter(date=date)
        reserved_tables = serializers.serialize('json', reserved_tables)
        all_tables = serializers.serialize('json', all_tables)
        return JsonResponse({'reserved_tables': reserved_tables, 'all_tables': all_tables})



