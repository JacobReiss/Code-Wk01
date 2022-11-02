a = 1
b = 2
c = 3
d = 4
e = 5
f = 6
g = 7
h = 8
i = 9

count = 0

while count != 9:
    
    x = input("Place an x on the board (1-9): ")
    
    if x == "1":
        a == "x"

    print (f"{a}|{b}|{c}")
    print ("-+-+-")
    print (f"{d}|{e}|{f}")
    print ("-+-+-")
    print (f"{g}|{h}|{i}")
    
    print (count)
    count+=1
    print (count)