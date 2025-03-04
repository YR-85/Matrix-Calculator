from tkinter import *
import copy

###########################################################################################################################
######################## MATRIX-KLASSE ####################################################################################
###########################################################################################################################

class Matrix:
    def __init__(self, ZL, SL):                                                       # ZL = Zeilenlänge, SL = Spaltenlänge
        self.ZL = ZL
        self.SL = SL
    
    def setmatrix(self, matrix):                                                      # Matrix ist eine Liste von Listen: genauer eine Liste, die die Zeilen der
        for i in range (self.SL):
            if len(matrix[i]) != self.ZL:
                raise ValueError("Die Matrix passt nicht zur eingegebenen Spalten und Zeilenanzahl!")
        
        if len(matrix) != self.SL:
            raise ValueError("Die Matrix passt nicht zur eingegebenen Spalten und Zeilenanzahl!")
        
        self.matrix = matrix                                                          # Matrix enthält (Idee: Tic Tac Toe Spiel, siehe VL)
    
    def getmatrix(self):
        return(self.matrix)
    
##########################################################################################################################

    def determinante(self):                                                           # Mit Hilfe von Dreiecks matrix und der Eigenschaft
        Matrix_2 = copy.copy(self.getmatrix())                                        # Multipliziert man eine Zeile mit einer Zahl x so ändert sich die
                                                                                      # Determinante um das das x-fache
        if len(Matrix_2[0]) != len(Matrix_2):
            raise ValueError("Die Matrix ist nicht quadratisch!")
        else:
            Det_fact = 1
            for a in range(self.ZL):                                                  #Diese for-Schleife bringt Matrix in obere Dreiecksform mit 1-en auf Diagonale
                zero_only = True
                for i in range(a,self.SL):
                    if Matrix_2[i][a] != 0:
                        zero_only = False
                
                if zero_only == True:
                    Det_fact = 0
                
                else:
                    Vorzeichen = 1
                    
                    for d in range(a,self.ZL):                                                 #Diese for Schleife tauscht aus Stabilitätsgründen Zeile mit betragsmäßig größten Eintrag an gewollte Stelle
                        if abs(Matrix_2[a][a]) < abs(Matrix_2[d][a]):
                            Matrix_2[a], Matrix_2[d] = Matrix_2[d], Matrix_2[a]
                            Vorzeichen = Vorzeichen * -1
            
            
                    factor = Matrix_2[a][a]
                    Det_fact = Det_fact * factor * Vorzeichen
                    Matrix_2[a] = [(Matrix_2[a][i]/factor) for i in range(self.SL)]            # brint eintrag 0,0 auf 1 und den Rest der Zeile verändert auch
                
                    for j in range(a+1,self.SL):                                               #subtrahiert 1 Zeile- von den anderen Zeilen
                        factor = Matrix_2[j][a]
                        Matrix_2[j] = [Matrix_2[j][i] - (factor * Matrix_2[a][i]) for i in range(self.SL)]
                
            Determinante = Det_fact
            return(Determinante)
            

##########################################################################################################################

    def inverse(self):
        Determinante = self.determinante()
        
        Matr = copy.copy(self.getmatrix())
        Inverse = [[0 for i in range(self.ZL)] for j in range(self.SL)]
        
        if self.ZL != self.SL:
            raise ValueError("Die Matrix ist nicht quadratisch")
            
        elif Determinante == 0:
            raise ZeroDivisionError("Die Determinante der Matrix ist NULL")
 
        else:
            for i in range(self.ZL):
                Inverse[i][i]=1
            
            for a in range(self.ZL):                                                       #Diese for-Schleife bringt Matrix in obere Dreiecksform mit 1-en auf Diagonale

                for d in range(a,self.ZL):                                                 #Diese for Schleife tauscht aus Stabilitätsgründen Zeile mit betragsmäßig größten Eintrag an gewollte Stelle
                    if abs(Matr[a][a]) < abs(Matr[d][a]):
                        Matr[a], Matr[d] = Matr[d], Matr[a]
                        Inverse[a],Inverse[d] = Inverse[d], Inverse[a]
                    
                factor = Matr[a][a]
                Matr[a] = [Matr[a][i]/factor for i in range(self.ZL)]                      #brint eintrag 0,0 auf 1 und den Rest der Zeile verändert auch
                Inverse[a] = [Inverse[a][i]/factor for i in range(self.ZL)]
            
                for j in range(a+1,self.SL):                                               #subtrahiert 1 Zeile- von den anderen Zeilen
                    factor = Matr[j][a]
                    Matr[j] = [Matr[j][i] - (factor * Matr[a][i]) for i in range(self.ZL)]    
                    Inverse[j] = [Inverse[j][i] - (factor * Inverse[a][i]) for i in range(self.ZL)]
                    
            ### Ab hier ist die Matrix in oberer Dreiecksform mit Einsen auf der Diagonale
            for b in range (self.SL-2,-1,-1):
                for c in range(self.SL-1,b,-1):
                   factor = Matr[b][c]
                   Matr[b] = [Matr[b][i] - (factor * Matr[c][i]) for i in range(self.ZL)]
                   Inverse[b] = [Inverse[b][i] - (factor * Inverse[c][i]) for i in range(self.ZL)]
            
            inv = Matrix(self.ZL, self.SL)
            inv.setmatrix(Inverse)
            return(inv)
    

##########################################################################################################################

    def solve(self):
        if self.ZL > self.SL+1:
            raise ValueError("unterbestimmt")
        elif self.SL >= self.ZL:
            raise AttributeError("Zeilenerror")
        else:
            Matr = copy.copy(self.getmatrix())
            
            Det_Matr = [zeile[:-1] for zeile in Matr] # entferne von jeder Zeile das letzte Element
            
            det_matrix = Matrix(self.SL, self.SL) # neues Matrix Objekt zur Speicherung der "eigentlichen" Matrix
            det_matrix.setmatrix(Det_Matr)
            Det = det_matrix.determinante()
            print(Det)


            if Det == 0:
                raise ZeroDivisionError("Die Determinante der Matrix ist NULL")
            else:   
                for a in range(self.SL):                                                        #Diese for-Schleife bringt Matrix in obere Dreiecksform mit 1-en auf Diagonale

                    for d in range(a,self.SL):                                                  #Diese for Schleife tauscht aus Stabilitätsgründen Zeile mit betragsmäßig größten Eintrag an gewollte Stelle
                        if abs(Matr[a][a]) < abs(Matr[d][a]):
                            Matr[a], Matr[d] = Matr[d], Matr[a]
                    
                    factor = Matr[a][a]
                    Matr[a] = [Matr[a][i]/factor for i in range(self.ZL)]                       # brint eintrag 0,0 auf 1 und den Rest der Zeile verändert auch
                
                    for j in range(a+1,self.SL):                                                #subtrahiert 1 Zeile- von den anderen Zeilen
                        factor = Matr[j][a]
                        Matr[j] = [Matr[j][i] - (factor * Matr[a][i]) for i in range(self.ZL)]   
                
                ### Ab hier ist die Matrix in oberer Dreiecksform mit Einsen auf der Diagonale ###
                for b in range (self.SL-2,-1,-1):
                    for c in range(self.SL-1,b,-1):
                       factor = Matr[b][c]
                       Matr[b] = [Matr[b][i] - (factor * Matr[c][i]) for i in range(self.ZL)]
                
                ### Ab hier Ausgabe der Lösung ###
                Lösung = []
                
                Lösung = [zeile[-1] for zeile in Matr]
                
                return(Lösung)
            

#############################################################################################################
    

    def multipl(self, other):
        Matrix1 = self.getmatrix()
        Matrix2 = other.getmatrix()
        Mult_Matr = [[0 for i in range(len(Matrix2[0]))] for j in range(len(Matrix1))]

        for i in range (len(Matrix1)):
            for j in range(len(Matrix2[0])):
                summe = 0
                for a in range(len(Matrix1[0])):
                    summe = summe + (Matrix1[i][a] * Matrix2[a][j])
                Mult_Matr[i][j] = summe
        
        result = Matrix(len(Matrix2[0]), len(Matrix1)) # neues Matrix Objekt
        result.setmatrix(Mult_Matr)
        return(result)
        
    
        
            
#############################################################################################################
######################## GUI Funtktionen ####################################################################
#############################################################################################################

def GUI_solve():
    try:
        clear_frame()
        take_values()
        Solution = M.solve()
        Label(frame_Ausgabetext, text="Lösung des LGS:\n(Beachte Rundungsfehler!)",
              font = "Helvetica 14 bold italic").grid(row=0, column=0, sticky=W, pady=4)
        for i in range(M.SL):
            Label(frame_Ausgabe, text=("x",i+1,"=",round(Solution[i],5)),
                  font = "Helvetica 18 bold italic", bd=15).grid(row=1+i, column=0, sticky=W, pady=4)
    except ValueError:
        Label(frame_Ausgabetext, text="Das LGS ist unterbestimmt, kann keine (eindeutige) Lösung angeben!",
              fg = "red",font = "Helvetica 14 bold italic").grid(row=0, column=0, sticky=W, pady=4)
    except AttributeError:
        Label(frame_Ausgabetext, text="Das LGS hat zu viele Zeilen, kann keine (eindeutige) Lösung angeben!",
              fg = "red",font = "Helvetica 14 bold italic").grid(row=0, column=0, sticky=W, pady=4)
    except ZeroDivisionError:
        Label(frame_Ausgabetext, text="Die Determinante ist 0, kann keine (eindeutige) Lösung angeben",
              fg = "red",font = "Helvetica 14 bold italic").grid(row=0, column=0, sticky=W, pady=4)       
    

def GUI_inverse():
    clear_frame()
    take_values()
    try:
        Inverse = M.inverse().getmatrix()
        
        Label(frame_Ausgabetext, text="Das ist die Inverse:\n(Achte auf Rundungsfehler!)",
              font = "Helvetica 14 bold italic").grid(row=0, column=0, sticky=W, pady=4)
        for i in range(M.SL):
            for j in range(M.ZL):
                Eintrag = float(Inverse[i][j])
                Label(frame_Ausgabe, text=round(Eintrag,5),font = "Helvetica 14 bold italic", bd=15).grid(row=1+i, column=0+j, sticky=W, pady=4)
    except ValueError:
        Label(frame_Ausgabetext, text="Nur quadratische Matrizen sind invertierbar!",
              fg = "red",font = "Helvetica 14 bold italic").grid(row=0, column=0, sticky=W, pady=4)
    except ZeroDivisionError:
        Label(frame_Ausgabetext, text="Die Matrix ist nicht invertierbar, denn die Determinante = 0",
              fg = "red",font = "Helvetica 14 bold italic").grid(row=0, column=0, sticky=W, pady=4)
    

def GUI_multipl():
    clear_frame()
    try:
        take_values()
        take_values2()
        result = M.multipl(M2)
        Mult_Matr = result.getmatrix()

        
        Label(frame_Ausgabetext, text="Das ist das Ergebnis:\n(Achte auf Rundungsfehler!)",
                  font = "Helvetica 14 bold italic").grid(row=0, column=0, sticky=W, pady=4)
        for i in range(result.SL):
                for j in range(result.ZL):
                    Eintrag = float(Mult_Matr[i][j])
                    Label(frame_Ausgabe, text=round(Eintrag,5),font = "Helvetica 14 bold italic", bd=15).grid(row=1+i, column=0+j, sticky=W, pady=4)
    except ZeroDivisionError:
        Label(frame_Ausgabetext, text="Ein unbekannter Fehler ist aufgetreten.",
                  fg = "red",font = "Helvetica 14 bold italic").grid(row=0, column=0, sticky=W, pady=4)
        
def GUI_determinante():
    clear_frame()
    take_values()
    try:
        Det = M.determinante()
        Label(frame_Ausgabetext, text="Das ist die Determinante:\n(Achte auf Rundungsfehler!)",
                  font = "Helvetica 14 bold italic").grid(row=0, column=0, sticky=W, pady=4)
        Label(frame_Ausgabe, text=round(Det,2),font = "Helvetica 14 bold italic", bd=15).grid(row=1, column=0, sticky=W, pady=4)
    except ValueError:
        Label(frame_Ausgabetext, text="Kann nur Determinante von quadratischer Matrix berechnen!",
                  fg = "red",font = "Helvetica 14 bold italic").grid(row=0, column=0, sticky=W, pady=4)
    except:
        Label(frame_Ausgabetext, text="Ein unbekannter Fehler ist aufgetreten.",
                  fg = "red",font = "Helvetica 14 bold italic").grid(row=0, column=0, sticky=W, pady=4)
        

#############################################################################################################
######### GRAFISCHE OBERFLÄCHE ##############################################################################
#############################################################################################################

def clear_frame():                                                        
    while len(frame_Ausgabetext.children) != 0:
        name, widget = frame_Ausgabetext.children.popitem()
        widget.pack_forget()
        widget.destroy()

    while len(frame_Ausgabe.children) != 0:
        name, widget = frame_Ausgabe.children.popitem()
        widget.pack_forget()
        widget.destroy()
        
    
            

def Enter(event):                                     #Ablauf nach drücken der Enter Taste
    if z == 1:
        for i in range(Alte_Zeilenanzahl):
            for j in range(Alte_Spaltenanzahl):
                Entry_Matrix[i][j].grid_forget()
        get_size()

        for i in range(Alte_Zeilenanzahl2):
            for j in range(Alte_Spaltenanzahl2):
                Entry_Matrix2[i][j].grid_forget()
        sec_matr()
            
    else:
        get_size()

def get_size():                                       #Baut aus eingeg. SL & ZL das nxm Feld in Tkinter auf
    global z
    z = 1
    global Alte_Zeilenanzahl
    global Alte_Spaltenanzahl
    Alte_Zeilenanzahl = int(SL.get())
    Alte_Spaltenanzahl = int(ZL.get())
    global Entry_Matrix
    Entry_Matrix = []
    for i in range (int(SL.get())):
        Zeile = []
        for j in range(int(ZL.get())):
            x = Entry(frame_Matrixelemente)
            x.grid(row=i+3, column=j)          
            Zeile.append(x)            
        Entry_Matrix.append(Zeile)
    Label(frame_Matrixelemente, text=("Matrix:"),
                      font = "Helvetica 11 bold italic").grid(row=2, column=0, sticky=W, pady=4)
    global button1
    
    button = Button(frame_Matrixops, text='Invertieren', command=GUI_inverse).grid(row=1, column=0, sticky=W, pady=4)
    button = Button(frame_Matrixops, text='LGS lösen', command=GUI_solve).grid(row=1, column=1, sticky=W, pady=4)
    button = Button(frame_Matrixops, text='Determinante', command=GUI_determinante).grid(row=1, column=2, sticky=W, pady=4)
    button = Button(frame_Matrixops, text='Multiplizieren', command=sec_matr).grid(row=1, column=3, sticky=W, pady=4)
    Label(frame_Matrixfaq, text="\nInvertieren:\nBerechnet zur eingegebenen Matrix,\ndie inverse Matrix\n\nLGS lösen:\nBerechnet die Lösung des eingegebenen LGS.\nDie rechte Spalte ist der b-Vektor\n \nDeterminante:\nBerechnet die Determinante der eingegebenen Matrix\n\n Multiplizieren:\nÖffnet eine weitere Eingabematrix, \ndie nach Eingabe von rechts an die Matrix multipliziert wird.\n(Falls Multiplikation von links erwünscht ist,\nbitte die Matrizen in umgekehrter Reihenfolge eingeben!)\n").grid(row=2, column=1)
   
   
def get_size2():                                       #Baut aus eingeg. SL & ZL das nxm Feld in Tkinter auf
    z = 2
    global Alte_Zeilenanzahl2
    global Alte_Spaltenanzahl2
    Alte_Zeilenanzahl2 = int(ZL.get())
    Alte_Spaltenanzahl2 = int(ZL2.get())
    global Entry_Matrix2
    Entry_Matrix2 = []
    for i in range (Alte_Zeilenanzahl2):
        Zeile = []
        for j in range(int(ZL2.get())):
            x = Entry(frame_Matrixelemente2)
            x.grid(row=i+3, column=j)          
            Zeile.append(x)            
        Entry_Matrix2.append(Zeile)
    Label(frame_Matrixelemente2, text=("Matrix 2:"),
                      font = "Helvetica 11 bold italic").grid(row=2, column=0, sticky=W, pady=4)
    button = Button(frame_Matrixops2, text='Multipliziere mit erster Matrix', command=GUI_multipl).grid(row=0, column=0, sticky=W, pady=4)
    

def take_values():                              #Nimmt nach "Matrix festlegen" die Werte aus den Feldern(Entiteis) und macht Matrix
    global M
    M = Matrix(Alte_Spaltenanzahl , Alte_Zeilenanzahl)
    Matrix1 = []
    for j in range(Alte_Zeilenanzahl):
        Zeile = [] 
        for i in range(Alte_Spaltenanzahl):
            x = Entry_Matrix[j][i].get()
            Zeile.append(float(x))
        Matrix1.append(Zeile)
    M.setmatrix(Matrix1)
    return(M)

def take_values2():                              #Nimmt nach "Matrix festlegen" die Werte aus den Feldern(Entiteis) und macht Matrix
    global M2
    M2 = Matrix(Alte_Spaltenanzahl2 , Alte_Spaltenanzahl)
    Matrix2 = []
    for j in range(Alte_Zeilenanzahl2):
        Zeile = [] 
        for i in range(Alte_Spaltenanzahl2):
            x = Entry_Matrix2[j][i].get()
            Zeile.append(float(x))
        Matrix2.append(Zeile)
    M2.setmatrix(Matrix2)
    return(M2)

def sec_matr():
    global ZL2
    Label(frame_create_Matrix_2, text="Größe Matrix 2").grid(row=0, column=0)
    Label(frame_create_Matrix_2, text="Anzahl\nSpalten:").grid(row=1, column=0)
    Label(frame_create_Matrix_2, text="Anzahl\nZeilen:").grid(row=1, column=1)
    ZL2 = Entry(frame_create_Matrix_2)
    SL2 = Alte_Spaltenanzahl
    ZL2.grid(row=2, column=0)
    
    Label(frame_create_Matrix_2, text=Alte_Spaltenanzahl).grid(row=2, column=1)
    button = Button(frame_create_Matrix_2, text='OK', command=get_size2).grid(row=2, column=3, sticky=W, pady=4)
    

master = Tk()
frame_title = Frame(master)
frame_title.grid(row=0, column=0, sticky=W, pady=4)
frame_title2 = Frame(master)
frame_title2.grid(row=0, column=1, sticky=W, pady=4)
frame_Matrixgroesse = Frame(master, highlightbackground="black", highlightthickness=1)
frame_Matrixgroesse.grid(row=1, column=0, sticky=W, pady=4)
frame_Matrixelemente = Frame(master, highlightbackground="black", highlightthickness=1)
frame_Matrixelemente.grid(row=2, column=0, sticky=W, pady=4)
frame_Matrixops = Frame(master)
frame_Matrixops.grid(row=3, column=0, sticky=W, pady=4)
frame_Matrixfaq = Frame(master)
frame_Matrixfaq.grid(row=6, column=0, sticky=W, pady=4)
frame_create_Matrix_2 = Frame(master,  highlightbackground="black", highlightthickness=1)
frame_create_Matrix_2.grid(row=1, column=1, sticky=W, pady=4)
frame_Matrixelemente2 = Frame(master, highlightbackground="black", highlightthickness=1)
frame_Matrixelemente2.grid(row=2, column=1, sticky=W, pady=4)
frame_Matrixops2 = Frame(master)
frame_Matrixops2.grid(row=3, column=1, sticky=W, pady=4)
frame_Ausgabetext = Frame(master)
frame_Ausgabetext.grid(row=4, column=0, sticky=W, pady=4)
frame_Ausgabe = Frame(master, highlightbackground="black", highlightthickness=5, )
frame_Ausgabe.grid(row=5, column=0, sticky=W, pady=4)

Label(frame_title, text="Matrix-Rechner",font = "Helvetica 14 bold italic").grid(row=0, column=0)
Label(frame_title2, text="",font = "Helvetica 14 bold italic").grid(row=0, column=0)


a = Label(frame_Matrixgroesse, text="Anzahl\nSpalten:")
b = Label(frame_Matrixgroesse, text="Anzahl\nZeilen:")
Label(frame_Matrixgroesse, text="Größe Matrix:").grid(row=0)
a.grid(row=1, column=0)
b.grid(row=1, column=1)
ZL = Entry(frame_Matrixgroesse)
SL = Entry(frame_Matrixgroesse)
ZL.grid(row=2, column=0)
SL.grid(row=2, column=1)

z = 0
button1 = None 
Entry_Matrix = []               
Entry_Matrix2 = []
master.bind('<Return>', Enter)

mainloop( )


        
        
        
