from django.contrib import admin
from .models import visitor_model, staff_member_model, drink_model, visitor_detail_model, visitor_drink_model

# Register your models here.
admin.site.register(visitor_model)
admin.site.register(staff_member_model)
admin.site.register(drink_model)
admin.site.register(visitor_detail_model)
admin.site.register(visitor_drink_model)
