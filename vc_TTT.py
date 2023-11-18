from tkinter import *
from tkinter import ttk
win = Tk()
win.title("Project# Tic-Tac-Toe-Game")
win.config(bg="Teal")
win.geometry("800x450")
#treak moves of players------------------------------------------------------------------------------------------>
board_dic={1:"",2:"",3:"",
           4:"",5:"",6:"",
           7:"",8:"",9:"",
           "X":0,"O":0,"D":0} #x,o,draw--counts
turn="X"       
import speech_recognition as sr
def data_get():
    global turn
    sr_recognizer = sr.Recognizer()
    print("Recognizing your voice.......")
    with sr.Microphone() as source:
        try: 
            audio_data = sr_recognizer.listen(source,timeout=2)
            output = sr_recognizer.recognize_google(audio_data, language='en-IN')
            print(output)
            if len(output)>0:
                lis,st=[],""
                for ch in output:
                    if ch in "0123456789":
                        lis.append(int(ch))
                        st+=ch+" "
                if len(st)>0:
                    #row_col["text"]=st
                    row_col.config(text=st[0:3],font=("Arial",25,"bold"))
#voice command for row ( 1 )============================================================>                    
                    if lis[0]==0 and lis[1]==0:
                        lis=[]
                        if button1["text"]=="X" or button1["text"]=="O":
                            row_col.config(text=st+"box is already filled speak again..",font=("Arial",13,'bold'))
                        elif check_c(board_dic):
                            board_dic[1]=turn
                            print(board_dic)
                            button1["text"]=turn
                            button1.config(font=("Arial",100,"bold"))
                            if check_winners(board_dic):
                                winner_screen["text"]=turn+" WINNER!"
                                board_dic[turn]+=1
                                if turn=="X":
                                    x_score["text"]=str(board_dic["X"]).zfill(2)
                                elif turn=="O":
                                    o_score["text"]=str(board_dic["O"]).zfill(2)   
                                return no_click(board_dic)
                            elif draw_game(board_dic)==False:
                                winner_screen["text"]="X,O Draw!"
                                board_dic["D"]+=1
                                draw["text"]=str(board_dic["D"]).zfill(2)
                                return no_click(board_dic)
                            elif turn=="X":
                                turn="O"
                            else:
                                turn="X"    
                            winner_screen["text"]=turn+" 's Turn" 
                    elif lis[0]==0 and lis[1]==1:
                        lis=[]
                        if button2["text"]=="X" or button2["text"]=="O":
                            row_col.config(text=st+"box is already filled speak again..",font=("Arial",13,"bold"))
                        elif check_c(board_dic):
                            board_dic[2]=turn
                            print(board_dic)
                            button2["text"]=turn
                            button2.config(font=("Arial",100,"bold"))
                            if check_winners(board_dic):
                                winner_screen["text"]=turn+" WINNER!"
                                board_dic[turn]+=1
                                if turn=="X":
                                    x_score["text"]=str(board_dic["X"]).zfill(2)
                                elif turn=="O":
                                    o_score["text"]=str(board_dic["O"]).zfill(2)   
                                return no_click(board_dic)
                            elif draw_game(board_dic)==False:
                                winner_screen["text"]="X,O Draw!"
                                board_dic["D"]+=1
                                draw["text"]=str(board_dic["D"]).zfill(2)
                                return no_click(board_dic)
                            elif turn=="X":
                                turn="O"
                            else:
                                turn="X"    
                            winner_screen["text"]=turn+" 's Turn" 
                    elif lis[0]==0 and lis[1]==2:
                        lis=[]
                        if button3["text"]=="X" or button3["text"]=="O":
                            row_col.config(text=st+"box is already filled speak again..",font=("Arial",13,'bold'))
                        elif check_c(board_dic):
                            board_dic[3]=turn
                            print(board_dic)
                            button3["text"]=turn
                            button3.config(font=("Arial",100,"bold"))
                            if check_winners(board_dic):
                                winner_screen["text"]=turn+" WINNER!"
                                board_dic[turn]+=1
                                if turn=="X":
                                    x_score["text"]=str(board_dic["X"]).zfill(2)
                                elif turn=="O":
                                    o_score["text"]=str(board_dic["O"]).zfill(2)   
                                return no_click(board_dic)
                            elif draw_game(board_dic)==False:
                                winner_screen["text"]="X,O Draw!"
                                board_dic["D"]+=1
                                draw["text"]=str(board_dic["D"]).zfill(2)
                                return no_click(board_dic)
                            elif turn=="X":
                                turn="O"
                            else:
                                turn="X"    
                            winner_screen["text"]=turn+" 's Turn"
#voice command for row ( 2 )==========================================================>  
                    elif lis[0]==1 and lis[1]==0:
                        lis=[]
                        if button4["text"]=="X" or button4["text"]=="O":
                            row_col.config(text=st+"box is already filled speak again..",font=("Arial",13,'bold'))
                        elif check_c(board_dic):
                            board_dic[4]=turn
                            print(board_dic)
                            button4["text"]=turn
                            button4.config(font=("Arial",100,"bold"))
                            if check_winners(board_dic):
                                winner_screen["text"]=turn+" WINNER!"
                                board_dic[turn]+=1
                                if turn=="X":
                                    x_score["text"]=str(board_dic["X"]).zfill(2)
                                elif turn=="O":
                                    o_score["text"]=str(board_dic["O"]).zfill(2)   
                                return no_click(board_dic)
                            elif draw_game(board_dic)==False:
                                winner_screen["text"]="X,O Draw!"
                                board_dic["D"]+=1
                                draw["text"]=str(board_dic["D"]).zfill(2)
                                return no_click(board_dic)
                            elif turn=="X":
                                turn="O"
                            else:
                                turn="X"    
                            winner_screen["text"]=turn+" 's Turn" 
                    elif lis[0]==1 and lis[1]==1:
                        lis=[]
                        if button5["text"]=="X" or button5["text"]=="O":
                            row_col.config(text=st+"box is already filled speak again..",font=("Arial",13,'bold'))
                        elif check_c(board_dic):
                            board_dic[5]=turn
                            print(board_dic)
                            button5["text"]=turn
                            button5.config(font=("Arial",100,"bold"))
                            if check_winners(board_dic):
                                winner_screen["text"]=turn+" WINNER!"
                                board_dic[turn]+=1
                                if turn=="X":
                                    x_score["text"]=str(board_dic["X"]).zfill(2)
                                elif turn=="O":
                                    o_score["text"]=str(board_dic["O"]).zfill(2)   
                                return no_click(board_dic)
                            elif draw_game(board_dic)==False:
                                winner_screen["text"]="X,O Draw!"
                                board_dic["D"]+=1
                                draw["text"]=str(board_dic["D"]).zfill(2)
                                return no_click(board_dic)
                            elif turn=="X":
                                turn="O"
                            else:
                                turn="X"    
                            winner_screen["text"]=turn+" 's Turn" 
                    elif lis[0]==1 and lis[1]==2:
                        lis=[]
                        if button6["text"]=="X" or button6["text"]=="O":
                           row_col.config(text=st+"box is already filled speak again..",font=("Arial",13,'bold'))
                        elif check_c(board_dic):
                            board_dic[6]=turn
                            print(board_dic)
                            button6["text"]=turn
                            button6.config(font=("Arial",100,"bold"))
                            if check_winners(board_dic):
                                winner_screen["text"]=turn+" WINNER!"
                                board_dic[turn]+=1
                                if turn=="X":
                                    x_score["text"]=str(board_dic["X"]).zfill(2)
                                elif turn=="O":
                                    o_score["text"]=str(board_dic["O"]).zfill(2)   
                                return no_click(board_dic)
                            elif draw_game(board_dic)==False:
                                winner_screen["text"]="X,O Draw!"
                                board_dic["D"]+=1
                                draw["text"]=str(board_dic["D"]).zfill(2)
                                return no_click(board_dic)
                            elif turn=="X":
                                turn="O"
                            else:
                                turn="X"    
                            winner_screen["text"]=turn+" 's Turn"
#voice command rwo for ( 3 )==============================================================>                            
                    elif lis[0]==2 and lis[1]==0:
                        lis=[]
                        if button7["text"]=="X" or button7["text"]=="O":
                           row_col.config(text=st+"box is already filled speak again..",font=("Arial",13,'bold'))
                        elif check_c(board_dic):
                            board_dic[7]=turn
                            print(board_dic)
                            button7["text"]=turn
                            button7.config(font=("Arial",100,"bold"))
                            if check_winners(board_dic):
                                winner_screen["text"]=turn+" WINNER!"
                                board_dic[turn]+=1
                                if turn=="X":
                                    x_score["text"]=str(board_dic["X"]).zfill(2)
                                elif turn=="O":
                                    o_score["text"]=str(board_dic["O"]).zfill(2)   
                                return no_click(board_dic)
                            elif draw_game(board_dic)==False:
                                winner_screen["text"]="X,O Draw!"
                                board_dic["D"]+=1
                                draw["text"]=str(board_dic["D"]).zfill(2)
                                return no_click(board_dic)
                            elif turn=="X":
                                turn="O"
                            else:
                                turn="X"    
                            winner_screen["text"]=turn+" 's Turn" 
                    elif lis[0]==2 and lis[1]==1:
                        lis=[]
                        if button8["text"]=="X" or button8["text"]=="O":
                            row_col.config(text=st+"box is already filled speak again..",font=("Arial",13,'bold'))
                        elif check_c(board_dic):
                            board_dic[8]=turn
                            print(board_dic)
                            button8["text"]=turn
                            button8.config(font=("Arial",100,"bold"))
                            if check_winners(board_dic):
                                winner_screen["text"]=turn+" WINNER!"
                                board_dic[turn]+=1
                                if turn=="X":
                                    x_score["text"]=str(board_dic["X"]).zfill(2)
                                elif turn=="O":
                                    o_score["text"]=str(board_dic["O"]).zfill(2)   
                                return no_click(board_dic)
                            elif draw_game(board_dic)==False:
                                winner_screen["text"]="X,O Draw!"
                                board_dic["D"]+=1
                                draw["text"]=str(board_dic["D"]).zfill(2)
                                return no_click(board_dic)
                            elif turn=="X":
                                turn="O"
                            else:
                                turn="X"    
                            winner_screen["text"]=turn+" 's Turn" 
                    elif lis[0]==2 and lis[1]==2:
                        lis=[]
                        if button9["text"]=="X" or button9["text"]=="O":
                            row_col.config(text=st+"box is already filled speak again..",font=("Arial",13,'bold'))
                        elif check_c(board_dic):
                            board_dic[9]=turn
                            print(board_dic)
                            button9["text"]=turn
                            button9.config(font=("Arial",100,"bold"))
                            if check_winners(board_dic):
                                winner_screen["text"]=turn+" WINNER!"
                                board_dic[turn]+=1
                                if turn=="X":
                                    x_score["text"]=str(board_dic["X"]).zfill(2)
                                elif turn=="O":
                                    o_score["text"]=str(board_dic["O"]).zfill(2)   
                                return no_click(board_dic)
                            elif draw_game(board_dic)==False:
                                winner_screen["text"]="X,O Draw!"
                                board_dic["D"]+=1
                                draw["text"]=str(board_dic["D"]).zfill(2)
                                return no_click(board_dic)
                            elif turn=="X":
                                turn="O"
                            else:
                                turn="X"    
                            winner_screen["text"]=turn+" 's Turn"
                    else:
                        row_col.config(text="something wrong speak again..",font=("Arial",10))        
                else:
                    row_col.config(text="something wrong speak again..",font=("Arial",10))                           
                            
        except:
            row_col.config(text="can't understand try again..",font=("Arial",10))


#Click/voice_cd will not work if Player is win the match----------------------------------------------------------->
def no_click(board_dic):
    for nc in range(1,10):
        board_dic[nc]=00 
    return True 
def check_c(board_dic):
    for cc in range(1,10):
        if board_dic[cc]=="":
            return True
    else:
        return False               

#check who is the winner------------------------------------------------------------------------------------------->
def check_winners(board_dic):
#check row    
    if board_dic[1]==board_dic[2]==board_dic[3]==turn:
        return True
    elif board_dic[4]==board_dic[5]==board_dic[6]==turn:
        return True
    elif board_dic[7]==board_dic[8]==board_dic[9]==turn:
        return True
#check column
    elif board_dic[1]==board_dic[4]==board_dic[7]==turn:
        return True
    elif board_dic[2]==board_dic[5]==board_dic[8]==turn:
        return True
    elif board_dic[3]==board_dic[6]==board_dic[9]==turn:
        return True
#check Diagonals 
    elif board_dic[1]==board_dic[5]==board_dic[9]==turn:
        return True
    elif board_dic[3]==board_dic[5]==board_dic[7]==turn:
        return True
    else:
        return False
#cheack for draw--------------------------------------------------------------------------------------------------> 
def draw_game(board_dic):
    for i in range(1,10):
        if board_dic[i]=="":
            return True
    else:
        return False 
#game re_start---------------------------------------------------------------------------------------------------->
def restart():
    for j in range(1,10):
        board_dic[j]=""
    button1["text"]=""
    button2["text"]=""
    button3["text"]=""
    button4["text"]=""
    button5["text"]=""
    button6["text"]=""
    button7["text"]=""
    button8["text"]=""
    button9["text"]=""
    winner_screen["text"]=turn+" 's Turn"  

#reset whole game data-------------------------------------------------------------------------------------------->
def reset_all_data():
    board_dic["X"]=0
    board_dic["O"]=0
    board_dic["D"]=0
    x_score["text"]="00"
    o_score["text"]="00"
    draw["text"]="00"
    return restart()
              
#play And click Events or track pleyers data----------------------------------------------------------------------->
def play(event):
    global turn
    button=event.widget
    click=str(button)
    data=click[-1]
    if data=="n":
        data=1
    else:
        data=int(data)    
    if button["text"]!="X" and button["text"]!="O" and check_c(board_dic):
        if turn=="X":
            button["text"]="X"
            button.config(text='X',font=("Arial",100,"bold"))
            board_dic[data]=turn
            if check_winners(board_dic):
                winner_screen["text"]=turn+" WINNER!"
                board_dic[turn]+=1
                if turn=="X":
                    x_score["text"]=str(board_dic["X"]).zfill(2)
                elif turn=="O":
                    o_score["text"]=str(board_dic["O"]).zfill(2)   
                return no_click(board_dic)
            elif draw_game(board_dic)==False:
                winner_screen["text"]="X,O Draw!"
                board_dic["D"]+=1
                draw["text"]=str(board_dic["D"]).zfill(2)
                return no_click(board_dic)
            else:    
                turn="O"
                winner_screen["text"]=turn+" 's Turn"
        else:
            button["text"]="O"
            button.config(text='O',font=("Arial",100,"bold"))
            board_dic[data]=turn
            if check_winners(board_dic):
                winner_screen["text"]=turn+" WINNER!"
                board_dic[turn]+=1
                if turn=="X":
                    x_score["text"]=str(board_dic["X"]).zfill(2)
                elif turn=="O":
                    o_score["text"]=str(board_dic["O"]).zfill(2)
                return no_click(board_dic)
            elif draw_game(board_dic)==False:
                winner_screen["text"]="X,O Draw!"
                board_dic["D"]+=1
                draw["text"]=str(board_dic["D"]).zfill(2)
                return no_click(board_dic)
            else:    
                turn="X"
                winner_screen["text"]=turn+" 's Turn"
    print(board_dic)         

#------------------------------------------Tic Tac Toe Board------------------------------------------------------£
#First Row-------------------------------------------------------------------------------------------------------->
button1=Button(win,text="0 , 0",font=("Arial",7,"bold")) 
button1.place(x=0,y=0,height=150,width=150)
button1.config(bg="yellow",fg="black",borderwidth=5)
button1.bind("<Button-1>",play)       

button2=Button(win,text="0 , 1",font=("Arial",7,"bold")) 
button2.place(x=150,y=0,height=150,width=150)
button2.config(bg="yellow",fg="black",borderwidth=5)
button2.bind("<Button-1>",play)  

button3=Button(win,text="0 , 2",font=("Arial",7,"bold")) 
button3.place(x=300,y=0,height=150,width=150)
button3.config(bg="yellow",fg="black",borderwidth=5)
button3.bind("<Button-1>",play)   

#Second Row------------------------------------------------------------------------------------------------------->
button4=Button(win,text="1 , 0",font=("Arial",7,"bold")) 
button4.place(x=0,y=150,height=150,width=150)
button4.config(bg="yellow",fg="black",borderwidth=5)
button4.bind("<Button-1>",play)           

button5=Button(win,text="1 , 1",font=("Arial",7,"bold")) 
button5.place(x=150,y=150,height=150,width=150)
button5.config(bg="yellow",fg="black",borderwidth=5)
button5.bind("<Button-1>",play)  

button6=Button(win,text="1 , 2",font=("Arial",7,"bold")) 
button6.place(x=300,y=150,height=150,width=150)
button6.config(bg="yellow",fg="black",borderwidth=5)
button6.bind("<Button-1>",play)  

#Thired Row------------------------------------------------------------------------------------------------------->
button7=Button(win,text="2 , 0",font=("Arial",7,"bold")) 
button7.place(x=0,y=300,height=150,width=150)
button7.config(bg="yellow",fg="black",borderwidth=5)
button7.bind("<Button-1>",play)            

button8=Button(win,text="2 , 1",font=("Arial",7,"bold")) 
button8.place(x=150,y=300,height=150,width=150)
button8.config(bg="yellow",fg="black",borderwidth=5)
button8.bind("<Button-1>",play)  

button9=Button(win,text="2 , 2",font=("Arial",7,"bold")) 
button9.place(x=300,y=300,height=150,width=150)
button9.config(bg="yellow",fg="black",borderwidth=5)
button9.bind("<Button-1>",play)   

#display all the data whose played by the players------------------------------------------------------------------>
x_o_drow_score=Label(win,text="Score-X   ||    Score-O   ||    Draw!",font=("Arial",15,"bold"))
x_o_drow_score.place(x=452,y=0,height=40,width=347)

x_score=Label(win,text="00",font=("Arial",15,"bold"))
x_score.place(x=485,y=40,height=50,width=50)
x_score.config(fg="#C10000")

o_score=Label(win,text="00",font=("Arial",15,"bold"))
o_score.place(x=607,y=40,height=50,width=50)
o_score.config(fg="#C10000")

draw=Label(win,text="00",font=("Arial",15,"bold"))
draw.place(x=725,y=40,height=50,width=50)
draw.config(fg="#C10000")

winner_screen=Label(win,text="X 's turn ",font=("Arial",40,"bold"))
winner_screen.place(x=452,y=100,height=60,width=347)
winner_screen.config(fg="#0010AF")

#Game restart button----------------------------------------------------------------------------------------------->
restart_button=Button(win,text="Re-Start",font=("Arial",17,"bold"),command=restart)
restart_button.place(x=500,y=175,height=50,width=100)
restart_button.config(bg="red")

#Game restart + reset game data button----------------------------------------------------------------------------->
reset_alll=Button(win,text="Re-Set-All",font=("Arial",15,"bold"),command=reset_all_data)
reset_alll.place(x=650,y=175,height=50,width=100)
reset_alll.config(bg="red")

#Voice Command Label----------------------------------------------------------------------------------------------->
voice_commend=Label(win,text="play game using voice command",font=("Arial",15,"bold"))
voice_commend.place(x=452,y=235,height=25,width=347)
voice_commend.config(bg="#C1C400")

#Mini display Label------------------------------------------------------------------------------------------------>
row_col=Label(win,text="no data",font=("Arial",18))
row_col.place(x=475,y=280,height=30,width=300)

#Voice Command button---------------------------------------------------------------------------------------------->
voice_cd_button=Button(win,text="voice cd",font=("Arial",15,"bold"),command=data_get)
voice_cd_button.place(x=570,y=330,height=45,width=110)
voice_cd_button.config(bg="red") 
win.mainloop()              

