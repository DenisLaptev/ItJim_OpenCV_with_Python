import os

path = r'./__init__.py'

#------------------------ ТОЛЬКО имя файла в path-------------------------
print(os.path.basename(path))
# __init__.py








#------------------------ ТОЛЬКО имя папки файла в path-------------------------
print(os.path.dirname(path))
#









#------------------------ проверить, существует ли файл в path-------------------------
#path = r'./__init__.py'
print(os.path.exists(path))# True

print(os.path.exists(r'C:\MachineLearning\fake.py'))# False











#------------------------
# os.path.isfile
# os.path.isdir
# -------------------------
print(os.path.isfile(r'./__init__.py'))  # True
print(os.path.isdir(r'./__init__.py'))  # False
print(os.path.isdir(r'../'))  # True
print(os.path.isfile(r'../'))  # False









#------------------------ os.path.join-------------------------
print(os.path.join(r'../', '__init__.py'))
# ../__init__.py











#------------------------ os.path.split-------------------------
print(os.path.split(r'../__init__.py'))
# ('..', '__init__.py')
