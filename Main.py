import re
def crear_memoria(memoria): 
    for i in range(537329664,537329700):
        memoria[str(hex(i)).upper()] = "0x00000000"
    return memoria

def variables():
    global registro
    global memoria
    global instrucciones
    global codigo
    global archivo
    global lineTex
    global lineData
    global error
    global descripcionError 
    lineTex = None
    lineData = None
    codigo = {}
    memoria = {}
    instrucciones = ["mov", "ldr","add","sub","neg","xor"]
    registro = {"r0":"valor","r1":"valor","r2":"valor","r3":"valor","r4": "valor","r5":"valor","r6":"valor","r7":"valor","r8":"valor","r9":"valor","r10":"valor","r11":"valor","r12":"valor","r13":"valor","r14":"valor","r15":"valor"}
    memoria = crear_memoria(memoria)

def leer_codigo(archivo,codigo):

    archivoR = open(archivo,"r")
    i = 0
    
    while True:
        line = archivoR.readline()
        if not line:
            break
        elif line.isspace() == False:
            line = re.sub("[\\n]","",line.strip())
            if line == ".data":
                if lineData == None:
                    lineData = i
                else:
                    codigoError = 1
                    descripcionError = ".data ya fue definido" 
            elif line == ".text":
                if lineTex == None:
                    lineTex = i
                else:
                    codigoError = 2
                    descripcionError = ".text ya fue definido"
            codigo[i] = line
            i += 1
    del(i)
    archivoR.close()
    del(line)

variables() 
leer_codigo("Codigo.txt",codigo)
print(lineTex)
print(lineData)