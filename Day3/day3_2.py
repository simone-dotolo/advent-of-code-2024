with open('input.txt') as f:
    lines = f.readlines()

    #mul(***,***)
    ans = 0
    enable = True
    for line in lines:
        for i in range(len(line)):
            if line[i:i+4] == 'do()':
                print(f'do {i}')
                enable = True
            elif line[i:i+7] == 'don\'t()':
                print(f'dont {i}')
                enable = False

            if line[i:i+4] == 'mul(':
                inside = line[i:i+12].split('mul(')[1].split(')')
                if len(inside) < 2:
                    continue
                inside = inside[0]
                inside = inside.split(',')
                if len(inside) != 2:
                    continue
                if enable:
                    ans += (int(inside[0]) * int(inside[1]))
    print(ans)