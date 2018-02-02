from statistics import mean
if __name__ == '__main__':
    dic = dict()
    for _ in range(int(input())):
        record = input()
        name = record.split()[0]
        marks = list(map(float,record.split()[1:]))
        avg = mean(marks)
        dic.update({name: avg})
    search = input()
    for key, value in dic.items():
        if key == search:
            print("{:.2f}".format(value))