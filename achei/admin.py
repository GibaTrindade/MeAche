from django.contrib import admin
from .models import Lugar, Comodo, Compartimento, Objeto, HistoricoTransferencias
# Register your models here.

class CustomHistoricoAdmin(admin.ModelAdmin):
	list_display = ['objeto', 'compartimentoDe', 'compartimentoPara']

class CustomLugarAdmin(admin.ModelAdmin):
	list_display = ['nome', 'descricao', 'autor']

class CustomObjetoAdmin(admin.ModelAdmin):
	list_display = ['nome', 'compartimento', 'descricao', 'autor']


admin.site.register(Lugar, CustomLugarAdmin)
admin.site.register(Comodo)
admin.site.register(Compartimento)
admin.site.register(Objeto, CustomObjetoAdmin)
admin.site.register(HistoricoTransferencias, CustomHistoricoAdmin)