import cv2
import numpy as np

image = cv2.imread('./logo/sfr.jpg')
frame = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

h = frame[:,:,0]
s = frame[:,:,1]

rouge = 0
jaune = 0
vert = 0
cyan = 0
bleu = 0
magenta = 0

for index, element in enumerate(h):
	for index2, element2  in enumerate(element):
		
		if s[index][index2] < 100:
			continue
		if element2>(329/2) or element2<(30/2):
			rouge += 1
		if element2>29/2 and element2<90/2:
			jaune += 1
		if element2>89/2 and element2<150/2:
			vert += 1
		if element2>149/2 and element2<210/2:
			cyan += 1
		if element2>209/2 and element2<270/2:
			bleu += 1
		if element2>269/2 and element2<330/2:
			magenta += 1

tab = [rouge, jaune, vert, cyan, bleu, magenta]
tab.sort()
print(tab)

print("Couleur prioritaire:")
if tab[5] == 0:
	print("blanc")
if tab[5] == rouge:
	print("rouge")
if tab[5] == jaune:
	print("jaune")
if tab[5] == vert:
	print("vert")
if tab[5] == cyan:
	print("cyan")
if tab[5] == bleu:
	print("bleu")
if tab[5] == magenta:
	print("magenta")

print("\nCouleur secondaire:")
if tab[4] == 0:
        print("blanc")
elif tab[4] == rouge:
        print("rouge")
elif tab[4] == jaune:
        print("jaune")
elif tab[4] == vert:
        print("vert")
elif tab[4] == cyan:
        print("cyan")
elif tab[4] == bleu:
        print("bleu")
elif tab[4] == magenta:
        print("magenta")



# cv2.imshow("show",image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
