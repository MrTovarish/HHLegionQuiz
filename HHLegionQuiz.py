from tkinter import *

root = Tk()

#Creating a Label Widget
myLabel = Label(root, text='Hello World!')
#Shoving it onto the screen
myLabel.pack()

root.mainloop()

input('Test Input')
if(input == 'Test'):
    print('Pass')
else:
    print('Fail')
#Recreate the Horus Heresy Legion picker
#Need to create a reference for each legion to apply weights to
#Each answer will add weights to each legion for which association makes sense
#Chosen Legion will generate based on highest weight.  
#If weights are tied - needs decision

#Loyalists: Dark Angels,White Scars,Space Wolves,Imperial Fists,Blood Angels,Iron Hands,Ultramarines,Salamanders,Raven Guard
#Traitors: Emperor's Children,IronWarriors,Night Lords,World Eaters,Death Guard,Thousand Sons,Sons of Horus,Word Bearers,Alpha Legion

#this is NOT a decision tree.  Needs to be dynamically weighted, allowing for all questions to be answered

#Weights will be 1, 2, or 3 points.  
#Need to select a minimum or consistent amount of points distributed per question
#Need mechanism (or manually) to ensure certain Legions are not favored by sheer volume of questions related to them

def assign_legion(legion):
    global lgn
    if legion == 'Dark Angels':
        lgn = 'Dark Angels'
    elif legion == 'Salamanders':
        lgn = 'Salamanders'
    elif legion == 'Imperial Fists':
        lgn = 'Imperial Fists'
    elif legion == 'White Scars':
        lgn = 'White Scars'
    elif legion == 'Space Wolves':
        lgn = 'Space Wolves'
    elif legion == 'Blood Angels':
        lgn = 'Blood Angels'
    elif legion == 'Iron Hands':
        lgn = 'Iron Hands'
    elif legion == 'Ultramarines':
        lgn = 'Ultramarines' 
    elif legion == 'Raven Guard':
        lgn = 'Raven Guard'
    elif legion == 'Emperor\'s Children':
        lgn = 'Emperor\'s Children'
    elif legion == 'Iron Warriors':
        lgn = 'Iron Warriors'
    elif legion == 'Night Lords':
        lgn = 'Night Lords'
    elif legion == 'World Eaters':
        lgn = 'World Eaters'
    elif legion == 'Death Guard':
        lgn = 'Death Guard'
    elif legion == 'Thousand Sons':
        lgn = 'Thousand Sons'
    elif legion == 'Sons of Horus':
        lgn = 'Sons of Horus'
    elif legion == 'Word Bearers':
        lgn = 'Word Bearers'
    elif legion == 'Alpha Legion':
        lgn = 'Alpha Legion'                                                           
    else:
        lgn = 'Fail'
        if(lgn == 'Fail'):
            raise Exception('Error, please refresh the page')
        

        
assign_legion('Dark Angels')

print(lgn)

def assign_weight():
    if input == True:
        print('Dark Angels' + '3')