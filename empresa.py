class Funcionario:
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario
    
    def calcular_pagamento(self):
        return self.salario
    
class Gerente(Funcionario):
    def __init__(self, nome, salario, cargo, bonus):
        super().__init__(nome, salario, cargo)
        self.bonus = bonus

    def calcular_pagamento(self):
        return self.salario + self.bonus
    
class Desenvolvedor(Funcionario):
    def __init__(self, nome, salario, cargo, horas_extras=0, valor_hora_extra=0):
        super().__init__(nome, salario, cargo)
        self.horas_extras = horas_extras
        self.valor_hora_extra = valor_hora_extra

    def calcular_pagamento(self):
        return self.salario + (self.horas_extras * self.valor_hora_extra)
    
class SistemaEmpresa:
    def __init__(self):
        self.funcionarios = []

    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)

    def processar_pagamentos(self):
        for funcionario in self.funcionarios:
            print(f"Pagamento de {funcionario.nome}: R$ {funcionario.calcular_pagamento():.2f}")

carlos = Gerente("Carlos", 8000, "Gerente de Projetos", 2000)
ana = Desenvolvedor("Ana", 5000, "Desenvolvedora", horas_extras=10, valor_hora_extra=50)

print(carlos)
print(ana)

sistema = SistemaEmpresa()
sistema.adicionar_funcionario(carlos)
sistema.adicionar_funcionario(ana)

sistema.processar_pagamentos()