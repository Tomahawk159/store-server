from django.contrib import admin
from users.models import User, EmailVerefication
from products.admin import BasketAdmin


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username',)
    inlines = (BasketAdmin,)


@admin.register(EmailVerefication)
class EmailVereficationAdmin(admin.ModelAdmin):
    list_display = ('user', 'code', 'expiration')
    fields = ('code', 'user', 'expiration', 'created')
    readonly_fields = ('created',)
