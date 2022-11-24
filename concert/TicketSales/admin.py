from django.contrib import admin
from TicketSales.models import consertmodel
from TicketSales.models import ticketmodel
from TicketSales.models import locationmodel
from TicketSales.models import profilemodel
from TicketSales.models import timemodel

# Register your models here.

admin.site.register(consertmodel) 
admin.site.register(ticketmodel)
admin.site.register(locationmodel)
admin.site.register(profilemodel)
admin.site.register(timemodel)