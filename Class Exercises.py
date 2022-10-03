class No:

    def __init__ (self, valor, dir, esqr):
        self.item= valor
        self.dir= dir 
        self.esqr= esqr
        self.pai = None

class ARVOREBINARIA:
     def __init__(self):
      self.raiz=None


raiz = No (20,None,None)
No1 = No (36, None, None)
No2 = No (12, None, None)
No3 = No (5, None, None)
No4 = No (5, None, None)
raiz.dir = No1
raiz.esqr = No2, No3, No4
        


print (raiz.dir.item)
print (raiz.item)
