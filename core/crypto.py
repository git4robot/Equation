from re import *
from errors import *
class _Test_key:
      def __init__(self, key, method, *type):
            self.key = key
            self.method = method
            self.type = type

      def test_type(self):
            try:
                  assert type(self.key) in self.type
            except AssertionError:
                  raise KeyTypeError(self.key, self.method, self.type) from None

class Shift:
      def __init__(self):
            self.letter_list = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'.split(' ')
            
      def encipher(self, msg, secret_key):
            test = _Test_key(secret_key, 'Shift Encrypt', int)
            test.test_type()
            self.pattern_list = findall(r'[\s]|[0123456789]|[~`!@#\$%\^&\*()_\+\-={}|\[\]\\:";\'\<\>\?,./", ]', msg)
            msg = msg.upper()
            for x in self.pattern_list:
                  msg = msg.replace(x, '')

            self.msg_list = list(msg)
            self.index_list = []
            for x in range(len(msg)):
                  index = self.letter_list.index(self.msg_list[x])
                  self.index_list.append(index + secret_key)

            temp_index = 0
            for x in self.index_list:
                  if x > 26:
                        x -= 26
                  self.index_list[temp_index] = x
                  temp_index += 1
                        
            self.output_list = []
            for x in self.index_list:
                  self.output_list.append(self.letter_list[x])
                  
            self.output = ''
            for x in self.output_list:
                  self.output += x
            return self.output

      def decipher(self, msg, secret_key):
            test = _Test_key(secret_key, 'Shift Decrypt', int)
            test.test_type()
            return self.encipher(msg, -secret_key)

class Affine:
      def __init__(self):
            self.a = 5
            self.b = 8
            self.m = 26
            self.areverse = 21
            self.letter_list = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'.split(' ')
            self.number_list = list(range(26))
            
      def encipher(self, msg):
            self.pattern_list = findall(r'[\s]|[0123456789]|[~`!@#\$%\^&\*()_\+\-={}|\[\]\\:";\'\<\>\?,./", ]', msg)
            msg = msg.upper()
            for x in self.pattern_list:
                  msg = msg.replace(x, '')

            self.msg_list = list(msg)
            
            self.output_list = []
            for char in self.msg_list:
                  x = self.letter_list.index(char)
                  self.output_list.append((self.a * self.number_list[x] + self.b) % self.m)

            self.output = ''
            for x in self.output_list:
                  self.output += self.letter_list[self.number_list[x]]
            return self.output

      def decipher(self, msg):
            self.pattern_list = findall(r'[\s]|[0123456789]|[~`!@#\$%\^&\*()_\+\-={}|\[\]\\:";\'\<\>\?,./", ]', msg)
            msg = msg.upper()
            for x in self.pattern_list:
                  msg = msg.replace(x, '')

            self.msg_list = list(msg)
            self.output_list = []
            for char in self.msg_list:
                  x = self.letter_list.index(char)
                  self.output_list.append((self.areverse * (self.number_list[x] - self.b)) % self.m)

            self.output = ''
            for x in self.output_list:
                  self.output += self.letter_list[self.number_list[x]]
            return self.output

class Vigenere:
      def __init__(self):
            self.letter_list = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'.split(' ')
            self.number_list = list(range(26))

      def encipher(self, msg, secret_key):
            test = _Test_key(secret_key, 'Vigenere Encrypt', str)
            test.test_type()
            self.pattern_list = findall(r'[\s]|[0123456789]|[~`!@#\$%\^&\*()_\+\-={}|\[\]\\:";\'\<\>\?,./", ]', msg)
            msg = msg.upper()
            for x in self.pattern_list:
                  msg = msg.replace(x, '')

            self.secret_key = secret_key.upper()
            while True:
                  if len(self.secret_key) < len(msg):
                        self.secret_key *= 2
                  else:
                        self.secret_key = self.secret_key[:len(msg)].upper()
                        break

            self.encipher_text_list1 = [x for x in list(msg)]
            self.encipher_text_list2 = [x for x in list(self.secret_key)]
            self.encipher_text_list = []
            for x in range(len(msg)):
                  self.encipher_text_list += [[self.encipher_text_list1[x], self.encipher_text_list2[x]]]

            self.output_list = []
            for x in range(len(msg)):
                  self.num_msg = self.number_list[self.letter_list.index(self.encipher_text_list[x][0])]
                  self.num_key = self.number_list[self.letter_list.index(self.encipher_text_list[x][1])]
                  self.new_letter_list = self.letter_list[self.number_list[self.num_msg]:] + list(self.letter_list[0:self.number_list[self.num_msg]])
                  self.output_list += self.new_letter_list[self.num_key]

            self.output = ''
            for x in self.output_list:
                  self.output += x
            return self.output

      def decipher(self, msg, secret_key):
            test = _Test_key(secret_key, 'Vigenere Decrypt', str)
            test.test_type()
            self.pattern_list = findall(r'[\s]|[0123456789]|[~`!@#\$%\^&\*()_\+\-={}|\[\]\\:";\'\<\>\?,./", ]', msg)
            msg = msg.upper()
            for x in self.pattern_list:
                  msg = msg.replace(x, '')

            self.secret_key = secret_key.upper()
            while True:
                  if len(self.secret_key) < len(msg):
                        self.secret_key *= 2
                  else:
                        self.secret_key = self.secret_key[:len(msg)].upper()
                        break
            
            self.decipher_text_list1 = [x for x in list(msg)]
            self.decipher_text_list2 = [x for x in list(self.secret_key)]
            self.decipher_text_list = []
            for x in range(len(msg)):
                  self.decipher_text_list += [[self.decipher_text_list1[x], self.decipher_text_list2[x]]]

            self.output_list = []
            self.msg_list = list(msg)
            for x in range(len(msg)):
                  self.num_msg = self.number_list[self.letter_list.index(self.decipher_text_list[x][0])]
                  self.num_key = self.number_list[self.letter_list.index(self.decipher_text_list[x][1])]
                  self.new_letter_list = self.letter_list[self.number_list[self.num_key]:] + list(self.letter_list[0:self.number_list[self.num_key]])
                  self.output_list += self.letter_list[self.new_letter_list.index(self.msg_list[x])]

            self.output = ''
            for x in self.output_list:
                  self.output += x
            return self.output

class Hill:
      def __init__(self):
            from numpy import matrix
            self.letter_list = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'.split(' ')
            self.number_list = list(range(26))
            self.is_numpy = True
            self.mod = 26

      def encipher(self, msg, secret_key):
            try: from numpy import matrix
            except ImportError: self.is_numpy = False

            test = _Test_key(secret_key, 'Hill Encrypt', list, matrix)
            test.test_type()
            self.pattern_list = findall(r'[\s]|[0123456789]|[~`!@#\$%\^&\*()_\+\-={}|\[\]\\:";\'\<\>\?,./", ]', msg)
            msg = msg.upper()
            for x in self.pattern_list:
                  msg = msg.replace(x, '')

            self.secret_key = secret_key
            self.msg_list = list(msg)
            self.index_list = []
            for x in range(len(msg)):
                  index = self.letter_list.index(self.msg_list[x])
                  self.index_list.append(index)
            
            if self.is_numpy:
                  from numpy.linalg import det
                  if not det(self.secret_key): raise KeyNumError(self.secret_key, 'Hill Encrypt')
                  
                  try: self.msg_tolist = (self.secret_key * matrix([self.index_list]).T % self.mod).tolist()
                  except ValueError: raise KeyNumError(self.secret_key, 'Hill Encrypt') from None
                  
                  self.msg_list = []
                  for x in range(len(self.msg_tolist)):
                        self.msg_list.append(self.msg_tolist[x][0])
                  
                  self.output_list = []
                  for char in self.msg_list:
                        x = self.letter_list[self.number_list.index(char)]
                        self.output_list.append(x)

                  self.output = ''
                  for x in self.output_list:
                        self.output += x
                  return self.output


      def decipher(self, msg, secret_key):
            try: from numpy import matrix
            except ImportError: self.is_numpy = False

            test = _Test_key(secret_key, 'Hill Decrypt', list, matrix)
            test.test_type()
            self.pattern_list = findall(r'[\s]|[0123456789]|[~`!@#\$%\^&\*(（）)_\+\-={}|\[\]\\:";\'\<\>\?,./", ]', msg)
            msg = msg.upper()
            for x in self.pattern_list:
                  msg = msg.replace(x, '')

            self.secret_key = secret_key
            self.msg_list = list(msg)
            self.index_list = []
            for x in range(len(msg)):
                  index = self.letter_list.index(self.msg_list[x])
                  self.index_list.append(index)
            
            if self.is_numpy:
                  print(matrix(self.index_list), '\n', self.secret_key.I)
                  print(self.secret_key.I * matrix(self.index_list).T)
                  
class Rsa:
      def __init__(self):
            pass

      def encipher(self, msg, secret_key1, secret_key2):
            test = _Test_key(secret_key1, 'Rsa Encrypt', int)
            test.test_type()
            test = _Test_key(secret_key2, 'Rsa Encrypt', int)
            test.test_type()
            self.pattern_list = findall(r'[\s]|[0123456789]|[~`!@#\$%\^&\*()_\+\-={}|\[\]\\:";\'\<\>\?,./", ]', msg)
            msg = msg.upper()
            for x in self.pattern_list:
                  msg = msg.replace(x, '')

            self.secret_key1 = secret_key1
            self.secret_key2 = secret_key2
            for i in range(2, int(self.secret_key1 ** 0.5 + 1)):
                  if self.secret_key1 % i == 0 or self.secret_key2 % i == 0: raise KeyNumError(self.secret_key1, 'Rsa Encrypt', self.secret_key2)
            

class All:
      def encipher(self, msg):
            from random import randint
            self.msg = msg.upper()
            self.key = randint(2, 52)
            self.msg = Shift().encipher(self.msg, self.key)
            print(self.msg)

def demo():
      from numpy import matrix
      '''
      shift = Shift()
      print(shift.encipher('Hell o Wo46, rld', 14))
      print(shift.decipher('VSZ46 35ZCKCF ZR', 14))
      affine = Affine()
      print(affine.encipher('AFF INE 8 /?CI PHER'))
      print(affine.decipher('IHHW VCS69  583(WFRCP'))
      '''
      vigenere = Vigenere()
      print(vigenere.encipher('AT 7*&*&*&Ta CK A 5t%^3D9 AwN 4^9', 'Lemon'))
      print(vigenere.decipher('QRG36K kt HR246^*#&@^ZQE B356PR', 'Encrypt'))
      #'''
      #hill = Hill()
      #print(hill.encipher('A578^&c9()():"{}\'T&', matrix([[6, 24, 1], [13, 16, 10], [20, 17, 15]])))
      #print(hill.decipher('   Hi 46%34:{}:{}66a4T;;;\'9(', matrix([[3, 3], [2, 5]])))
      #rsa = Rsa()
      #print(rsa.encipher('A578^&c9()():"{}\'T&', 43, 101))
      
      #all = All()
      #print(all.encipher('HiHello'))

if __name__ == '__main__':
      demo()
            
