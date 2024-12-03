with open('input.txt') as f:
    lines = f.readlines()

    #mul(***,***)
    ans = 0
    for line in lines:
        for i in range(len(line)):
            if line[i:i+4] == 'mul(':
                #print(line[i:i+12])
                inside = line[i:i+12].split('mul(')[1].split(')')
                if len(inside) < 2:
                    #print(line[i:i+12] + ' bad')
                    continue
                inside = inside[0]
                inside = inside.split(',')
                if len(inside) != 2:
                    #print(line[i:i+12] + ' bad')
                    continue
                #print(line[i:i+12] + ' good')
                ans += (int(inside[0]) * int(inside[1]))
    print(ans)