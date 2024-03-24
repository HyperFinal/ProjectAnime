import os

path = os.getcwd()

os.system(fr'start "runner" cmd /k "cd "{path}" && python -m streamlit run app.py"')