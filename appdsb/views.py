import csv
import telepot
from django.core.mail import send_mail
from django.db.models.functions import Round
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView

from .models import DSB
from django.views.generic.base import TemplateView
from django.db.models import Max, Min, Avg, Count

# Create your views here.


def home(request):
    tab = DSB.objects.all()
    s = {'tab': tab}
    return render(request, 'acceuil/index.html', s)


def second(request):
    tab = DSB.objects.all()
    temperature = DSB.objects.latest('dt')
    stats = tab.aggregate(max=Max('temp'), min=Min('temp'), avg=Round(Avg('temp'), 3))
    s = {'tab': tab, 'temp': temperature.temp, 'dt': temperature.dt, 'stats': stats}
    return render(request, 'second/TableDesValeur.html', s)



def ds18b20(request):
    tab = DSB.objects.all()
    s = {'tab': tab}
    return render(request, 'second/htmldsb.html', s)


class EditorChartView(TemplateView):
    template_name = 'second/htmldsb.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tab"] = DSB.objects.all()
        return context

def exp_csv(request):
    obj = DSB.objects.all()
    response = HttpResponse('text/csv')
    response['Content-Disposition'] = 'attachment; filename=DHT.csv'
    writer = csv.writer(response)
    writer.writerow(['ID', 'Temp', 'DT'])
    studs = obj.values_list('id', 'temp', 'dt')
    for std in studs:
        writer.writerow(std)
    return response


def dboperation(request):
    temp_count = DSB.objects.all().aggregate(count=Count('temp'))
    temp_max = DSB.objects.all().aggregate(max=Max('temp'))
    temp_min = DSB.objects.all().aggregate(min=Min('temp'))
    temp_avg = DSB.objects.all().aggregate(avg=Avg('temp'))
    return render(request, 'operation.html', {"count": temp_count, "max": temp_max,
                                              "min": temp_min, "avg": temp_avg})


