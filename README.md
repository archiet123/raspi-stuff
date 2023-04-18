# raspi-stuff
punchcard reader raspi

## how to run
download repo and move to directory in cmd/ vscode

run "python brightestPoint.py" into terminal

### changing target image

inside brightestPoint.py line 23 = img = cv2.imread(f'assets/card.jpg')#reading init pic
assetsm/card is the target image, change "card" to one of the following:
  * card
  * first_image
