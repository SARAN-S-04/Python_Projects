
def func():
    a=375
    t=a
    x=0
    y=0
    while(t!=0):
        x=t%10
        y=y+x
        t/=10
    else:
        if(y/10>0):
            t=y
            x=0
            y=0
            func()
        else:
            print(y)
            
# func()
# # print(35.7%10)
# def func():
#     a = 375
#     t = a
#     x = 0
#     y = 0
#     while t != 0:
#         x = t % 10
#         y = y + x
#         t //= 10  # Use integer division to remove the last digit
#     else:
#         if t == 0:  # Terminate recursion when t becomes 0
#             print(y)
#         else:
#             print("Error: t is negative!")  # Handle unexpected cases

func()
