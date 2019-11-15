def readSize(Path):
    ret = {}
    with open(Path) as f:
        lines = f.readlines()
        pair = []
        for line in lines:
            line = line.strip()
            line = line.replace('(', '')
            line = line.replace(')', '')
            line = line.split(',')
            for i in range(int(len(line) / 2)):
                pair.append([int(line[(2 * i)]), int(line[(2 * i) + 1])])
            ret['A'] = pair[0:int( len(pair) / 2)]
            ret['B'] = pair[int( len(pair) / 2):]
    return ret


