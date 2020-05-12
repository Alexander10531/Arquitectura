import re

class Codigo:

    def __init__(self,archivo):
        self.registro = {"lineaText": None, "lineaData": None, "error" : None, "descrError" : None,"r0":"valor","r1":"valor","r2":"valor","r3":"valor","r4": "valor","r5":"valor","r6":"valor","r7":"valor","r8":"valor","r9":"valor","r10":"valor","r11":"valor","r12":"valor","r13":"valor","r14":"valor","r15":"valor",} 
        self.instrucciones = {"mov":self.mov,"add":self.add,"sub":self.sub,"ldr":self.ldr,".word":self.word,"wfi":self.wfi}
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
        return self.registro["lineaData"]

    def mov(self,line):
        print("mov")
    
    def add(self,line):
        print("add")

    def sub(self,line):
        return "Aqui va su codigo :')"

    def ldr(self,line):
        return "Aqui va su codigo :')"

    def word(self,line):
        print("Simon, vamos a reservas memoria")

    def wfi(self):
        pass
    
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
                    if self.registro["lineaData"] == None:
                        self.registro["lineaData"] = i
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
        return {str(hex(i)).upper() : "0x00000000" for i in range(537329664,537329700)}

    def exec_text(self,lineaText):
        if lineaText != None:
            lineaText+= 1
            while True:
                if lineaText in self.codigo and lineaText != self.registro["lineaData"] and lineaText < max(codigo.codigo) + 1:
                    self.comprobar_instruccion(lineaText)
                else:
                    break
                lineaText+= 1

    def comprobar_instruccion(self,line):
        
        f = lambda x: x if x in self.codigo[line] else None
        
        lista = list(filter(None,list(map(f,self.instrucciones))))
        
        if len(lista) == 1:
            self.instrucciones[lista[0]](self.codigo[line])
        

codigo = Codigo("Codigo.txt")
codigo.exec_text(codigo.registro["lineaText"])

