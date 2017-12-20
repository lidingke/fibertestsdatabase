from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Instrument,Result,ResultColumns

@admin.register(Instrument)
class InstrumentAdmin(admin.ModelAdmin):
    # date_hierarchy = 'pub_date'
    list_display = ["serialsnumber","instrumenttype"]
    ordering = ['-id']


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    # date_hierarchy = 'pub_date'
    search_field = ['owner',]
    list_filter = ['owner','instrument',]
    list_display = ['owner','instrument','corediameter','claddiameter','coreroundness','cladroundness','concentricity']

    list_per_page = 10
    ordering = ['-id']

@admin.register(ResultColumns)
class ResultColumnsAdmin(admin.ModelAdmin):
    # date_hierarchy = 'pub_date'
    list_display = ['name', 'key']