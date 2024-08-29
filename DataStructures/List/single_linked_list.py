def new_list():
    newlist = {"first": None, "last":None, "size":0}
    return newlist

def add_first(lista,element):
    lista["first"].insert(0,element)
    lista["size"]+=1
    return lista

def add_last(lista, element):
    lista["last"].append(element)
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
        return lista["first"]["info"]

def last_element(lista):
    if is_empty(lista) == False:
        return lista["last"]["info"]
    
def get_element(lista,pos):
    if pos < 0:
        raise IndexError("La posición debe ser mayor o igual a cero.")
    i = 0
    current = lista["first"]
    while i < lista["size"]:
        if i == pos:
            return current["info"]
        i+=1
        current["next"]
        
def delete_element(lista,pos):
    if is_empty(lista) == True:
        raise IndexError("la lista no puede estar vacia")
    else:
        
        
