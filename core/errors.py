class VersionError(ImportError):
      def __str__(self):
            return f'''Equation Module Requires Python Version 3.6+.'''

class EquationError(ValueError):
      pass

class CaculateError(EquationError):
      def __init__(self, inputstr):
            self.inputstr = inputstr
      
      def __str__(self):
            return f'''Cannot caculate equation {repr(self.inputstr)}.'''

class PowerError(EquationError):
      def __init__(self, inputint):
            self.inputint = inputint
      
      def __str__(self):
            return f'''Power wrong: {repr(self.inputint)}.'''

class SymbolError(ValueError):
      pass

class SymbolTypeError(SymbolError):
      def __init__(self, symbol):
            self.symbol = symbol
            
      def __str__(self):
            return f'''Except symbol type \'str\', got \'{type(self.symbol).__name__}\'.'''

class SymbolNameError(SymbolError):
      def __init__(self, name):
            self.name = name
            
      def __str__(self):
            return f'''Invalid symbol name '{self.name}'.'''

class SymbolOrderError(SymbolError):
      def __init__(self, correct, symbol):
            self.correct = correct
            self.symbol = symbol
            
      def __str__(self):
            return f'''Except \'{self.correct}\', got \'{self.symbol}\'.'''

class CryptoError(TypeError):
      pass

class EncryptError(CryptoError):
      def __init__(self, msg, method):
            self.msg = msg
            self.method = method
            
      def __str__(self):
            return f'''Cannot encrypt \'{self.msg}\' using {self.method}.'''

class CannotDecryptError(CryptoError):
      def __init__(self, msg, method):
            self.msg = msg
            self.method = method
            
      def __str__(self):
            return f'''\'{self.msg.title()}\' cannot be decrypt by {self.method}.'''

class DecryptError(CryptoError):
      def __init__(self, msg, method):
            self.msg = msg
            self.method = method
            
      def __str__(self):
            return f'''Cannot decrypt \'{self.msg}\' using {self.method}.'''

class SecretKeyError(CryptoError):
      pass

class KeyTypeError(SecretKeyError):
      def __init__(self, key, method, type):
            self.key = key
            self.method = method 
            self.type = type
            
      def __str__(self):
            return f'''Invalid key type \'{type(self.key).__name__}\' for {self.method}, except type {self.type}.'''

class KeyNumError(SecretKeyError):
      def __init__(self, key, method, key2 = None):
            self.key = key
            self.method = method
            self.key2 = key2
            
      def __str__(self):
            if self.key2 != None:
                  return f'''Invalid key \'{self.key}\' and key \'{self.key2}\' for {self.method}.'''

            return f'''Invalid key \'{self.key}\' for {self.method}.'''
