import pyautogui
def print2(pa):
    pyautogui.alert(str(pa))
class arabi:
    def __init__(self,No,No2):
        self.no=No
        self.no2=No2
    def جمع(self):
        print2(self.no+self.no2)
    def منها(self):
        print2(self.no-self.no2)
    def ضرب(self):
        print2(self.no*self.no2)
    def تقسيم(self):
        print2(self.no/self.no2)
    def نا_معلوم(self):
        a=self.no
        b=self.no2
        c=int(input('کم عدد الخطوات التي تستغرقها ؟'))
        for x in range(1,c+1):
            a=(a+b)/2
            print2(a)
        d=a
        print2('الرقم النهائي ='+str(d))
class arabi1:
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
        print2("عدد الأعداد الأولية ="+str(c))
    def moadeleye_3n(self):
        w=''
        totel=0
        if self.no1==4 or self.no1==2 or self.no1==1:
            print2('الرقم المطلوب غير صحيح.')
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
            print2(str(w)+'إجابة دائمة')
            print2('العدد الاجمالي للأرقام متساوي ='+str(totel))
    def factorial(self):
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
            print2(str(self.no1)+'إنه توم.')
        else:
            print2(str(self.no1)+'ليس توم')
