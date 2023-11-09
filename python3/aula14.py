a = 'AAAA'
b = 'BBBB'
c = 1.1
string = 'a={nome1} b={nome2} c={nome3:.2f}'
formato = string.format(
  nome1=a, nome2=b, nome3=c) #se nomear um parâmetro, tem que nomear todas os outrso que vier DEPOIS DO PARÂMETRO NOMEADO
# se referindo ao nome da variavel: parâmetro
# se referindo valor da variável: argumento

print(formato)

# out of range = está fora do numero de paramtros a se procurar