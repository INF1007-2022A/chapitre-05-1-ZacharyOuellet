#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List


def convert_to_absolute(number: float) -> float:
    if number >=0:
        return number
    return -number



def use_prefixes() -> List[str]:
    prefixes, suffixe = 'JKLMNOPQ', 'ack'
    names = []
    for prefix in prefixes:
        names.append(prefix+suffixe)
    return names

def is_prime(n):
    for i in range(2, int(n**(1/2))+1):
        if n % i == 0:
            return False
    return True

def prime_integer_summation() -> int:
    sum_of_primes = 0
    number_of_primes = 0
    current_number = 2
    while number_of_primes < 100:
        if is_prime(current_number):
            number_of_primes += 1
            sum_of_primes += current_number
        current_number += 1
    return sum_of_primes


def factorial(number: int) -> int:
    fact = 1
    if number <= 0:
        return 1
    for i in range(2, number+1):
        fact *= i
    return fact


def use_continue() -> None:
    for i in range(1,11):
        if i == 5:
            continue
        print(i)


def verify_ages(groups: List[List[int]]) -> List[bool]:
    result = []
    for group in groups:
        if len(group)<=3 or len(group)>10:
            result.append(False)
            continue
        if 25 in group:
            result.append(True)
            continue
        for age in group:
            if age<18:
                result.append(False)
                break
            if age > 70 and 50 in group:
                result.append(False)
                break
        else:
            result.append(True)
    return result


def main() -> None:
    number = -4.325
    print(f"La valeur absolue du nombre {number} est {convert_to_absolute(number)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 premiers nombre premier est : {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()

    groups = [
        [15, 28, 65, 70, 72], [18, 24, 22, 50, 70], [25, 2],
              [20, 22, 23, 24, 18, 75, 51, 49, 100, 18, 20, 20], [70, 50, 26, 28], [75, 50, 18, 25],
              [13, 25, 80, 15], [20, 30, 40, 50, 60], [75, 50, 100, 28]
    ]
    print(f"Les différents groupes sont: {groups}")
    print(f"L'acceptance des groupes est: {verify_ages(groups)}")


if __name__ == '__main__':
    main()
