if __name__ == '__main__':
    l = []
    for _ in range(int(input())):
        l.append([input(),float(input())])
    second_highest = sorted(list(set(score for name,score in l)))[1]
        #print(sorted(list(set(score for name,score in l))))
        #print(second_highest)
    for name, score in sorted(l):
        if score == second_highest:
            print(name)
