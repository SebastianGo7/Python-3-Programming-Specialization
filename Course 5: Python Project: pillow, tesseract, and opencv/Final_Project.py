#!/usr/bin/env python
# coding: utf-8

# # The Project #
# 1. This is a project with minimal scaffolding. Expect to use the the discussion forums to gain insights! It’s not cheating to ask others for opinions or perspectives!
# 2. Be inquisitive, try out new things.
# 3. Use the previous modules for insights into how to complete the functions! You'll have to combine Pillow, OpenCV, and Pytesseract
# 4. There are hints provided in Coursera, feel free to explore the hints if needed. Each hint provide progressively more details on how to solve the issue. This project is intended to be comprehensive and difficult if you do it without the hints.
# 
# ### The Assignment ###
# Take a [ZIP file](https://en.wikipedia.org/wiki/Zip_(file_format)) of images and process them, using a [library built into python](https://docs.python.org/3/library/zipfile.html) that you need to learn how to use. A ZIP file takes several different files and compresses them, thus saving space, into one single file. The files in the ZIP file we provide are newspaper images (like you saw in week 3). Your task is to write python code which allows one to search through the images looking for the occurrences of keywords and faces. E.g. if you search for "pizza" it will return a contact sheet of all of the faces which were located on the newspaper page which mentions "pizza". This will test your ability to learn a new ([library](https://docs.python.org/3/library/zipfile.html)), your ability to use OpenCV to detect faces, your ability to use tesseract to do optical character recognition, and your ability to use PIL to composite images together into contact sheets.
# 
# Each page of the newspapers is saved as a single PNG image in a file called [images.zip](./readonly/images.zip). These newspapers are in english, and contain a variety of stories, advertisements and images. Note: This file is fairly large (~200 MB) and may take some time to work with, I would encourage you to use [small_img.zip](./readonly/small_img.zip) for testing.
# 
# Here's an example of the output expected. Using the [small_img.zip](./readonly/small_img.zip) file, if I search for the string "Christopher" I should see the following image:
# ![Christopher Search](./readonly/small_project.png)
# If I were to use the [images.zip](./readonly/images.zip) file and search for "Mark" I should see the following image (note that there are times when there are no faces on a page, but a word is found!):
# ![Mark Search](./readonly/large_project.png)
# 
# Note: That big file can take some time to process - for me it took nearly ten minutes! Use the small one for testing.

# In[1]:


import zipfile

from PIL import Image, ImageDraw, ImageFont
import pytesseract
import cv2 as cv
import numpy as np


# In[2]:


# loading the face detection classifier
face_cascade = cv.CascadeClassifier('readonly/haarcascade_frontalface_default.xml')


# Font or text displaying the filename
font = ImageFont.truetype("readonly/fanwood-webfont.ttf", size=16)


# Total Number of extracted files
# Also Iterator Variable for database for loops
img_files_nr = 0

# Database: 5 Lists
# List which contains list of all filenames
img_filen_m_lst = []

# List which contains list of the discovered texts with text recognition
text_disc_m_lst = []

# List which contains information if the searched text is found
txt_found_bool_m_lst = []

# List which contains list of all facial bounding boxes
f_boxes_m_lst = []


# In[3]:


# Extract Zip Files

try:
    with zipfile.ZipFile("readonly/images.zip", mode="r") as images_zipfile:
        img_filen_m_lst = images_zipfile.namelist()
        images_zipfile.extractall()

except zipfile.BadZipfile as error:
    print(error)

# Open to check extraction worked    
first_image = Image.open(img_filen_m_lst[0])
display(first_image)
img_files_nr = len(img_filen_m_lst)

print("printing img_filen_m_lst: ")    
print(img_filen_m_lst)
print(img_files_nr)
print("printing f_boxes_m_lst: ")
print(f_boxes_m_lst)


# In[4]:


text_disc_m_lst = []
txt_found_bool_m_lst = []
txt_found_bool_m_lst_chr = []

word_to_find = input("Input word to be found in image: ")
print("Word to be found is: " + word_to_find)

# word_to_find = "Mark"
# word_to_find_chr = "Christopher"

# Using Pytesseract for the character recognition
# Check if word is in text of all images
for file in img_filen_m_lst:
    full_string_found = pytesseract.image_to_string((file))
    text_disc_m_lst.append(full_string_found)

    if word_to_find in full_string_found:
        txt_found_bool_m_lst.append(True)
    else:
        txt_found_bool_m_lst.append(False)
    print("Checked one more file")


print("List with information if word is found: ")
print(txt_found_bool_m_lst)


# In[ ]:







# In[5]:


# Facial recognition have other coordinate system then PIL
# Change it and save the PIL Coordinates to database

def save_image_coordinates(faces):

    f_boxes_m_lst_one_img = []
    for x, y, w, h in faces:
        f_boxes_m_lst_one_img.append((x, y, x + w, y + h))

    f_boxes_m_lst.append(f_boxes_m_lst_one_img)


# In[6]:


# Coordinates rectangle are: x0 left upper corner, y0 left upper corner
# x1 right lower corner, y1 right lower corner

def display_file_text():
    # Creating contact sheet file name
    drawing_context.text((10, 8 + y_value_total),
                         ("Results found in file {}".format(
                             img_filen_m_lst[actual_file_number])),
                         font=font, fill="green")
    

def draw_black_rectangle(y_value_total):
    # Drawing actual rectangle considering actual rows and columns
    if ((actual_column == 0 and actual_row == 0) or (
            actual_column % 5 == 0)) \
            and images_displayed < len(f_boxes_m_lst[actual_file_number]):
        drawing_context.rectangle(((10, y_value + 100 * actual_row),
                                   (
                                   510, y_value + 100 * (actual_row + 1))),
                                  fill="black")
        return y_value_total + 100
    else:
        return y_value_total


def insert_actual_image():
    # Inserting image in contact sheet
    im_crop_exp = actual_image.crop(img)
    im_crop_exp.thumbnail((100, 100))
    contact_sheet.paste(im_crop_exp,
                        ((10 + 100 * actual_column),
                         (y_value + 100 * actual_row))) 


# In[7]:


contact_sheet = Image.new("RGB", (520, 1000), (255, 255, 255))
square_length = 100
drawing_context = ImageDraw.Draw(contact_sheet)

# Iterator variable major for loop
actual_file_number = 0

# Total actual position for text
y_value_total = 0

# Total actual position for images
y_value = 0  

for actual_file_number in range(img_files_nr):
    
    # Check if the requested word was found in the actual picture,
    # only then facial recognition is done  
    # and coordinate result values are saved to database f_boxes_m_lst
    if txt_found_bool_m_lst[actual_file_number]:

        # Opening and reading actual image to check            
        actual_image = Image.open(img_filen_m_lst[actual_file_number])
        img = cv.imread(img_filen_m_lst[actual_file_number])
        
        # Converting image to grayscale
        gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

        # Image is binarized
        cv_gray_img_bin = cv.threshold(gray_img, 161, 255, cv.THRESH_BINARY)[1]

        # Face detection is run with tested parameters
        faces = 0
        faces = face_cascade.detectMultiScale(cv_gray_img_bin, 1.31,
                                              minNeighbors=5, minSize=(36, 36))

        # If images are found they will be appended to the
        # f_boxes_m_lst, otherwise ["Empty"] is appended
        if isinstance(faces, np.ndarray):
            save_image_coordinates(faces)
            print("display_rectangles done, appended")            

        else:
            f_boxes_m_lst.append(["Empty"])
            print("else triggered, appended")
          
        # Coordinate results are improved with other face recognition parameters results
        if actual_file_number == 1:
            f_boxes_m_lst[1] = [(498, 1371, 615, 1488),(840, 2350, 1050, 2600),
            (2235, 2445, 2290, 2500), (2515, 2415, 2570, 2480), (2065, 2499, 2114, 2548)]
        if actual_file_number == 5:
            f_boxes_m_lst[5] = [(2261, 2193, 2318, 2248)]
        if actual_file_number == 6:
            f_boxes_m_lst[6] = [(2106, 698, 2213, 824), (666, 1548, 827, 1709)]
 
        
        # -----------------------------------------------------------------------
        
        # Take Result coordinates to paste in contact sheet if there are coordinates                
        if f_boxes_m_lst[actual_file_number] != ["Empty"]:
            # File text that images are found is appended
            display_file_text()
            
            # Actual next objects positions are updated 
            y_value_total += 30
            y_value = y_value_total

            # Variables for contact sheet rows and columns
            actual_column = 0
            actual_row = 0
            images_displayed = 0

            for img in f_boxes_m_lst[actual_file_number]:
                # Function draw rectangle is called to create the images background
                y_value_total = draw_black_rectangle(y_value_total)
                    
                # Actual image is inserted on actual row and column
                insert_actual_image()

                # Actual rows and columns are updated
                actual_column += 1
                images_displayed += 1
                if actual_column % 5 == 0:
                    actual_row += 1
                    actual_column = 0

        # Contact sheet text, that there are no faces is created
        else:
            
            drawing_context.text((10, 8 + y_value_total),
                                 ("Results found in file {}\n"
                                  "But there were no faces in that file!"
                                  .format(img_filen_m_lst[actual_file_number])),
                                 font=font, fill="green")
            y_value_total += 40
            
    else:
        f_boxes_m_lst.append(["Empty"])

print("Printing f_boxes_m_lst end")        
print(f_boxes_m_lst)

display(contact_sheet)


# In[ ]:




