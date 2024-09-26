def generate_fibonacci(number:int):
    a=0
    b=1
    res=[]
    ctr=0
    while ctr<int(number):
        res.append(a)
        sum=a+b
        a=b
        b=sum
        
        ctr+=1
    return res
if __name__ == '__main__':
    numbers=generate_fibonacci(5)
    print("Fibonacci Numbers Are: ")
    for i in numbers:
        print(i)