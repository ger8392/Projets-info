
from dataclasses import dataclass
@dataclass()
class Rationnel:
    p:int
    q:int
def frac_to_str (rationnel:Rationnel)->str:

    p2=str(rationnel.p)
    q2=str(rationnel.q)
    if rationnel.q==1 or (rationnel.p==0 and rationnel.q !=0):
        fraction=str(p2)
    elif rationnel.q==0:
        fraction=str("Le denominateur ne peut pas valoir 0")
    else:
        fraction= str(p2 + "/" + q2)
    return fraction

def reduce (ratio:Rationnel)->Rationnel:
    if ratio.q<0:
        ratio.p=-ratio.p
        ratio.q=-ratio.q
    ratio2=Rationnel(ratio.p,ratio.q)
    if ratio.p<0:
        ratio.p=-ratio.p
    if ratio.q<0:
        ratio.q=-ratio.q
    while (ratio.p !=0 and ratio.q !=0):
        if ratio.p>=ratio.q:
            ratio=Rationnel((ratio.p)%(ratio.q),ratio.q)
        else:
            ratio=Rationnel((ratio.p),(ratio.q)%(ratio.p))

    if ratio.p !=0:
        p1=int((ratio2.p)/(ratio.p))
        q1=int((ratio2.q)/(ratio.p))
    elif ratio.q !=0:
        p1=int(ratio2.p/ratio.q)
        q1=int(ratio2.q/ratio.q)
    else :
        p1=int(0)
        q1=int (0)
    ratio3=Rationnel(p1,q1)
    return (ratio3)

def add(r1:Rationnel,r2:Rationnel)->Rationnel:
    r3=Rationnel(r1.p*r2.q+r2.p*r1.q,r1.q*r2.q)
    r3=reduce(r3)
    return r3

def substract(r1:Rationnel,r2:Rationnel)->Rationnel:
    r3=Rationnel(-r2.p,r2.q)
    return(add(r1,r3))

def multiply(r1:Rationnel,r2:Rationnel)->Rationnel:
    r3=Rationnel(r1.p*r2.p,r1.q*r2.q)
    r3=reduce(r3)
    return r3

def divide (r1:Rationnel,r2:Rationnel)->Rationnel:
    r3=Rationnel(r2.q,r2.p)
    return multiply(r1,r3)




def main() -> None:
    ratio1=Rationnel(-3,5)
    ratio2=Rationnel(1,2)
    ratio3=Rationnel(2,1)
    print(frac_to_str(divide(ratio2,ratio1)))
    print(frac_to_str(divide(ratio3,ratio1)))
    print(frac_to_str(divide(ratio1,ratio1)))






if __name__=="__main__":
    main()
