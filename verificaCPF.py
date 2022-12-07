# PROGRAMA PARA VERIFICAR CPF VÁLIDO

def calculaDV(x):
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


entrada = input('Digite o CPF: ')

cpfFirsts = []
cpfDV = []

for k in range(len(entrada)):
    if k < 9:
        cpfFirsts.append(int(entrada[k]))
    if k > 8:
        cpfDV.append(int(entrada[k]))

if len(cpfFirsts)+len(cpfDV) > 11 or len(cpfFirsts)+len(cpfDV) < 11:
    print('CPF inválido: O CPF deve ter 11 dígitos!')
else:
    dig1, dig2 = calculaDV(cpfFirsts)

if cpfDV[0] == dig1 and cpfDV[1] == dig2:
    print('O CPF {}{}{}.{}{}{}.{}{}{}-{}{} é válido!'.format(cpfFirsts[0],
                                                           cpfFirsts[1],
                                                           cpfFirsts[2],
                                                           cpfFirsts[3],
                                                           cpfFirsts[4],
                                                           cpfFirsts[5],
                                                           cpfFirsts[6],
                                                           cpfFirsts[7],
                                                           cpfFirsts[8],
                                                           cpfDV[0],
                                                           cpfDV[1]))
else:
    print('O CPF {}{}{}.{}{}{}.{}{}{}-{}{} não é válido!'.format(cpfFirsts[0],
                                                                 cpfFirsts[1],
                                                                 cpfFirsts[2],
                                                                 cpfFirsts[3],
                                                                 cpfFirsts[4],
                                                                 cpfFirsts[5],
                                                                 cpfFirsts[6],
                                                                 cpfFirsts[7],
                                                                 cpfFirsts[8],
                                                                 cpfDV[0],
                                                                 cpfDV[1])
          )