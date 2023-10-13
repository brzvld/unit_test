#!/usr/bin/python3
import os
import contextlib

#ver2
#рекурсивный проход по каталогам в поисках файлов
#поиск в каждом файле строки в нескольких кодировках


#поиск в каждом файле строки (подстроки) в указаной кодировке
def search_string_mcode_file(file_name, encoding_s, stroka_s):
  result_dict = dict()#словарь для найденных номеров строк и самих строк в которых найдена подстрока

  #счетчик номера строки в файле
  number_string = 0

  #искомая строка
  #перевод в нижний регистр
  stroka_search = stroka_s.lower()

  #открытие  файла в нужной кодировке,
  #далее построчное чтение файла (без загрузки всего его в память)  
  with open(file_name, 'r', encoding=encoding_s, errors='ignore') as f1:
    for read_string in f1:

      number_string += 1#после прочтения строки из файла увеличиваем счетчик на 1

      #перевод в нижний регистр
      #далее, поиск подстроки в строке в нижнем регистре
      #и печать строки из файла в первоначальном виде
      read_string1 = read_string.lower()
      if read_string1.find(stroka_search) != -1:#если подстрока найдена в строке...

        read_string = read_string.replace('\n','')#удаляем перевод строки в конце строки
        result_dict[number_string]=read_string#добавляем в словарь:  ключ - номер строки в файле, в которой надена подстрока, значение - строка вкотолрой найдена подстрока

  return result_dict#возвращаем словарь с результатами поиска в файле
#===



#функция, которая проходит по каталогам
def stroll_file_dir(dir):
  result_search = dict()
  fff_name = ''
  #подавляем вывод ошибок OSError (много запутанных взаимных ссылок на файлы)
  #подавляем исключение без try...except
  with contextlib.suppress(OSError):
    #заходим в каждый подкаталог текущего каталога
    for name in os.listdir(dir):
      path = os.path.join(dir, name)
      #если это файл то пишем его название и текущий каталог
      if os.path.isfile(path):

      #print("Каталог:", dir, "файл:", name)
        fff_name = dir+"/"+name
        #print("Файл:",dir+"/"+name)
        print("Файл:", fff_name )


        #поиск строки в файле, 4 кодировки c map работает
        #====
        #для запуска map создаем 3 списка одинокового размера (по 4)
        fff_string = 'приве'

        fff_name_lst = [fff_name, fff_name, fff_name, fff_name]
        fff_code_lst = ['utf-8', 'koi8-r', 'cp866', 'cp1251']        
        fff_string_lst = [fff_string, fff_string, fff_string, fff_string]
        
        #print(fff_name_lst, fff_code_lst, fff_string_lst)
        result_search_lst =list(map(search_string_mcode_file, fff_name_lst, fff_code_lst, fff_string_lst ))
        #print(result_search_lst)
        
        #печать только удачных результатов поиска
        #если в списке пустой элемент-словарь, то не печатаем его
        #проходим по списку, где элементы словари
        for i in range(len(result_search_lst)):
          if len(result_search_lst[i]) != 0:            
            #если словарь непустой, то создаем строку из его ключей и значений и печатаем ее
            print('Номер строки : Строка, в которой найдено')
            s_result = ''
            for i_dict in result_search_lst[i]:#проходим по всем ключам каждого словаря
              s_result += str(i_dict) + ' : ' + result_search_lst[i][i_dict] + '\n'
            print(s_result)

        
        #====
        
    #если это каталог, то запускаем(ся) фунцию рекурсивно
      else:
        
        stroll_file_dir(path)
#===




#
cur_dir = "/home/vlad/python_prog/00/recursive2/1"

stroll_file_dir(cur_dir)
