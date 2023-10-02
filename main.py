# Yet Another Image Processer
# CMPT 120 D300
# Authors: Jeff Chiang(301451653), Mike Kim(301459116)
# Date: November 21st, 2021
# Description:Image Manipulator
# Platform used : Replit.com

import cmpt120imageProjHelper
import cmpt120imageManip
import tkinter.filedialog
import pygame
pygame.init()
# This line has exactly 100 characters (including the period), use it to keep each line under limit.
# list of system options
# Top portion of the system options
system = [
            "Q: Quit",
            "O: Open",
            "S: Save Current Image",
            "R: Reload Original Image"
         ]
# list of basic operation options 
basic = [
          "1. Apply Red Filter",
          "2. Apply Green Filter",
          "3. Apply Blue Filter",
          "4. Apply Sepia Filter",
          "5. Apply Warm Filter",
          "6. Apply Cold Filter",
          "7: Switch to Advanced Functions"
         ]

# list of advanced operation options

advanced = [
                "1: Rotate Left",
                "2. Rotate Right",
                "3. Double Size",
                "4. Half Size",
                "5. Locate Fish",
                "6: Switch to Basic Functions"
             ]

# a helper function that generates a list of strings to be displayed in the interface
# Makes the menu - BIG PRINT FUNC.
def generateMenu(state):
    """
    Input:  state - a dictionary containing the state values of the application
    Returns: a list of strings, each element represets a line in the interface
    """
    menuString = ["Welcome to CMPT 120 Image Processer!"]
    menuString.append("") # an empty line
    menuString.append("Choose the following options:")
    menuString.append("") # an empty line
    menuString += system
    menuString.append("") # an empty line
    
    # build the list differently depending on the mode attribute
    if state["mode"] == "basic":
        menuString.append("--Basic Mode--")
        menuString += basic
        menuString.append("")
        menuString.append("Enter your choice(Q/O/S/R or 1-7)")
    elif state["mode"] == "advanced":
        menuString.append("--Advanced Mode--")
        menuString += advanced
        menuString.append("")
        menuString.append("Enter your choice(Q/O/S/R or 1-6)")
    else:
        menuString.append("Error: Unknown mode!")

    return menuString

# a helper function that returns the result image as a result of the operation chosen by the user
# it also updates the state values when necessary (e.g, the mode attribute if the user switches mode)
# where all the "magic" happens -----------------------------
def handleUserInput(state, img):
    """
    Input:  state - a dictionary containing the state values of the application
            img - the 2d array of RGB values to be operated on
    Returns: the 2d array of RGB vales of the result image of an operation chosen by the user
    """
    userInput = state["lastUserInput"].upper()
    # handle the system functionalities
    if userInput.isalpha(): # check if the input is an alphabet
        print("Log: Doing system functionalities " + userInput)
        
        # When user inputs Q:
        if userInput == "Q": # this case actually won't happen, it's here as an example
          print("Log: Quitting...")
        
        # When user inputs O:
        if userInput == "O":
          print("Log: Opening Image...")
          # opens window and gets files on the side
          tkinter.Tk().withdraw()
          openFilename = tkinter.filedialog.askopenfilename()
          # img is a dark canvas- assigns a file 
          img = cmpt120imageProjHelper.getImage(openFilename)
          text = str(openFilename)
          text = text.split("/")
          cmpt120imageProjHelper.showInterface(img,text[-1],generateMenu(state))
          appStateValues["lastOpenFilename"] = openFilename
       
        # When user inputs S:
        if userInput == "S":
          print("Log: Saving Image...")
          tkinter.Tk().withdraw()
          saveFilename = tkinter.filedialog.asksaveasfilename() 
          cmpt120imageProjHelper.saveImage(img,saveFilename)
          appStateValues["lastSaveFilename"] = saveFilename
          cmpt120imageProjHelper.showInterface(img,appStateValues["lastSaveFilename"],generateMenu(state)) 
        
        # When user inputs R:
        if userInput == "R":
          img = cmpt120imageProjHelper.getImage(appStateValues["lastOpenFilename"])
          cmpt120imageProjHelper.showInterface(img,"Reloaded Image",generateMenu(state))
          #print
        
    # or handle the manipulation functionalities based on which mode the application is in
    elif userInput.isdigit(): # has to be a digit for manipulation options
        num = ["1","2","3","4","5","6","7"]
        print("Log: Doing manipulation functionalities " + userInput)
        # The output from the user's input:
        if state["mode"] == "basic":
            # Output for 1:
            if userInput == "1":
              if appStateValues["lastUserInput"] in num:
                print("Log: Performing " + basic[int(userInput)-1])
                img1 = cmpt120imageManip.ApplyRedFilter(currentImg)
                cmpt120imageProjHelper.showInterface(img1, "Apply Red Filter", generateMenu(state))
              else:
                print("Log: Performing " + basic[int(userInput)-1])
                img = appStateValues["lastOpenFilename"]
                img2 = cmpt120imageManip.ApplyRedFilter(img)
                cmpt120imageProjHelper.showInterface(img2, "Apply Red Filter", generateMenu(state))
                img2 = currentImg
                appStateValues["lastUserInput"] = "1"
            
            # Output for 2:
            if userInput == "2":
              if appStateValues["lastUserInput"] in num:
                print("Log: Performing " + basic[int(userInput)-1])
                img1 = cmpt120imageManip.ApplyGreenFilter(currentImg)
                cmpt120imageProjHelper.showInterface(img1, "Apply Green Filter", generateMenu(state))
              else:
                print("Log: Performing " + basic[int(userInput)-1])
                img = appStateValues["lastOpenFilename"]
                img2 = cmpt120imageManip.ApplyGreenFilter(currentImg)
                cmpt120imageProjHelper.showInterface(img2, "Apply Green Filter", generateMenu(state))
                img = currentImg
                appStateValues["lastUserInput"] = "2"
            
            # Output for 3:
            if userInput == "3":
              if appStateValues["lastUserInput"] in num:
                print("Log: Performing " + basic[int(userInput)-1])
                img1 = cmpt120imageManip.ApplyBlueFilter(currentImg)
                cmpt120imageProjHelper.showInterface(img1, "Apply Blue Filter", generateMenu(state))
              else:
                print("Log: Performing " + basic[int(userInput)-1])
                img = appStateValues["lastOpenFilename"]
                img = cmpt120imageManip.ApplyBlueFilter(img)
                cmpt120imageProjHelper.showInterface(img, "Apply Blue Filter", generateMenu(state))
                img = currentImg
                appStateValues["lastUserInput"] = "3"
            
            # Output for 4:    
            if userInput == "4":
              if appStateValues["lastUserInput"] in num:
                print("Log: Performing " + basic[int(userInput)-1])
                img1 = cmpt120imageManip.ApplySepiaFilter(currentImg)
                cmpt120imageProjHelper.showInterface(img1, "Apply Sepia Filter", generateMenu(state))
              else:
                print("Log: Performing " + basic[int(userInput)-1])
                img = appStateValues["lastOpenFilename"]
                img = cmpt120imageManip.ApplySepiaFilter(img)
                cmpt120imageProjHelper.showInterface(img, "Apply Sepia Filter", generateMenu(state))
                img = currentImg
                appStateValues["lastUserInput"] = "4"
            
            # Output for 5:    
            if userInput == "5":
              if appStateValues["lastUserInput"] in num:
                print("Log: Performing " + basic[int(userInput)-1])
                img1 = cmpt120imageManip.ApplyWarmFilter(currentImg)
                cmpt120imageProjHelper.showInterface(img1, "Apply Warm Filter", generateMenu(state))
              else:
                print("Log: Performing " + basic[int(userInput)-1])
                img = appStateValues["lastOpenFilename"]
                img = cmpt120imageManip.ApplySepiaFilter(img)
                cmpt120imageProjHelper.showInterface(img, "Apply Warm Filter", generateMenu(state))
                img = currentImg
                appStateValues["lastUserInput"] = "5"
            
            # Output for 6:    
            if userInput == "6":
              if appStateValues["lastUserInput"] in num:
                print("Log: Performing " + basic[int(userInput)-1])
                img1 = cmpt120imageManip.ApplyColdFilter(currentImg)
                cmpt120imageProjHelper.showInterface(img1, "Apply Cold Filter", generateMenu(state))
              else:
                print("Log: Performing " + basic[int(userInput)-1])
                img = appStateValues["lastOpenFilename"]
                img = cmpt120imageManip.ApplyColdFilter(img)
                cmpt120imageProjHelper.showInterface(img, "Apply Cold Filter", generateMenu(state))
                img = currentImg
                appStateValues["lastUserInput"] = "6"
            # Output for 7:
            if userInput == "7":
              if appStateValues["lastUserInput"] in num:
                print("Log: Performing " + basic[int(userInput)-1])
                state["mode"] = "advanced"
                cmpt120imageProjHelper.showInterface(currentImg, "Advanced", generateMenu(state))
              else:
                print("Log: Performing " + basic[int(userInput)-1])
                state["mode"] = "advanced"
                img = appStateValues["lastOpenFilename"]
                cmpt120imageProjHelper.showInterface(img, "Advanced", generateMenu(state))
                img = currentImg
                appStateValues["lastUserInput"] = "7"
        
        # Outputs for Advanced Functions
        # Output for 1:
        if state["mode"] == "advanced":
          if userInput == '1':
            if appStateValues["lastUserInput"] in num:
              print("Log: Performing " + advanced[int(userInput)-1])
              img = cmpt120imageManip.rotateLeft(currentImg)
              cmpt120imageProjHelper.showInterface(img, "Rotate Left", generateMenu(state))
              appStateValues["lastUserInput"] = "1"
            else:
              print("functionalities")
              print("Log: Performing " + advanced[int(userInput)-1])
              img = appStateValues["lastOpenFilename"]
              img = cmpt120imageManip.rotateLeft(img)
              cmpt120imageProjHelper.showInterface(img, "Rotate Left", generateMenu(state))
              img = currentImg
              appStateValues["lastUserInput"] = "1"
          
          # Output for 2:
          if userInput == '2':
            if appStateValues["lastUserInput"] in num:
              print("Log: Performing " + advanced[int(userInput)-1])
              img = cmpt120imageManip.rotateRight(currentImg)
              cmpt120imageProjHelper.showInterface(img, "Rotate Right", generateMenu(state))
            else:
              print("Log: Performing " + advanced[int(userInput)-1])
              img = appStateValues["lastOpenFilename"]
              img = cmpt120imageManip.rotateRight(img)
              cmpt120imageProjHelper.showInterface(img, "Rotate Right", generateMenu(state))
              img = currentImg
              appStateValues["lastUserInput"] = "2"
          
          # Output for 3:
          if userInput == '3':
            if appStateValues["lastUserInput"] in num:
              print("Log: Performing " + advanced[int(userInput)-1])
              img = cmpt120imageManip.doubleSize(currentImg)
              cmpt120imageProjHelper.showInterface(img, "Double Size", generateMenu(state))
            else:
              print("Log: Performing " + advanced[int(userInput)-1])
              img = appStateValues["lastOpenFilename"]
              img = cmpt120imageManip.doubleSize(img)
              cmpt120imageProjHelper.showInterface(img, "Double Size", generateMenu(state))
              img = currentImg
              appStateValues["lastUserInput"] = "3"
          
          # Output for 4:
          if userInput == '4':
            if appStateValues["lastUserInput"] in num:
              print("Log: Performing " + advanced[int(userInput)-1])
              img = cmpt120imageManip.halfSize(currentImg)
              cmpt120imageProjHelper.showInterface(img, "Half Size", generateMenu(state))
            else:
              print("Log: Performing " + advanced[int(userInput)-1])
              img = appStateValues["lastOpenFilename"]
              img = cmpt120imageManip.halfSize(img)
              cmpt120imageProjHelper.showInterface(img, "Half Size", generateMenu(state))
              img = currentImg
              appStateValues["lastUserInput"] = "4"
          
          # Output for 5:
          if userInput == '5':
            if appStateValues["lastUserInput"] in num:
              print("Log: Performing " + advanced[int(userInput)-1])
              dimensions = cmpt120imageManip.locate_Fish(currentImg)
              img = cmpt120imageManip.draw_square(dimensions[0],dimensions[1],currentImg)
              cmpt120imageProjHelper.showInterface(img, "Locate Fish", generateMenu(state))
            else:
              print("Log: Performing " + advanced[int(userInput)-1])
              img = appStateValues["lastOpenFilename"]
              dimensions = cmpt120imageManip.locate_Fish(img)
              img = cmpt120imageManip.draw_square(dimensions[0],dimensions[1],currentImg)
              cmpt120imageProjHelper.showInterface(img, "Locate Fish", generateMenu(state))
              img = currentImg
              appStateValues["lastUserInput"] = "5"
          
          # Output for 6:
          if userInput == "6":
            if appStateValues["lastUserInput"] in num:
              print("Log: Performing " + advanced[int(userInput)-1])
              state["mode"] = "basic"
              cmpt120imageProjHelper.showInterface(currentImg, "basic", generateMenu(state))
            else:
              print("Log: Performing " + basic[int(userInput)-1])
              state["mode"] = "basic"
              img = appStateValues["lastOpenFilename"]
              cmpt120imageProjHelper.showInterface(img, "Basic", generateMenu(state))
              img = currentImg
              appStateValues["lastUserInput"] = "6"
    
    # If user types something that isn't an option
    else: # unrecognized user input
        print("Log: Unrecognized user input: " + userInput)
    return img

# *** DO NOT change any of the code below this point ***

# use a dictionary to remember several state values of the application
appStateValues = {
                    "mode": "basic",
                    "lastOpenFilename": "",
                    "lastSaveFilename": "",
                    "lastUserInput": ""
                 }

currentImg = cmpt120imageProjHelper.getBlackImage(300, 200) # create a default 300 x 200 black image
cmpt120imageProjHelper.showInterface(currentImg, "No Image", generateMenu(appStateValues)) # note how it is used

# ***this is the event-loop of the application. Keep the remainder of the code unmodified***
keepRunning = True
# a while-loop getting events from pygame
while keepRunning:
    ### use the pygame event handling system ###
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            appStateValues["lastUserInput"] = pygame.key.name(event.key)
            # prepare to quit the loop if user inputs "q" or "Q"
            if appStateValues["lastUserInput"].upper() == "Q":
                keepRunning = False
            # otherwise let the helper function handle the input
            else:
                currentImg = handleUserInput(appStateValues, currentImg)
        elif event.type == pygame.QUIT: #another way to quit the program is to click the close botton
            keepRunning = False

# shutdown everything from the pygame package
pygame.quit()

print("Log: Program Quit")
