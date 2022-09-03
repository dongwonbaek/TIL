def family(**kwargs):
    for peo, name in kwargs:
        print(peo, ":", name)
family(father = 'John', mother = 'Jane', me = 'John Jr.')