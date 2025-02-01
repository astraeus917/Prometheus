# Python Terminal Tool Source Code


## Instalar o gettext

Baixar o gettext compilado para Windows:

    https://github.com/mlocati/gettext-iconv-windows/releases/tag/v0.23-v1.17



## Sistema de tradução

Instalar:

    xgettext

Criar o .po:

    xgettext -o locale/messages.pot main.py

Copiar o .pot para o .po:

    copy locale\messages.pot locale\pt_BR\LC_MESSAGES\messages.po

Modelo para editar o arquivo .po:

    msgid "Hello, World!"
    msgstr "Olá, Mundo!"

    msgid "This is a test message."
    msgstr "Esta é uma mensagem de teste."

Compilar o .po para .mo:

    msgfmt -o locale\pt_BR\LC_MESSAGES\messages.mo locale\pt_BR\LC_MESSAGES\messages.po

    msgfmt -o locale\en_US\LC_MESSAGES\messages.mo locale\en_US\LC_MESSAGES\messages.po


