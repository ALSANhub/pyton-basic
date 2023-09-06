salario1: float; salario2: float;
nome1: str; nome2: str;
idade: int;
sexo: str;


nome1 = input ("Nome da primeira pessoa: ");
salario1 = float(input("salario da primeira pessoa: "));

nome2 = input ("Nome da segunda pessoa: ");
salario2 = float(input("salario da segunda pessoa: "));

idade = int(input("digite uma idade "));
sexo = input("Digite um sexo (F/M): ");

print(f"nome 1: {nome1}");
print(f"Salario 1: {salario1:.2f}");
print(f"nome 2: {nome2}");
print(f"Salario 2: {salario2:.2f}");
print(f"idade: {idade}");
print(f"Sexo: {sexo}");
