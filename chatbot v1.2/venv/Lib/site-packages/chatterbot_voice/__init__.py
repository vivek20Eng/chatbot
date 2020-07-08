import sys

if 'install' not in sys.argv and 'egg_info' not in sys.argv:
    from .voice import VoiceInput
    from .voice import VoiceOutput

__version__ = '0.1.5'
__author__ = 'Gunther Cox'
__email__ = 'gunthercx@gmail.com'
__all__ = (
    'VoiceInput',
    'VoiceOutput',
)
