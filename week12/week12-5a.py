a = 1500000000 # 把數字變很大，變成15億
b = 2000000000 # 把數字變很大，變成20億
ans = 0
for i in range(1, a+1):
  if a%i==0 and b%i==0:
    print( i, '有整除')
    ans = 1
print(ans, '是最大公因數')