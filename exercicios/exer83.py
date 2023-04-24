# program que verifica uma expressão e retorna se ele é valida ou não

expr = str(input('Digite a expressão: '))
pilha = []
for simb in expr:
    if simb == "(":
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('A expressão é valida')
else:
    print('A expressão está errada')