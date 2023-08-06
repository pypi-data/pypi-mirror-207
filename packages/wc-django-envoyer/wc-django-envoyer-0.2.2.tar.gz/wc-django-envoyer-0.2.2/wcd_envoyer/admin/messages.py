from django.contrib import admin
from django.contrib.messages import INFO

from wcd_envoyer.models import Message
from wcd_envoyer.shortcuts import default_sender
from django.utils.translation import pgettext, pgettext_lazy

from .utils import JsonDataAdminMixin


@admin.register(Message)
class MessageAdmin(JsonDataAdminMixin, admin.ModelAdmin):
    messages_sender = default_sender
    actions = 'resend_action',
    list_display = 'channel', 'event', 'status', 'created_at', 'updated_at',
    list_filter = 'channel', 'event', 'status',
    readonly_fields = 'json_data', 'created_at', 'updated_at',
    date_hierarchy = 'created_at'
    search_fields = 'channel', 'event', 'recipients', 'data', 'status',

    def resend_action(self, request, qs):
        messages = list(qs)
        self.messages_sender.resend(messages)

        self.message_user(
            request=request,
            message=(
                pgettext('wcd_envoyer', 'Resent {} letters.')
                .format(len(messages))
            ),
            level=INFO,
        )
    resend_action.short_description = pgettext_lazy(
        'wcd_envoyer', 'Resend letters',
    )
