import cv2
import numpy as np
import matplotlib.pyplot as plt

def my_function():
  print("Hello from a function") 

#cropImageLeft
#Desc : return an img of the top left of an img
#Params :
#   img : picture (from a cv.imread(...) )
#Return :
#   croppedImg : picture of the top left of the img in param
def cropImageLeft(img):
    #height of the  cropped picture
    #we take the height of the param img and we divide by 2
    heightCropped = int(np.size(img, 0)/2)
    #width of the cropped picture
    #we take the width of the param img and we divide by 3
    widthCropped = int(np.size(img, 1)/3)
    #we crop the img at the top left
    #(0,0) is the top left of the picture in opencv
    #we cut the param img from (0,0) to (height,width) 
    croppedImg = img[0:0+heightCropped, 0:0+widthCropped]
    return(croppedImg)

#cropImageRight
#Desc : return an img of the top right of an img
#Params :
#   img : picture (from a cv.imread(...) )
#Return :
#   croppedImg : picture of the top right of the img in param
def cropImageRight(img):
    #height of the  cropped picture
    #we take the height of the param img and we divide by 2
    heightCropped = int(np.size(img, 0)/2)
    #width of the cropped picture
    #we take the width of the param img and we divide by 3
    widthCropped = int(np.size(img, 1)/3)
    #we crop the img at the top left
    #(0,0) is the top right of the picture in opencv
    #we cut the param img from (0, 2*widthCropped) (half of the img) to () 
    croppedImg = img[0:0+heightCropped, widthCropped*2:widthCropped*3]	
    return(croppedImg)
  
#CompareLogo
#Desc : Compare a picture to another (logo) and return the number of matches
#Params :
#  img: cropped image of the street where a logo can be
#  imgLogo: image of a logo
#Return :
#  number of matches
def compareLogo(img, imgLogo):
    #We take keypoints and descriptor of the picture
    kp1, des1 = sift.detectAndCompute(img, None)
    #We take keypoints and descriptor of the logo
    kp2, des2 = sift.detectAndCompute(imgLogo, None)
    # BFMatcher with default params
    # It's the tool to have matches
    bf = cv.BFMatcher()
    #We take the matches
    matches = bf.knnMatch(des1,des2,k=2)
    #Array to stock the best matches
    good = []
    for m,n in matches:
        # Apply ratio test to select the best matches
        if m.distance < 0.75*n.distance:
            good.append([m])
    #We return the number of good matches
    return(len(good))


#lengthLetter
#Desc : Calculate approximatively the length of a word in pixels to show the label of the logo
#       It can be a word or a sentence
#Param :
#  word : a word in string
#Return
#  wordLength : the number of pixel corresponding to the length of the label
def lenghtLetter(word):
  #Length of the word
  wordLength = 0
  #Length of a standard letter (low case and not a double letter like m or w)
  lenghtLetter = 17
  #We cut the word into a list of letters
  letters = list(word)
  #for every letter of the word
  for letter in letters:
    #We check if it's a 'm' or a 'w'
    if (letter == 'm' or letter == 'w' or letter == 'M' or letter == 'W'):
      #If so, we increase the length even more than if it was a standard letter 
      wordLength = wordLength + 5
    #If the letter is in uppercase
    if (letter.isupper()):
      #we increase the length even more than if it was a standard letter 
      wordLength = wordLength + 3
    #We increase the length of the word each at each letter
    wordLength = wordLength + lenghtLetter
  #We return the final number corresponding to the length of the word
  return wordLength

def coef(number, scale):
	return (scale * number)

#label
#Desc : put a label on the picture to the indicated coordonate
#Params :
#   img : picture (from a cv.imread(...) )
#   labelName : name of the label, a string of characters
#   coord : coordinate where we want to put the labe
#           the coordinate correspond to the bottom left of the label
#           the coordinate have to be in a tuple: (x,y)
#Return: nothing, the label is put directly on the img of param
def label(img, labelName, coord):

  sizeLetter=2

  #We extract the coordinates
  x,y = coord

  xPosition=x-150
  yPosition=y-150

  #Number of letter of the name
  nbLetter = len(labelName)

 #length in pixels of the label
  lengthLabel = lenghtLetter(labelName)
  #Coordinates of the letters
  xRect1 = int(xPosition-coef(lengthLabel/2,sizeLetter))
  #print("xRect1")
  #print(xRect1)
  yRect1 = int(yPosition+coef(20,sizeLetter))
  #print("yRect1")
  #print(yRect1)
  xRect2 = int(xPosition+coef(lengthLabel/2,sizeLetter))
  #print("xRect2")
  #print(xRect2)
  yRect2 = int(yPosition-coef(13,sizeLetter))
  #print("yRect2")
  #print(yRect2)

  #image's width
  heightImg = (np.size(img, 0))
  #image's height
  widthImg = (np.size(img, 1))
  #width of the rectangle
  widthRect = abs(xRect2 - xRect1)
  #height of the rectangle
  heightRect = abs(yRect1 - yRect2)

  #We calculate the margin needed to create the frame
  marginRect = coef(3,sizeLetter)

  #All the cases 
  if(xRect1 < 0):
    #print("oui1")
    xRect1 = 0
    xRect2 = xRect1 + widthRect
  if (xRect2 > widthImg):
    #print("oui2")
    xRect2 = widthImg
    xRect1 = int(xRect2-widthRect)
  if(yRect2 < 0):
    #print("oui3")
    yRect2 = 0
    yRect1 = int(yRect2 + heightRect)
  if(yRect1 > heightImg):
    #print("oui4")
    yRect1 = heightImg
    yRect2 = int(yRect1 - heightRect)

  #Coordinate of the labels
  xLabel = xRect1
  yLabel = yRect1 - 8

  #We create the location of the (red) frame
  xFrame1 = xRect1-marginRect
  yFrame1 = yRect1+marginRect
  xFrame2 = xRect2+marginRect
  yFrame2 = yRect2-marginRect

  #We draw the white rectangle at the coordinate of the label
  cv2.rectangle(img, (xRect1,yRect1), (xRect2, yRect2), (0,0,0), thickness=-1, lineType=8, shift=0)
  #We draw the red frame
  cv2.rectangle(img, (xFrame1,yFrame1), (xFrame2, yFrame2), (255,255,255), thickness=3, lineType=8, shift=0)

  cv2.line(img, (x,y), (xRect2, yRect2+30), (0,0,0), thickness=3, lineType=8, shift=0)  

  #params of the label's text 
  font                   = cv2.FONT_HERSHEY_SIMPLEX
  bottomLeftCornerOfText = (xLabel, yLabel)
  fontScale              = sizeLetter
  fontColor              = (255,255,255)
  lineType               = 2
  #We put the text on the white rectangle
  cv2.putText(img, labelName, 
      bottomLeftCornerOfText, 
      font, 
      fontScale,
      fontColor,
      lineType)
    
