import pyautogui
def print2(pa):
    pyautogui.alert(pa)
class calculator:
    def __init__(self,No,No2):
        self.no=No
        self.no2=No2
    def totel(self):
        print2(self.no+self.no2)
    def subtraction(self):
        print2(self.no-self.no2)
    def Multiplication(self):
        print2(self.no*self.no2)
    def Division(self):
        print2(self.no/self.no2)
    def Unknown(self):
        a=self.no
        b=self.no2
        c=int(pyautogui.prompt('How far does it go?'))
        for x in range(1,c+1):
            a=(a+b)/2
            print2(a)
        d=a
        print2('final number='+str(d))
class math3:
    def __init__(self,no):
        self.no1=no
    def ravesh_gharbol(self):
        prime = [True for i in range(self.no1+1)] 
      
        p = 2
        while(p * p <= self.no1): 
                
            if (prime[p] == True): 
                    
                for i in range(p*2,self.no1+1,p): 
                    prime[i] = False
            p += 1
        c = 0
       
        for p in range(2, self.no1+1): 
            if prime[p]: 
                c += 1
        print2('Number of prime numbers '+str(c))
    def moadeleye_3n(self):
        totel=0
        w=''
        if self.no1==4 or self.no1==2 or self.no1==1:
            print2('The number is incorrect')
        else:
            while not self.no1==4:
                if self.no1%2==0:
                    self.no1=int(self.no1/2)
                    totel+=1
                    w=w+str(self.no1)+' : '
                else:
                    self.no1=self.no1*3+1
                    totel+=1
                    w=w+str(self.no1)+' : '
            print2(w+'The permanent answer')
            print2('The total number is equal to= ',totel)
    def factoriel(self):
        z=0
        for b in range(1,self.no1+1):
            z=z*b+1
        print2(z)
    def Tom(self):
        c=0
        for b in range(1,int((self.no1+1)/2)+1):
            if self.no1%b==0:
                c+=b
        if c==self.no1:
            print2(str(self.no1)+' is Tom.')
        else:
            print2(str(self.no1)+' isn\'t tom')

