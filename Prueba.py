def add():
    return "Aqui va su funcion"

def sub():
    return "Aqui va su funcion"

line = "Etiqueta: add r1, #12"

diccionario = {"add":add, "sub":sub}

f = lambda x: x if x in line else None
def diferente_None():
    
list(map(f,diccionario))