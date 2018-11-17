from django.contrib import admin

from .models import Language,Sentence,SyntaxPost,Report,Marker

class SyntaxPostAdmin(admin.ModelAdmin):
    readonly_fields = ('updated',)
    list_display=('content','language')


admin.site.register(Language)
admin.site.register(Sentence)
admin.site.register(SyntaxPost,SyntaxPostAdmin)
admin.site.register(Report)
admin.site.register(Marker)
# Register your models here.
