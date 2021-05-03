lattice_record = {}

def lattice_paths(x, y):
    if (x,y) in lattice_record.keys():
        return lattice_record[(x,y)]
    elif min([x,y]) == 0:
        return(1)
    else:
        if (x-1,y) not in lattice_record.keys():
            lattice_record[(x-1,y)] = lattice_paths(x-1,y)
        if (x,y-1) not in lattice_record.keys():
            lattice_record[(x,y-1)] = lattice_paths(x,y-1)
        return(lattice_record[x-1,y]+lattice_record[x,y-1])
print(lattice_paths(20,20))
