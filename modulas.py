import math1
import math2
import time
import pyautogui
def input2(pa):
    pp=pyautogui.prompt(pa)
    return pp
def c2(pb,pc):
    pp=pyautogui.confirm(pb,'box',pc)
    return pp
def print2(pd):
    pyautogui.alert(pd)
t1 = time.time()
l = str(c2('English(E) or Persian(P)?',['E','P']))
if l == 'E':
    M = ['Tom number', 'Prime number', 'factorial', 'three n plas one', 'Screening method']
    C1 = ['totel', 'subtraction', 'Multiplication', 'Division', 'Unknown']
    d = str(c2('math(M) or calculator(C)?',['M','C']))
    if d == 'M':
        c = str(c2('Ok.Enter your work.',M))
        a = int(input2('Enter Number #1='))

        if c == 'Tom number':
            math2.math3(a).Tom()
        if c == 'factorial':
            math2.math3(a).factorial()
        if c == 'Prime number':
            math2.math3(a).ravesh_gharbol()
        if c == 'three n plas one':
            math2.math3(a).moadeleye_3n()
        if c == 'Screening method':
            math2.math3(a).ravesh_gharbol()
    elif d == 'C':
        c = str(c2('Ok.Enter your work=',C1))
        a = int(input2('Enter Number#1='))
        b = int(input2('Enter Number#2='))
        if c == 'totel':
            math2.calculator(a, b).totel()
        if c == 'subtraction':
            math2.calculator(a, b).subtraction()
        if c == 'Multiplication':
            math2.calculator(a, b).Multiplication()
        if c == 'Division':
            math2.calculator(a, b).Division()
        if c == 'Unknown':
            math2.calculator(a, b).Unknown()
if l == 'P':
    M = ['اعداد تام', 'اعداد اول', 'فاکتوريل', 'سه ن بعلاوه يک', 'روش غربال']
    C1 = ['جمع', 'منها', 'ضرب', 'تقسيم', 'نا_معلوم']
    d = str(c2('رياضي(M) or ماشين حساب(C)?',['M','C']))
    if d == 'M':
        c = str(c2('خب.کارتان چيست؟',M))
        a = int(input2('عدد اول='))
        if c == 'اعداد تام':
            math1.math2(a).Tom()
        if c == 'فاکتوريل':
            math1.math2(a).factorial()
        if c == 'اعداد اول':
            math1.math2(a).ravesh_gharbol()
        if c == 'سه ن بعلاوه يک':
            math1.math2(a).moadeleye_3n()
        if c == 'روش غربال':
            math1.math2(a).ravesh_gharbol()
    elif d == 'C':
        c = str(c2('خب کارتان چيست=',C1))
        a = int(input2('عدد اول='))
        b = int(input2('عدد دوم='))
        if c == 'جمع':
            math1.calculator(a, b).جمع()
        if c == 'منها':
            math1.calculator(a, b).منها()
        if c == 'ضرب':
            math1.calculator(a, b).ضرب()
        if c == 'تقسيم':
            math1.calculator(a, b).تقسيم()
        if c == 'نا_معلوم':
            math1.calculator(a, b).نا_معلوم()

t2 = time.time()
print2('time requast='+str(t2 - t1))
