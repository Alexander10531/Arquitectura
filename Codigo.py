import re

class Codigo:

    def __init__(self,archivo):
        # Registros, tambien se encuentran los valores lineaText, lineaData, error, descrError que se usan para el control del programa
        self.registro = {"lineaText": None, "lineaData": None, "error" : None, "descrError" : None,"r0":"valor","r1":"valor","r2":"valor","r3":"valor","r4": "valor","r5":"valor","r6":"valor","r7":"valor","r8":"valor","r9":"valor","r10":"valor","r11":"valor","r12":"valor","r13":"valor","r14":"valor","r15":"valor",} 
        # Diccionario de instrucciones en las que se encuentran los nombres de las instrucciones y estan asociados a las funciones
        self.instrucciones = {"mov":self.mov,"add":self.add,"sub":self.sub,"ldr":self.ldr,".word":self.word,"wfi":self.wfi}
        # Diccionario de direccionas RAM asociadas asociadas en un inicio a un valor 0x00000000 en su valor por defecto, que sera definido
        # con la funcion crear_memoria()
        self.etiquetas = {}
        self.ram = {}
        self.ram = self.crear_memoria(self.ram)
        # Lectura de linea por linea del texto en cuestion
        self.codigo = {}
        self.archivo = archivo
        # Funcion que lee el codigo a "ensamblar"   
        self.leer_codigo(self.archivo, self.codigo)

    def getRegistro(self):
        return self.registro
    
    def getInstrucciones(self):
        return self.instrucciones
    
    def getMemoria(self):
        return self.ram
    
    def getCodigo(self):
        return self.codigo
    
    def getArchivo(self):
        return self.archivo
    
    def getError(self):
        return self.error
    
    def getCodigo(self):
        return self.codigo
    
    def getDescrError(self):
        return self.descrError
    
    def getLineaText(self):
        return self.registro["lineaText"]
    
    def getLineaData(self):
        return self.registro["lineaData"]

    def mov(self,line):
        #evalúa la sintaxis de la función mov con un registro y una constante
        lineaConst=re.search(r"mov r([0-9]{1}|1[0-5]{1}), #([0-9]{1}|1[0-9]{1,2}|[2-9][0-9]|2[0-5]{2})$", line)
        #evalúa la sintaxis de la función mov con dos registros
        lineaRegis=re.search(r"mov r([0-9]{1}|1[0-5]{1}), r([0-9]{1}|1[0-5]{1})$", line)
        if lineaConst != None:
            registro=re.search(r"r([0-9]{1,2})", line).group() #para extraer el registro usado en la función
            constante=re.search(r"#([0-9]{1,3})", line).group().split("#") #para extraer la constante
            self.registro[registro]=hex(int(constante[1])).upper()
        elif lineaRegis != None:
            registro1=re.search(r"r([0-9]{1,2})", line).group() #para extraer el primer registro usado en la función
            registro2=re.search(r", r([0-9]{1,3})", line).group().split(" ") #para extraer el segundo registro usado en la función
            self.registro[registro1]=self.registro[registro2[1]].upper()    
        else:
            print("Error de sintaxis en: ", line)
            exit() #se sale del programa si encuentra un error de sintaxis
    
    def add(self,line):
        print("add")

    def sub(self,line):
        return "Aqui va su codigo :')"

    def ldr(self,line):
        return "Aqui va su codigo :')"

    def word(self,line):
        if len()

    def wfi(self):
        pass
    
    def leer_codigo(self,archivo,codigo):
        # Se realiza la lectura del archivo
        archivoR = open(archivo,"r")
        # Variable centinela que lleva el control de las lineas de codigo.
        i = 1

        # Bucle encargado de realizar la asocicion linea a linea del codigo.
        while True:
            # Lectura de la n-esima linea
            line = archivoR.readline()
            # Si no existe una linea mas se detiene el ciclo.
            if not line:
                break
            # Si la linea es una cadena de texto que carece de caracteres entonces no la almacenara en 
            # el diccionario.
            elif line.isspace() == False:
                # Se realiza un arreglo sobre la linea de codigo capturada, de modo que si posee espacios a su 
                # izquierda o derecha los elimina, ademas elimina el caracter asociado al salto de linea
                line = re.sub("[\\n]","",line.strip())
                # Se realiza un condicional dado que si encuentra la etiqueta .data la almacena para poder realizar 
                # un control sobre los bloques
                if line == ".data":
                    if self.registro["lineaData"] == None:
                        self.registro["lineaData"] = i
                    else:
                        self.codigoError = 1
                        self.descrError = ".data ya fue definido"
                # El mismo proceso del condicional anterior 
                elif line == ".text":
                    if self.registro["lineaText"] == None:
                        self.registro["lineaText"] = i
                    else:
                        self.codigoError = 2
                        self.descrError = ".text ya fue definido"
                codigo[i] = line
            i += 1
        # Eliminacion de las variables y cerrado del archivo ya usado
        del(i)
        archivoR.close()
        del(line)

    def crear_memoria(self,memoria): 
        # Creacion de un diccionario que asocia la direccion de memoria con su valor por defecto, 0x00000000
        return {str(hex(i)).upper() : "0x00000000" for i in range(537329664,537329700)}

    def exec_text(self,lineaText):
        # Esta liea evalua si existe una etiqueta llemada .text
        if lineaText != None:
            lineaText+= 1
            # Bucle que se usa para evaluar cada una de las lineas de codigo utilizadas
            while True:
                if lineaText in self.codigo and lineaText != self.registro["lineaData"]:
                    self.comprobar_instruccion(lineaText)
                elif lineaText == self.registro["lineaData"] or lineaText > max(self.codigo) + 1:
                    break
                lineaText+= 1
    
    def comprobar_instruccion(self,line):
        # Se crea una funcion lambda que servira para saber si el elemento x, se encuentra en en la linea 
        # de codigo que se quiere ejecutar         
        f = lambda x: x if x in self.codigo[line] else None
        
        #Funcion map que se usa en conjunto con la funcion "f" y luego filtra todos los elementos None
        # solo para quedarse con las direcciones
        lista = list(filter(None,list(map(f,self.instrucciones))))
        
        # Si la lista retorna mas de dos valores eso quiere decir que el usuario ingreso mas de dos valores 
        # en su codigo. Ejemplo mov add r1, #255
        if len(lista) == 1:
            self.instrucciones[lista[0]](self.codigo[line])
    
    def exec_data(self,lineaData):
        # La logica de esta funcion se maneja de la misma manera que exec_text
        if lineaData != None:
            lineaData +=1
            while True:
                if lineaData in self.codigo and lineaData != self.registro["lineaText"]:
                    self.comprobar_instruccion(lineaData)
                elif lineaData == self.registro["lineaText"] or lineaData > max(self.codigo) + 1:
                    break
                lineaData+=1

codigo = Codigo("Codigo.txt")
codigo.exec_data(codigo.registro["lineaData"])
print("-------------------------------------")
codigo.exec_text(codigo.registro["lineaText"])
