from django.conf import settings

DJANGO_CLICKHOUSE_LOGGER_HOST = getattr(settings, 'DJANGO_CLICKHOUSE_LOGGER_HOST', None)
DJANGO_CLICKHOUSE_LOGGER_PORT = getattr(settings, 'DJANGO_CLICKHOUSE_LOGGER_PORT', 9000)
DJANGO_CLICKHOUSE_LOGGER_USER = getattr(settings, 'DJANGO_CLICKHOUSE_LOGGER_USER', 'default')
DJANGO_CLICKHOUSE_LOGGER_PASSWORD = getattr(settings, 'DJANGO_CLICKHOUSE_LOGGER_PASSWORD', '')
DJANGO_CLICKHOUSE_LOGGER_TTL_DAY = getattr(settings, 'DJANGO_CLICKHOUSE_LOGGER_TTL_DAY', 7)
DJANGO_CLICKHOUSE_LOGGER_REQUEST_EXTRA = getattr(settings, 'DJANGO_CLICKHOUSE_LOGGER_REQUEST_EXTRA', 'session')
