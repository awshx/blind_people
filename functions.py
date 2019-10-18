import cv2 as cv
import numpy as np

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


def lenghtLetter(word):
  wordLength = 0
  lenghtLetter = 17
  letters = list(word)
  for letter in letters:
    if (letter == 'm' or letter == 'w'):
      wordLength = wordLength + 10
    if (letter.isupper()):
      wordLength = wordLength + 10 
    wordLength = wordLength + lenghtLetter
  return wordLength


def label(img, labelName, coord):
  x,y = coord
  nbLetter = len(labelName)
  cv.rectangle(img, (x,y+5), (x+lenghtLetter(labelName), y-28), (255,255,255), thickness=-1, lineType=8, shift=0)
  font                   = cv.FONT_HERSHEY_SIMPLEX
  bottomLeftCornerOfText = (x + 3, y-3)
  fontScale              = 1
  fontColor              = (0,255,0)
  lineType               = 2
  cv.putText(img, labelName, 
      bottomLeftCornerOfText, 
      font, 
      fontScale,
      fontColor,
      lineType)
    
