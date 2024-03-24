import os

file = open('./requirements.txt','r')
content = file.read()

RequireList = content.split()
print(RequireList)
path = os.getcwd()

for package in RequireList:
    os.system(fr'start "runner" cmd /k "cd "{path}" && pip install {package} && exit"')