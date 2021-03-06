def decToBase(num,base):
    digits = []
    while num > 0:
        num, remainder = divmod(num, base)
        digits.append(remainder)
    return int(''.join(str(i) for i in digits[::-1]))

def permutasi(items):
    if len(items) <= 1:
        yield items
    else:
        for nextItems in permutasi(items[1:]):
            for i in range(len(nextItems) + 1):
                yield nextItems[:i] + items[0:1] + nextItems[i:]

                
def main():
    str = input("Text :")
    print(list(permutasi(str)))

if __name__ == '__main__':
    main()
