# Beatriz Reis - G22FAD6 - CC4P12
# Sofia Gozzoli - F3428D6 - CC3P12
# Giovanna Zanetti - G181719 - CC4P12

class Node:
    def __init__(self, data, previous, prox):
        self.data = data
        self.previous = previous
        self.next = prox
 
class CDLinkedList:
    def __init__(self):
        self.header = Node(None, None, None)
        self.size = 0

    def empty_list(self):
        return self.size == 0
    
    #Método necessário para ser possível usar a função len()
    def __len__(self):
        return self.size

    #responsável por verificar os nós entre dois valores
    def insert_between(self, item, predecessor, successor): 
        novoNo = Node(item, predecessor, successor)
        predecessor.next = novoNo
        self.size += 1
        
        return novoNo

    def insert_first(self, data):
        self.insert_between(data, self.header, self.header.next)

    def insert_last(self, data):
        self.insert_between(data, self.header.previous, self.header)

    def insert_atPosition(self, index, elemento):
        sucessor = self.header.next
        
        if self.empty_list():
            print("Lista vazia")
        
        elif index == 0:
            self.insert_first(elemento)   

        elif index > len(Lista):
            print("Posição maior que a quantidade de itens!")
        
        else:
            for i in range(index):
                sucessor = sucessor.next
            
            succesor = sucessor.next
            predecessor = sucessor.previous
            novoNo = Node(elemento, predecessor, succesor)
            sucessor.next = novoNo

            self.size += 1
    
    def delete_node(self, node):
        predecessor = node.previous
        successor = node.next
        predecessor.next = successor
        successor.previous = predecessor
        self.size -= 1

        #armazena o elemento removido 
        element = node.data
        node.previous = node.next = node.element = None
        
        return element
    
    def delete_first(self):
        if self.empty_list():
            print("Lista vazia")
        return self.delete_node(self.header.next) 
    
    def delete_last(self):
        if self.empty_list():
            print("Lista vazia")
        return self.delete_node(self.header.previous)

    def delete_selectPosition(self, index):
        sucessor = self.header.next
        
        if self.empty_list():
            print("Lista vazia")

        else:
            if index == 0:
                self.delete_first() #deleta primeiro item com método delete_first()
            else:
                for i in range(index):
                    sucessor = sucessor.next
                
                if sucessor == self.header.previous:
                    self.delete_last() #deleta último item com método delete_last()
                else:
                    #deleta o que estiver no meio com o delete_node()
                    self.delete_node(sucessor)

    
    def delete_selectItem(self, elemento): 
        sucessor = self.header.next
        
        if self.empty_list():
            print("Lista vazia")

        else:
            if elemento == sucessor.data:
                self.delete_first() 
            else:
                while elemento != sucessor.data:
                    sucessor = sucessor.next
                  
                if sucessor.data == self.header.previous.data:
                    self.delete_last() 
                else:
                    self.delete_node(sucessor)
    
    def search_position (self, index):
        sucessor = self.header.next
        
        if self.empty_list():
            print("Lista vazia")

        elif index > len(Lista):
            print("Posição maior que a quantidade de itens!")
        
        else:
            for i in range(index):
                sucessor = sucessor.next
            print("Elemento encontrado na posição", index, ": ", sucessor.data)

    def search_element (self,elemento):
        sucessor = self.header
        found = False;
                
        while sucessor != None and not found:
            if sucessor.data == elemento:
                found = True
                print("Elemento encontrado: ",elemento)
            else:
                sucessor = sucessor.next
            
        if (found == False):
            print("Elemento não encontrado: ",elemento)

    def print_list(self):
        temp = self.header.next
        x = []
       
        while temp != None:
            x.append(temp.data)
            temp = temp.next
            
        return x

Lista = CDLinkedList()

Lista.insert_first(15)
Lista.insert_first(14)
Lista.insert_first(12)
Lista.insert_first(11)
Lista.insert_first(10)

print("Quantidade de elementos da lista:")
print(len(Lista))

print("\nLista: ") 
print(Lista.print_list())

print("\nInserir no começo da lista: ")
elemento = int(input("Digite o elemento que deseja adicionar: "))
Lista.insert_first(elemento)
print(Lista.print_list())

print("\nInserir na posição determinada: ") 
elemento = int(input("Digite o elemento que deseja adicionar: "))
index = int(input("Digite a posição que deseja inserir: "))
Lista.insert_atPosition(elemento, index) 
print(Lista.print_list())

print("\nBuscar elemento pela posição (começando do 0): ")
index = int(input("Digite a posição que deseja buscar: "))
Lista.search_position(index)
print(Lista.print_list())

print("\nBuscar elemento: ")
elemento = int(input("Digite o elemento que deseja buscar: "))
Lista.search_element(elemento)
print(Lista.print_list()) 

print("\nRemover item da primeira posição: ") 
Lista.delete_first()
print(Lista.print_list())

print("\nRemover item de posição determinada: ")
index = int(input("Escolha a posição do nó que deseja remover: "))
Lista.delete_selectPosition(index) 
print(Lista.print_list())

print("\nRemover elemento determinado: ")
elemento = int(input("Escolha o elemento que deseja remover: "))
Lista.delete_selectItem(elemento) 
print(Lista.print_list())

print("\nInserir no final da lista: ")
elemento = int(input("Digite o elemento que deseja adicionar: "))
Lista.insert_last(elemento)
print(Lista.print_list())

print("\nRemover item da última posição: ") 
Lista.delete_last()
print(Lista.print_list())
