print("Calculadora Juros Simples")
valor_emprestimo = input("Qual o valor do emprestimo?")
taxa = input("Qual foi a taxa de juros?") 
taxa = (float(taxa) / float(100))
tempo = ("Em quantas parcelas você precisa para pagar?")
print(float(tempo))
valor_final = float(valor_emprestimo) + (float(valor_emprestimo) * float(taxa) * float(tempo))
print(valor_final)
