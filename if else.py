'''' x = 10;

print("Bom dia!");

if x < 0:
    print('Boa tarde!');

print('Boa Noite');

'''''
hora: int;

hora = int(input('Digite uma hora do dia: '));

if hora < 12:
    print('Bom dia!');
elif hora < 18:
    print('Boa tarde!');
else:
    print('Boa noite!');
