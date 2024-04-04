
# a=int(input("Nhap a: "))

# if (a%2==0): 
#    print ("chan")
# else:
#     print("le") 


# VONG LAP
# index = 0
# while index < 5:
#     print("AAAA")
#     index = index + 1


#  cho n so nguyen nhap bp, in tu 1 ->n

# n=int(input("Nhap n: "))
# i = 1
# while i < n+1:
#     print(i, end=" ")
#     i = i+1
# for i in range(1,n+1):
#     print(i)

# CODE NGAN
# for i in range(1,int(input("Nhap n: "))+1):
#     print(i) 


# CHho a, b nhap tu ban phim,  neu a>=b  in "DUNG" else in ra so chan trong doan [a,b]
# a=int(input("Nhập a: "))
# b=int(input("Nhập b: "))
# if a >=b: 
#     print('Dừng')
# else:
    # for i in range(a, b+1):
    #     if i%2==0:
    #         print(i, end = " ")
# cách nào cũng dc sài for/ while
    # while a<= b:
    #     if a%2==0:
    #         print(a)
    #     a=a+1
    
    
    
# vi tri chu t    
# a='aaaatggggggg'
# dem = 0
# for i in a:
#     if i == "t":
#         print(dem)
#         break
#     dem = dem + 1
    # dùng hàm index 
    # print(a.index('t'))
    
# in ra chung k co a
# b='aaaatggggggg'
# for i in b:
#     if i == "a":
#         continue
#     print(i, end="")

# KIỂM TRA N NHẬP TU BP SỐ NT



# n=int(input("Nhap n: "))

# if n<2:
#     print("Khong Nguyen to") 
# dem = 0
# for i in range (2, n-1):
#     if n%i==0:
#         dem=dem+1
#         break
# if dem == 0:
#     print("Nguyen to") 
# else:
#     print("Khong Nguyen to") 
        

# if n<2:
#     print("Khong Nguyen to") 
# dem = 0
# for i in range(0, n+1):
#     for i in range (2, n-1):
#         if n%i==0:
#             dem=dem+1
#             break
#     if dem == 0:
#         print(i,end="")
    # print("Nguyen to") 
# else:
#     print("Khong Nguyen to")    
# HAm kt snt: GG

# for i in range(0,n+1):
#     if(i%2==0):
#         print(i," la 1")
#     elif i%3==0:
#         print(i," la 2")
#     elif i%5==0:
#         print(i," la 3")


#  tinh tong giai thua cac so nguyen 1->n
# n=int(input("Nhap n: "))

# def tinhGiaiThua(n: int):
#     s = 1
#     for i in range(1, n+1):
#         s = s*i
#     return s

# def tinhTongGiaiThua(n:int):
#     s = 0
#     for i in range(1, n+1):
#         s = s + tinhGiaiThua(i)
#     return s
# print(tinhTongGiaiThua(n))


# def kiemTraSNT(x:int):
#     if x < 2: 
#         return 0
#     dem = 0
#     for i in range (2,x-1):
#         if(x%i==0):
#             dem = dem + 1
#         break
#     if dem == 0:
#         return 1
#     else: 
#         return 0
    
# def lietKetSNT(x:int):
#     for i in range(1,x+1):
#         if(kiemTraSNT(i)==1):
#             print(i)

# x=int(input("Nhap x: "))
# print(lietKetSNT(x))






# def TinhTong3soThuc(a:float, b:float, c:float):
#     return a+b+c
# print(TinhTong3soThuc(1.2, 3.5,5.6))


# tinh tong so le tu [a,b] tren mot dong
# print(sum([i for i in range(int(input("Nhập a: ")),int(input("Nhập b: "))+1) if i%2!=0]))
# a=int(input("Nhập a: "))
# b=int(input("Nhập b: "))
# s=[]
# for i in range(a,b+1)
#     if i%2==1
#         s.append(i)
# print("Mang s", s)
# print(sum(s))

# a=int(input("Nhập a: "))
# n = dict()
# for i in range(1,a+1):
#     n[i] = [j if j in range(1,i+1)]
# print(n)

# 

n=int(input("Nhập n: "))
a = {}
for i in range(1,n+1):
    a[i]=i*i