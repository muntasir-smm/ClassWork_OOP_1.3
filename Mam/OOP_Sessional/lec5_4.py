def pairDiff(n):
    m = []
    for i in len(n)-1:
        m = m.append(abs(n[i], n[i+1])) 
        print(m)
    return m
def main():
    n = [3, 4, 56, 55, 33, 22]
    m = []
    m = pairDiff(n)
    print(m)