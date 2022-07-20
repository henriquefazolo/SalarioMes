'''
Um trabalhador trabalha 40 horas por semana.
Escreva um algoritmo que leia o número de horas trabalhadas em cada semana de um mês,
o salário por hora e escreva o salário total do mês do funcionário (considere que o mês possua 4 semanas exatas).
'''


class SalarioMes:
    def __init__(self, numero_horas_trabalhadas, salario_hora):
        """

        :param numero_horas_trabalhadas: valor inteiro de horas trabalhadas
        :param salario_hora: valor float referente ao valor por hora trabalhada
        """
        self.numero_horas_trabalhadas = numero_horas_trabalhadas
        self.salario_hora = salario_hora
        self.semanas_mes = 4

    def salario_total(self):
        """
        Calcula o salario total do mes
        :return: Salario total do mes
        """
        salario = round((self.numero_horas_trabalhadas * self.salario_hora * self.semanas_mes), 2)
        return salario


f = SalarioMes(100, 10)
print(f.salario_total())
