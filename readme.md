# Python source code for shell-like tool

---

## Project Description:

This project is source code to aid in the creation of shell-like tools.

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

2. (Optional) Create a virtual environment for your project.

```sh
cd PyToolSourceCode
python -m venv pytoolsc_env
```

2. a. Activate the virtual environment.

```sh
pytoolsc_env\Scripts\activate
```

2. b. Deactivate the virtual environment.

```sh
deactivate
```

3. Install the necessary requirements.

```sh
pip install -r requirements.txt
```

---

## How to install and use gettext to create translations.

Gettext is used to compile *.po* files to *.mo* which are the files used in the tool's translation system *python-gettext*. There is the *xgettext* tool that can be used to assist this translation process, research more about it.

- [GNU Project, gettext](https://www.gnu.org/software/gettext/)
- [Docs Python, gettext](https://docs.python.org/3/library/gettext.html)

### Windows.

1. Download the compiled gettext for Windows.

```sh
https://github.com/mlocati/gettext-iconv-windows/releases/tag/v0.23-v1.17
```

