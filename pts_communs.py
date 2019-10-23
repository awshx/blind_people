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
def lengthLetter(word):
  #Length of the word
  wordLength = 0
  #Length of a standard letter (low case and not a double letter like m or w)
  lengthLetter = 17
  #We cut the word into a list of letters
  letters = list(word)
  #for every letter of the word
  for letter in letters:
    #We check if it's a 'm' or a 'w'
    if (letter == 'm' or letter == 'w'):
      #If so, we increase the length even more than if it was a standard letter 
      wordLength = wordLength + 10
    #If the letter is in uppercase
    if (letter.isupper()):
      #we increase the length even more than if it was a standard letter 
      wordLength = wordLength + 10
    #We increase the length of the word each at each letter
    wordLength = wordLength + lengthLetter
  #We return the final number corresponding to the length of the word
  return wordLength


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
  #We extract the coordinates
  x,y = coord
  #Number of letter of the name
  nbLetter = len(labelName)
  #We draw the white rectangle at the coordinate of the label
  cv2.rectangle(img, (x,y+5), (x+lengthLetter(labelName), y-28), (255,255,255), thickness=-1, lineType=8, shift=0)
  #params of the label's text 
  font                   = cv.FONT_HERSHEY_SIMPLEX
  bottomLeftCornerOfText = (x + 3, y-3)
  fontScale              = 1
  fontColor              = (0,255,0)
  lineType               = 2
  #We put the text on the white rectangle
  cv2.putText(img, labelName, 
      bottomLeftCornerOfText, 
      font, 
      fontScale,
      fontColor,
      lineType)
    
