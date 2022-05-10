from tkinter import *
import time
from random import randint
from board import Board
from rollbuttons import rollandmovebutton
from movementofpawn import *
from startposition import start
from customisedbutton import btn
from tkinter import messagebox


class Ludo:
    def __init__(self, root,sixdotdice,fivedotdice,fourdotdice,threedotdice,twodotdice,onedotdice):
        print("\nWelcome to Ludo Night\nHope you have fun playing this\nEnjoy!\n")
        print("NOTE:Ludo Night is supported for 2 to 4 players!\n")
        print("Position 1 starts at the start of red square and there are 52 boxes for every coin to move excluding the way to their own homes\nPurple shape marks stops\n")
        print("Enter number of players first in a seperate window!\n")
        self.window = root
        # Make canvas
        self.excanvas = Canvas(root, bg="purple", width=800, height=630)
        self.excanvas.pack(fill=BOTH,expand=1)

        # Using list as data structures to store data 
        self.redcoin = []
        self.greencoin = []
        self.yellowcoin = []
        self.bluecoin = []

        self.redlabel = []
        self.greenlabel = []
        self.yellowlabel = []
        self.bluelabel = []

        self.rolldice = []
        self.totalplayers = []

        # sides of dice
        self.block_number_side = [onedotdice,twodotdice,threedotdice,fourdotdice,fivedotdice,sixdotdice]

        # Use for store specific position of all coins
        self.red_coord_store = [-1, -1, -1, -1]
        self.green_coord_store = [-1, -1, -1, -1]
        self.yellow_coord_store = [-1, -1, -1, -1]
        self.blue_coord_store = [-1, -1, -1, -1]
        
        #coin position set to -1 by default
        self.red_coin_position = [-1,-1,-1,-1]
        self.green_coin_position = [-1,-1,-1,-1]
        self.yellow_coin_position = [-1,-1,-1,-1]
        self.blue_coin_position = [-1,-1,-1,-1]
        
##        # counters initialized for movement of coins/pawns
        self.move_red_counter = 0  #helps in moving the coin/pawn
        self.move_green_counter = 0
        self.move_yellow_counter = 0
        self.move_blue_counter = 0

        self.take_permission = 0  #helps in prediction winners and runner up
        self.six_with_overlap = 0

        self.six_counter = 0 #number of six
        self.timetaken = -1

        # By default some function calls for creating board and more
        b=Board()
        b.ludoboard(self)

        c=rollandmovebutton()
        c.rollingforred(self)

        d=rollandmovebutton()
        d.rollingforblue(self)

        e=rollandmovebutton()
        e.rollingforyellow(self)

        f=rollandmovebutton()
        f.rollingforgreen(self)

        self.inputnumberofplayers()


    

    # INPUT TOTAL NUMBER OF PLAYERS
    def inputnumberofplayers(self):
        for i in range(4):
            self.rolldice[i][1]['state'] = DISABLED

        # Making other window to take control over
        top = Toplevel()
        top.geometry("600x150")
        top.maxsize(600,150)
        top.minsize(600,150)
        top.config(bg="purple")
        

        head = Label(top,text="Enter number of players ",font=("Arial",25,"bold","roman"),bg="purple",fg="white")
        head.place(x=70,y=30)
        take_entry = Entry(top,font=("Arial",18,"bold","roman"),relief=SUNKEN,bd=7,width=12)
        take_entry.place(x=150,y=80)
        take_entry.focus()
        

        def filtering():# checking players
            response_take = self.input_filtering(take_entry.get())
            if response_take is True and int(take_entry.get())>1:  #this is for checking players are greater than 1, should be between 2,3 or 4
                for player in range(int(take_entry.get())):
                    self.totalplayers.append(player)  #appending players as 0,1,2,3 
                print(self.totalplayers)  #it will show in starting how many players are playing
                self.make_command()
                top.destroy()
            else:
                messagebox.showerror("Players Input Error", "Please input number of players between 2 and 4")

        submit_btn = Button(top,text="PLAY",bg="black",fg="white",font=("Arial",13,"bold"),relief=RAISED,bd=8,command=filtering)
        submit_btn.place(x=350,y=80)
        top.mainloop()


        # Input value checking
    def input_filtering(self,coin_number):
        try:
            if (4>=int(coin_number)>=1) or type(coin_number) == int:
                return True
            else:
                return False
        except:
            return False


    # Get block value after prediction based on probability
    def rolling(self,color_indicator): #color_indicator represents color of team
        try:
            if color_indicator == "red":
                block_value_predict = self.rolldice[0] #0 represents red
                permanent_block_number =self.move_red_counter= randint(1, 6) #selects random number from 1 to 6

            elif color_indicator == "blue":
                block_value_predict = self.rolldice[1]  #1 represents blue
                permanent_block_number = self.move_blue_counter=randint(1, 6)

            elif color_indicator == "yellow":
                block_value_predict = self.rolldice[2]  #2 represents yellow 
                permanent_block_number = self.move_yellow_counter=randint(1, 6)

            elif color_indicator=='green':
                block_value_predict = self.rolldice[3]  #3 represents green
                permanent_block_number = self.move_green_counter=randint(1, 6)


            block_value_predict[1]['state'] = DISABLED #as we have rolled the dice roll button is disabled here

            # rolling of dice
            temporarycounter = 15
            while temporarycounter>0:
                movecounter = randint(1, 6)
                block_value_predict[0]['image'] = self.block_number_side[movecounter - 1]  #changing picture of dice while rolling
                self.window.update()
                time.sleep(0.1)  #to show actual rolling
                temporarycounter-=1

            print("Roling result: ", permanent_block_number)

            # Permanent value containing image 
            block_value_predict[0]['image'] = self.block_number_side[permanent_block_number-1] #finally sets the image of dice obtained after rolling
            ins=btn()
            ins.instructionalandcustomisedbutton(self,color_indicator,permanent_block_number,block_value_predict)
        except:
            print("Force stop error")

    
    # Roll button abling or disabling
    def make_command(self):
        if  self.timetaken == -1:
            pass
        else: #if their is less than 6 and no pawn outside roll button disabled
            self.rolldice[self.totalplayers[self.timetaken]][1]['state'] = DISABLED
        if  self.timetaken == len(self.totalplayers)-1:
            self.timetaken = -1

        self.timetaken+=1
        self.rolldice[self.totalplayers[self.timetaken]][1]['state'] = NORMAL #will make roll button enable


    def store_instructional_btn(self, block_indicator, predictor, entry_controller, give_finally):
        temp = []
        temp.append(block_indicator)
        temp.append(predictor)
        temp.append(entry_controller)
        temp.append(give_finally)
        self.rolldice.append(temp) #appending instruction for evry team in a seperate list

        #block_indicator represents dice that roles for evry turn
        #predictor represents prediction or rolling button
        #entry_controller represents entry of coin/ label number
        #give_finally represents move button

        # self.rolldice[0] = information for red
        # self.rolldice[1] = information for blue
        # self.rolldice[2] = information for yellow
        # self.rolldice[3] = information for green

        # self.rolldice[something][1] = Roll btn
        # self.rolldice[something][3] = Move btn


    # When two coins overlap, one of them will go to their home
    def coord_overlap(self, counter_coin, color_coin, path_to_traverse_before_overlap):
        if  color_coin!="red":
            for take_coin_number in range(len(self.red_coord_store)):
                if  self.red_coord_store[take_coin_number] == counter_coin:
                    if path_to_traverse_before_overlap == 6:
                        self.six_with_overlap=1
                    else:
                        self.timetaken-=1

                    self.excanvas.delete(self.redcoin[take_coin_number])
                    self.redlabel[take_coin_number].place_forget()
                    self.red_coin_position[take_coin_number] = -1
                    self.red_coord_store[take_coin_number] = -1

                    if take_coin_number == 0:
                       remade_coin = self.excanvas.create_oval(150,55, 180,95, width=2, fill="red", outline="black")
                       self.redlabel[take_coin_number].place(x=150, y=60)
                    elif take_coin_number == 1:
                        remade_coin = self.excanvas.create_oval(260, 55,300,95, width=2, fill="red", outline="black")
                        self.redlabel[take_coin_number].place(x=270, y=60)
                    elif take_coin_number == 2:
                        remade_coin = self.excanvas.create_oval(260,155,300,195, width=2, fill="red", outline="black")
                        self.redlabel[take_coin_number].place(x=270, y=160)
                    else:
                        remade_coin = self.excanvas.create_oval(140, 155, 180, 195, width=2,fill="red", outline="black")
                        self.redlabel[take_coin_number].place(x=150, y=160)

                    self.redcoin[take_coin_number]=remade_coin
                    
        ######################################################################################################################
                    
        if  color_coin != "green":
            for take_coin_number in range(len(self.green_coord_store)):
                if  self.green_coord_store[take_coin_number] == counter_coin:
                    if path_to_traverse_before_overlap == 6:
                        self.six_with_overlap = 1
                    else:
                        self.timetaken-=1

                    self.excanvas.delete(self.greencoin[take_coin_number])
                    self.greenlabel[take_coin_number].place_forget()
                    self.green_coin_position[take_coin_number] = -1
                    self.green_coord_store[take_coin_number] = -1

                    if take_coin_number == 0:
                        remade_coin = self.excanvas.create_oval(500,55, 540,95, width=2, fill="green", outline="black")
                        self.greenlabel[take_coin_number].place(x=510, y=60)
                    elif take_coin_number == 1:
                        remade_coin = self.excanvas.create_oval(620, 55, 660,95, width=2, fill="green", outline="black")
                        self.greenlabel[take_coin_number].place(x=630, y=60)
                    elif take_coin_number == 2:
                        remade_coin = self.excanvas.create_oval(620,155,660, 195, width=2, fill="green", outline="black")
                        self.greenlabel[take_coin_number].place(x=630, y=160)
                    else:
                        remade_coin = self.excanvas.create_oval(500,155,540,195, width=2, fill="green", outline="black")
                        self.greenlabel[take_coin_number].place(x=510, y=160)

                    self.greencoin[take_coin_number] = remade_coin

        ######################################################################################################################


        if  color_coin != "yellow":
            for take_coin_number in range(len(self.yellow_coord_store)):
                if  self.yellow_coord_store[take_coin_number] == counter_coin:
                    if path_to_traverse_before_overlap == 6:
                        self.six_with_overlap = 1
                    else:
                        self.timetaken -= 1

                    self.excanvas.delete(self.yellowcoin[take_coin_number])
                    self.yellowlabel[take_coin_number].place_forget()
                    self.yellow_coin_position[take_coin_number] = -1
                    self.yellow_coord_store[take_coin_number] = -1

                    if take_coin_number == 0:
                        remade_coin = self.excanvas.create_oval(500,435, 540,475, width=2, fill="yellow", outline="black")
                        self.yellowlabel[take_coin_number].place(x=510, y=440)
                    elif take_coin_number == 1:
                        remade_coin = self.excanvas.create_oval(620, 435,660, 475, width=2, fill="yellow", outline="black")
                        self.yellowlabel[take_coin_number].place(x=630, y=440)
                    elif take_coin_number == 2:
                        remade_coin = self.excanvas.create_oval(620, 535, 660,575, width=2, fill="yellow", outline="black")
                        self.yellowlabel[take_coin_number].place(x=630, y=540)
                    else:
                        remade_coin = self.excanvas.create_oval(500, 535, 540,575, width=2, fill="yellow", outline="black")
                        self.yellowlabel[take_coin_number].place(x=510, y=540)

                    self.yellowcoin[take_coin_number] = remade_coin

        ######################################################################################################################

        if  color_coin != "blue":
            for take_coin_number in range(len(self.blue_coord_store)):
                if  self.blue_coord_store[take_coin_number] == counter_coin:
                    if path_to_traverse_before_overlap == 6:
                        self.six_with_overlap = 1
                    else:
                        self.timetaken -= 1

                    self.excanvas.delete(self.bluecoin[take_coin_number])
                    self.bluelabel[take_coin_number].place_forget()
                    self.blue_coin_position[take_coin_number] = -1
                    self.blue_coord_store[take_coin_number]=-1

                    if take_coin_number == 0:
                        remade_coin = self.excanvas.create_oval(140,435, 180,475, width=2, fill="blue", outline="black")
                        self.bluelabel[take_coin_number].place(x=100+40+10, y=30 + (40*6)+(40*3)+40+10)
                    elif take_coin_number == 1:
                        remade_coin = self.excanvas.create_oval(260, 435, 300,475, width=2, fill="blue", outline="black")
                        self.bluelabel[take_coin_number].place(x=270, y=440)
                    elif take_coin_number == 2:
                        remade_coin = self.excanvas.create_oval(260, 535,300,575, width=2, fill="blue", outline="black")
                        self.bluelabel[take_coin_number].place(x=270, y=540)
                    else:
                        remade_coin = self.excanvas.create_oval( 140,535, 180,575, width=2, fill="blue", outline="black")
                        self.bluelabel[take_coin_number].place(x=150, y=540)

                    self.bluecoin[take_coin_number] = remade_coin


    def under_room_traversal_control(self,specific_coin,number_label,number_label_x,number_label_y,path_counter,counter_coin,color_coin): #if a pawn reaches near completion of its path
        if color_coin == "red" and counter_coin >= 100:
            if int(counter_coin)+int(path_counter)<=106:
               counter_coin = self.room_red_traversal(specific_coin, number_label, number_label_x, number_label_y, path_counter, counter_coin)

        elif color_coin == "green" and counter_coin >= 100:
            if  int(counter_coin) + int(path_counter) <= 106:
                counter_coin = self.room_green_traversal(specific_coin, number_label, number_label_x, number_label_y,path_counter,counter_coin)

        elif color_coin == "yellow" and counter_coin >= 100:
            if  int(counter_coin) + int(path_counter) <= 106:
                counter_coin = self.room_yellow_traversal(specific_coin, number_label, number_label_x, number_label_y,path_counter,counter_coin)

        elif color_coin == "blue" and counter_coin >= 100:
            if  int(counter_coin) + int(path_counter) <= 106:
                counter_coin = self.room_blue_traversal(specific_coin, number_label, number_label_x, number_label_y,path_counter,counter_coin)

        return counter_coin


#########################################################################################################################################################

    def room_red_traversal(self, specific_coin, number_label, number_label_x, number_label_y, path_counter, counter_coin):
        while path_counter>0:
            counter_coin += 1
            path_counter -= 1
            self.excanvas.move(specific_coin, 40, 0)
            number_label_x+=40
            number_label.place(x=number_label_x,y=number_label_y)
            self.window.update()
            time.sleep(0.2)
        return counter_coin

#########################################################################################################################################################

    def room_green_traversal(self, specific_coin, number_label, number_label_x, number_label_y, path_counter, counter_coin):
        while path_counter > 0:
            counter_coin += 1
            path_counter -= 1
            self.excanvas.move(specific_coin, 0, 40)
            number_label_y += 40
            number_label.place(x=number_label_x, y=number_label_y)
            self.window.update()
            time.sleep(0.2)
        return counter_coin

#########################################################################################################################################################    

    def room_yellow_traversal(self, specific_coin, number_label, number_label_x, number_label_y,path_counter,counter_coin):
        while path_counter > 0:
            counter_coin += 1
            path_counter -= 1
            self.excanvas.move(specific_coin, -40, 0)
            number_label_x -= 40
            number_label.place(x=number_label_x, y=number_label_y)
            self.window.update()
            time.sleep(0.2)
        return counter_coin

#########################################################################################################################################################    

    def room_blue_traversal(self, specific_coin, number_label, number_label_x, number_label_y,path_counter,counter_coin):
        while path_counter > 0:
            counter_coin += 1
            path_counter -= 1
            self.excanvas.move(specific_coin, 0, -40)
            number_label_y -= 40
            number_label.place(x=number_label_x, y=number_label_y)
            self.window.update()
            time.sleep(0.2)
        return counter_coin

    def check_winner_and_runner(self,color_coin):
        destination_reached = 0 # Check for all specific color coins
        if color_coin == "red":
            temp_store = self.red_coord_store
            temp_delete = 0# Player index
        elif color_coin == "green":
            temp_store = self.green_coord_store
            temp_delete = 3# Player index
        elif color_coin == "yellow":
            temp_store = self.yellow_coord_store
            temp_delete = 2# Player index
        else:
            temp_store = self.blue_coord_store
            temp_delete = 1# Player index

        for take in temp_store:
            if take == 106:
                destination_reached = 1
            else:
                destination_reached = 0
                break

        if  destination_reached == 1:# If all coins in block reach to the destination, winner and runner check
            self.take_permission += 1
            if self.take_permission == 1:# Winner check
                messagebox.showinfo("Winner","Congrats! You are the winner")
            elif self.take_permission == 2:# 1st runner check
                messagebox.showinfo("Winner", "Wow! You are 1st runner")
            elif self.take_permission == 3:# 2nd runner check
                messagebox.showinfo("Winner", "Wow! You are 2nd runner")

            self.rolldice[temp_delete][1]['state'] = DISABLED
            self.totalplayers.remove(temp_delete)

            if len(self.totalplayers) == 1:
                messagebox.showinfo("Game Over","Good bye!!")
                self.rolldice[0][1]['state'] = DISABLED
                return False
            else:
                self.timetaken-=1
        else:
            print("Winner not decided")

        return True

    

        

r=Tk()
r.title('LUDO NIGHT')
r.maxsize(800,640)
r.minsize(800,640)
sixdotdice=PhotoImage(file='six.png')
fivedotdice=PhotoImage(file='five.png')
fourdotdice=PhotoImage(file='four.png')
threedotdice=PhotoImage(file='three.png')
twodotdice=PhotoImage(file='two.png')
onedotdice=PhotoImage(file='one.png')
Ludo(r,sixdotdice,fivedotdice,fourdotdice,threedotdice,twodotdice,onedotdice)
r.mainloop()
             
