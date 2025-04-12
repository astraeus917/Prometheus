@echo off
@chcp 65001 > nul
goto :main


:: Custom color scheme.
:colors
    set fore.black=[30m
    set fore.red=[31m
    set fore.green=[32m
    set fore.yellow=[33m
    set fore.blue=[34m
    set fore.purple=[35m
    set fore.cyan=[36m
    set fore.white=[37m
    exit /b 0


:: Function that performs the installation of the requirements.
:install
    cls && title Installing...

    :: Iniciando a instalação.
    echo.
    echo %fore.white%[%fore.cyan%pytoolsc%fore.white%]-(%fore.cyan%setup%fore.white%) - Installation process started, this may take a few minutes.

    :: Criando ambiente virtual.
    echo.
    echo %fore.cyan%1. %fore.white%Creating virtual environment...
    echo.
    python -m venv .venv
    echo %fore.green%   [ok] %fore.white%virtual environment created.

    :: Ativando o ambiente virtual.
    echo.
    echo %fore.cyan%2. %fore.white%Activating virtual environment...
    echo.
    call .venv\Scripts\activate.bat
    echo %fore.green%   [ok] %fore.white%virtual environment activated.

    :: Instalando os requisitos.
    echo.
    echo %fore.cyan%3. %fore.white%Installing the requirements...
    echo.
    pip install -r requirements.txt
    echo %fore.green%   [ok] %fore.white%installed requirements.

    :: Desativando o ambiente virtual.
    echo.
    echo %fore.cyan%4. %fore.white%Deactivating virtual environment...
    echo.
    call deactivate
    echo %fore.green%   [ok] %fore.white%disabled virtual environment

    :: Instalação completa.
    echo.
    echo %fore.white%[%fore.cyan%pytoolsc%fore.white%]-(%fore.cyan%setup%fore.white%) - Installation completed successfully!
    echo.
    set /p cmd="Press ENTER to exit."
    exit

    pause
    exit /b 0


:: Help information.
:help
    echo.
    echo %fore.white%Command List:
    echo %fore.white%[ %fore.cyan%install %fore.white%] -- to install requirements
    echo %fore.white%[ %fore.cyan%exit %fore.white%] -- to close install.bat
    echo %fore.white%[ %fore.cyan%clear %fore.white%] -- clear the setup screen
    exit /b 0


:: Main banner.
:banner
    echo.
    echo %fore.cyan%Python source code for shell-like tool
    echo.
    echo %fore.white%Make sure you have %fore.cyan%Python %fore.white%and %fore.cyan%PIP %fore.white%installed before proceeding, both are required
    exit /b 0


:input
    echo.
    set /p cmd=" %fore.white%[%fore.cyan%pytoolsc%fore.white%]-(%fore.cyan%setup%fore.white%) >> Enter the command: "

    if "%cmd%" == "install" (
        goto :install
    ) else if "%cmd%" == "clear" (
        goto :main
    ) else if "%cmd%" == "exit" (
        echo .
        echo Exinting...
        exit
    ) else (
        goto :input
    )


:: Main function.
:main
    cls && title PyToolSourceCode
    
    call :colors
    call :banner
    call :help
    call :input

