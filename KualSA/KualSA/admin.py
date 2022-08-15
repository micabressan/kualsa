from django.contrib import admin
from .models import Sliders, Videos, Novedades

admin.site.register(Sliders)
admin.site.register(Videos)
admin.site.register(Novedades)

admin.site.site_header = 'KualSA'
admin.site.index_title = 'Panel de control de KualSA'
admin.site.site_title = 'KualSA'