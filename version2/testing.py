import numpy as np
import cv2
import matplotlib.pyplot as plt
import cv2
import os
import argparse


print(f"\nimage to select from:")
print("abc123, abcCard, all80, card, first_image, realTest, spacedPunches\n")
#creating a parser
parser = argparse.ArgumentParser()
#adding the argument, "--name" is how this value is refered to if there are multiple arguments parsed.
parser.add_argument('--imageName', type=str, required=True)

#assigning argument to variable
value = parser.parse_args()

print(f"image selected: {value.imageName}")

read = cv2.imread(f'ImagesToRead/{value.imageName}.jpg')
cv2.imshow('window', read)
cv2.waitKey()

