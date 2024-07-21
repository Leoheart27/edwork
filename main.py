class LinkedListNode:
    def __init__(self, color, num, next=None):
        self.num = num
        self.color = color
        self.next = next
        self.data = f'[{color}, {num}]'

class ListaEncadeadaSimples:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = LinkedListNode(value=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = LinkedListNode(value=elem)
                node = node.next


    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        return 'Lista de pacientes - > ' + ' - '.join(nodes)
    
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next
        
    def inserir_com_prioridade(self, node): # insere o cartão no inicio da lista se o cartão for A ou o numero for menor que o head
        if self.head is None or self.head.color == 'V':
            node.next = self.head
            self.head = node
            return
        if self.head == 'A' and self.head.num > node.num:
            node.next = self.head
            self.head = node
            return
        current_node = self.head
        while current_node.next is not None and current_node.next.num < node.num and current_node.next.color != 'V':
            current_node = current_node.next
        node.next = current_node.next
        current_node.next = node
        return

    def inserir_sem_prioridade(self, node): # insere o cartão no final da lista
        if self.head is None:
            self.head = node
            return
        
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next

        current_node.next = node
        return
    
    def atender_paciente(self): #printa o primeiro paciente da fila no console e o remove da lista
        if self.head is None:
            return
        print(f'Atendendo paciente de cartão cor {self.head.color} e número {self.head.num}')
        self.head = self.head.next 
        



linked_list = ListaEncadeadaSimples()

def inserir(): #função que inseri os cartões na lista
            card_type = input('Informe a cor do cartão (A/V): ').upper()
            card_number = int(input('Número do cartão: '))
            if card_type == 'V':
                linked_list.inserir_sem_prioridade(LinkedListNode(card_type, card_number))
            elif card_type == 'A':
                linked_list.inserir_com_prioridade(LinkedListNode(card_type, card_number))
            else:
                print('Opcão inválida')

# Opções de menu
running = True
while running: # Console de interação com o usuiário
    print('1 - Adcionar paciente na fila')
    print('2 - Mostrar pacientes na fila')
    print('3 - Chamar paciente')
    print('4 - Sair')

    option = int(input('Escolha uma opção: '))

    if option == 1:
        inserir()
    elif option == 2:
        print(linked_list)
    elif option == 3:
        linked_list.atender_paciente()
    elif option == 4:
        print('Saindo...')
        running = False
    else:
        print('Opcão inválida')