from tkinter import *
from tkinter import messagebox

from PIL import Image, ImageTk

# THIS FUNCTION WOULD BE EXECUTED ONCE THE USER CLICKS THE BUTTON NAMED SQUARE
def square():
    # THE PROGRAM WOULD RESIZE THE PROGRAM'S WINDOW
    cRoot.geometry("500x400")
    # THIS FUNCTION WOULD BE EXECUTED ONCE THE USER CLICKS THE RETURN BUTTON
    # THIS FUNCTION DESTROYS THE WIDGETS INSIDE THE WINDOW AND GOES BACK TO THE
    # START FUNCTION.
    def square_return():
        sqrImage_LBL.destroy()
        cRoot.sqr_LBL.destroy()
        s_LBL.destroy()
        s_TXT.destroy()
        solve_BTN.destroy()
        back_BTN.destroy()
        try:
            squareResult_LBL.destroy()
        except:
            pass
        start()
    # THIS FUNCTION WOULD BE PROCESSED ONCE THE USER CLICKS THE SOLVE BUTTON
    def square_solve():
        # THE 'squareResult_LBL' would become a global variable so that it could be used outside this specific function
        global squareResult_LBL
        # THE PROGRAM WOULD TRY TO DESTROY THE RESULT LABEL IF IT IS PRESENT BEFORE THE USER CLICKED THE SOLVE BUTTON
        try:
            squareResult_LBL.destroy()
        except:
            pass
        s = s_TXT.get( "0.0" , END )
        squareResult_LBL = Label ( cRoot , text = " Result : " + str( float(s)**2 ) , font = ( "Courier" ,8 ,  "bold" ) ,
                                   width = "29" )
        squareResult_LBL.place ( x = 280 , y = 260 )
    # THE PROGRAM WOULD PROCESS THIS FUNCTION THAT DESTROY THE SELECTION WIDGETS PRESENT IN THE MENU.
    clearSelection()
    # THE PROGRAM WOULD OPEN AND RESIZE THE IMAGE THAT WOULD DISPLAY THE SQUARE.
    sqrImage_resize = Image.open( "squareImage.png" ).resize( (250 , 250), Image.ANTIALIAS )
    sqrImage = ImageTk.PhotoImage( sqrImage_resize )
    sqrImage_LBL = Label( cRoot , image = sqrImage )
    sqrImage_LBL.photo = sqrImage
    sqrImage_LBL.place( x = 15 , y = 95 )

    # THESE ARE THE MAIN WIDGETS IN THE WINDOW
    cRoot.sqr_LBL = Label ( cRoot , font = ( "Courier" , 12 , "bold" ) , text = "SQUARE's\nAREA" , width = "20"
                                , height = "20" ,bg = "#b09db9" , fg = "Black" )
    cRoot.sqr_LBL.place( x = 280 , y = 95 , height = 50 )

    s_LBL = Label ( text = " Value of 'S' : "  )
    s_LBL.place ( x = 345 , y = 160 )

    s_TXT = Text ( cRoot , bd = 0 , bg = "White" , height = "1" , width = "23" , font = "Arial" )
    s_TXT.place ( x = 280 , y = 180 )

    solve_BTN = Button ( cRoot , font = ( "Courier" , 8 , "bold" ) , text = "SOLVE" , width = "20"
                                , height = "5" ,bg = "Orange" , fg = "Black" , command = square_solve )
    solve_BTN.place ( x = 310 , y = 210 , height = 30 )

    back_BTN = Button ( cRoot , font = ( "Courier" , 8 , "bold" ) , text = "RETURN" , width = "20"
                                , height = "5" ,bg = "Orange" , fg = "Black" , command = square_return )
    back_BTN.place ( x = 310 , y = 290 , height = 30 )

# THIS FUNCTION IS SIMILAR TO THE PREVIOUS ONE, IT WILL BE EXECUTED ONCE THE USER CHOSE THE BUTTON NAMED CUBE
# MOST OF THIS FUNCTION'S PROCESSES IS SIMILAR TO THE PREVIOUS FUNCTION, IT IS JUST TWEAKED A LITTLE BIT.
def cube():
    cRoot.geometry("500x400")
    def cube_return():
        cubeImage_LBL.destroy()
        cRoot.cube_LBL.destroy()
        s_LBL.destroy()
        s_TXT.destroy()
        solve_BTN.destroy()
        back_BTN.destroy()
        try:
            cubeResult_LBL.destroy()
        except:
            pass
        start()

    def cube_solve():
        global cubeResult_LBL
        try:
            cubeResult_LBL.destroy()
        except:
            pass
        s = s_TXT.get( "0.0" , END )
        cubeResult_LBL = Label ( cRoot , text = " Result : " + str( float(s)**3 ) , font = ( "Courier" ,8 ,  "bold" ) ,
                                   width = "29" )
        cubeResult_LBL.place ( x = 280 , y = 260 )
        
    clearSelection()
    cubeImage_resize = Image.open( "cubeImage.png" ).resize( (250 , 250), Image.ANTIALIAS )
    cubeImage = ImageTk.PhotoImage( cubeImage_resize )
    cubeImage_LBL = Label( cRoot , image = cubeImage )
    cubeImage_LBL.photo = cubeImage
    cubeImage_LBL.place( x = 15 , y = 95 )

    # THESE ARE THE MAIN WIDGETS PRESENT THAT WOULD BE PRESENT ONCE THE CUBE BUTTON IS SELECTED
    cRoot.cube_LBL = Label ( cRoot , font = ( "Courier" , 12 , "bold" ) , text = "CUBE's\nVOLUME" , width = "20"
                                , height = "20" ,bg = "#b09db9" , fg = "Black" )
    cRoot.cube_LBL.place( x = 280 , y = 95 , height = 50 )

    s_LBL = Label ( text = " Value of 'S' : "  )
    s_LBL.place ( x = 345 , y = 160 )

    s_TXT = Text ( cRoot , bd = 0 , bg = "White" , height = "1" , width = "23" , font = "Arial" )
    s_TXT.place ( x = 280 , y = 180 )

    solve_BTN = Button ( cRoot , font = ( "Courier" , 8 , "bold" ) , text = "SOLVE" , width = "20"
                                , height = "5" ,bg = "Orange" , fg = "Black" , command = cube_solve )
    solve_BTN.place ( x = 310 , y = 210 , height = 30 )

    back_BTN = Button ( cRoot , font = ( "Courier" , 8 , "bold" ) , text = "RETURN" , width = "20"
                                , height = "5" ,bg = "Orange" , fg = "Black" , command = cube_return )
    back_BTN.place ( x = 310 , y = 290 , height = 30 )

# THIS FUNCTION IS SIMILAR TO THE PREVIOUS FUNCTIONS.
# THIS FUNCTION ONLY ASKS FOR THE CIRCLE'S RADIUS AND CALCULATES THE AREA OF THE CIRCLE
def circle():
    cRoot.geometry("500x400")
    def circle_return():
        circleImage_LBL.destroy()
        cRoot.circle_LBL.destroy()
        r_LBL.destroy()
        r_TXT.destroy()
        solve_BTN.destroy()
        back_BTN.destroy()
        try:
            circleResult_LBL.destroy()
        except:
            pass
        start()

    def circle_solve():
        global circleResult_LBL
        try:
            circleResult_LBL.destroy()
        except:
            pass
        r = r_TXT.get( "0.0" , END )
        circleResult_LBL = Label ( cRoot , text = " Result : " + str( (float(r)**2)*3.14 ) , font = ( "Courier" ,8 ,  "bold" ) ,
                                   width = "29" )
        circleResult_LBL.place ( x = 280 , y = 260 )
        
    clearSelection()
    circleImage_resize = Image.open( "circleImage.png" ).resize( (250 , 250), Image.ANTIALIAS )
    circleImage = ImageTk.PhotoImage( circleImage_resize )
    circleImage_LBL = Label( cRoot , image = circleImage )
    circleImage_LBL.photo = circleImage
    circleImage_LBL.place( x = 15 , y = 95 )

    # THESE ARE THE MAIN WIDGETS
    cRoot.circle_LBL = Label ( cRoot , font = ( "Courier" , 12 , "bold" ) , text = "CIRCLE's\nAREA" , width = "20"
                                , height = "20" ,bg = "#b09db9" , fg = "Black" )
    cRoot.circle_LBL.place( x = 280 , y = 95 , height = 50 )

    r_LBL = Label ( text = " What is the radius ? "  )
    r_LBL.place ( x = 330 , y = 160 )

    r_TXT = Text ( cRoot , bd = 0 , bg = "White" , height = "1" , width = "23" , font = "Arial" )
    r_TXT.place ( x = 280 , y = 180 )

    solve_BTN = Button ( cRoot , font = ( "Courier" , 8 , "bold" ) , text = "SOLVE" , width = "20"
                                , height = "5" ,bg = "Orange" , fg = "Black" , command = circle_solve )
    solve_BTN.place ( x = 310 , y = 210 , height = 30 )

    back_BTN = Button ( cRoot , font = ( "Courier" , 8 , "bold" ) , text = "RETURN" , width = "20"
                                , height = "5" ,bg = "Orange" , fg = "Black" , command = circle_return )
    back_BTN.place ( x = 310 , y = 290 , height = 30 )    

# THIS FUNCTION IS SIMILAR TO THE CIRLE FUNCTION, THE ONLY DIFFERENCE IS THAT THIS CALCULATES
# THE VOLUME OF THE SPHERE.
def sphere():
    cRoot.geometry("500x400")
    def sphere_return():
        sphereImage_LBL.destroy()
        cRoot.sphere_LBL.destroy()
        r_LBL.destroy()
        r_TXT.destroy()
        solve_BTN.destroy()
        back_BTN.destroy()
        try:
            sphereResult_LBL.destroy()
        except:
            pass
        start()

    def sphere_solve():
        global sphereResult_LBL
        try:
            sphereResult_LBL.destroy()
        except:
            pass
        r = r_TXT.get( "0.0" , END )
        sphereResult_LBL = Label ( cRoot , text = " Result : " + str( (float(r)**3)*(3.14)*(4/3) ) , font = ( "Courier" ,8 ,  "bold" ) ,
                                   width = "29" )
        sphereResult_LBL.place ( x = 280 , y = 260 )
        
    clearSelection()
    sphereImage_resize = Image.open( "sphereImage.png" ).resize( (250 , 250), Image.ANTIALIAS )
    sphereImage = ImageTk.PhotoImage( sphereImage_resize )
    sphereImage_LBL = Label( cRoot , image = sphereImage )
    sphereImage_LBL.photo = sphereImage
    sphereImage_LBL.place( x = 15 , y = 95 )

    # THE MAIN WIDGETS THAT WOULD BE PRESENT IN THE WINDOW
    cRoot.sphere_LBL = Label ( cRoot , font = ( "Courier" , 12 , "bold" ) , text = "SPHERE's\nVOLUME" , width = "20"
                                , height = "20" ,bg = "#b09db9" , fg = "Black" )
    cRoot.sphere_LBL.place( x = 280 , y = 95 , height = 50 )

    r_LBL = Label ( text = " What is the radius ? "  )
    r_LBL.place ( x = 330 , y = 160 )

    r_TXT = Text ( cRoot , bd = 0 , bg = "White" , height = "1" , width = "23" , font = "Arial" )
    r_TXT.place ( x = 280 , y = 180 )

    solve_BTN = Button ( cRoot , font = ( "Courier" , 8 , "bold" ) , text = "SOLVE" , width = "20"
                                , height = "5" ,bg = "Orange" , fg = "Black" , command = sphere_solve )
    solve_BTN.place ( x = 310 , y = 210 , height = 30 )

    back_BTN = Button ( cRoot , font = ( "Courier" , 8 , "bold" ) , text = "RETURN" , width = "20"
                                , height = "5" ,bg = "Orange" , fg = "Black" , command = sphere_return )
    back_BTN.place ( x = 310 , y = 290 , height = 30 )

# THIS FUNCTION CALCULATES THE AREA OF THE RECTANGLE BASED ON THE USER'S INPUT.
# HERE THE PROGRAM WOULD ASK FOR THE LENGTH AND WIDTH OF THE RECTANGLE.
def rectangle():
    cRoot.geometry("500x400")
    def rectangle_return():
        rectangleImage_LBL.destroy()
        cRoot.rectangle_LBL.destroy()
        l_LBL.destroy()
        l_TXT.destroy()
        w_LBL.destroy()
        w_TXT.destroy()
        solve_BTN.destroy()
        back_BTN.destroy()
        try:
            rectangleResult_LBL.destroy()
        except:
            pass
        start()

    def rectangle_solve():
        global rectangleResult_LBL
        try:
            rectangleResult_LBL.destroy()
        except:
            pass
        l = l_TXT.get( "0.0" , END )
        w = w_TXT.get( "0.0" , END )
        rectangleResult_LBL = Label ( cRoot , text = " Result : " + str( float(l)*float(w) ) , font = ( "Courier" ,8 ,  "bold" ) ,
                                   width = "29" )
        rectangleResult_LBL.place ( x = 280 , y = 320 )
        
    clearSelection()
    rectangleImage_resize = Image.open( "rectangleImage.png" ).resize( (250 , 250), Image.ANTIALIAS )
    rectangleImage = ImageTk.PhotoImage( rectangleImage_resize )
    rectangleImage_LBL = Label( cRoot , image = rectangleImage )
    rectangleImage_LBL.photo = rectangleImage
    rectangleImage_LBL.place( x = 15 , y = 95 )

    # THE MAIN WIDGETS
    cRoot.rectangle_LBL = Label ( cRoot , font = ( "Courier" , 12 , "bold" ) , text = "RECTANGLE's\nAREA" , width = "20"
                                , height = "20" ,bg = "#b09db9" , fg = "Black" )
    cRoot.rectangle_LBL.place( x = 280 , y = 95 , height = 50 )

    l_LBL = Label ( text = " What is the length ? "  )
    l_LBL.place ( x = 330 , y = 160 )

    l_TXT = Text ( cRoot , bd = 0 , bg = "White" , height = "1" , width = "23" , font = "Arial" )
    l_TXT.place ( x = 280 , y = 180 )

    w_LBL = Label ( text = " What is the width ? "  )
    w_LBL.place ( x = 330 , y = 210 )

    w_TXT = Text ( cRoot , bd = 0 , bg = "White" , height = "1" , width = "23" , font = "Arial" )
    w_TXT.place ( x = 280 , y = 240 )

    solve_BTN = Button ( cRoot , font = ( "Courier" , 8 , "bold" ) , text = "SOLVE" , width = "20"
                                , height = "5" ,bg = "Orange" , fg = "Black" , command = rectangle_solve )
    solve_BTN.place ( x = 310 , y = 270 , height = 30 )

    back_BTN = Button ( cRoot , font = ( "Courier" , 8 , "bold" ) , text = "RETURN" , width = "20"
                                , height = "5" ,bg = "Orange" , fg = "Black" , command = rectangle_return )
    back_BTN.place ( x = 310 , y = 350 , height = 30 )

# THIS FUNCTION CALCULATES THE AREA OF THE PARALLELOGRAM BASED ON THE USER'S INPUT.
# HERE THE PROGRAM WOULD ASK FOR THE PARALLELOGRAM'S BASE AND HEIGHT
def parallelogram():
    cRoot.geometry("500x400")
    def parallelogram_return():
        parallelogramImage_LBL.destroy()
        cRoot.parallelogram_LBL.destroy()
        b_LBL.destroy()
        b_TXT.destroy()
        h_LBL.destroy()
        h_TXT.destroy()
        solve_BTN.destroy()
        back_BTN.destroy()
        try:
            parallelogramResult_LBL.destroy()
        except:
            pass
        start()

    def parallelogram_solve():
        global parallelogramResult_LBL
        try:
            parallelogramResult_LBL.destroy()
        except:
            pass
        b = b_TXT.get( "0.0" , END )
        h = h_TXT.get( "0.0" , END )
        parallelogramResult_LBL = Label ( cRoot , text = " Result : " + str( float(b)*float(h) ) , font = ( "Courier" ,8 ,  "bold" ) ,
                                   width = "29" )
        parallelogramResult_LBL.place ( x = 280 , y = 320 )
        
    clearSelection()
    parallelogramImage_resize = Image.open( "parallelogramImage.png" ).resize( (250 , 250), Image.ANTIALIAS )
    parallelogramImage = ImageTk.PhotoImage( parallelogramImage_resize )
    parallelogramImage_LBL = Label( cRoot , image = parallelogramImage )
    parallelogramImage_LBL.photo = parallelogramImage
    parallelogramImage_LBL.place( x = 15 , y = 95 )

    cRoot.parallelogram_LBL = Label ( cRoot , font = ( "Courier" , 12 , "bold" ) , text = "PARALLELOGRAM's\nAREA" , width = "20"
                                , height = "20" ,bg = "#b09db9" , fg = "Black" )
    cRoot.parallelogram_LBL.place( x = 280 , y = 95 , height = 50 )

    b_LBL = Label ( text = " What is the base ? "  )
    b_LBL.place ( x = 330 , y = 160 )

    b_TXT = Text ( cRoot , bd = 0 , bg = "White" , height = "1" , width = "23" , font = "Arial" )
    b_TXT.place ( x = 280 , y = 180 )

    h_LBL = Label ( text = " What is the height ? "  )
    h_LBL.place ( x = 330 , y = 210 )

    h_TXT = Text ( cRoot , bd = 0 , bg = "White" , height = "1" , width = "23" , font = "Arial" )
    h_TXT.place ( x = 280 , y = 240 )

    solve_BTN = Button ( cRoot , font = ( "Courier" , 8 , "bold" ) , text = "SOLVE" , width = "20"
                                , height = "5" ,bg = "Orange" , fg = "Black" , command = parallelogram_solve )
    solve_BTN.place ( x = 310 , y = 270 , height = 30 )

    back_BTN = Button ( cRoot , font = ( "Courier" , 8 , "bold" ) , text = "RETURN" , width = "20"
                                , height = "5" ,bg = "Orange" , fg = "Black" , command = parallelogram_return )
    back_BTN.place ( x = 310 , y = 350 , height = 30 )


# THIS FUNCTION CALCULATES THE AREA OF THE TRIANGLE.
# THIS FUNCTION WOULD ONLY BE EXECUTED IF THE USER SELECTS THE BUTTON NAME TRIANGLE.
def triangle():
    cRoot.geometry("500x400")
    def triangle_return():
        triangleImage_LBL.destroy()
        cRoot.triangle_LBL.destroy()
        b_LBL.destroy()
        b_TXT.destroy()
        h_LBL.destroy()
        h_TXT.destroy()
        solve_BTN.destroy()
        back_BTN.destroy()
        try:
            triangleResult_LBL.destroy()
        except:
            pass
        start()

    def triangle_solve():
        global triangleResult_LBL
        try:
            triangleResult_LBL.destroy()
        except:
            pass
        b = b_TXT.get( "0.0" , END )
        h = h_TXT.get( "0.0" , END )
        triangleResult_LBL = Label ( cRoot , text = " Result : " + str( float(b)*float(h)*(1/2) ) , font = ( "Courier" ,8 ,  "bold" ) ,
                                   width = "29" )
        triangleResult_LBL.place ( x = 280 , y = 320 )
        
    clearSelection()
    triangleImage_resize = Image.open( "triangleImage.png" ).resize( (250 , 250), Image.ANTIALIAS )
    triangleImage = ImageTk.PhotoImage( triangleImage_resize )
    triangleImage_LBL = Label( cRoot , image = triangleImage )
    triangleImage_LBL.photo = triangleImage
    triangleImage_LBL.place( x = 15 , y = 95 )

    cRoot.triangle_LBL = Label ( cRoot , font = ( "Courier" , 12 , "bold" ) , text = "TRIANGE's\nAREA" , width = "20"
                                , height = "20" ,bg = "#b09db9" , fg = "Black" )
    cRoot.triangle_LBL.place( x = 280 , y = 95 , height = 50 )

    b_LBL = Label ( text = " What is the base ? "  )
    b_LBL.place ( x = 330 , y = 160 )

    b_TXT = Text ( cRoot , bd = 0 , bg = "White" , height = "1" , width = "23" , font = "Arial" )
    b_TXT.place ( x = 280 , y = 180 )

    h_LBL = Label ( text = " What is the height ? "  )
    h_LBL.place ( x = 330 , y = 210 )

    h_TXT = Text ( cRoot , bd = 0 , bg = "White" , height = "1" , width = "23" , font = "Arial" )
    h_TXT.place ( x = 280 , y = 240 )

    solve_BTN = Button ( cRoot , font = ( "Courier" , 8 , "bold" ) , text = "SOLVE" , width = "20"
                                , height = "5" ,bg = "Orange" , fg = "Black" , command = triangle_solve )
    solve_BTN.place ( x = 310 , y = 270 , height = 30 )

    back_BTN = Button ( cRoot , font = ( "Courier" , 8 , "bold" ) , text = "RETURN" , width = "20"
                                , height = "5" ,bg = "Orange" , fg = "Black" , command = triangle_return )
    back_BTN.place ( x = 310 , y = 350 , height = 30 )

# THIS FUNCTION WOULD ONLY BE PROCESSED ONCE THE USER CHOSE THE BUTTON NAMED 'CONE'
# THE PROGRAM WOULD BE ASKING FOR THE CONE'S RADIUS AND HEIGHT, AND WOULD OUTPUT THE CONE'S VOLUME.
def cone():
    cRoot.geometry("500x400")
    def cone_return():
        coneImage_LBL.destroy()
        cRoot.cone_LBL.destroy()
        r_LBL.destroy()
        r_TXT.destroy()
        h_LBL.destroy()
        h_TXT.destroy()
        solve_BTN.destroy()
        back_BTN.destroy()
        try:
            coneResult_LBL.destroy()
        except:
            pass
        start()

    def cone_solve():
        global coneResult_LBL
        try:
            coneResult_LBL.destroy()
        except:
            pass
        r = r_TXT.get( "0.0" , END )
        h = h_TXT.get( "0.0" , END )
        coneResult_LBL = Label ( cRoot , text = " Result : " + str( (float(r)**2)*(float(h))*(1/3)*3.14 ) , font = ( "Courier" ,8 ,  "bold" ) ,
                                   width = "29" )
        coneResult_LBL.place ( x = 280 , y = 320 )
        
    clearSelection()
    coneImage_resize = Image.open( "coneImage.png" ).resize( (250 , 250), Image.ANTIALIAS )
    coneImage = ImageTk.PhotoImage( coneImage_resize )
    coneImage_LBL = Label( cRoot , image = coneImage )
    coneImage_LBL.photo = coneImage
    coneImage_LBL.place( x = 15 , y = 95 )

    cRoot.cone_LBL = Label ( cRoot , font = ( "Courier" , 12 , "bold" ) , text = "CONE's\nVOLUME" , width = "20"
                                , height = "20" ,bg = "#b09db9" , fg = "Black" )
    cRoot.cone_LBL.place( x = 280 , y = 95 , height = 50 )

    # THESE ARE THE MAIN WIDGETS THAT WOULD BE PRESENT IN THE SCRREN.
    r_LBL = Label ( text = " What is the radius ? "  )
    r_LBL.place ( x = 330 , y = 160 )

    r_TXT = Text ( cRoot , bd = 0 , bg = "White" , height = "1" , width = "23" , font = "Arial" )
    r_TXT.place ( x = 280 , y = 180 )

    h_LBL = Label ( text = " What is the height ? "  )
    h_LBL.place ( x = 330 , y = 210 )

    h_TXT = Text ( cRoot , bd = 0 , bg = "White" , height = "1" , width = "23" , font = "Arial" )
    h_TXT.place ( x = 280 , y = 240 )

    solve_BTN = Button ( cRoot , font = ( "Courier" , 8 , "bold" ) , text = "SOLVE" , width = "20"
                                , height = "5" ,bg = "Orange" , fg = "Black" , command = cone_solve )
    solve_BTN.place ( x = 310 , y = 270 , height = 30 )

    back_BTN = Button ( cRoot , font = ( "Courier" , 8 , "bold" ) , text = "RETURN" , width = "20"
                                , height = "5" ,bg = "Orange" , fg = "Black" , command = cone_return )
    back_BTN.place ( x = 310 , y = 350 , height = 30 )


# THIS FUNCTION WOULD BE PROCESSED ONCE THE USER SELECTS THE CYCLINDER BUTTON.
# THIS FUNCTION CALCULATES THE CYLINDER'S VOLUME BASEDD ON THE USER'S INPUT.
def cylinder():
    cRoot.geometry("500x400")
    def cylinder_return():
        cylinderImage_LBL.destroy()
        cRoot.cylinder_LBL.destroy()
        r_LBL.destroy()
        r_TXT.destroy()
        h_LBL.destroy()
        h_TXT.destroy()
        solve_BTN.destroy()
        back_BTN.destroy()
        try:
            cylinderResult_LBL.destroy()
        except:
            pass
        start()

    def cylinder_solve():
        global cylinderResult_LBL
        try:
            cylinderResult_LBL.destroy()
        except:
            pass
        r = r_TXT.get( "0.0" , END )
        h = h_TXT.get( "0.0" , END )
        cylinderResult_LBL = Label ( cRoot , text = " Result : " + str( (float(r)**2)*(float(h))*3.14 ) , font = ( "Courier" ,8 ,  "bold" ) ,
                                   width = "29" )
        cylinderResult_LBL.place ( x = 280 , y = 320 )
        
    clearSelection()
    cylinderImage_resize = Image.open( "cylinderImage.png" ).resize( (250 , 250), Image.ANTIALIAS )
    cylinderImage = ImageTk.PhotoImage( cylinderImage_resize )
    cylinderImage_LBL = Label( cRoot , image = cylinderImage )
    cylinderImage_LBL.photo = cylinderImage
    cylinderImage_LBL.place( x = 15 , y = 95 )

    cRoot.cylinder_LBL = Label ( cRoot , font = ( "Courier" , 12 , "bold" ) , text = "CYLINDER's\nVOLUME" , width = "20"
                                , height = "20" ,bg = "#b09db9" , fg = "Black" )
    cRoot.cylinder_LBL.place( x = 280 , y = 95 , height = 50 )

    r_LBL = Label ( text = " What is the radius ? "  )
    r_LBL.place ( x = 330 , y = 160 )

    r_TXT = Text ( cRoot , bd = 0 , bg = "White" , height = "1" , width = "23" , font = "Arial" )
    r_TXT.place ( x = 280 , y = 180 )

    h_LBL = Label ( text = " What is the height ? "  )
    h_LBL.place ( x = 330 , y = 210 )

    h_TXT = Text ( cRoot , bd = 0 , bg = "White" , height = "1" , width = "23" , font = "Arial" )
    h_TXT.place ( x = 280 , y = 240 )

    solve_BTN = Button ( cRoot , font = ( "Courier" , 8 , "bold" ) , text = "SOLVE" , width = "20"
                                , height = "5" ,bg = "Orange" , fg = "Black" , command = cylinder_solve )
    solve_BTN.place ( x = 310 , y = 270 , height = 30 )

    back_BTN = Button ( cRoot , font = ( "Courier" , 8 , "bold" ) , text = "RETURN" , width = "20"
                                , height = "5" ,bg = "Orange" , fg = "Black" , command = cylinder_return )
    back_BTN.place ( x = 310 , y = 350 , height = 30 )

# THIS IS THE UNCTION FOR THE BUTTON NAMED 'TRAPEZOID', AND WOULD ONLY BE EXECUTED IFF THE USER SELECTS THE BUTTON.
# THIS FUNCTION CALCULATES THE TRAPEZOID'S AREA BASED ON THE USER'S INPUTTED VALUES.
def trapezoid():
    cRoot.geometry("500x450")
    def trapezoid_return():
        trapezoidImage_LBL.destroy()
        cRoot.trapezoid_LBL.destroy()
        a_LBL.destroy()
        a_TXT.destroy()
        b_LBL.destroy()
        b_TXT.destroy()
        h_LBL.destroy()
        h_TXT.destroy()
        solve_BTN.destroy()
        back_BTN.destroy()
        try:
            trapezoidResult_LBL.destroy()
        except:
            pass
        start()

    def trapezoid_solve():
        global trapezoidResult_LBL
        try:
            trapezoidResult_LBL.destroy()
        except:
            pass
        a = a_TXT.get( "0.0" , END )
        b = b_TXT.get( "0.0" , END )
        h = h_TXT.get( "0.0" , END )
        trapezoidResult_LBL = Label ( cRoot , text = " Result : " + str( (( float(a) + float(b)) / 2 ) * float(h) ) , font = ( "Courier" ,8 ,  "bold" ) ,
                                   width = "29" )
        trapezoidResult_LBL.place ( x = 280 , y = 380 )
        
    clearSelection()
    trapezoidImage_resize = Image.open( "trapezoidImage.png" ).resize( (250 , 250), Image.ANTIALIAS )
    trapezoidImage = ImageTk.PhotoImage( trapezoidImage_resize )
    trapezoidImage_LBL = Label( cRoot , image = trapezoidImage )
    trapezoidImage_LBL.photo = trapezoidImage
    trapezoidImage_LBL.place( x = 15 , y = 95 )

    cRoot.trapezoid_LBL = Label ( cRoot , font = ( "Courier" , 12 , "bold" ) , text = "TRAPEZOID's\nAREA" , width = "20"
                                , height = "20" ,bg = "#b09db9" , fg = "Black" )
    cRoot.trapezoid_LBL.place( x = 280 , y = 95 , height = 50 )

    a_LBL = Label ( text = " What is the value of 'a' ? "  )
    a_LBL.place ( x = 330 , y = 160 )

    a_TXT = Text ( cRoot , bd = 0 , bg = "White" , height = "1" , width = "23" , font = "Arial" )
    a_TXT.place ( x = 280 , y = 180 )

    b_LBL = Label ( text = " What is the value of 'b' ? "  )
    b_LBL.place ( x = 330 , y = 210 )

    b_TXT = Text ( cRoot , bd = 0 , bg = "White" , height = "1" , width = "23" , font = "Arial" )
    b_TXT.place ( x = 280 , y = 240 )

    h_LBL = Label ( text = " What is the value of 'h' ? "  )
    h_LBL.place ( x = 330 , y = 270 )

    h_TXT = Text ( cRoot , bd = 0 , bg = "White" , height = "1" , width = "23" , font = "Arial" )
    h_TXT.place ( x = 280 , y = 300 )

    solve_BTN = Button ( cRoot , font = ( "Courier" , 8 , "bold" ) , text = "SOLVE" , width = "20"
                                , height = "5" ,bg = "Orange" , fg = "Black" , command = trapezoid_solve )
    solve_BTN.place ( x = 310 , y = 330 , height = 30 )

    back_BTN = Button ( cRoot , font = ( "Courier" , 8 , "bold" ) , text = "RETURN" , width = "20"
                                , height = "5" ,bg = "Orange" , fg = "Black" , command = trapezoid_return )
    back_BTN.place ( x = 310 , y = 410 , height = 30 )

# THIS IS THE FUNCTION FOR THE RECTANGULAR SOLID.
# THIS WOULD CALCULATE THE AREA OF THE RECTANGULAR SOLID BASED ON THE USER'S INPUT.
def rSolid():
    cRoot.geometry("500x450")
    def rSolid_return():
        rSolidImage_LBL.destroy()
        cRoot.rSolid_LBL.destroy()
        l_LBL.destroy()
        l_TXT.destroy()
        w_LBL.destroy()
        w_TXT.destroy()
        h_LBL.destroy()
        h_TXT.destroy()
        solve_BTN.destroy()
        back_BTN.destroy()
        try:
            rSolidResult_LBL.destroy()
        except:
            pass
        start()

    def rSolid_solve():
        global rSolidResult_LBL
        try:
            rSolidResult_LBL.destroy()
        except:
            pass
        l = l_TXT.get( "0.0" , END )
        w = w_TXT.get( "0.0" , END )
        h = h_TXT.get( "0.0" , END )
        rSolidResult_LBL = Label ( cRoot , text = " Result : " + str( float(l) * float(w) * float(h) ) , font = ( "Courier" ,8 ,  "bold" ) ,
                                   width = "29" )
        rSolidResult_LBL.place ( x = 280 , y = 380 )
        
    clearSelection()
    rSolidImage_resize = Image.open( "rSolidImage.png" ).resize( (250 , 250), Image.ANTIALIAS )
    rSolidImage = ImageTk.PhotoImage( rSolidImage_resize )
    rSolidImage_LBL = Label( cRoot , image = rSolidImage )
    rSolidImage_LBL.photo = rSolidImage
    rSolidImage_LBL.place( x = 15 , y = 95 )

    cRoot.rSolid_LBL = Label ( cRoot , font = ( "Courier" , 12 , "bold" ) , text = "RECTANGULAR\nSOLID's AREA" , width = "20"
                                , height = "20" ,bg = "#b09db9" , fg = "Black" )
    cRoot.rSolid_LBL.place( x = 280 , y = 95 , height = 50 )

    l_LBL = Label ( text = " What is the value of 'l' ? "  )
    l_LBL.place ( x = 330 , y = 160 )

    l_TXT = Text ( cRoot , bd = 0 , bg = "White" , height = "1" , width = "23" , font = "Arial" )
    l_TXT.place ( x = 280 , y = 180 )

    w_LBL = Label ( text = " What is the value of 'w' ? "  )
    w_LBL.place ( x = 330 , y = 210 )

    w_TXT = Text ( cRoot , bd = 0 , bg = "White" , height = "1" , width = "23" , font = "Arial" )
    w_TXT.place ( x = 280 , y = 240 )

    h_LBL = Label ( text = " What is the value of 'h' ? "  )
    h_LBL.place ( x = 330 , y = 270 )

    h_TXT = Text ( cRoot , bd = 0 , bg = "White" , height = "1" , width = "23" , font = "Arial" )
    h_TXT.place ( x = 280 , y = 300 )

    solve_BTN = Button ( cRoot , font = ( "Courier" , 8 , "bold" ) , text = "SOLVE" , width = "20"
                                , height = "5" ,bg = "Orange" , fg = "Black" , command = rSolid_solve )
    solve_BTN.place ( x = 310 , y = 330 , height = 30 )

    back_BTN = Button ( cRoot , font = ( "Courier" , 8 , "bold" ) , text = "RETURN" , width = "20"
                                , height = "5" ,bg = "Orange" , fg = "Black" , command = rSolid_return )
    back_BTN.place ( x = 310 , y = 410 , height = 30 )


# THIS IS THE FUNCTION FOR THE TRAPEZOIDAL PRISM.
# THIS CALCULATES THE VOLUME OF THE TRAPEZOIDAL PRISM BASED ON THE USER'S INPUTTED VALUES.
def tPrism():
    cRoot.geometry("500x400")
    def tPrism_return():
        tPrismImage_LBL.destroy()
        cRoot.tPrism_LBL.destroy()
        B_LBL.destroy()
        B_TXT.destroy()
        h_LBL.destroy()
        h_TXT.destroy()
        solve_BTN.destroy()
        back_BTN.destroy()
        try:
            tPrismResult_LBL.destroy()
        except:
            pass
        start()

    def tPrism_solve():
        global tPrismResult_LBL
        try:
            tPrismResult_LBL.destroy()
        except:
            pass
        B = B_TXT.get( "0.0" , END )
        h = h_TXT.get( "0.0" , END )
        tPrismResult_LBL = Label ( cRoot , text = " Result : " + str( float(B)* float(h) ) , font = ( "Courier" ,8 ,  "bold" ) ,
                                   width = "29" )
        tPrismResult_LBL.place ( x = 280 , y = 320 )
        
    clearSelection()
    tPrismImage_resize = Image.open( "tPrismImage.png" ).resize( (250 , 250), Image.ANTIALIAS )
    tPrismImage = ImageTk.PhotoImage( tPrismImage_resize )
    tPrismImage_LBL = Label( cRoot , image = tPrismImage )
    tPrismImage_LBL.photo = tPrismImage
    tPrismImage_LBL.place( x = 15 , y = 95 )

    cRoot.tPrism_LBL = Label ( cRoot , font = ( "Courier" , 12 , "bold" ) , text = "TRAPEZOIDAL\nPRISM's VOLUME" , width = "20"
                                , height = "20" ,bg = "#b09db9" , fg = "Black" )
    cRoot.tPrism_LBL.place( x = 280 , y = 95 , height = 50 )

    B_LBL = Label ( text = " What is the value of 'Base'? "  )
    B_LBL.place ( x = 315 , y = 160 )

    B_TXT = Text ( cRoot , bd = 0 , bg = "White" , height = "1" , width = "23" , font = "Arial" )
    B_TXT.place ( x = 280 , y = 180 )

    h_LBL = Label ( text = " What is the height ? "  )
    h_LBL.place ( x = 330 , y = 210 )

    h_TXT = Text ( cRoot , bd = 0 , bg = "White" , height = "1" , width = "23" , font = "Arial" )
    h_TXT.place ( x = 280 , y = 240 )

    solve_BTN = Button ( cRoot , font = ( "Courier" , 8 , "bold" ) , text = "SOLVE" , width = "20"
                                , height = "5" ,bg = "Orange" , fg = "Black" , command = tPrism_solve )
    solve_BTN.place ( x = 310 , y = 270 , height = 30 )

    back_BTN = Button ( cRoot , font = ( "Courier" , 8 , "bold" ) , text = "RETURN" , width = "20"
                                , height = "5" ,bg = "Orange" , fg = "Black" , command = tPrism_return )
    back_BTN.place ( x = 310 , y = 350 , height = 30 )


# THIS FUNCTION WOULD BE EXECUTED ONCE THE USER SELECTS THE TRIANGULAR PRISM BUTTON.
# THIS FUNCTION WOULD SOLVE FOR THE TRIANGULAR PRISM'S VOLUME BASED ON THE USER'S INPUT.
def tPyramid():
    cRoot.geometry("500x400")
    def tPyramid_return():
        tPyramidImage_LBL.destroy()
        cRoot.tPyramid_LBL.destroy()
        B_LBL.destroy()
        B_TXT.destroy()
        h_LBL.destroy()
        h_TXT.destroy()
        solve_BTN.destroy()
        back_BTN.destroy()
        try:
            tPyramidResult_LBL.destroy()
        except:
            pass
        start()

    def tPyramid_solve():
        global tPyramidResult_LBL
        try:
            tPyramidResult_LBL.destroy()
        except:
            pass
        B = B_TXT.get( "0.0" , END )
        h = h_TXT.get( "0.0" , END )
        tPyramidResult_LBL = Label ( cRoot , text = " Result : " + str( (float(B)* float(h)) * (1/3) ) , font = ( "Courier" ,8 ,  "bold" ) ,
                                   width = "29" )
        tPyramidResult_LBL.place ( x = 280 , y = 320 )
        
    clearSelection()
    tPyramidImage_resize = Image.open( "tPyramidImage.png" ).resize( (250 , 250), Image.ANTIALIAS )
    tPyramidImage = ImageTk.PhotoImage( tPyramidImage_resize )
    tPyramidImage_LBL = Label( cRoot , image = tPyramidImage )
    tPyramidImage_LBL.photo = tPyramidImage
    tPyramidImage_LBL.place( x = 15 , y = 95 )

    cRoot.tPyramid_LBL = Label ( cRoot , font = ( "Courier" , 12 , "bold" ) , text = "TRIANGULAR\nPYRAMID's VOLUME" , width = "20"
                                , height = "20" ,bg = "#b09db9" , fg = "Black" )
    cRoot.tPyramid_LBL.place( x = 280 , y = 95 , height = 50 )

    B_LBL = Label ( text = " What is the value of 'Base'? "  )
    B_LBL.place ( x = 315 , y = 160 )

    B_TXT = Text ( cRoot , bd = 0 , bg = "White" , height = "1" , width = "23" , font = "Arial" )
    B_TXT.place ( x = 280 , y = 180 )

    h_LBL = Label ( text = " What is the height ? "  )
    h_LBL.place ( x = 330 , y = 210 )

    h_TXT = Text ( cRoot , bd = 0 , bg = "White" , height = "1" , width = "23" , font = "Arial" )
    h_TXT.place ( x = 280 , y = 240 )

    solve_BTN = Button ( cRoot , font = ( "Courier" , 8 , "bold" ) , text = "SOLVE" , width = "20"
                                , height = "5" ,bg = "Orange" , fg = "Black" , command = tPyramid_solve )
    solve_BTN.place ( x = 310 , y = 270 , height = 30 )

    back_BTN = Button ( cRoot , font = ( "Courier" , 8 , "bold" ) , text = "RETURN" , width = "20"
                                , height = "5" ,bg = "Orange" , fg = "Black" , command = tPyramid_return )
    back_BTN.place ( x = 310 , y = 350 , height = 30 )

# THIS FUNCTION CLEARS/DESTROYS THE WIDGETS THAT ARE PRESENT IN THE MAIN MENU/SELECTION PHASE.
def clearSelection():
    cRoot.askLBL.destroy()
    cRoot.areaLBL.destroy()
    cRoot.volumeLBL.destroy()
    cRoot.squareBTN.destroy()
    cRoot.rectangleBTN.destroy()
    cRoot.triangleBTN.destroy()
    cRoot.circleBTN.destroy()
    cRoot.trapezoidBTN.destroy()
    cRoot.parallelogramBTN.destroy()
    cRoot.cubeBTN.destroy()
    cRoot.coneBTN.destroy()
    cRoot.cylinderBTN.destroy()
    cRoot.sphereBTN.destroy()
    cRoot.tPrismBTN.destroy()
    cRoot.tPyramidBTN.destroy()
    cRoot.rSolidBTN.destroy()

# THIS IS THE FUNCTION THAT GENERATES THE WIDGETS THAT WOULD ASK FOR THE USER'S CHOICE
# DEPENDING ON THE USER'S CHOICE, ONE OF THE PREVIOUS FUNCTIONS WOULD BE EXECUTED.
def start():
    cRoot.geometry("500x500")
    #
    cRoot.askLBL = Label ( text = "WHAT TO CALCULATE?" , bg = "WHITE" , fg = "BLUE",
                            width = "20" , height = "1" , font = ( "courier" , 24 , "bold" ))
    cRoot.askLBL.place( x = 50 , y = 90 )
    #
    cRoot.areaLBL = Label ( cRoot , font = ( "Courier" , 25 , "bold" ) , text = "AREA" , width = "8"
                                , height = "20" ,bg = "#b09db9" , fg = "Black" )
    cRoot.areaLBL.place( x = 60 , y = 150 , height = 40 )
    #
    cRoot.squareBTN = Button ( cRoot , font = ( "Courier" , 15 , "bold" ) , text = "SQUARE" , width = "10"
                                , height = "50" ,bg = "orange" , fg = "black" , command = square )
    cRoot.squareBTN.place( x = 75 , y = 200 , height = 20 )
    #
    cRoot.rectangleBTN = Button ( cRoot , font = ( "Courier" , 15 , "bold" ) , text = "RECTANGLE" , width = "10"
                                , height = "50" ,bg = "orange" , fg = "black" , command = rectangle )
    cRoot.rectangleBTN.place( x = 75 , y = 235 , height = 20 )
    #
    cRoot.triangleBTN = Button ( cRoot , font = ( "Courier" , 15 , "bold" ) , text = "TRIANGLE" , width = "10"
                                , height = "50" ,bg = "orange" , fg = "black" , command = triangle )
    cRoot.triangleBTN.place( x = 75 , y = 270 , height = 20 )
    #
    cRoot.circleBTN = Button ( cRoot , font = ( "Courier" , 15 , "bold" ) , text = "CIRCLE" , width = "10"
                                , height = "50" ,bg = "orange" , fg = "black" , command = circle )
    cRoot.circleBTN.place( x = 75 , y = 305 , height = 20 )
    #
    cRoot.trapezoidBTN = Button ( cRoot , font = ( "Courier" , 15 , "bold" ) , text = "TRAPEZOID" , width = "10"
                                , height = "50" ,bg = "orange" , fg = "black" , command = trapezoid )
    cRoot.trapezoidBTN.place( x = 75 , y = 345 , height = 20 )
    #
    cRoot.parallelogramBTN = Button ( cRoot , font = ( "Courier" , 15 , "bold" ) , text = "PARALLELOGRAM" , width = "13"
                                , height = "50" ,bg = "orange" , fg = "black" , command = parallelogram )
    cRoot.parallelogramBTN.place( x = 60 , y = 385 , height = 20 )

    #
    cRoot.volumeLBL = Label ( cRoot , font = ( "Courier" , 25 , "bold" ) , text = "VOLUME" , width = "8"
                                , height = "20" ,bg = "#b09db9" , fg = "Black" )
    cRoot.volumeLBL.place( x = 260 , y = 150 , height = 40 )
    #
    cRoot.cubeBTN = Button ( cRoot , font = ( "Courier" , 15 , "bold" ) , text = "CUBE" , width = "10"
                                , height = "50" ,bg = "orange" , fg = "black" , command = cube )
    cRoot.cubeBTN.place( x = 275 , y = 200 , height = 20 )
    #
    cRoot.coneBTN = Button ( cRoot , font = ( "Courier" , 15 , "bold" ) , text = "CONE" , width = "10"
                                , height = "50" ,bg = "orange" , fg = "black" , command = cone )
    cRoot.coneBTN.place( x = 275 , y = 230 , height = 20 )
    #
    cRoot.cylinderBTN = Button ( cRoot , font = ( "Courier" , 15 , "bold" ) , text = "CYLINDER" , width = "10"
                                , height = "50" ,bg = "orange" , fg = "black" , command = cylinder )
    cRoot.cylinderBTN.place( x = 275 , y = 260 , height = 20 )
    #
    cRoot.sphereBTN = Button ( cRoot , font = ( "Courier" , 15 , "bold" ) , text = "SPHERE" , width = "10"
                                , height = "50" ,bg = "orange" , fg = "black" , command = sphere )
    cRoot.sphereBTN.place( x = 275 , y = 290 , height = 20 )
    #
    cRoot.tPrismBTN = Button ( cRoot , font = ( "Courier" , 8 , "bold" ) , text = "TRAPEZOIDAL\nPRISM" , width = "17"
                                , height = "2" ,bg = "orange" , fg = "black" , command = tPrism )
    cRoot.tPrismBTN.place( x = 275 , y = 320 , height = 28 )
    #
    cRoot.tPyramidBTN = Button ( cRoot , font = ( "Courier" , 8 , "bold" ) , text = "TRIANGULAR\nPYRAMID" , width = "17"
                                , height = "2" ,bg = "orange" , fg = "black" , command = tPyramid )
    cRoot.tPyramidBTN.place( x = 275 , y = 360 , height = 28 )
    #
    cRoot.rSolidBTN = Button ( cRoot , font = ( "Courier" , 8 , "bold" ) , text = "RECTANGULAR\nSOLID" , width = "17"
                                , height = "2" ,bg = "orange" , fg = "black" , command = rSolid )
    cRoot.rSolidBTN.place( x = 275 , y = 400 , height = 28 )
    

# THIS BLOCK OF CODE MAKES ROOT OF THE PROGRAM'S UI
# cRoot : THE TKINTER'S ROOT/ GUI'S ROOT.
cRoot = Tk()
cRoot.title( "CALCULATOR PROGRAM" )
cRoot.geometry("500x500")
cRoot.resizable( width = FALSE , height = FALSE )
cRoot.config( background = "LIGHTBLUE" )
cRoot.programName = Label ( text = "CALCULATOR PROGRAM" , bg = "black" , fg = "white",
                            width = "100" , height = "2" , font = ( "courier" , 24 , "bold" ))
cRoot.programName.pack()
    
# HERE, THE PROGRAM WOULD BE EXECUTING THE START FUNCTION TO GENERATE THE INITIAL WIDGETS THAT WOULD ASK
# FOR THE USER'S CHOICE.
programStart = start()

# LASTLY, THIS IS THE LINE OF CODE THAT WOULD INITIATE THE UI's MAIN LOOP.
# MAIN LOOP PREVENTS THE PROGRAM FROM TERMINATING.
cRoot.mainloop()
