class Model:
    def __init__(self):
        self.num = 0
        self.linha = -1
        self.pascal = []
        self.numerador = []
        self.denominador = []

    # Coeficiente binominal == n! / p! * (p - n)!
    # Onde n(numerador) é igual ao número de linhas, e p(denominador) o número de colunas,
    # sendo que a cada linha, aumenta uma coluna

    def trianguloPascal(self):
        self.linha += 1

        for i in range(self.linha):
            if(i == 0):
                self.numerador.append(i)
                self.denominador.append(i)
                self.pascal.append(i)
            else:
                self.numerador.append([i] * (i + 1))
                self.denominador.append([i] * (i + 1))
                self.pascal.append([i] * (i + 1))

        for i in range(1, self.linha):
            self.num = 0
            for j in range(i):
                self.denominador[i][j] = self.num
                self.num += 1

        for i in range(1, self.linha):
            for j in range(i):
                self.pascal[i][j] = self.fatorial(self.numerador[i][j]) / self.fatorial(self.denominador[i][j]) * self.fatorial((self.numerador[i][j] - self.denominador[i][j]))



        return f"{self.numerador}\n{self.denominador}"

    def fatorial(self, numeroFatorado):
        num2 = numeroFatorado

        while (numeroFatorado > 1):
            num2 = num2 * (numeroFatorado - 1)
            numeroFatorado -= 1

        return num2