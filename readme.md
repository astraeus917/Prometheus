# Python source code for CLI tool

---

## Informações Básicas:
- Autor: Astraeus @xzhyan7
- Versão: 1.2
- Idioma padrão: inglês
- Linguagem: Python

## Descrição do Projeto:

O projeto se trata de um codigo fonte para facilitar a criação de ferramentas do tipo CLI (Command Line Interface). Esse código já esta todo estruturado para que você possa modificar, criar e adicionar novas  funcionalidades. Você pode adicionar códigos para automatização de tarefas no Windows ou até mesmo criar codigos e scripts para usar se você atuar na area de Hacking.

## Caracteristicas:
- Esquema de Tradução
- Messagens de Alerta
- Banners ASCII
- Comandos por categoria
- Adição de scripts
- Cores Personalizadas
- Login por meio de credenciais registradas no sistema
- Registro de credenciais no sistema

## Bibliotecas Python principais usadas/instaladas:
- [colorama](https://pypi.org/project/colorama/)
- [python-gettext](https://pypi.org/project/python-gettext/)
- [keyring](https://pypi.org/project/keyring/)

---

## Como usar o codigo fonte:

1. Clone o codigo fonte do repositorio github.

```sh
git clone https://github.com/astraeus47/PyToolSourceCode.git
```

2. Use o install.bat que automatiza o processo de instalação dos requisitos.

---

## Como usar o esquema de tradução:

O esquema de tradução funciona usanado a biblioteca python-gettext e o gettext compilador. Dentro do codigo  é definido "_gettext" para indicar que um texto tem tradução e deve ser traduzido conforme o idioma configurado.
As traduções seguem o seguinte caminho "config/locale/" dentro vai ter a pasta com nome do idioma (pt_BR, en_US ou outro idioma) e dentro da pasta do idioma a pasta "LC_MESSAGES". Dentro de "LC_MESSAGES" tem os arquivos messages.po e messages.mo. O messages.po é onde tem os textos com sua referente tradução, já o messages.mo é o arquivo de tradução já compilado.

Siga o passo a passo para entender melhor como usar.

1. Download do compilador gettext para Windows.

```sh
https://github.com/mlocati/gettext-iconv-windows/releases/tag/v0.23-v1.17
```

2. Use "gettext" para indicar um texto que vai ter tradução.

Veja um exemplo usado o print(), o texto esta dentro de _gettext(""):

```python
print(_gettext("Exemplo de texto que vai ser traduzido."))

```

## Criar arquivo de tradução.

O arquivo pode ser criado automaticamente usando o xgettext, se quiser pesquise mais sobre isso. O comando deve ser algo como "xgettext -o messages.pot main.py".

1. Seguindo o esquema diretorio de tradução (config/locale/pt_BR/LC_MESSAGES) crie um arquivo chamado messages.po e nele você vai salvar os texto com tradução seguindo o seguinte esquema:

- msgid: is the original text.
- msgstr: is the translated text.

```sh
msgid "Hello, World!"
msgstr "Olá, Mundo!"

msgid "This is a test message."
msgstr "Esta é uma mensagem de teste."
```

2. Para compilar o "messages.po" para "messages.mo" use o seguinte comando:

```sh
msgfmt -o config\locale\pt_BR\LC_MESSAGES\messages.mo config\locale\pt_BR\LC_MESSAGES\messages.po
```

---

## Como usar as mensagens personalizadas de alerta.

O "alert()" é a função da mensagem de alerta e deve ser passado uma tupla, ex: alert('info', "Exiting...) ou com o gettext alert('error', _gettext("Problema na ferramenta!")).

- INFO (info): para mensagens de informação
- SUCCESS (success): para mensagens de sucesso
- ERROR (error): para mensagens de erro

```python
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        alert('info', _gettext("Exiting..."))
        sys.exit()
```

---

## Adicionando novos comandos.

Os comandos devem ser adicionados dentro de categorias ou se for o caso deve ser criado uma nova categoria.

1. Dentro de "src/settings.py" adicione o comando novo a uma categoria existente ou crie uma nova categoria.

```python
# New category of commands:
new_commands = {
    'cmd01': _gettext("comando 01"),
    'cmd02': _gettext("comando 02"),
    'cmd0': _gettext("comando 03"),
}
```

2. Depois disso é só adicionar essa categoria e as condições dos comandos adicionados nela, isso dentro de "src/main.py".

```python
# New category of commands:
def new_commands(self, args):
    if args[0] == 'cmd01':
        Here you create the code based on what your command will execute.

    elif args[0] == 'cmd02':
        Here you create the code based on what your command will execute.

    else:
        return
```

## Registro de credenciais no sistema.


## Login de acesso com credenciais salvas no sistema.

