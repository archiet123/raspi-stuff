def getCharacter(final):
	if final > 20 and final < 50:
		selector = 0
		return selector
	elif final > 55 and final < 90:
		selector = 1
		return selector
	elif final > 95 and final < 120:
		selector = 2		
		return selector
	elif final > 125 and final < 151:
		selector = 3		
		return selector
	elif final > 151 and final < 180:
		selector = 4
		return selector
	elif final > 190 and final < 210:
		selector = 5
		return selector
	elif final > 230 and final < 250:
		selector = 6
		return selector
	elif final > 265 and final < 280:
		selector = 7
		return selector
	elif final > 295 and final < 320:
		selector = 8
		return selector
	elif final > 330 and final < 350:
		selector = 9
		return selector
	

final = 140
selector = getCharacter(final)
print(selector)