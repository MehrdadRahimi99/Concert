from django.shortcuts import render
from django.http import HttpResponse
from TicketSales.models import concertmodel

# Create your views here.

def concertListView(request):
    concerts=concertmodel.objects.all()
    return HttpResponse(concerts)