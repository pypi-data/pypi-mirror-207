from django.contrib import admin

from bcmr.models import *


class AuthTokenAdmin(admin.ModelAdmin):
    list_display = [
        'id',
    ]

class TokenAdmin(admin.ModelAdmin):
    list_display = [
        'category',
        'is_nft',
        'name',
        'symbol',
        'decimals',
        'status',
        'date_created',
    ]

class RegistryAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'active',
        'description',
        'date_created',
        'latest_revision',
    ]

class TokenHistoryAdmin(admin.ModelAdmin):
    list_display = [
        'date',
    ]


admin.site.register(AuthToken, AuthTokenAdmin)
admin.site.register(Token, TokenAdmin)
admin.site.register(Registry, RegistryAdmin)
admin.site.register(TokenHistory, TokenHistoryAdmin)
