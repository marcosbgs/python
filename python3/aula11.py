# 1. (n + n) são os primeiros a serem executados. Se tiver parenteses dentro de parenteses, o mais interno será executado primeiro.
# 2. ** segundo a ser executado
# 3. * / // % primeiro a multiplicação, divisão, divisão simples e resto
# 4. + - soma e subtração

conta_1 = (1 + int (0.5 + 0.5)) ** (5 + 5)
print(conta_1)