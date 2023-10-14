from django.contrib import admin

from price.models import HallList, Price, HourDelta


class PriceInline(admin.TabularInline):
    model = Price
    extra = 1


class HallAdmin(admin.ModelAdmin):
    inlines = (PriceInline,)



class HoursDeltaInline(admin.TabularInline):
    model = HourDelta
    extra = 1


class PriceAdmin(admin.ModelAdmin):
    inlines = (HoursDeltaInline,)


admin.site.register(HallList, HallAdmin)
admin.site.register(Price, PriceAdmin)
