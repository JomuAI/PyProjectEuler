def run(n, i = 2):
    while i*i < n:
        while n%i == 0:
            n = int(n/i)
        i = i+1
    return n

if __name__ == "__main__":
    print(run(600851475143))