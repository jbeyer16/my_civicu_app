from django.contrib import admin
from .models import Image, UserLabel, TotalVotes
# from .models import Question

# Register your models here.

# admin.site.register(Question)


class ImageAdmin(admin.ModelAdmin):
    date_hierarchy = 'taken_date'
    list_display = ('taken_date', 'created_date', 'imgfile', 'caption', 
                    'uploaded_by')
    search_fields = ('caption', 'imgfile')


admin.site.register(Image, ImageAdmin)
admin.site.register(UserLabel)
admin.stie.register(TotalVotes)
