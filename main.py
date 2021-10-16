import math

# [1, 2, 4, 6, 7, 4, 8, 9]
# [1, 2, 3, 4]
# lista[1:2]
from copy import copy, deepcopy


def are_doar_elemente_div_cu_2(lista):
    for element in lista:
        if element % 2 != 0:
            return False
    return True


def secventa_divizibila_cu_doi(lista):
    lista_secvente = []

    # lista[start:end]
    for start in range(0, len(lista)):
        for end in range(start + 1, len(lista)):
            if are_doar_elemente_div_cu_2(lista[start:end]):
                lista_secvente.append(lista[start:end])

    max_sec = []

    for secventa in lista_secvente:
        if len(secventa) > len(max_sec):
            max_sec = secventa

    return max_sec


def is_prime(numar):
    if numar < 2:
        return False
    if numar == 2:
        return True
    if numar % 2 == 0:
        return False
    for x in range(3, int(math.sqrt(numar)) + 1, 2):
        if numar % x == 0:
            return False
    return True


def gaseste_prime(lista):
    result_list = []

    for element in lista:
        if is_prime(element):
            result_list.append(element)

    return result_list


def main():
    stop = False
    lista = []
    while not stop:
        print("""
            1 -> Citire lista 1
            2 -> Citire lista 2
            3 -> Afisare numere prime
            4 -> Afisare secventa divizibila cu 2
            x -> Exit
         """)
        command = input("Alege comanda: ")
        if command == 'x':
            stop = True
        elif command == '1':
            lista = citire_lista1()
        elif command == '2':
            lista = citire_lista2()
        elif command == '3':
            lista_prime = gaseste_prime(lista)
            print(lista_prime)
        elif command == '4':
            lista_dvi_2 = secventa_divizibila_cu_doi(lista)
            print(lista_dvi_2)


def citire_lista1():
    result_list = []
    dimensiune = int(input("Dimensiune lista: "))

    while dimensiune:
        element = int(input("Introduceti un element: "))
        result_list.append(element)
        dimensiune -= 1

    return result_list

def citire_lista2():
    result_list = []
    string_lista = input("Introduceti lista: ")

    string_elemente = string_lista.split(sep=" ")

    for string_element in string_elemente:
        element = int(string_element)
        result_list.append(element)

    return result_list

# main()

# Exemplu 1
# result_list = [1, 2, 3]
# result_list2 = result_list
# result_list2.append(3)
# print(result_list)
# print(result_list2)

# Exemplu 2
# result_list = [1, 2, 3, 4, 5, 6, 7]
# print(result_list[1:3])

#[[1,2,3],[1,2,3]]

main_list = []

second_list = [1, 2, 3]
third_list = [1, 2, 3]

third_list[2] = 4

main_list.append(second_list)
main_list.append(third_list)

main_list2 = deepcopy(main_list)

main_list.append(1)
main_list[0].append(4)
# second_list.append(4)

print(main_list)
print(main_list2)