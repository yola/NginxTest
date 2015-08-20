__version__ = '0.1-yola1'

try:
    from nginxtest.server import NginxServer       # NOQA
except ImportError:
    pass   # early import via setup.py
