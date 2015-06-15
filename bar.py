# import numpy
# import cv2
# # from matplotlib import pyplot as plt

# def showImage(inColor):
# 	img = cv2.imread('Lenna512.png', inColor)
# 	cv2.imshow('image', img)
# 	# plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
# 	# plt.xticks([]), plt.yticks([])
# 	# plt.show()

# inColor = True
# while True:
# 	key = cv2.waitKey(0)
# 	if key == ord('1'):
# 		inColor = True;
# 	if key == ord('2'):
# 		inColor = False;
# 	if key == 27:
# 		break
# 	showImage(inColor)
# cv2.destroyAllWindows()
