# Expresion Regular: ^([A-z]{1}[\w_]*:)?\s*\.word\s+(0x[0-9A-Fa-z]+|0b[0-1]+|\d+)$
# Valores a tener presente cuando k = 32 [-2147483648,2 147 483 647]
#
import re

class Codigo:

    def __init__(self,archivo):
        # Registros, tambien se encuentran los valores lineaText, lineaData, error, descrError que se usan para el control del programa
        self.registro = {"lineaText": None, "lineaData": None,"lineaError": None, "error" : None, "descrError" : None,"r0":"valor","r1":"valor","r2":"valor","r3":"valor","r4": "valor","r5":"valor","r6":"valor","r7":"valor","r8":"valor","r9":"valor","r10":"valor","r11":"valor","r12":"valor","r13":"valor","r14":"valor","r15":"valor",} 
        # Diccionario de instrucciones en las que se encuentran los nombres de las instrucciones y estan asociados a las funciones
        self.instrucciones = {"mov":self.mov,"add":self.add,"sub":self.sub,"str":self.strp,"ldr":self.ldr,".word":self.word,"wfi":self.wfi}
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

    def ca2(self,numero,k):
        vMin=-2**(k-1)
        vMax=2**(k-1)-1
        if numero < 0 and k in [8,16,32] and numero>=vMin and numero<=vMax:
            not_=int("1"*k,2)
            numero='{0:0{1}b}'.format(abs(numero),k)
            ca1=not_-int("%s"%numero,2)
            ca2 = ca1+1
            return '0b{0:0{1}b}'.format(ca2,k)
        elif numero >=0:
            return numero
        elif not(numero>=vMin and numero<=vMax):
            self.registro["error"] = 5
            self.registro["descrError"] = "El valor no puede almacenarse en k = " + str(k)
        elif not(k in [8,16,32]):
            self.registro["error"] = 6
            self.registro["descrError"] = "K no valido"

    def mov(self,line):
        #evalúa la sintaxis de la función mov con un registro y una constante
        lineaConstDec=re.search(r"mov r([0-9]|1[0-5]), #(([0-9]|[1-9][0-9]|2[0-5]{2}))$", line)
        lineaConstBin=re.search(r"mov r([0-9]|1[0-5]), #0b([0-1]{1,8})$", line)
        lineaConstHex=re.search(r"mov r([0-9]|1[0-5]), #(0X|0x)([A-F0-9]{1,2}|[a-f0-9]{1,2})$", line)
        #evalúa la sintaxis de la función mov con dos registros
        lineaRegis=re.search(r"mov r([0-9]|1[0-5]), r([0-9]|1[0-5])$", line)

        registro=re.search(r"r([0-9]{1,2})", line).group() #para extraer el registro usado en la función
        if lineaConstDec != None: 
            constante=re.search(r"#([0-9]{1,2})", line).group().split("#") #para extraer la constante
            self.registro[registro]='0x{0:0{1}X}'.format(int(constante[1]),8)
        elif lineaConstBin != None:
            constante=re.search(r"#0b([0-1]{1,8})", line).group().split("0b")
            self.registro[registro]='0x{0:0{1}X}'.format(int(str(constante[1]),2),8) 
        elif lineaConstHex != None:
            constante=re.search(r"#(0X|0x)([A-F0-9]{1,2}|[a-f0-9]{1,2})", line).group().split("0x")
            self.registro[registro]='0x{0:0{1}X}'.format(int(str(constante[1]),16),8) 
        elif lineaRegis != None: 
            registro2=re.search(r", r([0-9]{1,2})", line).group().split(" ") #para extraer el segundo registro usado en la función
            self.registro[registro]=self.registro[registro2[1]]
        else:
            print("Error de sintaxis en: ", line)
            exit() #se sale del programa si encuentra un error en la sintaxis
    
    def add(self,line):
        print("add")

    def sub(self,line):
        return "Aqui va su codigo :')"

    def ldr(self,line):
        return "Aqui va su codigo :')"

    def strp(self,line):
        pass

    def obtener_direccion(self,valor = None):
        return hex(537329664 + list(self.ram.values()).index("0x00")) if valor == None else hex(537329664 + list(self.ram.values()).index(valor))

    def word(self,line):
        if re.search(r"^([A-z]{1}[\w_]*:)?\s*\.word\s+(0x[0-9A-Fa-z]+|0b[0-1]+|\d+)$",line) != None:
            if re.search(r"^[\w\d]+:",line) == None:
                pass
            else:
                pass
        else:
            self.registro["error"] = 4
            self.registro["descrError"] = "Error de sintaxis"
            self.registro["lineaError"] = self.obtener_llave(line,self.codigo)

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
        return {str(hex(i)).upper() : "0x00" for i in range(537329664,537329700)}

    def exec_text(self,lineaText):
        # Esta liea evalua si existe una etiqueta llemada .text
        if lineaText != None:
            lineaText+= 1
            # Bucle que se usa para evaluar cada una de las lineas de codigo utilizadas
            while True:
                if lineaText in self.codigo and lineaText != self.registro["lineaData"] and self.registro["error"] == None:
                    self.comprobar_instruccion(lineaText)
                elif lineaText == self.registro["lineaData"] or lineaText > max(self.codigo) + 1 or self.registro["error"] != None:
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
        else:
            self.registro["error"] = 4
            self.registro["descrError"] = "Error de sintaxis"
            self.registro["lineaError"] = line

    def exec_data(self,lineaData):
        # La logica de esta funcion se maneja de la misma manera que exec_text
        if lineaData != None:
            lineaData +=1
            while True:
                if lineaData in self.codigo and lineaData != self.registro["lineaText"] and self.registro["error"] == None:
                    self.comprobar_instruccion(lineaData)
                elif lineaData == self.registro["lineaText"] or lineaData > max(self.codigo) + 1 or self.registro["error"] != None:
                    break
                lineaData+=1

    def obtener_llave(self,linea,diccionario):
        
        #Obtiene los valores y las llaves de un diccionario
        valores = list(diccionario.values())
        llaves = list(diccionario.keys())

        # if de una sola linea que devuelve la llave de un diccionario
        return llaves[valores.index(linea)] if linea in valores else None

codigo = Codigo("Codigo.txt")
