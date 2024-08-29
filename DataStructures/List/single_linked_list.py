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
    if is_empty(lista) or pos <= 0 or pos > lista["size"]:
        raise IndexError("la lista no puede estar vacia")
    else:
        i = 0
        nodo_actual = lista["first"]
        while i < pos - 1:
            nodo_actual = nodo_actual["next"]
            i += 1
        removed = nodo_actual["next"]
        nodo_actual["next"] = removed["next"]
    lista["size"] -= 1
    return lista


    
def remove_first(lista):
    if is_empty(lista): 
        raise IndexError("la lista no puede estar vacia")
    primero = lista["first"]
    siguiente = primero["next"]
    lista["first"] = siguiente 
    lista["size"] -= 1
    return primero
    
def remove_last(lista):
    if is_empty(lista):
         raise IndexError("la lista no puede estar vacia")
    else: 
        nodo = lista["first"]
        i = 0
        while i < lista["size"]-2:
            nodo_actual = nodo_actual["next"]
            i += 1
        ultimo_nodo = nodo_actual["next"]
        nodo_actual["next"] = None
        lista["size"] -= 1
        return ultimo_nodo

def insert_element(lista, elemento, pos):
    if pos < 0 or pos > lista["size"]:
        raise IndexError("Posición fuera de rango.")
    
    nuevo_nodo = {"info": elemento, "next": None} 
    if pos == 0:
        nuevo_nodo["next"] = lista["first"]
        lista["first"] = nuevo_nodo
    else:
        nodo_actual = lista["first"]
        i = 0
        while i < pos - 1:
            nodo_actual = nodo_actual["next"]
            i+=1
        nuevo_nodo["next"] = nodo_actual["next"]
        nodo_actual["next"] = nuevo_nodo
    lista["size"] += 1
    return lista   

def is_present(lista, element, cmp_function):
    nodo_actual = lista["first"]
    i = 0
    while nodo_actual is not None:
        if cmp_function(nodo_actual["data"], element) == 0:
            return i
        nodo_actual = nodo_actual["next"]
        i += 1
    return -1

def change_info(lista, pos, new_info):
    if pos < 0 or pos >= lista["size"]:
        raise IndexError("Posición fuera de rango.")

    nodo_actual = lista["first"]
    i = 0
    while i < pos:
        nodo_actual = nodo_actual["next"]
        i += 1
    nodo_actual["data"] = new_info
    return lista
