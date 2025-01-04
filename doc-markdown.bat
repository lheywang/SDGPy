@echo off
echo ==========================================================
echo Generating Markdown documentation...
echo ==========================================================

rem Creating folder structure
if not exist "documentation" mkdir documentation
cd documentation
if not exist "markdown" mkdir markdown
cd ..

rem Iterating over first level folder to generate docs.
rem This is fine for simple modules
cd .\SDGPy\
for /D %%i in (*) do (
    echo|set /p="Generatic doc for %%i ... "
    if not exist "..\documentation\markdown\%%i" mkdir ..\documentation\markdown\%%i
    pydoc-markdown -p %%i > ..\documentation\markdown\%%i\%%i.md
    echo Done !
)

rem Generatic global doc project
echo|set /p="Generatic doc for SDGPy ... "
pydoc-markdown -p SDGpy > ..\documentation\markdown\SDGPy.md
echo Done !

echo =========================================================
echo Finished creating Markdown documentation !
echo =========================================================

pause