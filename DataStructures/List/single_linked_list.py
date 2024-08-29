import list_node as nd

def new_list():
    newlist = {"first": None, "last":None, "size":0}
    return newlist

def add_first(lista,element):
    nodo = nd.new_single_node(element)
    if lista["size"] == 0:
        lista["first"] = nodo
        lista["size"]+=1
    else:
        primero_antes = lista["first"]
        nodo["next"] = primero_antes
        lista["first"] = nodo
        lista["size"]+=1
    return lista

def add_last(lista, element):
    nodo = nd.new_single_node(element)
    if lista["size"] == 0:
        lista["first"] = nodo
        lista["last"] = nodo
        lista["size"]+=1
    else:
        lista["last"]["next"] = nodo 
        lista["last"] = nodo
        lista["size"]+=1
    return lista

def is_empty(lista):
    if lista["size"] == 0:
        return True
    else:
        return False
    
def size(lista):
    return lista["size"]

def first_element(lista):
    if is_empty(lista) == False:
        return nd.get_element(lista["first"])

def last_element(lista):
    if is_empty(lista) == False:
        return nd.get_element(lista["last"])
    
def get_element(lista,pos):
    if pos < 0:
        raise IndexError("La posición debe ser mayor o igual a cero.")
    i = 0
    current = lista["first"]
    while i < lista["size"]:
        if i == pos:
            return nd.get_element(current)
        i+=1
        current = current["next"]
        


def interator(lista):
    current = lista["first"]
    lista_n = []
    while current != None:
        lista_n.append(nd.get_element(current))
        current = current["next"]
    return lista_n
        
        
