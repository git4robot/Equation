from errors import SymbolTypeError, SymbolNameError, SymbolOrderError

def Symbols(symbol):
      global out
      nowsym = symbol.split(' ')
      try: intsym = int(symbol)
      except ValueError:
            pass
      else:
            if not isinstance(symbol, str):
                  raise SymbolTypeError(symbol)
            if not isinstance(intsym, str):
                  raise SymbolNameError(intsym)

      try:
            er = nowsym[1]
      except IndexError:
            out = nowsym[0]
            return out
      out = nowsym
      return out
            
def demo():
      #Symbols(87)  #Error
      #Symbols('9487')  #Error
      x = Symbols('x')
      print(x)

if __name__ == '__main__':
      demo()
