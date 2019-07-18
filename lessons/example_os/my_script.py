import os

#посмотреть, с какой платформой вы работаете
print(os.name) # ответ: nt

#информация о ПК
print(os.environ)

#посмотреть адрес текущей директории
print(os.getcwd())

#создание папок по указанному адресу
#path = r'C:\MachineLearning\ItJim\python\Task_1_Hello_Sausages_Project\example_os\pytest\2014\02\19'
#os.makedirs(path)

#код пытается удалить файл path.
#os.remove(r"C:\MachineLearning\ItJim\python\Task_1_Hello_Sausages_Project\example_os\pytest\2014\02\19\test.txt")

#код попытается удалить каталог под названием pytest из каталога,
#используемого в данный момент в работе.
#os.rmdir("pytest")

#удалить пустые вложенные каталоги.
#os.removedirs("pytest")


#переименовать файл или папку
#path_src = r"C:\MachineLearning\ItJim\python\Task_1_Hello_Sausages_Project\example_os\pytest\2014\02\19\test.txt"
#path_dst = r"C:\MachineLearning\ItJim\python\Task_1_Hello_Sausages_Project\example_os\pytest\2014\02\19\pytest.txt"
#os.rename(path_src, path_dst)


#«запустить» файл в привязанной к нему программе
#os.startfile(r"C:\MachineLearning\ItJim\python\Task_1_Hello_Sausages_Project\example_os\pytest\2014\02\19\pytest.txt")

print('-------------------------------------------')
#указываем путь (path) к данной папке.
#в цикле можем получить доступ ко всем файлам и подпапкам данной папки.
path = r'./sausages'
for root, dirs, files in os.walk(path):
    print('root=',root)
    for _dir in dirs:
        print(_dir)
    print('~~~~~~~~~~~~~~~~')
    for _file in files:
        print(_file)





