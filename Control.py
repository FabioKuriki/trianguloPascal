from Model import Model

class Control:
    def __init__(self):
        self.model = Model()

    def solicitarNum(self):
        while(self.model.linha < 0 ):
            self.model.linha = int(input("Informe um número: "))

            if(self.model.linha < 0 ):
                print("Informe um valor positivo!!")

        print(self.model.trianguloPascal())