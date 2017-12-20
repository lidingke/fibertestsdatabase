from django.contrib import admin
from django import forms

from .models import Instrument,Result,ResultColumns

@admin.register(Instrument)
class InstrumentAdmin(admin.ModelAdmin):
    # date_hierarchy = 'pub_date'
    list_display = ["serialsnumber","instrumenttype"]
    ordering = ['-id']


class ResultForm(forms.ModelForm):

    class Meta:
        model = Result
        exclude = ['owner']

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    # date_hierarchy = 'pub_date'
    search_field = ['owner',]
    list_filter = ['owner','instrument',]
    list_display = ['owner','instrument_number','corediameter','claddiameter','coreroundness','cladroundness','concentricity']

    list_per_page = 10
    ordering = ['-id']

    def instrument_number(self,obj):
        string = "%s" %obj.instrument
        return  string.split(':')[-1]

    instrument_number.short_description = '测试设备'

@admin.register(ResultColumns)
class ResultColumnsAdmin(admin.ModelAdmin):
    # date_hierarchy = 'pub_date'
    list_display = ['name', 'key']