import cv2
import openpyxl 
from datetime import date
from zipfile import ZipFile
import os
import pytesseract #optical char recogn
# import matplotlib.pyplot as plt
from pytesseract import Output


# def captch_ex(img):
#     img_final = img
#     img2gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     ret, mask = cv2.threshold(img2gray, 180, 255, cv2.THRESH_BINARY)
#     image_final = cv2.bitwise_and(img2gray, img2gray, mask=mask)
#     ret, new_img = cv2.threshold(image_final, 180, 255, cv2.THRESH_BINARY)  # for black text , cv.THRESH_BINARY_INV

#     kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3,
#                                                          3))  # to manipulate the orientation of dilution , large x means horizonatally dilating  more, large y means vertically dilating more
#     dilated = cv2.dilate(new_img, kernel, iterations=9)  # dilate , more the iteration more the dilation

#     # for cv2.x.x

#     contours, hierarchy = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)  # findContours returns 3 variables for getting contours
#     # for cv3.x.x comment above line and uncomment line below
#     #image, contours, hierarchy = cv2.findContours(dilated,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)


#     for contour in contours:
#         # get rectangle bounding contour
#         [x, y, w, h] = cv2.boundingRect(contour)

#         # Don't plot small false positives that aren't text
#         if w < 35 and h < 35:
#             continue

#         # draw rectangle around contour on original image
#         cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 2)
#         print("Hello")
#         '''
#         #you can crop image and send to OCR  , false detected will return no text :)
#         cropped = img_final[y :y +  h , x : x + w]

#         s = file_name + '/crop_' + str(index) + '.jpg' 
#         cv2.imwrite(s , cropped)
#         index = index + 1

#         '''
#     # write original image with added contours to disk
#     # cv2.imshow('captcha_result', img)
#     # plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
#     # plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
#     # plt.show()


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

zipObj = ZipFile('sample.zip', 'w')
dat = date.today()
dat = dat.strftime("%m/%d/%y")
# template1.png is the template 
# certificate 
template_path = 'template12.jpeg'
# Excel file containing names of  
# the participants 
details_path = 'sheet.xlsx'
  
# Output Paths 
output_path = 'D:\Python Everything\Certificate_Sukku'
   
# Setting the font size and font 
# colour 
font_size = 3
font_color = (0,0,0) 
   
# Coordinates on the certificate where 
# will be printing the name (set 
# according to your own template) 

# coordinate_y_adjustment = -40
# coordinate_x_adjustment = 7
# coordinate_y_Date = -195
# coordinate_x_Date = -160

# loading the details.xlsx workbook  
# and grabbing the active sheet 
obj = openpyxl.load_workbook(details_path) 
sheet = obj.active 
img = cv2.imread(template_path)

data = pytesseract.image_to_data(img, output_type=Output.DICT)
# print(data)
for i in range (len(data['text'])):
    data['text'][i] = data['text'][i].lower()

ind_to = data['text'].index('to')
ind_this = data['text'].index('this')
ind_for = data['text'].index('in')

left = (data['left'][ind_to] + data['left'][ind_this])//2
right = (data['top'][ind_to] + data['left'][ind_for])//2

# data=pytesseract.image_to_boxes(img)
# print(data)

# suz = str(data[0])
# data = data.split(' ')
# print(data)
# for i in range (len(data)):
#     # print("d")
#     if i%5 == 0:
#         suz += data[i]
# print(suz)
# captch_ex(img)
'''
# Convert the image to gray scale 
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

# Performing OTSU threshold 
ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV) 

# Specify structure shape and kernel size.  
# Kernel size increases or decreases the area  
# of the rectangle to be detected. 
# A smaller value like (10, 10) will detect  
# each word instead of a sentence. 
rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18)) 

# Appplying dilation on the threshold image 
dilation = cv2.dilate(thresh1, rect_kernel, iterations = 1) 

# Finding contours 
contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL,  
                                                cv2.CHAIN_APPROX_NONE) 

# Creating a copy of image 
im2 = img.copy() 

# A text file is created and flushed 
# file = open("recognized.txt", "w+") 
# file.write("") 
# file.close() 

# Looping through the identified contours 
# Then rectangular part is cropped and passed on 
# to pytesseract for extracting text from it 
# Extracted text is then written into the text file 
for cnt in contours: 
    x, y, w, h = cv2.boundingRect(cnt) 
    print(x,y,w,h)
    # Drawing a rectangle on copied image 
    rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2) 
    # plt.imshow(rect, cmap = 'gray', interpolation = 'bicubic')
    # plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
    # plt.show()

    # Cropping the text block for giving input to OCR 
    cropped = im2[y:y + h, x:x + w] 

    # Apply OCR on the cropped image 
    text = pytesseract.image_to_string(cropped)

    # Appending the text into file 
    # file.write(text) 
    # file.write("\n") 
    
    # # Close the file 
    # file.close()
    
    
'''

# printing for the first 10 names in the 
# excel sheet 
for i in range(1,11): 
    # grabs the row=i and column=1 cell  
    # that contains the name value of that 
    # cell is stored in the variable certi_name 
    get_name = sheet.cell(row = i ,column = 1) 
    certi_name = get_name.value 
    #print(certi_name)
    # read the certificate template 
    img = cv2.imread(template_path)
    # choose the font from opencv 
    font = cv2.FONT_HERSHEY_PLAIN               
   
    # get the size of the name to be 
    # printed 
    # text_size = cv2.getTextSize(certi_name, font, font_size, 10)[0]     
   
    # get the (x,y) coordinates where the 
    # name is to written on the template 
    # The function cv.putText accepts only 
    # integer arguments so convert it into 'int'. 
    # text_x = (img.shape[1] - text_size[0]) / 2 + coordinate_x_adjustment  
    # text_y = (img.shape[0] + text_size[1]) / 2 - coordinate_y_adjustment 
    # text_x = int(text_x) 
    # text_y = int(text_y) 

    # textx = (img.shape[1] - text_size[0]) / 2 + coordinate_x_Date
    # texty = (img.shape[0] + text_size[1]) / 2 - coordinate_y_Date
    # textx = int(textx) 
    # texty = int(texty) 

# O 776 447 792 463 0
# I 492 311 498 324 0

    # (500,447 ),  
    cv2.putText(img, 'Sukrati', 
              (left-50,right+40),  
              font, 
              font_size, 
              font_color, 4)

    # cv2.putText(img, certi_name, 
    #           (text_x ,text_y ),  
    #           font, 
    #           font_size, 
    #           font_color, 4)

    # cv2.putText(img, dat, 
    #         (textx ,texty ),  
    #         font, 
    #         font_size - 1.5, 
    #         font_color, 2) 

    # Output path along with the name of the 
    # certificate generated 
    certi_path = output_path + '/certi{}'.format(i) + '.png'
    img_path = 'certi{}'.format(i) + '.png'
    # Save the certificate
               
    cv2.imwrite(certi_path,img)
    zipObj.write(img_path)
    os.remove(img_path)
    
zipObj.close()


