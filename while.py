x: int;
soma : int = 0;

x = int(input('Digite o priemiro numero: '));

while x != 0:
    soma = soma + x;
    x = int(input('Digite outro numero: '));

print('SOMA = ', soma);
