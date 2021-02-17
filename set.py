# #conjunto não pode haver duplicidade

conjunto = {1,3,4}
conjunto2 = {2,4,7,8}
conjuntoUni = conjunto.union(conjunto2)
conjuntoInt = conjunto.intersection(conjunto2)
print(f'União:{conjuntoUni}')
print(f'Intersecção:{conjuntoInt}')
conjuntoDif = conjunto.difference(conjunto2)
conjuntoDif2 = conjunto2.difference(conjunto)
print(f'Conjunto diferença de A e B: {conjuntoDif}')
print(f'Conjunto diferença de B e A: {conjuntoDif2}')
#diferença simetrica que só tem em um conjunto
conjuntoSim = conjunto.symmetric_difference(conjunto2)
print(f'Diferença simétrica: {conjuntoSim}')