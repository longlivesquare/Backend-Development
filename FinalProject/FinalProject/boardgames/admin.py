from django.contrib import admin
from .models import Boardgame,Category,Play,Player,Play_To_Player,Designer,Boardgame_Has_Designer

class BoardgameDesignerAdmin(admin.ModelAdmin):
    list_display = ('boardgame_id', 'designer_id')

class PlayToPlayerAdmin(admin.ModelAdmin):
    list_display = ('play_id', 'player_id')

class PlayAdmin(admin.ModelAdmin):
    list_display = ('boardgame_id', 'date', 'winning_player_id')
    date_hierarchy = 'date'
# Register your models here.

admin.site.register(Boardgame)
admin.site.register(Category)
admin.site.register(Play, PlayAdmin)
admin.site.register(Player)
admin.site.register(Play_To_Player, PlayToPlayerAdmin)
admin.site.register(Designer)
admin.site.register(Boardgame_Has_Designer, BoardgameDesignerAdmin)