if __name__ == '__main__':
    l = []
    n = int(input())
    for _ in range(n):
        cmd = input().split()
        if cmd[0] == 'print':
            print(l)
            continue
        elif len(cmd) == 3:
            cmd_exec = "l.{0[0]}({0[1]},{0[2]})".format(cmd)
            #cmd_exec = f"l.{cmd[0]}({cmd[1]},{cmd[2]})"
        elif len(cmd) == 2:
            cmd_exec = "l.{0[0]}({0[1]})".format(cmd)
        else:
            cmd_exec = "l.{0[0]}()".format(cmd)
        eval(cmd_exec)
