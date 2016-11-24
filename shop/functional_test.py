from selenium import webdriver
import unittest

class NewVistorTest(unittest.TestCase):
   #打开
   def setUp(self):
       self.brower = webdriver.Firefox()
       #隐式等待
       self.brower.implicitly_wait(3)
   #关闭
   def tearDown(self):
       self.brower.quit()
   def test_can_start_a_login(self):
       self.brower.get('http://127.0.0.1:8000/')
       self.assertIn('username',self.brower.title)
       self.fail('测试完成')


if __name__ == '__main__':
    unittest.main(warnings='ignore')