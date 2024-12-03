from gettext import ngettext
from django.utils.translation import ngettext
from django.contrib import admin, messages


from .form import SmartphoneForm

from .models import Smartphone, Chapter, Book




@admin.register(Smartphone)
class SmartphoneAdmin(admin.ModelAdmin):
    list_display = ['model', 'ram', 'height', 'price', 'status']
    #busqueda de texto
    search_fields = ['model']
    #lista de campos para buscar en la tabla
    #filtrar por un campo de tipo enum, ejemplo small o big o all
    list_filter = ['height']
    ordering = ['price', 'model']
    form = SmartphoneForm
    #agrupacion de modelos
    fieldsets = (
        ('Basic', {
            'fields': ('model', 'ram')
        }),
        ('Cost', {
            'fields': ('height', 'price')
        })
    )

    def marcar_agotado(self, request, queryset):
        actualizados = queryset.update(status='AGOTADO')
        self.message_user(
            request,
            ngettext(
                '%d smartphone was update',
                '%d smartphone where update',
                actualizados,
            ) % actualizados,
            messages.SUCCESS
        )
    actions=[marcar_agotado]


# Register your models here.

class ChapterInline(admin.TabularInline):
    model = Chapter
    extra = 1

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author']
    inlines = [ChapterInline]
