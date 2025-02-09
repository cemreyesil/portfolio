from django_hosts import patterns, host

host_patterns = patterns(
    '',
    host(r'', 'portfolio_cemre.urls', name=' '),
    host(r'admin', 'core.admin_urls', name='admin'),
)