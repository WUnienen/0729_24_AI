#猜數字遊戲
import random
import pyinputplus as pyip
def p():
    min=1
    max=100
    c=0
    t=random.randint(1,100)
    print("===========猜數字==========")
    while True:
        c+=1
        k=pyip.inputInt(f"猜數字範圍{min}-{max}:",min=min,max=max)
        if k==t:
            print(f"對了 答案是{k}")
            print(f"您猜了{c}次")
            break
        elif k>t:
            print("在小一點")
            max=k-1
        elif k<t:
            print("再大一點")
            min=k+1
        print(f"您已經猜了{c}次")

while True:
    p()
    i=pyip.inputYesNo('您還要繼續嗎(yes/no)')
    if i=='no':
        break
print("應用程式結束")