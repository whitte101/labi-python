def bilet(s):
    if len(s) != 6:
        return False
    
    first3 = s[0] + s[1] + s[2]

    second3 = s[3] + s[4] + s[5]

    if first3 == second3:
        return True
    else:
        return False

if __name__ == '__main__':
    s = input()
    bilet(s)








