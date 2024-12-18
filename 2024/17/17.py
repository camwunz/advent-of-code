from collections import *
from heapq import *
from math import *
from statistics import *
from itertools import *
from functools import *
from aocd import submit, data

FILENAME = "17/input.txt"

def get_input_from_file():
    with open(FILENAME) as f:
        lines = f.read().splitlines()
    return lines


def main2(A, lines):

    res = 0

    registers = {}
    registers['A'] = A
    registers['B'] = int(lines[1].split()[-1])
    registers['C'] = int(lines[2].split()[-1])
    program = [int(x) for x in lines[4].split()[-1].split(',')]
    # print(registers, program)

    def get_operand(operand):
        if 0<= operand <= 3:
            return operand
        if operand == 4:
            return registers['A']
        if operand == 5:
            return registers["B"]
        if operand == 6:
            return registers['C']
        raise TypeError(operand) 
    out = []
    i = 0
    while True:
        if not (0 <= i < len(program)):
            break
        opcode = program[i]
        combo_operand = get_operand(program[i+1])
        literal_operand = program[i+1]
        increase_2 = True

        if opcode == 0:
            num = registers['A']
            dem = 2 ** combo_operand
            registers['A'] = num//dem
        elif opcode == 1:
            registers['B'] = registers['B'] ^ literal_operand
        elif opcode == 2:
            registers['B'] = combo_operand % 8
        elif opcode == 3:
            if registers["A"] != 0:
                i = literal_operand
                increase_2 = False
        elif opcode == 4:
            registers['B'] = registers['B'] ^ registers['C']
        elif opcode == 5:
            out.append(combo_operand % 8)
        elif opcode == 6:
            num = registers['A']
            dem = 2 ** combo_operand
            registers['B'] = num//dem
        elif opcode == 7:
            num = registers['A']
            dem = 2 ** combo_operand
            registers['C'] = num//dem

        if increase_2:
            i += 2


    return ",".join([str(x) for x in out])

def main(lines):
    n = 1
    base_pow = 0
    while True:
        l = 8 ** base_pow 
        n = 6 * 8 ** base_pow
        # split for 3, 0
        if l >= 8:
            r = n+(l//8), n+(l // 8 * 2)
            d = r[1]-r[0]
            if d >= 8:
                r2 = r[0]+(d//8), r[0]+(d // 8 * 2)
                print(r2)
                for A in range(*r2):
                    ans = main2(A, lines)
                    nums = ans.split(",")
                    if nums[-1] == "0":
                        print(A, ans, len(ans.split(',')))
                        input()
        base_pow += 1
    return main2(A, lines)

def main3():
    n = 1
    base_pow = 0
    while True:
        res = encoded_program(n)
        if res[0] == [2]:
            print(n, res)
            input()
        n += 1

# @cache
goal = [2, 4, 1, 3, 7, 5, 0, 3, 4, 3, 1, 5, 5, 5, 3, 0]
def encoded_program(A):
    B = 0
    C = 0
    out = []
    while True:
        B = (A % 8) ^ 3
        C = A // (2 ** B)
        A = A // 8
        B = (B ^ C) ^ 5
        out.append(B % 8)

        # if out[-1] != goal[len(out)-1]:
        #     return None
        if A == 0:
            break
    return out


def binary_search():
    low = 35184372088832
    high =  281474976710656
    goal_len = 17
    while True:
        print(high, low)
        mid = (high + low) // 2
        out_mid = encoded_program(mid)
        out_mid_low = encoded_program(mid-1)
        if len(out_mid_low) == goal_len-1 and len(out_mid) == goal_len:
            return out_mid
        if len(out_mid) >= goal_len:
            high = mid
        else:
            low = mid

def extra():
    a = 35184372088832
    b = 281474976710656
    d = (b-a)//100000
    for n in range(a, b):
        print(n)
        if (n-a) % d == 0:
            print("space", n)
        res = encoded_program(n)
        if res and res == [2,4,1,3,7,5,0,3,4,3,1,5,5,5,3,0]:
            print(n)
            break

def find_bound(low, high, digit, index):
    sep = 8
    low = low
    high = high + 1

    d = (high - low) // sep
    ans = []
    for split in range(0, 8):
        bound = low + d * split
        l_output = bound, encoded_program(bound)
        h_output = (bound + d - 1), encoded_program((bound + d - 1))
        if l_output[1][index] == digit == h_output[1][index]:
            ans.append((l_output[0], h_output[0]))
    return ans

def find_bound_wrapper(bounds, digit, index):
    output = []
    for l, h in bounds:
        output += find_bound(l, h, digit, index)
    print(output)


look_array = [(236580836040232, 236580836040239), (236580836040296, 236580836040303), (236580836040320, 236580836040327), (236580836040360, 236580836040367), (236580836040376, 236580836040383), (236580840234536, 236580840234543), (236580840234600, 236580840234607), (236580840234624, 236580840234631), (236580840234664, 236580840234671), (236580840234680, 236580840234687), (236581645540904, 236581645540911), (236581645540968, 236581645540975), (236581645540992, 236581645540999), (236581645541032, 236581645541039), (236581645541048, 236581645541055)]
find_bound_wrapper(look_array,
    2,
    -16
)

def find():
    low = 228698550000000
    high = 246290604621823
    d = (high - low) // 100
    for val in range(low, high):
        if val % 10000000 == 0:
            print(val)
        res = encoded_program(val)
        if res == goal:
            print(res)
            return


# somewhere between
# 215504279044096 - 219902325555199
# or 
# 233096465088512 - 237494511599615

# low = 228698550000000
# high = 246290604621823
# find_bound()
# binary_search()
# main3()
# another()
# start of 16 = 211106232532992
# end of 16 =   246290604621823
# find()
# find_bound()
# 0 ends with 215184372088832
# if __name__ == "__main__":
#     # test input
#     # print("TEST INPUT:")
#     # lines = get_input_from_file()
#     # res = main(lines)
#     # if res is not None:
#     #     print(res)
#     # print()
#     # # real input
#     # input("waiting for input...")
#     print("REAL INPUT")
#     res = main3(data.splitlines())
#     if res is not None:
#         print(res)
#         to_submit = input("Would you like to submit? (y/n): ").strip().lower()
#         if to_submit == "y":
#             print("\x1B[3mSubmitting...\x1B[0m")
#             submit(res, reopen=False)
#         else:
#             print("\x1B[3mNot submitting...\x1B[0m")
#     else:
#         print("\x1B[3mNo answer returned, not submitting\x1B[0m")
