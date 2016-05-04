import operator
from random import choice, randint

def expression(lvl):
    comps={' > ':operator.gt,
       ' < ':operator.lt,
       ' <= ':operator.le,
       ' >= ':operator.ge,
       ' == ':operator.eq,
       ' != ':operator.ne
       }
    joints={' and ':operator.and_,
            ' or ':operator.or_,
            ' is not ':operator.is_not,
            ' is ':operator.is_}
    texts=[]
    exp=[]
    joint=[]
    for i in range(lvl):
        c = choice(comps.keys())
        x = randint(0,10)
        y = randint(0,10)
        txt = str(x)+str(c)+str(y)+' '
        texts.append(txt)   
        exp.append(comps[c](x,y))
        if lvl>1 and i<lvl-1:
            j=choice(joints.keys())  
            joint.append((j,joints[j]))
  
    x=1
    temp=exp[0]
    text=str(texts[0])
    for i in joint:
        k=i[0]
        v=i[1]
        text+=str(k)+str(texts[x])
        temp=v(temp,exp[x])
        x+=1
        
    boolean=temp
        
    return (text,boolean)
