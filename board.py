from tkinter import *
class Board:
    def ludoboard(self,obj):
        # Main board
        obj.excanvas.create_rectangle(100, 15, 700, 615, width=6, fill="white")


        ###################################################################

        #RED BOX

        obj.excanvas.create_rectangle(100,15,340,255,width=2,fill="red")  #mainredbox
        
        # path for red pawns/coins
        obj.excanvas.create_rectangle(100,255,340,295,width=2)
        obj.excanvas.create_rectangle(140,295,340,335, width=2, fill="red")
        obj.excanvas.create_rectangle(100,335,340,375, width=2)

        # seperation lines for red
        startxcoord=140
        startycoord=255
        endxcoord=140
        endycoord=375
        for i in range(5):
            obj.excanvas.create_line(startxcoord, startycoord, endxcoord, endycoord, width=2)
            startxcoord+=40
            endxcoord+=40

        #square boxes for coins    
        obj.excanvas.create_rectangle(140,55,180,95,width=2,fill='white')
        obj.excanvas.create_rectangle(260,55,300,95,width=2,fill='white')
        obj.excanvas.create_rectangle(140,155,180,195,width=2,fill='white')
        obj.excanvas.create_rectangle(260,155,300,195,width=2,fill='white')

        # start position of red pawn
        obj.excanvas.create_rectangle(140,255,180,295,fill="red",width=2)

        # red coins/pawns
        redcoin1 = obj.excanvas.create_oval(140, 55, 180, 95, width=2, fill="red", outline="black")
        redcoin2 = obj.excanvas.create_oval(260, 55, 300,95, width=2, fill="red", outline="black")
        redcoin3 = obj.excanvas.create_oval(260, 155,300,195, width=2, fill="red", outline="black")
        redcoin4 = obj.excanvas.create_oval(140, 155, 180, 195, width=2,fill="red", outline="black")
        obj.redcoin.append(redcoin1)
        obj.redcoin.append(redcoin2)
        obj.redcoin.append(redcoin3)
        obj.redcoin.append(redcoin4)

        # labels for pawns numbered as 1,2,3 or 4
        redlabelone = Label(obj.excanvas,text="1",font=("Arial",15,"bold"),bg='red',fg="black")
        redlabelone.place(x=150, y=60)
        redlabeltwo = Label(obj.excanvas, text="2", font=("Arial", 15, "bold"), bg="red", fg="black")
        redlabeltwo.place(x=270, y=60)
        redlabelthree = Label(obj.excanvas, text="3", font=("Arial", 15, "bold"), bg="red", fg="black")
        redlabelthree.place(x=270, y=160)
        redlabelfour = Label(obj.excanvas, text="4", font=("Arial", 15, "bold"), bg="red", fg="black")
        redlabelfour.place(x=150, y=160)
        obj.redlabel.append(redlabelone)
        obj.redlabel.append(redlabeltwo)
        obj.redlabel.append(redlabelthree)
        obj.redlabel.append(redlabelfour)


        #stop (unique shaped) near red 
        xx =200     
        yy =337                                             
        coord = [200,337,xx+5,yy+15,xx+15,yy+15,xx+10,yy+20,xx+15,yy+25,xx+5,yy+25,xx,yy+35]
        obj.excanvas.create_polygon(coord,width=2,fill="purple")




        
        ###################################################################

        #GREEN BOX

        obj.excanvas.create_rectangle(460,15,700,255,width=2,fill="green")  # main green square

        # path for green pawns/coins
        obj.excanvas.create_rectangle(340,15,380,255,width=2)
        obj.excanvas.create_rectangle(380,55,420,255,width=2, fill="green")
        obj.excanvas.create_rectangle(420,15,460,255,width=2)

        # seperation lines for green
        startxcoord=340
        startycoord=55
        endxcoord=460
        endycoord=55
        for i in range(5):
            obj.excanvas.create_line(startxcoord, startycoord, endxcoord, endycoord, width=2)
            startycoord+=40
            endycoord+=40

        # square boxes for green coins
        obj.excanvas.create_rectangle(500,55,540,95,width=2,fill='white')
        obj.excanvas.create_rectangle(620,55,660,95,width=2,fill='white')
        obj.excanvas.create_rectangle(500,155,540,195,width=2,fill='white')
        obj.excanvas.create_rectangle(620,155,660,195,width=2,fill='white')

        # start position of green pawn
        obj.excanvas.create_rectangle(420,55,460,95,fill="green",width=2)

        # green coins/pawns
        greencoin1 = obj.excanvas.create_oval(500,55, 540, 95, width=2, fill="green", outline="black")
        greencoin2 = obj.excanvas.create_oval(620,55, 660,95, width=2, fill="green", outline="black")
        greencoin3 = obj.excanvas.create_oval(620,155, 660,195, width=2, fill="green", outline="black")
        greencoin4 = obj.excanvas.create_oval(500, 155,540, 195, width=2, fill="green", outline="black")
        obj.greencoin.append(greencoin1)
        obj.greencoin.append(greencoin2)
        obj.greencoin.append(greencoin3)
        obj.greencoin.append(greencoin4)

        #labels for pawns numbered as 1,2,3 or 4
        greenlabelone = Label(obj.excanvas, text="1", font=("Arial", 15, "bold"), bg="green", fg="black")
        greenlabelone.place(x=510, y=60)
        greenlabeltwo = Label(obj.excanvas, text="2", font=("Arial", 15, "bold"), bg="green", fg="black")
        greenlabeltwo.place(x=630, y=60)
        greenlabelthree = Label(obj.excanvas, text="3", font=("Arial", 15, "bold"), bg="green", fg="black")
        greenlabelthree.place(x=630, y=160)
        greenlabelfour = Label(obj.excanvas, text="4", font=("Arial", 15, "bold"), bg="green", fg="black")
        greenlabelfour.place(x=510, y=160)
        obj.greenlabel.append(greenlabelone)
        obj.greenlabel.append(greenlabeltwo)
        obj.greenlabel.append(greenlabelthree)
        obj.greenlabel.append(greenlabelfour)

        #stop (unique shaped) near green
        xx = 360   
        yy = 97                                    
        coord = [360,97,xx+5,yy+15,xx+15,yy+15,xx+10,yy+20,xx+15,yy+25,xx+5,yy+25,xx,yy+35]
        obj.excanvas.create_polygon(coord,width=2,fill="purple")





        ###################################################################

        
        #BLUE BOX

        obj.excanvas.create_rectangle(100,375,340,615,width=2,fill="blue")  # main blue square

        # path for blue pawn/coins
        obj.excanvas.create_rectangle(100,375,380,615,width=2)
        obj.excanvas.create_rectangle(380,375, 420,575,width=2, fill="blue")
        obj.excanvas.create_rectangle(420,375,460,615,width=2)

        # seperation lines for blue
        startxcoord=340
        startycoord=415
        endxcoord=460
        endycoord=415
        for i in range(5):
            obj.excanvas.create_line(startxcoord, startycoord, endxcoord, endycoord, width=2)
            startycoord+=40
            endycoord+=40

        # square boxes for blue coins
        obj.excanvas.create_rectangle(140,435,180,475,width=2,fill='white')
        obj.excanvas.create_rectangle(260,435,300,475,width=2,fill='white')
        obj.excanvas.create_rectangle(140,535,180,575,width=2,fill='white')
        obj.excanvas.create_rectangle(260,535,300,575,width=2,fill='white')

        # start position of blue pawn
        obj.excanvas.create_rectangle(340,535,380,575,fill="blue",width=2)

        # Blue coins/pawns
        bluecoin1 = obj.excanvas.create_oval(140, 435, 180, 475, width=2, fill="blue", outline="black")
        bluecoin2 = obj.excanvas.create_oval(260, 436, 300, 475, width=2, fill="blue", outline="black")
        bluecoin3 = obj.excanvas.create_oval(260, 535, 300, 575, width=2, fill="blue", outline="black")
        bluecoin4 = obj.excanvas.create_oval( 140, 535, 180, 575, width=2, fill="blue", outline="black")
        obj.bluecoin.append(bluecoin1)
        obj.bluecoin.append(bluecoin2)
        obj.bluecoin.append(bluecoin3)
        obj.bluecoin.append(bluecoin4)

        #labels for pawns numbered as 1,2,3 or 4
        bluelabelone = Label(obj.excanvas, text="1", font=("Arial", 15, "bold"), bg="blue", fg="black")
        bluelabelone.place(x=150, y=440)
        bluelabeltwo = Label(obj.excanvas, text="2", font=("Arial", 15, "bold"), bg="blue", fg="black")
        bluelabeltwo.place(x=270, y=440)
        bluelabelthree = Label(obj.excanvas, text="3", font=("Arial", 15, "bold"), bg="blue", fg="black")
        bluelabelthree.place(x=270, y=540)
        bluelabelfour = Label(obj.excanvas, text="4", font=("Arial", 15, "bold"), bg="blue", fg="black")
        bluelabelfour.place(x=150, y=540)
        obj.bluelabel.append(bluelabelone)
        obj.bluelabel.append(bluelabeltwo)
        obj.bluelabel.append(bluelabelthree)
        obj.bluelabel.append(bluelabelfour)


        #stop (unique shaped) near blue 
        xx = 440   
        yy = 497                                                     
        coord = [440,497,xx+5,yy+15,xx+15,yy+15,xx+10,yy+20,xx+15,yy+25,xx+5,yy+25,xx,yy+35]
        obj.excanvas.create_polygon(coord,width=2,fill="purple")




        ###################################################################

        
        #YELLOW BOX
        
        
        obj.excanvas.create_rectangle(460,375,700,615,width=2, fill="yellow")# main yellow square

        # path for yellow pawns/coins
        obj.excanvas.create_rectangle(460,255,700,295,width=2)
        obj.excanvas.create_rectangle(460,295,660,335,width=2, fill="yellow")
        obj.excanvas.create_rectangle(460,335,700,375,width=2)

        # seperation lines for yellow
        startxcoord=500
        startycoord=255
        endxcoord=500
        endycoord=375
        for i in range(5):
            obj.excanvas.create_line(startxcoord, startycoord, endxcoord, endycoord, width=2)
            startxcoord+=40
            endxcoord+=40

        
        # square boxes for yellow coins
        obj.excanvas.create_rectangle(500,435,540,475,width=2,fill='white')
        obj.excanvas.create_rectangle(620,435,660,475,width=2,fill='white')
        obj.excanvas.create_rectangle(500,535,540,575,width=2,fill='white')
        obj.excanvas.create_rectangle(620,535,660,575,width=2,fill='white')   
        
        # start position of yellow pawn
        obj.excanvas.create_rectangle(620,335,660,375,fill="yellow",width=2)
        
        # yellow coins/pawns
        yellowcoin1 = obj.excanvas.create_oval(500, 435,540,475, width=2, fill="yellow", outline="black")
        yellowcoin2 = obj.excanvas.create_oval(620, 435, 660, 475, width=2, fill="yellow", outline="black")
        yellowcoin3 = obj.excanvas.create_oval(620, 535, 660, 575, width=2, fill="yellow", outline="black")
        yellowcoin4 = obj.excanvas.create_oval(500, 535, 540,575, width=2, fill="yellow", outline="black")
        obj.yellowcoin.append(yellowcoin1)
        obj.yellowcoin.append(yellowcoin2)
        obj.yellowcoin.append(yellowcoin3)
        obj.yellowcoin.append(yellowcoin4)

        #labels for pawns numbered as 1,2,3 or 4
        yellowlabelone = Label(obj.excanvas, text="1", font=("Arial", 15, "bold"), bg="yellow", fg="black")
        yellowlabelone.place(x=510, y=440)
        yellowlabeltwo = Label(obj.excanvas, text="2", font=("Arial", 15, "bold"), bg="yellow", fg="black")
        yellowlabeltwo.place(x=630, y=440)
        yellowlabelthree = Label(obj.excanvas, text="3", font=("Arial", 15, "bold"), bg="yellow", fg="black")
        yellowlabelthree.place(x=630, y=540)
        yellowlabelfour = Label(obj.excanvas, text="4", font=("Arial", 15, "bold"), bg="yellow", fg="black")
        yellowlabelfour.place(x=510, y=540)
        obj.yellowlabel.append(yellowlabelone)
        obj.yellowlabel.append(yellowlabeltwo)
        obj.yellowlabel.append(yellowlabelthree)
        obj.yellowlabel.append(yellowlabelfour)

        #stop (unique shaped) near yellow
        xx = 600     
        yy = 257
        coord = [600,257,xx+5,yy+15,xx+15,yy+15,xx+10,yy+20,xx+15,yy+25,xx+5,yy+25,xx,yy+35]
        obj.excanvas.create_polygon(coord,width=2,fill="purple")


        ############################################

        
        # Center design 
        obj.excanvas.create_polygon(340,255,400,315,340,375,width=2,outline="black",fill="red")
        obj.excanvas.create_polygon(340,375,400,315,460,375,width=2,outline="black",fill="blue")
        obj.excanvas.create_polygon(340,255,400,315,460,255,width=2,outline="black",fill="green")
        obj.excanvas.create_polygon(460,255,400,315,460,375,width=2,outline="black",fill="yellow")



       
        


        
        


       
