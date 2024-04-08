#등차 수열
#초항이 1이고 공차가 3인 등차수열
#an = an + 3 ,a1 = 1
def seq(n):
    if(n == 1):
        return 1
    return seq(n-1) + 3

a = seq(int(input("enter n : ")))
print("number is : ", a)