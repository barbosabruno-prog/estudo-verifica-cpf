# PROGRAMA PARA VERIFICAR CPF VÁLIDO

def calcula_dv(x):
    smt1 = 0
    cont = 10
    for i in range(len(x)):
        smt1 += x[i] * cont
        cont -= 1

    chkdig1 = 11 - (smt1 % 11)
    if chkdig1 > 9:
        dv1 = 0
    else:
        dv1 = chkdig1
    x.append(dv1)

    smt2 = 0
    cont = 11
    for j in range(len(x)):
        smt2 += x[j] * cont
        cont -= 1

    chkdig2 = 11 - (smt2 % 11)
    if chkdig2 > 9:
        dv2 = 0
    else:
        dv2 = chkdig2

    return dv1, dv2

def imprime_cpf(cpf_numeros, cpf_dv, veracidade):
    full_cpf = ''

    for i in range(len(cpf_numeros)-1):
        if i == 3 or i == 6:
            full_cpf += '.'
            full_cpf += str(cpf_numeros[i])
        else:
            full_cpf += str(cpf_numeros[i])

    if veracidade == True:
        print(f'O CPF {full_cpf}-{cpf_dv[0]}{cpf_dv[1]} é valido!')
    else:
        print(f'O CPF: {full_cpf}-{cpf_dv[0]}{cpf_dv[1]} não é valido!')
        
    return None

def verifica_cpf():
    entrada = input('Digite o CPF: ')

    cpf_corpo = []
    cpfDV = []

    for k in range(len(entrada)):
        if k < 9:
            cpf_corpo.append(int(entrada[k]))
        if k > 8:
            cpfDV.append(int(entrada[k]))

    if len(cpf_corpo)+len(cpfDV) > 11 or len(cpf_corpo)+len(cpfDV) < 11:
        print('CPF inválido: O CPF deve ter 11 dígitos!')
    else:
        dig1, dig2 = calcula_dv(cpf_corpo)

    if cpfDV[0] == dig1 and cpfDV[1] == dig2:
        is_valido = True
        imprime_cpf(cpf_corpo, cpfDV, is_valido)


    else:
        is_valido = False
        imprime_cpf(cpf_corpo, cpfDV, is_valido)

verifica_cpf()
