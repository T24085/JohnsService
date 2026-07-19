@echo off
cd /d "%~dp0"
set "PORT=5187"
if not exist node_modules (
  call npm install
)
start "John's Service Vite server" cmd /c "npm run dev -- --host 127.0.0.1 --port %PORT% --strictPort"

set /a ATTEMPTS=0
:wait_for_server
powershell -NoProfile -Command "try { Invoke-WebRequest -UseBasicParsing -Uri 'http://127.0.0.1:%PORT%/' -TimeoutSec 1 | Out-Null; exit 0 } catch { exit 1 }"
if %errorlevel%==0 goto open_browser
set /a ATTEMPTS+=1
if %ATTEMPTS% GEQ 30 goto server_failed
powershell -NoProfile -Command "Start-Sleep -Seconds 1"
goto wait_for_server

:open_browser
start "" "http://127.0.0.1:%PORT%/"
exit /b 0

:server_failed
echo John's Service website could not start on port %PORT%.
echo Check the Vite server window for details.
pause
