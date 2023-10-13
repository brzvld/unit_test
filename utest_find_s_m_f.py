import unittest
import find_string_mcode_files 


class FindfTest(unittest.TestCase):
  def test_search_string_mcode_file(self):
        #тестирование функции с задаными параметрами
        self.assertEqual(find_string_mcode_files.search_string_mcode_file('/home/vlad/python_prog/00/unit_test2/1/2/3/1txt_koi8r.txt','koi8-r','приве'), {2:'Привет', 4:'привет всем', 7:'приве1',9:'пРИВЕТИКэтоkoi8-r'})



if __name__ == '__main__':
  unittest.main()
