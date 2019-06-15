python -m venv venv/
call venv\Scripts\activate.bat
pip install --upgrade https://github.com/serg-bloim/aoe2-cheat/releases/download/{0}/aoe2stats-{0}-py3-none-any.whl
python -m aoe2stats install