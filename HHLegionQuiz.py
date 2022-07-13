from tkinter import *
import django

#MAYBE SHOULD BE BUILDING THIS IN JS INSTEAD EH?------------------------------------------------------------------------------------------------------------------

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

weight = 'base weight'

#Dark Angels weight variable
daw = 0
#Emperor's Children weight variable
ecw = 0
#Iron Warriors weight variable
iww = 0
#Salamanders weight variable
saw = 0
#Imperial Fists weight variable
ifw = 0
#Blood Angels weight variable
baw = 0
#Iron Hands weight variable
ihw = 0
#White Scars weight variable
wsw = 0
#Raven Guard weight variable
rgw = 0
#Ultramarines weight variable
umw = 0
#Space Wolves weight variable
sww = 0
#Death Guard weight variable
dgw = 0
#Thousand Sons weight variable
tsw = 0
#World Eaters weight variable
wew = 0
#Word Bearers weight variable
wbw = 0
#Night Lords weight variable
nlw = 0
#Sons of Horus weight variable
shw = 0
#Alpha Legion weight variable
alw = 0

print('You are invading a hostile planet. Do you spearhead with Fast Attack, or hunker down for to blast the enemy with Heavy Assault?')
#this part probably goes in the HTML
#for the purpose of this test code, we'll define the pys-onClick variable as 'tst'
tst = True
if tst == True:
    wsw = wsw + 3
    rgw = rgw + 2
    wew = wew + 1
elif tst == False:
    iww = iww + 3
    ifw = ifw + 2
    dgw = dgw + 1



    