letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
one ="EHRVXGAOBQUSIMZFLYNWKTPDJC"

def setup():
    print("wiring = [",end="")
    for i in range(len(letters)):
        print("["+str(i)+", "+str(one.index(letters[i]))+"], ",end="")
    print("]")

setup()