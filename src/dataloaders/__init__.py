def read_tsv(path):
    with open(path, 'r') as f:
        items = map(lambda x : x.strip().split('\t'), f.readlines())
    return map(list, zip(*items))