import itertools
def permutations(s):
    perms = ["".join(p) for p in itertools.permutations(s)]
    permsND = list(set(perms))
    return permsND