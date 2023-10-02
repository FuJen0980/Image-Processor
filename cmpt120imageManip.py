# Yet Another Image Processer
# CMPT 120 D300
# Authors: Jeff Chiang(301451653), Mike Kim(301459116)
# Date: November 21st, 2021
# Description:Image Manipulator Functions


import cmpt120imageProjHelper

# Basic Modes
# 1. Apply red filter 
def ApplyRedFilter(pixels):
  # A variable is assigned to represent the new image
  new_img = cmpt120imageProjHelper.getBlackImage(len(pixels[0]),len(pixels))
  height = len(pixels)
  width = len(pixels[0])
  # Nested for loop
  for row in range(height):
      for col in range(width):
        new_img[row][col] = pixels[row][col]
        image = new_img[row][col]
        image[1] = 0 # Set the G value to zero
        image[2] = 0 # Set the B value to zero
  return new_img

# 2. Apply green filter
def ApplyGreenFilter(pixels):
  height = len(pixels)
  width = len(pixels[0])
  for row in range(height):
      for col in range(width):
        image = pixels[row][col]
        image[0] = 0 # Set the R value to 0
        image[2] = 0 # Set the B value to 0
  return pixels

# 3. Apply blue filter
def ApplyBlueFilter(pixels):
  height = len(pixels)
  width = len(pixels[0])
  for row in range(height):
      for col in range(width):
        image = pixels[row][col]
        image[0] = 0 # Set the R value to 0
        image[1] = 0 # Set the G value to 0
  return pixels

# 4. Apply sepia filter 
def ApplySepiaFilter(pixels):
  height = len(pixels)
  width = len(pixels[0])
  # nested for loops
  for row in range(height):
      for col in range(width):
        image = pixels[row][col]
        # SepiaRed:
        SepiaRed = int(((image[0]*0.393) + (image[1]*0.769) + (image[2]*0.189)))
        # SepiaGreen:
        SepiaGreen = int(((image[0]*0.349) + (image[1]*0.686) + (image[2]*0.168)))
        # SepiaBlue:
        SepiaBlue = int(((image[0]*0.272) + (image[1]*0.534) + (image[2]*0.131)))
        SepiaRed = min(255,SepiaRed)
        SepiaGreen = min(255,SepiaGreen)
        SepiaBlue = min(255,SepiaBlue)
        image[0] = SepiaRed
        image[1] = SepiaGreen
        image[2] = SepiaBlue
  return pixels

# 5. Apply warm filter
def ApplyWarmFilter(pixels):
  height = len(pixels)
  width = len(pixels[0])
  # Nested for loop
  for row in range(height):
    for col in range(width):
      image = pixels[row][col]
      # Scale up if statement
      if image[0] < 64:
        scaleUpRedValue = image[0]/(64*80)
      elif 64 <= image[0] < 128:
        scaleUpRedValue = (image[0]-64)/(128-64) * (160-80) + 80
      else:
        scaleUpRedValue = (image[0]-128)/(255-128) * (255-160) + 160
      # Scale down if statement
      if image[2] < 64:
        scaleDownBlueValue = image[2]/(64*50)
      elif 64 <= image[2] & image[2] < 128:
        scaleDownBlueValue = image[2]-64/(128-64)*(100-50)+50
      else:
        scaleDownBlueValue = image[2]-128/(255-128) * (255-100) +100
      image[0] = scaleUpRedValue
      image[2] = scaleDownBlueValue
  return pixels 

# 6. Apply cold filter
def ApplyColdFilter(pixels):
  height = len(pixels)
  width = len(pixels[0])
  for row in range(height):
    for col in range(width):
      image = pixels[row][col]
      # Scale up if statement
      if image[2] < 64:
        scaleUpBlueValue = image[2]/(64*80)
      elif 64 <= image[2] < 128:
        scaleUpBlueValue = (image[2]-64)/(128-64) * (160-80) + 80
      else:
        scaleUpBlueValue = (image[2]-128)/(255-128) * (255-160) + 160
      # Scale down if statement
      if image[0] < 64:
        scaleDownRedValue = image[0]/(64*50)
      elif 64 <= image[0] & image[0] < 128:
        scaleDownRedValue = image[0]-64/(128-64)*(100-50)+50
      else:
        scaleDownRedValue = image[0]-128/(255-128) * (255-100) +100
      image[2] = scaleUpBlueValue
      image[0] = scaleDownRedValue
  return pixels

# ADVANCED FUNCTIONS

# 1. Rotate Left
def rotateLeft(pixels):
  new_img = cmpt120imageProjHelper.getBlackImage(len(pixels),len(pixels[0]))
  height = len(pixels)
  width = len(pixels[0])
  for row in range(height):
    for col in range (width):
      new_img[-col][row] = pixels[row][col]
  return new_img

# 2. Rotate Right
def rotateRight(pixels):
  new_img = cmpt120imageProjHelper.getBlackImage(len(pixels),len(pixels[0]))
  height = len(pixels)
  width = len(pixels[0])
  for row in range(height):
    for col in range (width):
      new_img[col][-row] = pixels[row][col]
  return new_img

# 3. Double Size
def doubleSize(pixels):
  new_img = cmpt120imageProjHelper.getBlackImage(len(pixels[0]*2),len(pixels)*2)
  height = len(pixels)
  width = len(pixels[0])
  # Nested for loop
  for row in range (height):
    for col in range (width):
      # Doubles the size of the image
      new_img[row*2][col*2] = pixels[row][col]
      new_img[row*2][(col*2)+1] = pixels[row][col]
      new_img[(row*2)+1][col*2] = pixels[row][col]
      new_img[(row*2)+1][(col*2)+1] = pixels[row][col]
  return new_img

# 4. Half Size
def halfSize(pixels):
  height = len(pixels)
  width = len(pixels[0])
  new_img = cmpt120imageProjHelper.getBlackImage(width//2,height//2)
  for row in range (height//2):
    for col in range (width//2):
      pixel_1 = pixels[row*2][col*2]
      pixel_2 = pixels[row*2][(col*2)+1]
      pixel_3 = pixels[(row*2)+1][col*2]
      pixel_4 = pixels[(row*2)+1][(col*2)+1] 
      # Decreases the size of the image by half
      new_img[row][col][0] = (pixel_1[0]+pixel_2[0]+pixel_3[0]+pixel_4[0])/4
      new_img[row][col][1] = (pixel_1[1]+pixel_2[1]+pixel_3[1]+pixel_4[1])/4
      new_img[row][col][2] = (pixel_1[2]+pixel_2[2]+pixel_3[2]+pixel_4[2])/4
  return new_img      

# 5. Locate fish
# Generate two different functions:
# One for locating the fish and one for drawing the square
# Locating the fish
def locate_Fish(pixels):
  height = len(pixels)
  width = len(pixels[0])
  for row in range(height):
    for col in range (width):
      image = pixels[row][col]
      h = cmpt120imageProjHelper.rgb_to_hsv(image[0],image[1],image[2])[0]
      s = cmpt120imageProjHelper.rgb_to_hsv(image[0],image[1],image[2])[1]
      v = cmpt120imageProjHelper.rgb_to_hsv(image[0],image[1],image[2])[2]
      if (55 < h < 120) & (95 < v <= 100) & (50 < s < 60):             
        return col, row

# Function that is drawing the square
def draw_square(start_col, start_row,pixels):
    height = len(pixels)
    width = len(pixels[0])
    end_row = start_row + 100
    left_col = start_col - 70
    right_col = start_col + 50
    # Nested for loop
    for row in range(height):
      for col in range (width):
        image = pixels[row][col]
        if row == start_row and left_col <= col <= right_col:
          # Turn the pixels green
          image[0] = 0
          image[1] = 255
          image[2] = 0 
        if row == end_row and left_col <= col <= right_col:
          # Turn the pixels green
          image[0] = 0
          image[1] = 255
          image[2] = 0 
        if col == left_col and start_row <= row <= end_row:
          # Turn the pixels green
          image[0] = 0
          image[1] = 255
          image[2] = 0
        if col == right_col and start_row <= row  <= end_row:
          # Turn the pixels green
          image[0] = 0
          image[1] = 255
          image[2] = 0
    return pixels
      
    