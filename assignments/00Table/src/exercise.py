import math
import os

def main():
    os.system("clear")
    x= 0.5
    print ("{'x':>8}{'y':>8} {'z':>8}")
    print ("----------------------------------------")
    
    while x <= 10:
        y = 3 * math.pow(x,2) + 7* x - 15
        z = y - 2 * math.pow(x,2)
        # ocho posiciones con dos decimales
        print (f"x:{x:8.2f}      y:{y:8.2f}       z:{z:8.2f}")
        x += 0.5

if __name__=='__main__':
    main()
