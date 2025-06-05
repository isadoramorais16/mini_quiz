print ("Seja muito bem vindo ao Quiz")
resp_user = input("Quer começar? (sim/não)")

if resp_user != "sim":
    quit()

XP = 0

print("Qual é o propósito da estrutura de controle "SE" (if)? \n (A) repetir um bloco de código várias vezes \n (B) Tomar decisões baseadas em condições específicas \n (C) Declarar variáveis \n (D) Imprimir texto na tela \n")
answer1 = input("Resposta: ").lower()

if answer1 == "b":
    (print("Correto!"))
    XP = XP + 10
    (print("Parabéns, você recebeu 10 pontos de XP!"))


else: 
    print("Incorreto")

print("O que é uma variável em programação? \n (A) um valor constante que não pode ser alterado \n (B) um espaço de memória que armazena um valor que pode ser alterado \n (C) uma função que executa uma tarefa específica \n (D) um tipo de dado que só pode armazenar números \n")
answer2 = input("Resposta: ").lower()

if answer2 == "b":
    XP = XP + 10
    (print("Parabéns, você recebeu 10 pontos de XP!"))
    
else: 
    print("Incorreto")

print(f"Quiz 1 finalizado... Pontuação: {XP}/20")