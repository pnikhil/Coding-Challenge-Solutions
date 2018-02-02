if __name__ == '__main__':
    n = int(input())
    l = input().split()
    int_list = set(map(int,l))
    print(sorted(list(int_list))[-2])