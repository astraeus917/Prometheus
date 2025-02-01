from src.settings import *


# Set and load translation.
translation = gettext.translation("messages", localedir=locale_path, languages=[lang], fallback=True) 
translation.install()
_ = translation.gettext


# Custom alert function using print().
def alert(type, text):
    try:
        # SUCCESS.
        if type == 'success':
            success_text = _("[SUCCESS]:")
            print(_(f"\n {fg_success}{success_text} {fg_text}{text}"))

        # INFO.
        elif type == 'info':
            info_text = _("[INFO]:")
            print(_(f"\n {fg_info}{info_text} {fg_text}{text}"))

        # ERROR.
        elif type == 'error':
            error_text = _("[ERROR]:")
            print(_(f"\n {fg_error}{error_text} {fg_text}{text}"))

        else:
            type = 'error'
            print(_(f"\n {fg_error}{error_text} {fg_text}{text}"))
    
    except Exception as error:
        alert(None, error)

