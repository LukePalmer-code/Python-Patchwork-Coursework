from graphics import *

###################################################################################
#UP2121336- LUKE PALMER- PYTHON COURSEWORK- PATCHES- 13th DECEMBER 2022
###################################################################################
#Start with the interface, take the inputs etc.  DONE
#Write all the functions for making circles, rectangles and other shapes DONE
#Make a list containing the colours: RED, GREEN, BLUE, ORANGE, CYAN and PURPLE DONE
#Define the window sizes: 500x500 OR 700x700 depending on inputs DONE
#Design the patches according to the designs on the PDF DONE
#Sort out coordinates and placements of patches DONE
#Make 5x5 and 7x7 versions DONE
#Optimise!!!!!!!! DONE
###################################################################################
def circlefromTL(win, tlPoint, radius, colour, outline):
    centre = centrePoint(tlPoint, radius)
    circle(win, centre, radius, colour, outline)

def brPoint(tlPoint, width, height):
    x = tlPoint.getX() + width
    y = tlPoint.getY() + height
    brPoint = Point(x, y)
    return brPoint

def centrePoint(tlPoint, radius):
    x = tlPoint.getX() + radius
    y = tlPoint.getY() + radius
    centre = Point(x, y)
    return centre

def circle(win, centre, radius, colour, outline):
    c = Circle(centre,radius)
    c.setFill(colour)
    c.setOutline(outline)
    c.draw(win)

def oblong(win, centre, colour, outline):
    centre_2 = Point(centre.x +(3), centre.y)
    centre_3 = Point(centre.x+(8), centre.y)
    radius = 10
    circlefromTL(win, centre, radius, colour, outline)
    circlefromTL(win, centre_2, radius, colour, outline)
    circlefromTL(win, centre_3, radius, colour, outline)

def rectangle(win, tlPoint, brPoint, colour, outline):
    r = Rectangle(tlPoint, brPoint)
    r.setFill(colour)
    r.setOutline(outline)
    r.draw(win)
    return r

def line(win, point1, point2, colour):
    l = Line(point1, point2)
    l.setOutline(colour)
    l.draw(win)
    return l

####################################################
####################################################
def PatchDesign1(win, chosen_colours, tlOffset):
    PatchSize = 110
    scale = 20
    alternateLine = True
    for x in range(0, PatchSize, scale):
        for y in range(0, PatchSize, scale):
            tl = Point(tlOffset.getX() + x, tlOffset.getY()+ y)
            if alternateLine:
                circlefromTL(win, tl, 10, chosen_colours, chosen_colours)
            else:
                circlefromTL(win, tl, 10, "white", chosen_colours)
            alternateLine = not alternateLine

def PatchDesign2(win, chosen_colours, tlOffset): #This whole patch needs work asap, last thing to fix!!
    scale = 20
    alternateLine = True
    for x in range(0, 20, scale):
        for y in range(0, 90, scale):
            tl = Point(tlOffset.getX() + x, tlOffset.getY() + y)
            centre = Point(tl.x + 20, tl.y)
            centre2 = Point(tl.x + 49, tl.y)
            centre3 = Point(tl.x + 70, tl.y)
            centre4 = Point(tl.x + 29, tl.y)
            centre5 = Point(tl.x + 78, tl.y)
            if alternateLine:
                circlefromTL(win, tl, 10, chosen_colours, chosen_colours)
                oblong(win, centre, chosen_colours, chosen_colours)
                circlefromTL(win, centre2, 10, chosen_colours, chosen_colours)
                oblong(win, centre3, chosen_colours, chosen_colours)
            else:
                oblong(win, tl, chosen_colours, chosen_colours)
                circlefromTL(win, centre4, 10, chosen_colours, chosen_colours)
                oblong(win, centre2, chosen_colours, chosen_colours)
                circlefromTL(win, centre5, 10, chosen_colours, chosen_colours)
            
            alternateLine = not alternateLine

def BlankPatch(win, chosen_colours, tlOffset):
    scale = 100
    tl = Point(tlOffset.getX(), tlOffset.getY())
    br = brPoint(tl, scale, scale)
    rectangle(win, tl, br, chosen_colours, chosen_colours)

def Main():
    win = GraphWin("UP2121336-Luke Palmer-Python Coursework-Patches", window_size, window_size)

    if Patch_Size == 7:
        for y in range(0, window_size, 100):
            for x in range(0, window_size, 100):
                tlPoint = Point(x, y)
                if tlPoint.x == tlPoint.y: 
                    PatchDesign1(win,chosen_colours[0],tlPoint) 
                elif x >= 100 and y == 0 :                      #PATCH DESIGN 1
                    PatchDesign1(win,chosen_colours[1],tlPoint) 
                elif x == 600 and y >= 100:                     #PATCH DESIGN 1
                    PatchDesign1(win,chosen_colours[1],tlPoint) 
                
                elif y == 100 and x >= 200 and x <= 500:        #BLANK PATCH
                    BlankPatch(win, chosen_colours[1], tlPoint) 
                elif y == 200 and x >= 300 and x <= 500:        #BLANK PATCH
                    BlankPatch(win, chosen_colours[1], tlPoint) 
                elif y == 300 and x >= 400 and x <= 500:        #BLANK PATCH
                    BlankPatch(win, chosen_colours[1], tlPoint) 
                elif y == 400 and x >= 500 and x <= 500:        #BLANK PATCH
                    BlankPatch(win, chosen_colours[1], tlPoint) 

                elif x == 100 and y >= 200 and y <= 500:         #PATCH DESIGN 2
                    PatchDesign2(win,chosen_colours[2],tlPoint)
                elif x == 200 and y >= 300 and y <= 500:         #PATCH DESIGN 2
                    PatchDesign2(win,chosen_colours[2],tlPoint)
                elif x == 300 and y >= 400 and y <= 500:         #PATCH DESIGN 2
                    PatchDesign2(win,chosen_colours[2],tlPoint)
                elif x == 400 and y >= 500 and y <= 500:         #PATCH DESIGN 2
                    PatchDesign2(win,chosen_colours[2],tlPoint)

                elif x>= 0 and y == 600:                        #BLANK PATCH
                    BlankPatch(win, chosen_colours[2], tlPoint) 
                elif x == 0 and y >= 0:                         #BLANK PATCH
                    BlankPatch(win, chosen_colours[2], tlPoint) 
        win.getMouse()
    
    elif Patch_Size == 5:
        for y in range(0, window_size, 100):
            for x in range(0, window_size, 100):
                tlPoint = Point(x, y)
                if tlPoint.x == tlPoint.y: 
                    PatchDesign1(win,chosen_colours[0],tlPoint) 
                elif x >= 100 and y == 0 :                      #PATCH DESIGN 1
                    PatchDesign1(win,chosen_colours[1],tlPoint) 
                elif x == 600 and y >= 100:                     #PATCH DESIGN 1
                    PatchDesign1(win,chosen_colours[1],tlPoint) 
                elif x == 400 and y >= 0:                       #PATCH DESIGN 1
                    PatchDesign1(win,chosen_colours[1],tlPoint) 

                elif y == 100 and x >= 200:                     #BLANK PATCH
                    BlankPatch(win, chosen_colours[1], tlPoint) 
                elif y == 200 and x >= 300:                     #BLANK PATCH
                    BlankPatch(win, chosen_colours[1], tlPoint) 
                elif y == 300 and x >= 300:                     #BLANK PATCH
                    BlankPatch(win, chosen_colours[1], tlPoint) 
                elif x >= 400 and y >= 400:                     #BLANK PATCH
                    BlankPatch(win, chosen_colours[2], tlPoint) 

                elif x == 100 and y >= 200 and y <= 300:        #PATCH DESIGN 2
                    PatchDesign2(win,chosen_colours[2],tlPoint)
                elif x == 200 and y == 300:                     #PATCH DESIGN 2
                    PatchDesign2(win,chosen_colours[2],tlPoint)

                elif y == 400 and x >= 0:                       #BLANK PATCH
                    BlankPatch(win, chosen_colours[2], tlPoint) 
                elif x == 0 and y >= 0:                         #BLANK PATCH
                    BlankPatch(win, chosen_colours[2], tlPoint) 
        win.getMouse()

colours = ["red", "green", "blue", "orange","cyan", "purple"]  #The list of colours available for the user to select from. 

First_Input = 1
while First_Input == 1:
    colour_choice1 = input("Please enter the first desired colour: ")
    if colour_choice1 not in colours:
        print("Invalid colour, please try again")
    else:
        First_Input = 0
        Second_Input = 1
        while Second_Input == 1:
            colour_choice2 = input("Please enter the second desired colour: ")
            if colour_choice2 not in colours:
                print("Invalid colour, please try again")
            else:
                Second_Input = 0
                Third_Input = 1
                while Third_Input == 1:
                    colour_choice3 = input("Please enter the third desired colour: ")
                    if colour_choice3 not in colours:
                        print("Invalid colour, please try again")
                    else:
                        Third_Input = 0
                        Fourth_Input = 1
                        while Fourth_Input == 1:
                            Patch_Size = int(input("Please enter the size of the patch: "))
                            if Patch_Size == 5:
                                print("Patch size = 5")
                                Fourth_Input = 0
                                window_size = 500
                                chosen_colours = [colour_choice1, colour_choice2, colour_choice3]
                                Main()
                            elif Patch_Size == 7:
                                print("Patch size = 7")
                                Fourth_Input = 0
                                window_size = 700
                                chosen_colours = [colour_choice1, colour_choice2, colour_choice3]
                                Main()
                            else:
                                print("")
                                print("Please enter a valid size.")
                                print("This can be either:")
                                print("5 for a 5x5 patch")
                                print("or")
                                print("7 for a 7x7 patch")
                                print("")

#this whole data entry system needs optimising in some way!!






