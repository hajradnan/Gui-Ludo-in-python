from tkinter import *
from playgame import game

class rollandmovebutton:
    def rollingforred(self,obj):
        block_predict_red = Label(obj.excanvas,image=obj.block_number_side[0])
        block_predict_red.place(x=45,y=15)
        predict_red = Button(obj.excanvas, bg="black", fg="white", relief=RAISED, bd=5, text="ROLL", font=("Arial", 8, "bold"), command=lambda: obj.rolling("red"))
        predict_red.place(x=37, y=55)
        entry_take_red = Entry(obj.excanvas,bg="white",fg="blue",font=("Arial",25,"bold","italic"),width=2,relief=SUNKEN,bd=5)
        entry_take_red.place(x=40,y=95)
        con=game()
        final_move = Button(obj.excanvas,bg="black",fg="white",relief=RAISED,bd=5,text="MOVE",font=("Arial",8,"bold"),command=lambda: con.main_controller(obj,"red",entry_take_red.get()),state=DISABLED)
        final_move.place(x=42,y=155)
        Label(obj.excanvas,text="Player 1",bg="black",fg="white",font=("Arial",15,"bold")).place(x=15,y=195)
        obj.store_instructional_btn(block_predict_red,predict_red,entry_take_red,final_move)

        #predict_red or for any color it represents the roll button for every team
        #entry_take_red or for any color, it represents the entry for coin number allow to move
        #final_move for any color is the move button
        #Label for any color/team represents the player tag 

    def rollingforblue(self,obj):
        block_predict_blue = Label(obj.excanvas, image=obj.block_number_side[0])
        block_predict_blue.place(x=45, y=385)
        predict_blue = Button(obj.excanvas, bg="black", fg="white", relief=RAISED, bd=5, text="ROLL",font=("Arial", 8, "bold"), command=lambda: obj.rolling("blue"))
        predict_blue.place(x=37, y=425)
        entry_take_blue = Entry(obj.excanvas, bg="white", fg="blue", font=("Arial", 25, "bold", "italic"), width=2,relief=SUNKEN, bd=5)
        entry_take_blue.place(x=40, y=465)
        con=game()
        final_move = Button(obj.excanvas, bg="black", fg="white", relief=RAISED, bd=5, text="MOVE", font=("Arial", 8, "bold"),command=lambda: con.main_controller(obj,"blue",entry_take_blue.get()),state=DISABLED)
        final_move.place(x=42, y=525)
        Label(obj.excanvas, text="Player 2", bg="black", fg="white", font=("Arial", 15, "bold")).place(x=15,y=565)
        obj.store_instructional_btn(block_predict_blue, predict_blue, entry_take_blue, final_move)

    def rollingforyellow(self,obj):
        block_predict_yellow = Label(obj.excanvas, image=obj.block_number_side[0])
        block_predict_yellow.place(x=720, y=385)
        predict_yellow = Button(obj.excanvas, bg="black", fg="white", relief=RAISED, bd=5, text="ROLL",font=("Arial", 8, "bold"), command=lambda: obj.rolling("yellow"))
        predict_yellow.place(x=712, y=425)
        entry_take_yellow = Entry(obj.excanvas, bg="white", fg="blue", font=("Arial", 25, "bold", "italic"),width=2, relief=SUNKEN, bd=5)
        entry_take_yellow.place(x=715, y=465)
        con=game()
        final_move = Button(obj.excanvas, bg="black", fg="white", relief=RAISED, bd=5, text="MOVE",font=("Arial", 8, "bold"),command=lambda: con.main_controller(obj,"yellow",entry_take_yellow.get()),state=DISABLED)
        final_move.place(x=719, y=525)
        Label(obj.excanvas, text="Player 3", bg="black", fg="white", font=("Arial", 15, "bold")).place(x=703,y=565)
        obj.store_instructional_btn(block_predict_yellow, predict_yellow, entry_take_yellow, final_move)

    def rollingforgreen(self,obj):
        block_predict_green = Label(obj.excanvas, image=obj.block_number_side[0])
        block_predict_green.place(x=720, y=15)
        predict_green = Button(obj.excanvas, bg="black", fg="white", relief=RAISED, bd=5, text="ROLL", font=("Arial", 8, "bold"), command=lambda: obj.rolling("green"))
        predict_green.place(x=712, y=55)
        entry_take_green = Entry(obj.excanvas, bg="white", fg="blue", font=("Arial", 25, "bold", "italic"), width=2, relief=SUNKEN, bd=5)
        entry_take_green.place(x=715, y=95)
        con=game()
        final_move = Button(obj.excanvas, bg="black", fg="white", relief=RAISED, bd=5, text="MOVE",font=("Arial", 8, "bold"),command=lambda: con.main_controller(obj,"green",entry_take_green.get()),state=DISABLED)
        final_move.place(x=719, y=155)
        Label(obj.excanvas, text="Player 4", bg="black", fg="white", font=("Arial", 15, "bold")).place(x=703, y=195)
        obj.store_instructional_btn(block_predict_green, predict_green, entry_take_green, final_move)

