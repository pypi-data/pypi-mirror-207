from dataclasses import dataclass, field
from typing import *

from px_settings.contrib.django import settings as setting_wrap

from .channels import ChannelInfoType
from .events import EventInfoType
from .const import SETTINGS_PREFIX


__all__ = 'Settings', 'settings',


@setting_wrap(SETTINGS_PREFIX)
@dataclass
class Settings:
    CHANNELS: Sequence[ChannelInfoType] = field(default_factory=list)
    EVENTS: Sequence[EventInfoType] = field(default_factory=list)
    JSON_ENCODER: str = 'django.core.serializers.json.DjangoJSONEncoder'


settings = Settings()


# class KLD_LETTRE_CHANNELS(TextChoices):
#     email = 'email', pgettext_lazy('kld_lettre', 'Email')
#     some_channel = 'sendpulse', pgettext_lazy('kld_lettre', 'Some channel')


# class KLD_LETTRE_EVENTS(TextChoices):
#     event1 = 'event1', pgettext_lazy('kld_lettre', 'Event 1')
#     event2 = 'event2', pgettext_lazy('kld_lettre', 'Event 2')


# KLD_LETTRE_EVENTS_CONTEXT = {
#     KLD_LETTRE_EVENTS.event1: {
#         'var1': pgettext_lazy('kld_lettre', 'Var 1'),
#         'var2': pgettext_lazy('kld_lettre', 'Var 2'),
#     },
#     KLD_LETTRE_EVENTS.event2: {
#         'var2': pgettext_lazy('kld_lettre', 'Var 2'),
#         'var3': pgettext_lazy('kld_lettre', 'Var 3'),
#     },
# }

# KLD_LETTRE_CHANNEL_EVENTS = {
#     KLD_LETTRE_CHANNELS.email: [
#         KLD_LETTRE_EVENTS.event1,
#         KLD_LETTRE_EVENTS.event2,
#     ],
#     KLD_LETTRE_CHANNELS.some_channel: [
#         KLD_LETTRE_EVENTS.event1,
#     ]
# }

# KLD_LETTRE_GENERATOR_RENDERERS = {
#     'kld_lettre.renderers.Jinja2Renderer': (
#         'kld_lettre.generators.field_plug.Jinja2PlugGenerator'
#     ),
# }

# KLD_LETTRE_BACKENDS = {
#     KLD_LETTRE_CHANNELS.email: (
#         'kld_lettre.backends.email.EmailMessageBackend'
#     ),
#     KLD_LETTRE_CHANNELS.some_channel: (
#         'kld_lettre.backends.base.BaseMessageBackend',
#         {
#             'config_form_path': 'kld_lettre.forms.BaseConfigForm',  # default value
#             'recipients_resolver_path': (
#                 'kld_lettre.recipients.BaseRecipientsResolver'  # default value
#             ),
#             'template_form_path': 'kld_lettre.forms.BaseTemplateForm',  # default value
#             'template_renderer_path': 'kld_lettre.renderers.Jinja2Renderer',  # default value
#             'template_data_generator_path': (
#                 'kld_lettre.generators.template_data.BaseTemplateDataGenerator'  # default value
#             ),
#         }
#     ),
# }
