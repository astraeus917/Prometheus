# Python source code for shell-like tool

---

## Project Description:

This project is source code to aid in the creation of shell-like tools.
Don't forget to read the commented texts to clarify doubts and use the code correctly.

## Project information:
- Author: Astraeus
- Language: Python
- Version: 1.0
- Default language: english (en_US)

## Features:
- ASCII banners
- Translation
- Alert messages

## Python libraries used:
- [colorama](https://pypi.org/project/colorama/)
- [python-gettext](https://pypi.org/project/python-gettext/)

## How to use the source code.

1. Clone the source code repository into your projects folder.

```sh
git clone https://github.com/astraeus47/PyToolSourceCode.git
```

2. Use install.bat to automatically install all requirements.

---

## How to install and use gettext to create translations.

Gettext is used to compile **.po** files to **.mo** which are the files used in the tool's translation system **python-gettext**. There is the **xgettext** tool that can be used to assist this translation process, research more about it.

- [GNU Project, gettext](https://www.gnu.org/software/gettext/)
- [Docs Python, gettext](https://docs.python.org/3/library/gettext.html)

### Windows.

1. Download the compiled gettext for Windows.

```sh
https://github.com/mlocati/gettext-iconv-windows/releases/tag/v0.23-v1.17
```

2. To indicate the text that will be affected by the translation use **_gettext**.

```sh
print(_gettext(f"Welcome to the tool's help menu, see below the list of available commands."))
```

3. To create new translations edit or create the file **messages.po**.

You can create the translation files manually or by using **xgettext* as a helper. **xgettext** can be used to automatically capture text from your code. Ex: **xgettext -o locale/messages.pot main.py**. Research this further if needed.

The default directory scheme used in the translation system is **locale/pt_BR/LC_MESSAGES**.

In the final directory **MESSAGES** there is the file **messages.po** and the file **messages.mo** (.mo is the compiled translation file).

- msgid: is the original text.
- msgstr: is the translated text.

```sh
msgid "Hello, World!"
msgstr "Olá, Mundo!"

msgid "This is a test message."
msgstr "Esta é uma mensagem de teste."
```

4. To compile the **messages.po** file use the following command.

```sh
msgfmt -o locale\pt_BR\LC_MESSAGES\messages.mo locale\pt_BR\LC_MESSAGES\messages.po
```

---

## How to use alert messages.

Alert messages are basically **print()** already styled to be used as alerts.

- INFO (info): For alerts that display information.
- SUCCESS (success): For success alerts.
- ERROR (error): For error alerts.

```python
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        alert('info', _gettext("Exiting..."))
        sys.exit()
```

Use the **alert()** function as a tuple, the first argument is the alert type **(info, error, success)** and the second argument is the text you want to print to the screen.

---

### New updates coming soon.


