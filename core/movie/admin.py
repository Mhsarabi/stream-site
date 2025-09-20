from django.contrib import admin
from movie.models import Movie,Actor,Genre,MovieRating,Series,SeriesRating,Episode,DownloadLog

# Register your models here.
admin.site.register(Movie)
admin.site.register(Actor)
admin.site.register(Genre)
admin.site.register(MovieRating)
admin.site.register(Series)
admin.site.register(SeriesRating)
admin.site.register(Episode)

@admin.register(DownloadLog)
class DownloadLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'ip_address', 'url', 'timestamp')
    list_filter = ('timestamp', 'user')
    search_fields = ('user__username', 'ip_address', 'url')




