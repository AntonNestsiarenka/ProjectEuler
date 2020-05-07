from datetime import datetime
import euler_project

def task1():
    """
       Найдите сумму всех чисел меньше 1000, кратных 3 или 5.
       Find the sum of all numbers less than 1000, multiples of 3 or 5.
    """
    lst_data = euler_project.gen_multiple_lst(3, 5, 1000)
    sum = euler_project.sum_of_list_items(lst_data)
    print(sum)

def task2():
    """Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона.
       Find the sum of all the even elements of the Fibonacci series that do not exceed four million.
    """
    fibonacci_sequence = euler_project.gen_fibonacci_sequence()
    sum = euler_project.sum_even_fibonacci_numbers(fibonacci_sequence)
    print(sum)

def task3():
    """Каков самый большой делитель числа 600851475143, являющийся простым числом?
       What is the largest divisor of 600851475143 being a prime number?
    """
    all_simple_dividers = euler_project.create_all_simple_dividers_of_number(600851475143)
    max_simple_divider = max(all_simple_dividers)
    print(max_simple_divider)

def task4():
    """
       Найдите самый большой палиндром, полученный умножением двух трехзначных чисел.
       Find the largest palindrome obtained by multiplying two three-digit numbers.
    """
    max_palindrom = euler_project.search_max_palindrom(2)
    print(max_palindrom)

def task5():
    """
       Какое самое маленькое число делится нацело на все числа от 1 до 20?
       What is the smallest number divisible entirely by all numbers from 1 to 20?
    """
    result = euler_project.least_multiple()
    print(result)

def task6():
    """
       Найдите разность между суммой квадратов и квадратом суммы первых ста натуральных чисел.
       Find the difference between the sum of the squares and the square of the sum of the first hundred natural numbers.
    """
    delta = euler_project.delta_sum_of_squares_and_square_of_sum(100)
    print(delta)

def task7():
    """
       Какое число является 10001-ым простым числом?
       Which number is the 10001st prime number?
    """
    simple_number = euler_project.get_simple_number(10001)
    print(simple_number)

def task8():
    """
       Наибольшее произведение четырех последовательных цифр в нижеприведенном 1000-значном числе равно 9 × 9 × 8 × 9 = 5832.
       The largest product of four consecutive digits in the 1000-digit number below is 9 × 9 × 8 × 9 = 5832.

        73167176531330624919225119674426574742355349194934
        96983520312774506326239578318016984801869478851843
        85861560789112949495459501737958331952853208805511
        12540698747158523863050715693290963295227443043557
        66896648950445244523161731856403098711121722383113
        62229893423380308135336276614282806444486645238749
        30358907296290491560440772390713810515859307960866
        70172427121883998797908792274921901699720888093776
        65727333001053367881220235421809751254540594752243
        52584907711670556013604839586446706324415722155397
        53697817977846174064955149290862569321978468622482
        83972241375657056057490261407972968652414535100474
        82166370484403199890008895243450658541227588666881
        16427171479924442928230863465674813919123162824586
        17866458359124566529476545682848912883142607690042
        24219022671055626321111109370544217506941658960408
        07198403850962455444362981230987879927244284909188
        84580156166097919133875499200524063689912560717606
        05886116467109405077541002256983155200055935729725
        71636269561882670428252483600823257530420752963450

        Найдите наибольшее произведение тринадцати последовательных цифр в данном числе.
        Find the largest product of thirteen consecutive digits in a given number.
    """
    max_product = euler_project.largest_product_of_consecutive_digits(13)
    print(max_product)

def task9():
    """
       Существует только одна тройка Пифагора, для которой a + b + c = 1000.
       Найдите произведение abc.
       There is only one Pythagorean triple for which a + b + c = 1000.
       Find the product abc.
    """
    result = euler_project.get_special_three_of_pythagoras(1000)
    product = 1
    for i in result:
        product *= i
    print(product)

def task10():
    """
       Найдите сумму всех простых чисел меньше двух миллионов.
       Find the sum of all primes less than two million.
    """
    sum = euler_project.sum_of_simple_numbers(2000000)
    print(sum)

def task11():
    """
       В таблице 20×20 (внизу) четыре числа на одной диагонали выделены красным.
       In the 20 × 20 table (bottom), four numbers on the same diagonal are highlighted in red.

       08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
       49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
       81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
       52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
       22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
       24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
       32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
       67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
       24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
       21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
       78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
       16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
       86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
       19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
       04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
       88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
       04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
       20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
       20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
       01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48

       Произведение этих чисел 26 × 63 × 78 × 14 = 1788696.
       Каково наибольшее произведение четырех подряд идущих чисел в таблице 20×20, расположенных в любом направлении (вверх, вниз, вправо, влево или по диагонали)?
       The product of these numbers is 26 × 63 × 78 × 14 = 1788696.
       What is the largest product of four consecutive numbers in a 20 × 20 table located in any direction (up, down, right, left, or diagonally)?
    """
    max_product = euler_project.max_all_product_in_matrix_2d(4)
    print(max_product)

def task12():
    """
       Каково первое треугольное число, у которого более пятисот делителей?
       What is the first triangular number with more than five hundred divisors?
    """
    triangl_number = euler_project.triangular_number_with_a_large_number_of_divisors(500)
    print(triangl_number)

def task13():
    """
       Найдите первые десять цифр суммы ста 50-значных чисел. Сто 50-значных чисел находятся в файле set_of_big_number.txt
       Find the first ten digits of the sum of one hundred 50-digit numbers. One hundred 50-digit numbers are in the file set_of_big_number.txt.
    """
    object_big_number = euler_project.sum_all_big_numbers()
    print(object_big_number.big_number[:10])

def task14():
    """
       Какой начальный элемент меньше миллиона генерирует самую длинную последовательность Коллатца?
       Which starting element of less than a million generates the longest Collatz sequence?
    """
    first_number = euler_project.first_number_of_longest_Collatz_sequence(1000000)
    print(first_number)

def task15():
    """
       Начиная в левом верхнем углу сетки 2×2 и имея возможность двигаться только вниз или вправо, существует ровно 6 маршрутов до правого нижнего угла сетки.
       Сколько существует таких маршрутов в сетке 20×20?
       Starting in the upper left corner of the grid 2 × 2 and having the ability to move only down or to the right, there are exactly 6 routes to the lower right corner of the grid.
       How many such routes exist in a 20 × 20 grid?
    """
    number_of_paths = euler_project.number_of_all_possible_paths_on_grid(20)
    print(number_of_paths)

def task16():
    """
       2 ** 15 = 32768, сумма цифр этого числа равна 3 + 2 + 7 + 6 + 8 = 26.
       Какова сумма цифр числа 2 ** 1000?
       2 ** 15 = 32768, the sum of the digits of this number is equal to 3 + 2 + 7 + 6 + 8 = 26.
       What is the sum of the digits of a number 2 ** 1000?
    """
    sum_of_digits = euler_project.sum_of_digits_of_big_power_number(2, 1000)
    print(sum_of_digits)


start_time = datetime.now()
task16()
print('{} {}'.format('Lead time:', datetime.now() - start_time))


