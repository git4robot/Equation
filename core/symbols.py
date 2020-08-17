from errors import SymbolTypeError, SymbolNameError, SymbolOrderError
def Symbols(symbol):
      try: intsym = int(symbol)
      except ValueError:
            pass
      else:
            if not isinstance(symbol, str):
                  raise SymbolTypeError(symbol)
            if not isinstance(intsym, str):
                  raise SymbolNameError(intsym)
      return symbol
            
def demo():
      #Symbols(87)  #Error
      #Symbols('9487')  #Error
      print(Symbols('2s'))

if __name__ == '__main__':
      demo()
