python -m venv venv/
call venv\Scripts\activate.bat
powershell.exe Start-Process python '-m','aoe2stats' -Verb runAs
start chrome http://localhost:5000