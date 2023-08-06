@echo off
REM build.bat

set PACKAGE=lv_velodyne
set activate_env=env\Scripts\activate

if "%1" == "" goto help

if "%1" == "build-env" (
    python -m venv env
    call %activate_env% && python -m pip install --upgrade pip flit bump2version
    goto end
)

if "%1" == "install" (
    call build.bat install-pkg
    call build.bat install-dev
    goto end
)

if "%1" == "install-pkg" (
    call %activate_env% && flit install --deps production --symlink
    goto end
)

if "%1" == "install-dev" (
    call %activate_env% && flit install --deps develop --symlink
    goto end
)

if "%1" == "test" (
    call %activate_env% && pytest -vv -s tests
    goto end
)

if "%1" == "publish" (
    call %activate_env% && flit publish
    goto end
)

if "%1" == "bump-major" (
    bump2version major
    goto end
)

if "%1" == "bump-minor" (
    bump2version minor
    goto end
)

if "%1" == "bump-patch" (
    bump2version patch
    goto end
)

if "%1" == "lint-check" (
    call %activate_env% && black --check %PACKAGE%/ tests/
    call %activate_env% && isort --check %PACKAGE%/ tests/
    goto end
)

if "%1" == "lint" (
    call %activate_env% && black %PACKAGE%/ tests/
    call %activate_env% && isort %PACKAGE%/ tests/
    goto end
)

if "%1" == "clean" (
    rmdir /s /q env
    rmdir /s /q build
    rmdir /s /q dist
    rmdir /s /q %PACKAGE%.egg-info
    for /r %%f in (*.pyc) do del /q %%f
    for /r %%d in (__pycache__) do rmdir /s /q %%d
    goto end
)

if "%1" == "reset" (
    call build.bat clean
    call build.bat build-env
    call build.bat install
    goto end
)

:help
echo Usage:
echo   build.bat [command]
echo
echo Available commands:
echo   build-env
echo   install
echo   install-pkg
echo   install-dev
echo   test
echo   publish
echo   bump-major
echo   bump-minor
echo   bump-patch
echo   lint-check
echo   lint
echo   clean
echo   reset

:end

