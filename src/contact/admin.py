from django.contrib import admin
from contact import models as con_model

# class StreetInline(admin.TabularInline):
#     model = con_model.Street
#     extra = 1
#
# class PhoneInline(admin.TabularInline):
#     model = con_model.Phone
#     extra = 1
#
# class LinkInline(admin.TabularInline):
#     model = con_model.Link
#     extra = 1
#
# class ContactAdmin(admin.ModelAdmin):
#     inlines = (StreetInline, PhoneInline, LinkInline)

admin.site.register(con_model.Address)
admin.site.register(con_model.Phone)
admin.site.register(con_model.Link)
admin.site.register(con_model.Contact)
