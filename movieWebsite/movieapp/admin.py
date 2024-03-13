from django.contrib import admin

from . models import Category,Movie,UserMovie,Review

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['genre','slug']
    prepopulated_fields = {'slug':('genre',)}
admin.site.register(Category,CategoryAdmin)

class MovieAdmin(admin.ModelAdmin):
    list_display = ['title','actors','date']
    list_editable = ['actors','date']
    prepopulated_fields = {'slug':('title',)}
    list_per_page = 20
admin.site.register(Movie,MovieAdmin)


class UserMovieAdmin(admin.ModelAdmin):
    list_display = ['title','actors','date']
    list_editable = ['actors', 'date']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(UserMovie,UserMovieAdmin)

admin.site.register(Review)

