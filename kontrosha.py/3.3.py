def slova(w, l):
    for i in range(len(w)-1, -1, -1):
        if w[i].starwith(l):
            return w(i)
    return "not found"
slova(w, l)
    