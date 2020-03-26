from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.mail import EmailMessage
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from django.template.loader import get_template
from tkinter import *

class ContactForm(forms.Form):
    fname = forms.CharField(required=True)
    #lname = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message= forms.CharField(required=True)

def detail(request):
    return render(request,'contact/detail.html')
def Contact(request):
    Contact_Form = ContactForm
    if request.method == 'POST':
        form = Contact_Form(data=request.POST)
        #print("hello")

        if form.is_valid():
            fname = request.POST.get('fname')
            #lname=request.POST.get('lname')

            email = request.POST.get('email')
            subject = request.POST.get('subject')
            message=request.POST.get('message')

            template = get_template('contact/contactform.txt')
            context = {
                'fname' : fname,
                #'lname' : lname,
                'email' : email,
                'subject' : subject,
                'message' : message,

            }

            content = template.render(context)

            email1 = EmailMessage(
                "New contact form email",
                content,
                "Creative web" + '',
                ['mkjaipur13@gmail.com'],
                headers = { 'Reply To': email }
            )

            email1.send()
        #return redirect('success')
        #else:
        #    print("Not valid")


    #return render(request, 'detail.html')
    return redirect('detail')

def sudoku(request):


    sudoku = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
              [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
              [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
    house=[[],[],[],[],[],[],[],[],[]]
    row=[[],[],[],[],[],[],[],[],[]]
    column=[[],[],[],[],[],[],[],[],[]]
    id={}




    class text1():

        def __init__(self, i, x,y,countx, county,pady):




            self.typ = Text(frame, wrap=WORD, width=1, height=1, font='bold 30')
            self.typ.grid(row=x, column=y,padx=3,pady=3)
            sudoku[i] = sudoku[i] + [countx - 2]
            sudoku[i] = sudoku[i] + [county - 1]
            sudoku[i] = sudoku[i] + [0]


        def input(self, i):
            de = self.typ.get(1.0, END)
            if de == '\n':
                de = 0
            else:
                de = de[0:1]
                de = int(de)
            sudoku[i][2] = de
        def fill(self,value):
            self.typ.delete(1.0, END)
            self.typ.insert(INSERT, value)


    text2 = []


    def solve():

        for i in range(0, 81):
            text2[i].input(i)
        for i in range(0,len(sudoku)):
            if sudoku[i][0] <= 3:
                if sudoku[i][1] <= 3:
                    house[0] = house[0] + [sudoku[i]]
                elif sudoku[i][1] <= 6:
                    house[1] = house[1] + [sudoku[i]]
                elif sudoku[i][1] <= 9:
                    house[2] = house[2] + [sudoku[i]]
            elif sudoku[i][0] <= 6:
                if sudoku[i][1] <= 3:
                    house[3] = house[3] + [sudoku[i]]
                elif sudoku[i][1] <= 6:
                    house[4] = house[4] + [sudoku[i]]
                elif sudoku[i][1] <= 9:
                    house[5] = house[5] + [sudoku[i]]
            elif sudoku[i][0] <= 9:
                if sudoku[i][1] <= 3:
                    house[6] = house[6] + [sudoku[i]]
                elif sudoku[i][1] <= 6:
                    house[7] = house[7] + [sudoku[i]]
                elif sudoku[i][1] <= 9:
                    house[8] = house[8] + [sudoku[i]]
            if sudoku[i][0] == 1:
                row[0] = row[0] + [sudoku[i][2]]
            if sudoku[i][0] == 2:
                row[1] = row[1] + [sudoku[i][2]]
            if sudoku[i][0] == 3:
                row[2] = row[2] + [sudoku[i][2]]
            if sudoku[i][0] == 4:
                row[3] = row[3] + [sudoku[i][2]]
            if sudoku[i][0] == 5:
                row[4] = row[4] + [sudoku[i][2]]
            if sudoku[i][0] == 6:
                row[5] = row[5] + [sudoku[i][2]]
            if sudoku[i][0] == 7:
                row[6] = row[6] + [sudoku[i][2]]
            if sudoku[i][0] == 8:
                row[7] = row[7] + [sudoku[i][2]]
            if sudoku[i][0] == 9:
                row[8] = row[8] + [sudoku[i][2]]

            if sudoku[i][1] == 1:
                column[0] = column[0] + [sudoku[i][2]]
            if sudoku[i][1] == 2:
                column[1] = column[1] + [sudoku[i][2]]
            if sudoku[i][1] == 3:
                column[2] = column[2] + [sudoku[i][2]]
            if sudoku[i][1] == 4:
                column[3] = column[3] + [sudoku[i][2]]
            if sudoku[i][1] == 5:
                column[4] = column[4] + [sudoku[i][2]]
            if sudoku[i][1] == 6:
                column[5] = column[5] + [sudoku[i][2]]
            if sudoku[i][1] == 7:
                column[6] = column[6] + [sudoku[i][2]]
            if sudoku[i][1] == 8:
                column[7] = column[7] + [sudoku[i][2]]
            if sudoku[i][1] == 9:
                column[8] = column[8] + [sudoku[i][2]]
        so=0
        for i in range(0,10):
            for j in range(0,9):
                for k in range(0,9):
                    if row[j][k]==0:
                        so=so+1
                        break
                if so==1:
                    break
            if so==1:
                so=0
                for i in range(0, 9):
                    housechecking(i)
                for i in range(0, 9):
                    if row[i].count(0) == 1:
                        ronelement(i)
                for i in range(0, 9):
                    if column[i].count(0) == 1:
                        conelement(i)
                for i in range(0, 9):
                    rowcheck(i)
                for i in range(0,9):
                    columncheck(i)
            else:
                break
        for i in range(0,9):
            for j in range(0,9):
                v=row[i][j]
                index=i*9+j

                text2[index].fill(v)
    def housechecking(m):
        a = 0
        b = 0
        c = 0
        r1 = 0
        c1 = 0
        for i in range(1, 10):
            try:
                for j in range(0, 9):
                    if house[m][j][2] == 0:
                        b = b + 1
                    if i == house[m][j][2]:
                        a = a + 1
                if a == 0:
                    for j in range(0, 9):
                        if house[m][j][2] == 0:
                            if i in row[house[m][j][0] - 1] or i in column[house[m][j][1] - 1]:
                                c = c + 1
                            else:
                                r1 = house[m][j][0]
                                c1 = house[m][j][1]
                    if c == b - 1:
                        for k in range(0, 9):
                            if house[m][k][0] == r1 and house[m][k][1] == c1:

                                house[m][k][2] = i
                                row[house[m][k][0]-1][house[m][k][1]-1]=i
                                column[house[m][k][1]-1][house[m][k][0]-1]=i
            except IndexError:

                pass
            a = 0
            c = 0
            r1 = 0
            b = 0
            c1 = 0
    def ronelement(m):
        a=0
        b=0
        k=[1,2,3,4,5,6,7,8,9]
        c=0
        for i in range(0,9):
            if row[m][i] in k:
                a=a+1
                del k[k.index(row[m][i])]
            if row[m][i]==0:
                c=i

        try:
            b = k[0]
        except IndexError:
           pass

        if a==8:
            row[m][c]=b
            column[c][m]=b
            if m<3:
                if c<3:
                    for i in range(0,9):
                        if house[0][i][0]==m+1 and house[0][i][1]==c+1:
                            house[0][i][2]=b
                elif c<6:
                    for i in range(0,9):
                        if house[1][i][0]==m+1 and house[1][i][1]==c+1:
                            house[1][i][2]=b

                elif c<9:
                    for i in range(0,9):
                        if house[2][i][0]==m+1 and house[2][i][1]==c+1:
                            house[2][i][2]=b
            elif m <6:
                if c < 3:
                    for i in range(0, 9):
                        if house[3][i][0] == m+1 and house[3][i][1] == c+1:
                            house[3][i][2] = b
                elif c < 6:
                    for i in range(0, 9):
                        if house[4][i][0] == m+1 and house[4][i][1] == c+1:
                            house[4][i][2] = b

                elif c < 9:
                    for i in range(0, 9):
                        if house[5][i][0] == m+1 and house[5][i][1] == c+1:
                            house[5][i][2] = b
            elif m < 9:
                if c < 3:
                    for i in range(0, 9):
                        if house[6][i][0] == m+1 and house[6][i][1] == c+1:
                            house[6][i][2] = b
                elif c < 6:
                    for i in range(0, 9):
                        if house[7][i][0] == m+1 and house[7][i][1] == c+1:
                            house[7][i][2] = b

                elif c < 9:
                    for i in range(0, 9):
                        if house[8][i][0] == m+1 and house[8][i][1] == c+1:
                            house[8][i][2] = b

    def conelement(c):
        a = 0
        b = 0
        k = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        m = 0
        for i in range(0, 9):
            try:

                if column[c][i] in k:
                    a = a + 1
                    del k[k.index(column[c][i])]
                if column[c][i] == 0:
                    m = i
            except IndexError:
                pass

        try:
            b = k[0]
        except IndexError:
            pass
        if a==8:
            column[c][m]=b
            row[m][c]= b
            if m<3:
                if c<3:
                    for i in range(0,9):
                        if house[0][i][0]==m+1 and house[0][i][1]==c+1:
                            house[0][i][2]=b
                elif c<6:
                    for i in range(0,9):
                        if house[1][i][0]==m+1 and house[1][i][1]==c+1:
                            house[1][i][2]=b

                elif c<9:
                    for i in range(0,9):
                        if house[2][i][0]==m+1 and house[2][i][1]==c+1:
                            house[2][i][2]=b
            elif m <6:
                if c < 3:
                    for i in range(0, 9):
                        if house[3][i][0] == m+1 and house[3][i][1] == c+1:
                            house[3][i][2] = b
                elif c < 6:
                    for i in range(0, 9):
                        if house[4][i][0] == m+1 and house[4][i][1] == c+1:
                            house[4][i][2] = b

                elif c < 9:
                    for i in range(0, 9):
                        if house[5][i][0] == m+1 and house[5][i][1] == c+1:
                            house[5][i][2] = b
            elif m < 9:
                if c < 3:
                    for i in range(0, 9):
                        if house[6][i][0] == m+1 and house[6][i][1] == c+1:
                            house[6][i][2] = b
                elif c < 6:
                    for i in range(0, 9):
                        if house[7][i][0] == m+1 and house[7][i][1] == c+1:
                            house[7][i][2] = b

                elif c < 9:
                    for i in range(0, 9):
                        if house[8][i][0] == m+1 and house[8][i][1] == c+1:
                            house[8][i][2] = b
    def honelement(h):
        a=0
        b=0
        c=0
        m=0
        k = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in range(0,9):
            if house[h][i][2] in k:
                a = a + 1
                del k[k.index(house[h][i][2])]
            if house[h][i][2]==0:
                m=house[h][i][0]-1
                c=house[h][i][1]-1
        try:
            b = k[0]
        except IndexError:
            pass

        if a == 8:
            row[m][c] = b
            column[c][m] = b
            if m < 3:
                if c < 3:
                    for i in range(0, 9):
                        if house[0][i][0] == m + 1 and house[0][i][1] == c + 1:
                            house[0][i][2] = b
                elif c < 6:
                    for i in range(0, 9):
                        if house[1][i][0] == m + 1 and house[1][i][1] == c + 1:
                            house[1][i][2] = b

                elif c < 9:
                    for i in range(0, 9):
                        if house[2][i][0] == m + 1 and house[2][i][1] == c + 1:
                            house[2][i][2] = b
            elif m < 6:
                if c < 3:
                    for i in range(0, 9):
                        if house[3][i][0] == m + 1 and house[3][i][1] == c + 1:
                            house[3][i][2] = b
                elif c < 6:
                    for i in range(0, 9):
                        if house[4][i][0] == m + 1 and house[4][i][1] == c + 1:
                            house[4][i][2] = b

                elif c < 9:
                    for i in range(0, 9):
                        if house[5][i][0] == m + 1 and house[5][i][1] == c + 1:
                            house[5][i][2] = b
            elif m < 9:
                if c < 3:
                    for i in range(0, 9):
                        if house[6][i][0] == m + 1 and house[6][i][1] == c + 1:
                            house[6][i][2] = b
                elif c < 6:
                    for i in range(0, 9):
                        if house[7][i][0] == m + 1 and house[7][i][1] == c + 1:
                            house[7][i][2] = b

                elif c < 9:
                    for i in range(0, 9):
                        if house[8][i][0] == m + 1 and house[8][i][1] == c + 1:
                            house[8][i][2] = b
    def rowcheck(r):
        a = 0
        b = 0
        c = 0
        r1 = 0
        c1 = 0
        w=[]
        for i in range(1, 10):
            try:
                for j in range(0, 9):
                    if row[r][j] == 0:
                        b = b + 1
                    if i == row[r][j]:
                        a = a + 1
                if a == 0:
                    for j in range(0, 9):
                        if row[r][j] == 0:
                            for i1 in range(0,9):
                                if r<3:
                                    if j<3:
                                        if house[0][i1][2]==i:
                                            c=c+1
                                            w=[0,1,2]

                                    elif j<6:
                                        if house[1][i1][2]==i:
                                            c=c+1
                                            w=[3,4,5]

                                    elif j<9:
                                        if house[2][i1][2]==i:
                                            c=c+1
                                            w=[6,7,8]

                                elif r<6:
                                    if j<3:
                                        if house[3][i1][2]==i:
                                            c=c+1
                                            w = [0, 1, 2]

                                    elif j<6:
                                        if house[4][i1][2]==i:
                                            c=c+1
                                            w = [3, 4, 5]

                                    elif j<9:
                                        if house[5][i1][2]==i:
                                            c=c+1
                                            w = [6, 7, 8]

                                elif r<9:
                                    if j<3:
                                        if house[6][i1][2]==i:
                                            c=c+1
                                            w = [0, 1, 2]

                                    elif j<6:
                                        if house[7][i1][2]==i:
                                            c=c+1
                                            w = [3, 4, 5]

                                    elif j<9:
                                        if house[8][i1][2]==i:
                                            c=c+1
                                            w = [6, 7, 8]

                            if i in column[j]:
                                if j not in w:
                                    c = c + 1

                            elif j not in w:
                                r1 = r
                                c1 = j

                    if c == b-1:
                        row[r1][c1]=i

                        column[c1][r1] = i
                        if r1 < 3:
                            if c1 < 3:
                                for j in range(0, 9):
                                    if house[0][j][0] == r1 + 1 and house[0][j][1] == c1 + 1:
                                        house[0][j][2] = i
                            elif c1 < 6:
                                for j in range(0, 9):
                                    if house[1][j][0] == r1 + 1 and house[1][j][1] == c1 + 1:
                                        house[1][j][2] = i

                            elif c1 < 9:
                                for j in range(0, 9):
                                    if house[2][j][0] == r1 + 1 and house[2][j][1] == c1 + 1:
                                        house[2][j][2] = i
                        elif r1 < 6:
                            if c1 < 3:
                                for j in range(0, 9):
                                    if house[3][j][0] == r1 + 1 and house[3][j][1] == c1 + 1:
                                        house[3][j][2] = i
                            elif c1 < 6:
                                for j in range(0, 9):
                                    if house[4][j][0] == r1 + 1 and house[4][j][1] == c1 + 1:
                                        house[4][j][2] = i

                            elif c1 < 9:
                                for j in range(0, 9):
                                    if house[5][j][0] == r1+ 1 and house[5][j][1] == c1 + 1:
                                        house[5][j][2] = i
                        elif r1 < 9:
                            if c1 < 3:
                                for j in range(0, 9):
                                    if house[6][j][0] == r1 + 1 and house[6][j][1] == c1 + 1:
                                        house[6][j][2] = i
                            elif c1 < 6:
                                for j in range(0, 9):
                                    if house[7][j][0] == r1 + 1 and house[7][j][1] == c1 + 1:
                                        house[7][j][2] = i

                            elif c1 < 9:
                                for j in range(0, 9):
                                    if house[8][j][0] == r1 + 1 and house[8][j][1] == c1 + 1:
                                        house[8][j][2] = i

            except IndexError:

                pass
            a = 0
            c = 0
            r1 = 0
            b = 0
            c1 = 0
            w=[]


    def columncheck(c2):
        a = 0
        b = 0
        c = 0
        r1 = 0
        c1 = 0
        w=[]
        for i in range(1, 10):
            try:
                for j in range(0, 9):
                    if column[c2][j] == 0:
                        b = b + 1
                    if i == column[c2][j]:
                        a = a + 1
                if a == 0:
                    for j in range(0, 9):
                        if column[c2][j] == 0:
                            for i1 in range(0,9):
                                if c2<3:
                                    if j<3:
                                        if house[0][i1][2]==i:
                                            c=c+1
                                            w=[0,1,2]
                                    elif j<6:
                                        if house[3][i1][2]==i:
                                            c=c+1
                                            w=[3,4,5]
                                    elif j<9:
                                        if house[6][i1][2]==i:
                                            c=c+1
                                            w=[6,7,8]
                                elif c2<6:
                                    if j<3:
                                        if house[1][i1][2]==i:
                                            c=c+1
                                            w = [0, 1, 2]
                                    elif j<6:
                                        if house[4][i1][2]==i:
                                            c=c+1
                                            w = [3, 4, 5]
                                    elif j<9:
                                        if house[7][i1][2]==i:
                                            c=c+1
                                            w = [6, 7, 8]
                                elif c2<9:
                                    if j<3:
                                        if house[2][i1][2]==i:
                                            c=c+1
                                            w = [0, 1, 2]
                                    elif j<6:
                                        if house[5][i1][2]==i:
                                            c=c+1
                                            w = [3, 4, 5]
                                    elif j<9:
                                        if house[8][i1][2]==i:
                                            c=c+1
                                            w = [6, 7, 8]
                            if i in row[j]:
                                if j not in w:
                                    c = c + 1

                            elif j not in w:
                                r1 = j
                                c1 = c2
                    if c == b-1:
                        row[r1][c1]=i
                        column[c1][r1] = i
                        if r1 < 3:
                            if c1 < 3:
                                for j in range(0, 9):
                                    if house[0][j][0] == r1 + 1 and house[0][j][1] == c1 + 1:
                                        house[0][j][2] = i
                            elif c1 < 6:
                                for j in range(0, 9):
                                    if house[1][j][0] == r1 + 1 and house[1][j][1] == c1 + 1:
                                        house[1][j][2] = i

                            elif c1 < 9:
                                for j in range(0, 9):
                                    if house[2][j][0] == r1 + 1 and house[2][j][1] == c1 + 1:
                                        house[2][j][2] = i
                        elif r1 < 6:
                            if c1 < 3:
                                for j in range(0, 9):
                                    if house[3][j][0] == r1 + 1 and house[3][j][1] == c1 + 1:
                                        house[3][j][2] = i
                            elif c1 < 6:
                                for j in range(0, 9):
                                    if house[4][j][0] == r1 + 1 and house[4][j][1] == c1 + 1:
                                        house[4][j][2] = i

                            elif c1 < 9:
                                for j in range(0, 9):
                                    if house[5][j][0] == r1+ 1 and house[5][j][1] == c1 + 1:
                                        house[5][j][2] = i
                        elif r1 < 9:
                            if c1 < 3:
                                for j in range(0, 9):
                                    if house[6][j][0] == r1 + 1 and house[6][j][1] == c1 + 1:
                                        house[6][j][2] = i
                            elif c1 < 6:
                                for j in range(0, 9):
                                    if house[7][j][0] == r1 + 1 and house[7][j][1] == c1 + 1:
                                        house[7][j][2] = i

                            elif c1 < 9:
                                for j in range(0, 9):
                                    if house[8][j][0] == r1 + 1 and house[8][j][1] == c1 + 1:
                                        house[8][j][2] = i

            except IndexError:

                pass
            a = 0
            c = 0
            r1 = 0
            b = 0
            c1 = 0
            w=[]






    root = Tk()
    x = 3
    y = 2
    county=2
    countx=3
    frame = Frame(root)
    frame.pack()
    frame1 = Frame(root)
    frame1.pack()
    pady=0
    for i in range(0, 81):

        text2 = text2 + [text1(i, x, y,countx,county,pady)]
        if i in [8, 17, 26, 35, 44, 53, 62, 71]:
            x = x + 1
            y = 2
            countx = countx + 1
            county = 2
        else:
            y = y + 1
            county = county + 1
        if i in [2]:
           pady=40
    button = Button(frame1, text="Solve", command=solve)
    button.grid(row=14, column=8)
    root.mainloop()
    return redirect('detail')
