responses=["Welcome to smart calculator","My name is Caluam","Thanks","Sorry,this is beyond my ability "]
def extract_number_from_text(text):
    l=[]
    for t in text.split(' '):
        try:
            l.append(float(t))
        except ValueError:
            pass
    return(l)
def lcm(a,b):
    L=a if a>b else b
    while L<=a*b:
        if L%a==0 and L%b==0:
            return L
        L+=1
def hcf(a,b):
    H=a if a<b else b
    while H>=a*b:
        if H%a==0 and H%b==0:
            return H
        H-=1
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multiply(a,b):
    return a*b
def division(a,b):
    return a/b
def end():
    responses([2])
    input("Press enter key to exit")
    exit()
def myname():
    print(responses[1])
def sorry():
    print(responses[3])
operations={"PLUS":add,"ADD":add,"ADDITION":add,"SUM":add,"MINUS":sub,"SUB":sub,"SUBSTRACK":sub,"SUBSTRACTION":sub,"DIFFERENCE":sub,"MULTIPLY":multiply,"PRODUCT":multiply,"MULTIPLICATION":multiply,"DIVIDE":division,"DIVISION":division,"LCM":lcm,"LEAST COMMON MULTIPLE":lcm,"HCF":hcf,"HIGHEST COMMON FACTOR":hcf}
commands={"NAME":myname,"CLOSE":end,"EXIT":end,"END":end}





  