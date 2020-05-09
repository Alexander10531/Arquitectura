import re

class Code:

    def __init__(self,archivo):
        self.registro = {"r0":"valor","r1":"valor","r2":"valor","r3":"valor","r4": "valor","r5":"valor","r6":"valor","r7":"valor","r8":"valor","r9":"valor","r10":"valor","r11":"valor","r12":"valor","r13":"valor","r14":"valor","r15":"valor"} 
        self.instrucciones = ["mov", "ldr","add","sub","neg","xor"]
        self.memoria = {}
        self.memoria = self.crear_memoria(self.memoria)
        self.codigo = {}
        self.archivo = archivo
        self.error = None 
        self.codigo = {}
        self.descrError = None   
        self.lineText = None
        self.lineData = None
        self.leer_codigo(self.archivo, self.codigo)

    def leer_codigo(self,archivo,codigo):
        
        archivoR = open(archivo,"r")
        i = 1

        while True:
            line = archivoR.readline()

            if not line:
                break
            elif line.isspace() == False:
                line = re.sub("[\\n]","",line.strip())
                print(line)
                if line == ".data":
                    if self.lineData == None:
                        self.lineData = i
                    else:
                        self.codigoError = 1
                        self.descrError = ".data ya fue definido" 
                elif line == ".text":
                    if self.lineText == None:
                        self.lineText = i
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

    
