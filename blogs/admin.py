from django.contrib import admin
from .models import Blogs

# Register your models here.


class BlogsAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_created', 'date_updated')
    list_display_links = ('title',)
    list_filter = ('title',)
    search_fields = ('title',)
    list_per_page = 10


admin.site.register(Blogs, BlogsAdmin)
