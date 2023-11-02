#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    count = len(sys.argv)
    sum = 0
    for i in range(count - 1):
        sum += int(sys.argv[i + 1])
    print(sum)
