from src.settings import *
from src.settings import _gettext


# Custom alert function using print().
def alert(type, text):
    try:
        # SUCCESS.
        if type == 'success':
            success_text = _gettext("[SUCCESS]:")
            print(_gettext(f"\n {fg_success}{success_text} {fg_text}{text}"))

        # INFO.
        elif type == 'info':
            info_text = _gettext("[INFO]:")
            print(_gettext(f"\n {fg_info}{info_text} {fg_text}{text}"))

        # ERROR.
        elif type == 'error':
            error_text = _gettext("[ERROR]:")
            print(_gettext(f"\n {fg_error}{error_text} {fg_text}{text}"))

        else:
            type = 'error'
            print(_gettext(f"\n {fg_error}{error_text} {fg_text}{text}"))
    
    except Exception as error:
        alert(None, error)

