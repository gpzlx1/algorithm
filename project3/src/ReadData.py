def read(Path):
    with open(Path) as f:
        lines = f.readlines()
        ret = []
        for line in lines:
            ret.append(int(line))
    return ret