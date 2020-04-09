import time

def timer(func):
    def wrapper(*args):
        avg_time = 0
        run = 10
        for _ in range(run):
            start_time = time.time()
            result = func(*args)
            end_time = time.time()
            avg_time += (end_time - start_time)
            
        avg_time /= run
        print("Среднее время выполнения  %.5f секунд" % avg_time)
        return result
        
    return wrapper

@timer
def fib(num):
    su3 = su5 = su35 = su7 = 0
    for i in range(0,num):
        if (i % 3 == 0 and i % 5 == 0):
            #print("FizzBuzz",i)
            su35 += i

        elif (i % 3 == 0) :
           # print("Fizz",i)
            su3 += i

        elif (i % 5 == 0):
           # print("Buzz",i)
            su5 += i
        
        elif (i % 7 == 0):
           # print("Buzz",i)
            su7 += i
        rez = su5 + su3 + su35 + su7
    return rez
    

def main():
    
    num = int(input("Введите лимит расчета функции "))
    result = fib(num)
    print ("Результат ", result) 
    
if __name__ == "__main__":
    main()