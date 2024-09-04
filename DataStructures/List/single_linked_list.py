from DataStructures.List import list_node as nd

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




def last_element(my_list): 
    current = my_list["first"]
    
    if current is None: 
        raise IndexError("La lista está vacía.")
    
    while current["next"] is not None: 
        current = current["next"] 
    
    return current["info"]
 

    
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


def delete_element(lista, pos):
    if lista["size"] == 0 or pos < 0 or pos >= lista["size"]:
        raise IndexError("Posición fuera de rango o la lista está vacía")

    if pos == 0:
        removed = lista["first"]
        lista["first"] = removed["next"]
        if lista["first"] is None:
            lista["last"] = None
    else:
        i = 0
        nodo_actual = lista["first"]
        while i < pos - 1:
            nodo_actual = nodo_actual["next"]
            i += 1
        removed = nodo_actual["next"]
        nodo_actual["next"] = removed["next"]
        if nodo_actual["next"] is None:
            lista["last"] = nodo_actual

    lista["size"] -= 1
    return lista


    
def remove_first(lista):
    print(lista)
    if is_empty(lista): 
        raise IndexError("La lista no puede estar vacía.")
    primero = lista["first"]
    if lista["first"] == lista["last"]:
        lista["first"] = None
        lista["last"] = None
    else:
        lista["first"] = primero["next"]
    lista["size"] -= 1
    print(lista)
    return primero


def change_info(lista, pos, new_info):
    if pos < 0 or pos >= lista["size"]:
        raise IndexError("Posición fuera de rango.")
    
    if lista["first"] is None:
        raise ValueError("La lista está vacía.")
    
    nodo_actual = lista["first"]
    i = 0
    while i < pos:
        if nodo_actual is None:
            raise ValueError("El nodo en la posición solicitada no existe.")
        nodo_actual = nodo_actual["next"]
        i += 1
    if nodo_actual is not None:
        nodo_actual["info"] = new_info
    else:
        raise ValueError("No se puede cambiar la información de un nodo nulo.")
    return lista

    
def remove_last(lista):
    if is_empty(lista):
        raise IndexError("La lista no puede estar vacía")

    if lista["size"] == 1:
        ultimo_nodo = lista["first"]
        lista["first"] = None
        lista["last"] = None
        lista["size"] -= 1
        return ultimo_nodo["info"]

    nodo_actual = lista["first"]
    while nodo_actual["next"]["next"] is not None:
        nodo_actual = nodo_actual["next"]

    ultimo_nodo = nodo_actual["next"]
    nodo_actual["next"] = None
    lista["last"] = nodo_actual
    lista["size"] -= 1

    return ultimo_nodo["info"]

      

def insert_element(lista, elemento, pos):
    if pos < 0 or pos > lista["size"]:
        raise IndexError("Posición fuera de rango.")
    
    nuevo_nodo = {"info": elemento, "next": None}
    
    if pos == 0:
        nuevo_nodo["next"] = lista["first"]
        lista["first"] = nuevo_nodo
        if lista["size"] == 0:
            lista["last"] = nuevo_nodo
    else:
        nodo_actual = lista["first"]
        i = 0
        while i < pos - 1:
            if nodo_actual is None:
                raise IndexError("Posición fuera del rango.") 
            
            nodo_actual = nodo_actual["next"]
            i += 1
            
        if nodo_actual is None:
            raise IndexError("Posición fuera del rango.")  
        
        nuevo_nodo["next"] = nodo_actual["next"]
        nodo_actual["next"] = nuevo_nodo
        
        if pos == lista["size"]:
            lista["last"] = nuevo_nodo
    
    lista["size"] += 1
    return lista





def is_present(lista, element, cmp_function):
    nodo_actual = lista["first"]
    i = 0
    while nodo_actual is not None:
        if cmp_function(nodo_actual["info"], element) == 0:
            return i
        nodo_actual = nodo_actual["next"]
        i += 1
    return -1

        
def exchange(my_list, pos1, pos2):
    if pos1 == pos2:
        return my_list 
    
    prev_1 = None
    current = my_list["first"]
    while current and current["info"] != pos1:  
        prev_1 = current
        current = current["next"] 
        
    prev_2 = None 
    current_2 = my_list["first"]
    while current_2 and current_2["info"] != pos2: 
        prev_2 = current_2
        current_2 = current_2["next"]
        
    if not current or not current_2: 
        return 
    
    if prev_1:
        prev_1["next"] = current_2
    else:
        my_list["first"] = current_2 
        
    if prev_2: 
        prev_2["next"] = current
    else: 
        my_list["first"] = current 
         
    current["next"], current_2["next"] = current_2["next"], current["next"]
    
    return my_list
          

def sub_list(lista, pos, num_elem):
    if pos < 0 or num_elem < 0:
        raise ValueError("La posición y el número de elementos deben ser no negativos.")
    
    sub_lista = {
        "size": 0,
        "first": None,
        "last": None
    }
    
    current = lista["first"]
    count = 0

    while current and count < pos:
        current = current["next"]
        count += 1

    while current and num_elem > 0:
        new_node = {
            "info": current["info"],
            "next": None
        }

        if sub_lista["first"] is None:  
            sub_lista["first"] = new_node
            sub_lista["last"] = new_node
        else:
            sub_lista["last"]["next"] = new_node
            sub_lista["last"] = new_node

        sub_lista["size"] += 1
        current = current["next"]
        num_elem -= 1

    return sub_lista


def compare_elements(self, element, info, key=None):
        try:
            if key:
                element_comp = key(element)
                info_comp = key(info)
            else:
                element_comp = element
                info_comp = info
                
            if element_comp == info_comp:
                return 0
            elif element_comp > info_comp:
                return 1
            else:
                return -1
        except Exception as e:
            raise Exception(f"Error al comparar elementos: {e}")
        
                

def defaultfunction(id1, id2):
    if id1 == id2:
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1
    