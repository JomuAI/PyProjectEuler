def run(a,b):
    tot=0
    while a<4000000:
        if a%2==0:
            tot+=a
        a,b=b,a+b
    return tot
    
if __name__ == "__main__":
    print (run(1,2))