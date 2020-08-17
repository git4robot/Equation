from core.symbols import Symbols
from core.errors import VersionError, CaculateError, PowerError, SymbolTypeError, SymbolNameError, EncryptError, CannotDecryptError, DecryptError

from sys import version_info
if version_info < (3, 6):
      raise VersionError
del version_info

class Linear:
      def __init__(self, equation):
            self.equation = equation.split('=')
      
      def linear(self):
            if '**' in self.equation[0] and '**' not in self.equation[1]:
                  raise PowerError(2)

def demo():
      linear1 = Linear('15a+33=849')
      linear1.linear()

if __name__ == '__main__':
      demo()

