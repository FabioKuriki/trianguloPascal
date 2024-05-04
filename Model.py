class Model:
    def __init__(self):
        self.num = 0
        self.linha = -1
        self.pascal = []
        self.numerador = []
        self.denominador = []
        self.pascalCompleto = ""

    # Coeficiente binominal == n! / p! * (n - p)!
    # Onde n(numerador) é igual ao número de linhas, e p(denominador) o número de colunas,
    # sendo que a cada linha, aumenta uma coluna

    def trianguloPascal(self):
        self.linha += 1

        # Instanciando as listas
        for i in range(self.linha):
            if(i == 0):
                self.numerador.append(i)
                self.denominador.append(i)
                self.pascal.append(i)
            else:
                self.numerador.append([i] * (i + 1))
                self.denominador.append([i] * (i + 1))
                self.pascal.append([i] * (i + 1))

        # Alterando os números na lista denominador
        for i in range(1, self.linha):
            self.num = 0
            for j in range(i+1):
                self.denominador[i][j] = self.num
                self.num += 1

        # Criando uma lista que guarda os números no triângulo Pascal
        for i in range(0, self.linha):
            if(i == 0):
                self.pascal[0] = self.fatorial(0)
            else:
                for j in range(i+1):
                    self.pascal[i][j] = self.fatorial(self.numerador[i][j]) // (self.fatorial(self.denominador[i][j]) * self.fatorial((self.numerador[i][j] - self.denominador[i][j])))


        # Montando o triângulo Pascal
        for i in range(0, self.linha):
            if(i == 0):
                self.pascalCompleto = "1\n"
            else:
                for j in range(i+1):
                    if(j != i):
                        self.pascalCompleto += f"{self.pascal[i][j]} "
                    else:
                        self.pascalCompleto += f"{self.pascal[i][j]}\n"


        return f"\n{self.pascalCompleto}"

    def fatorial(self, numeroFatorado):
        num2 = numeroFatorado

        while (numeroFatorado > 1):
            num2 = num2 * (numeroFatorado - 1)
            numeroFatorado -= 1

        if(numeroFatorado == 0):
            num2 = 1


        return num2