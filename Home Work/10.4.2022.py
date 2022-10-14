#Implemente uma lista duplamente encadeada circular que permita: 

#- Inserir item primeira posição; 

#- Inserir item (última posição); 

#- Inserir item em determinada posição; 

#- Buscar item de determinada posição;  

#- Buscar item por elemento; 

#- Remover item da primeira posição; 

#- Remover item da última posição; 

#- Remover item de determinada posição; 

#- Remover determinado elemento; 

#- Exibir a quantidade de elementos na lista; 

#- Exibir os elementos da lista.

# CC4P12
# Beatriz Reis - G22FAD6
# Sofia Gozzoli - F3428D6
# Giovanna Zanetti - G181719

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.InicioDaLista = None
    
    # Exibir elementos da lista
    def printLista(self):
        atual = self.InicioDaLista
         
        while atual is not None:
            print(atual.data)
            atual = atual.next
    
    # Exibir a quantidade de elementos da lista
    def quantElementos(self):
        if self.InicioDaLista is not None:
            atual = self.InicioDaLista
            proximo = atual.next
            cont = 1
            
            while proximo is not None:
                atual = atual.next
                proximo = atual.next
                cont+=1
            
            atual.next = None
            print("\nQuantidade de elementos: ",cont)
        else:
            print("Lista vazia")

    # Remover item da primeira posição 
    def removeDoComeco(self):
        
        if self.InicioDaLista is not None:
            atual = self.InicioDaLista
            self.InicioDaLista = atual.next
            del atual
        else:
            print("Lista vazia")
    
    # Remover item da última posição
    def removeDoFim (self):
        if self.InicioDaLista is not None:
            atual = self.InicioDaLista
            proximo = atual.next
            
            while proximo.next is not None:
                atual = atual.next
                proximo = atual.next
            
            atual.next = None
            del proximo
        else:
            print("Lista vazia")

    # Remover item de posição determinada
    def removeDoPonto (self, index):
        if self.InicioDaLista is not None:
            atual = self.InicioDaLista
            proximo = atual.next
            
            if index == 0: 
                Lista.removeDoComeco()
            else:
                for i in range(1,index):
                    if proximo:
                        atual = proximo
                        proximo = proximo.next
                
                atual.next = proximo.next
                del proximo
        else:
            print("Lista vazia")
            
  # Remover determinado elemento
    def removeElemento(self, index):
       atual = self.InicioDaLista
       anterior = None
       found = False

       while not found:
           if atual.data == index:
               found = True
           else:
               anterior = atual
               atual = atual.next
       if anterior == None:
           self.InicioDaLista = atual.next
       else:
           anterior.next = atual.next

    # Item inserido na primeira posição - ajustar
    def insereNoComeco(self, elemento):
        if self.InicioDaLista is None:
            atual = self.InicioDaLista

            novoNo = Node(elemento)
            novoNo.next = atual
            self.InicioDaLista = novoNo
            
        else:
            novoNo = Node(elemento)
            self.InicioDaLista = novoNo

    # Item inserido na posição determinada
    def insereNoPonto (self, index):
        cont = 0
        atual = self.InicioDaLista

        while cont<index-1 and atual is not None:
            cont +=1
            atual = atual.next
        
        if index == 1:
            novoNo = Node(elemento)
            novoNo.next = atual
            self.InicioDaLista = novoNo
        else:
            novoNo = Node(elemento)
            novoNo.next = atual.next
            atual.next = novoNo

    # Item inserido na última posição - ajustar
    def insereNoFim(self, elemento):
        if self.InicioDaLista is not None:
            atual = self.InicioDaLista
            
            while atual is not None:
                atual = atual.next

            novoNo = Node(elemento)
            novoNo.next = atual.next
    
        else:
            novoNo = Node(elemento)
            self.InicioDaLista = novoNo

    # Buscar item de posição determinada
    def buscaPosicao (self, index):
        if self.InicioDaLista is not None:
            atual = self.InicioDaLista
            proximo = atual.next
            
            if index == 0: 
                print("Elemento encontrado na posição",index, ": ", atual.data)
            else:
                for i in range(1,index):
                    if proximo:
                        atual = proximo
                        proximo = proximo.next
                    
                atual.next = proximo.next
                print("Elemento encontrado na posição",index, ": ", proximo.data)
        else:
            print("Lista vazia")

# Buscar item por elemento
    def buscaElemento (self,elemento):
            atual = self.InicioDaLista
            found = False;
                
            while atual != None and not found:
                if atual.data == elemento:
                    found = True
                    print("Elemento encontrado: ",elemento)
                else:
                    atual = atual.next
            
            if (found == False):
               print("Elemento não encontrado: ",elemento)
               
               
Lista = LinkedList()
meuNo = Node(10)
meuNo1 = Node(11)
meuNo2 = Node(12)
meuNo3 = Node(13)
meuNo4 = Node(0) 
Lista.InicioDaLista = meuNo

meuNo.next = meuNo1
meuNo1.next = meuNo2
meuNo2.next = meuNo3
meuNo3.next = meuNo4

Lista.quantElementos()

print("\nLista: ") 
Lista.printLista()

print("\nRemover item da última posição: ") 
Lista.removeDoFim()
Lista.printLista() 

print("\nRemover item da primeira posição: ") 
Lista.removeDoComeco()
Lista.printLista()

print("\nRemover item de posição determinada: ")
index = int(input("Escolha a posição do nó que deseja remover: "))
Lista.removeDoPonto(index)
Lista.printLista()

print("\nExcluir elemento: ")
elemento = int(input("Digite o elemento que deseja excluir: "))
Lista.removeElemento(elemento)
Lista.printLista()

print("\nInserir no começo da lista: ")
elemento = int(input("Digite o valor que deseja inserir: "))
Lista.insereNoComeco(elemento) #ajustar
Lista.printLista()

print("\nInserir no final da lista: ")
elemento = int(input("Digite o valor que deseja inserir: "))
Lista.insereNoFim(elemento) #ajustar
Lista.printLista()

print("\nInserir na posição determinada: ") 
index = int(input("Escolha a posição que deseja inserir o item: "))
elemento = int(input("Digite o valor que deseja inserir: "))
Lista.insereNoPonto(elemento) 
Lista.printLista()

print("\nBuscar elemento pela posição: ")
index = int(input("Digite a posição do valor que deseja buscar (começando do 0): "))
Lista.buscaPosicao(index)

print("\nBuscar elemento: ")
elemento = int(input("Digite o elemento que deseja buscar: "))
Lista.buscaElemento(elemento) #ajustar
Lista.printLista()
