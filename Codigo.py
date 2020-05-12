import re

class Codigo:

    def __init__(self,archivo):
        self.registro = {"lineaText": None, "lineaData": None, "error" : None, "descrError" : None,"r0":"valor","r1":"valor","r2":"valor","r3":"valor","r4": "valor","r5":"valor","r6":"valor","r7":"valor","r8":"valor","r9":"valor","r10":"valor","r11":"valor","r12":"valor","r13":"valor","r14":"valor","r15":"valor",} 
        self.instrucciones = {"mov":self.mov,"add":self.add,"sub":self.sub,"ldr":self.ldr}
        self.ram = {}
        self.ram = self.crear_memoria(self.ram)
        self.codigo = {}
        self.archivo = archivo
        self.error = None 
        self.descrError = None   
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
        return self.registro["lineaText"]

    def mov(self,line):
        #evalúa la sintaxis de la función mov con un registro y una constante
        lineaConst=re.search(r"mov r([0-9]{1}|1[0-5]{1}), #([0-9]{1}|1[0-9]{1,2}|[2-9][0-9]|2[0-5]{2})$", line)
        #evalúa la sintaxis de la función mov con dos registros
        lineaRegis=re.search(r"mov r([0-9]{1}|1[0-5]{1}), r([0-9]{1}|1[0-5]{1})$", line)
        if lineaConst != None:
            registro=re.search(r"r([0-9]{1,2})", line).group() #para extraer el registro usado en la función
            constante=re.search(r"#([0-9]{1,3})", line).group().split("#") #para extraer la constante
            self.registro[registro]=hex(int(constante[1]))
        elif lineaRegis != None:
            registro1=re.search(r"r([0-9]{1,2})", line).group() #para extraer el primer registro usado en la función
            registro2=re.search(r", r([0-9]{1,3})", line).group().split(" ") #para extraer el segundo registro usado en la función
            self.registro[registro1]=self.registro[registro2[1]]
        else:
            print("Error de sintaxis en: ", line)
            exit() #se sale del programa si encuentra un error de sintaxis
    
    def add(self,line):
        print("add")

    def sub(self,line):
        return "Aqui va su codigo :')"

    def ldr(self,line):
        return "Aqui va su codigo :')"

    def leer_codigo(self,archivo,codigo):
        
        archivoR = open(archivo,"r")
        i = 1

        while True:
            line = archivoR.readline()

            if not line:
                break
            elif line.isspace() == False:
                line = re.sub("[\\n]","",line.strip())
                if line == ".data":
                    if self.registro["lineaText"] == None:
                        self.registro["lineaText"] = i
                    else:
                        self.codigoError = 1
                        self.descrError = ".data ya fue definido" 
                elif line == ".text":
                    if self.registro["lineaText"] == None:
                        self.registro["lineaText"] = i
                    else:
                        self.codigoError = 2
                        self.descrError = ".text ya fue definido"
                codigo[i] = line
            i += 1

        del(i)
        archivoR.close()
        del(line)

    def crear_memoria(self,memoria): 
        for i in range(537329664,537329700):
            memoria[str(hex(i)).upper()] = "0x00000000"
        return memoria

    def exec_text(self,lineaText):
        if lineaText != None:
            lineaText+= 1
            while True:
                if lineaText in codigo.codigo:
                    self.comprobar_instruccion(lineaText)
                elif lineaText > max(codigo.codigo):
                    break
                lineaText+= 1

    def comprobar_instruccion(self,line):
        
        f = lambda x: x if x in self.codigo[line] else None
        
        lista = list(filter(None,list(map(f,self.instrucciones))))
        if len(lista) == 1:
            self.instrucciones[lista[0]](self.codigo[line])
        else:
            pass

codigo = Codigo("Codigo.txt")
codigo.exec_text(codigo.registro["lineaText"])
print(codigo.registro)
