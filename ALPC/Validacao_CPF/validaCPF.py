def valida_cpf(cpf):
    cpf = ''.join(c for c in cpf if c.isdigit())
    tamanho = len(cpf)
    
    if tamanho == 11 and cpf != cpf[0] * 11:
        return 1
    else:
        return 0

def encontra_digitos(cpf):
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    resto = (soma * 10) % 11
    digito1 = 0 if resto == 10 else resto

    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    resto = (soma * 10) % 11
    digito2 = 0 if resto == 10 else resto

    return 1 if cpf[-2:] == f'{digito1}{digito2}' else 0

colocar_cpf = input('Digite seu CPF para ver se é válido: ')
colocar_cpf = ''.join(c for c in colocar_cpf if c.isdigit())

resultado_cpf = 1 if valida_cpf(colocar_cpf) == 1 and encontra_digitos(colocar_cpf) == 1 else 0
print("CPF válido") if resultado_cpf == 1 else print("CPF inválido")
