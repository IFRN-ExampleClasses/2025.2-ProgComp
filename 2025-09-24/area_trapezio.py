'''
	Desenvolva um programa em Python que solicite ao usuário os valores da 
   base maior, base menor e altura de um trapézio e, em seguida, calcule e 
   exiba a sua área. 
	
   Utilize a fórmula da área do trapézio.
'''

baseMaior = float(input('Informe o valor da Base Maior: '))

baseMenor = float(input('Informe o valor da Base Menor: '))

altura = float(input('Informe o valor da Altura: '))

area = (baseMaior + baseMenor) * altura / 2

print(f'A área do trapézio é {area:.1f}')