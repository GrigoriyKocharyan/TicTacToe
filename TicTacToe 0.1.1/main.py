from pygame import *
from texts import *
import time
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
win = display.set_mode((500,500))
display.set_caption('TicTacToe')

gmap = [0, 0, 0,
		0, 0, 0,
		0, 0, 0]
char = 'КРЕСТИК'

playAgain = image.load('pagain.png')

playAgain = transform.scale(playAgain, (25,25))
''' { ПЕРЕМЕННЫЕ \/ '''
game = 0
VERSION = '0.1'

scene = 0
clicked = 0

''' ------------- } '''

text7 = font3.render('Версия: '+ str(VERSION), 1, (60,40,240))

while True:
	win.fill((10, 0, 40))
	m = mouse.get_pos()
	for i in event.get():
		if i.type == QUIT:
			quit()
			exit()
		if i.type == MOUSEBUTTONDOWN:
			if BUTTON_LEFT:
				clicked = 1
		if i.type == MOUSEBUTTONUP:
			if BUTTON_LEFT:
				clicked = 0

	if scene == 0:

		draw.rect(win, (20, 0, 80), (0, 0, 500, 80))


		draw.rect(win, (20, 0, 80), (50, 200, 200, 40), 0, 15)
		if m[0] >= 50 and m[0] <= 250 and m[1] >= 200 and m[1] <= 240:
			draw.rect(win, (40, 0, 160), (50,200,200,40), 3, 15)
			if clicked:
				scene = 1
				clicked = 0


		win.blit(text1, (10,10))
		win.blit(text2, (100, 202))
		win.blit(text7, (400, 480))

	if scene == 1:

		draw.rect(win, (20, 0, 80), (0, 0, 500, 80))

		draw.rect(win, (20, 0, 80), (50, 200, 250, 40), 0, 15)
		if m[0] >= 50 and m[0] <= 300 and m[1] >= 200 and m[1] <= 240:
			draw.rect(win, (40, 0, 160), (50, 200, 250, 40), 3, 15)
			if clicked:
				scene = 2

		draw.rect(win, (20, 0, 80), (450, 15, 40, 40), 0, 15)
		if m[0] >= 450 and m[0] <= 490 and m[1] >= 15 and m[1] <= 55:
			draw.rect(win, (40, 0, 160), (450, 15, 40, 40), 3, 15)
			if clicked:
				scene = 0

		draw.rect(win, (20, 0, 80), (50, 250, 250, 40), 0, 15)
		if m[0] >= 50 and m[0] <= 300 and m[1] >= 250 and m[1] <= 290:
			draw.rect(win, (40, 0, 160), (50, 250, 250, 40), 3, 15)
			if clicked:
				scene = 3
				clicked = 0

		win.blit(text3, (70, 202))
		win.blit(text5, (60+50, 202+50))
		win.blit(text6, (458, 17))
		win.blit(text4, (10, 10))

	if scene == 3:

		game = 1

		if game == 1:
			if char == 'КРЕСТИК':
				draw.line(win, (255,0,0), (230,10), (260,40), 4)
				draw.line(win, (255, 0, 0),(260, 10), (230, 40), 4)
			if char == "НОЛИК":
				draw.circle(win, (0,0,255), (245, 25), 15, 4)


			if m[0] >= 100 and m[0] <= 200 and m[1] >= 100 and m[1] <= 200:
				if clicked:
					clicked = 0
					if char == 'КРЕСТИК':
						if gmap[0] != 1 and gmap[0] != -1:
							gmap[0] = 1
							char = 'НОЛИК'
					elif char == 'НОЛИК':
						if gmap[0] != -1 and gmap[0] != 1:
							gmap[0] = -1
							char = 'КРЕСТИК'
			if gmap[0] == 1:
				draw.line(win, (255, 0, 0), (100, 100), (200, 200), 4)
				draw.line(win, (255, 0, 0), (200, 100), (100, 200), 4)
			if gmap[0] == -1:
				draw.circle(win, (0,0,255), (150,150), 50, 4)

			if m[0] >= 200 and m[0] <= 300 and m[1] >= 100 and m[1] <= 200:
				if clicked:
					clicked = 0
					if char == 'КРЕСТИК':
						if gmap[1] != 1 and gmap[1] != -1:
							gmap[1] = 1
							char = 'НОЛИК'
					elif char == 'НОЛИК':
						if gmap[1] != -1 and gmap[1] != 1:
							gmap[1] = -1
							char = 'КРЕСТИК'
			if gmap[1] == 1:
				draw.line(win, (255, 0, 0), (200, 100), (300, 200), 4)
				draw.line(win, (255, 0, 0), (300, 100), (200, 200), 4)
			if gmap[1] == -1:
				draw.circle(win, (0,0,255), (250,150), 50, 4)



			if m[0] >= 300 and m[0] <= 400 and m[1] >= 100 and m[1] <= 200:
				if clicked:
					clicked = 0
					if char == 'КРЕСТИК':
						if gmap[2] != 1 and gmap[2] != -1:
							gmap[2] = 1
							char = 'НОЛИК'
					elif char == 'НОЛИК':
						if gmap[2] != -1 and gmap[2] != 1:
							gmap[2] = -1
							char = 'КРЕСТИК'
			if gmap[2] == 1:
				draw.line(win, (255, 0, 0), (300, 100), (400, 200), 4)
				draw.line(win, (255, 0, 0), (400, 100), (300, 200), 4)
			if gmap[2] == -1:
				draw.circle(win, (0,0,255), (350,150), 50, 4)



			if m[0] >= 100 and m[0] <= 200 and m[1] >= 200 and m[1] <= 300:
				if clicked:
					clicked = 0
					if char == 'КРЕСТИК':
						if gmap[3] != 1 and gmap[3] != -1:
							gmap[3] = 1
							char = 'НОЛИК'
					elif char == 'НОЛИК':
						if gmap[3] != -1 and gmap[3] != 1:
							gmap[3] = -1
							char = 'КРЕСТИК'
			if gmap[3] == 1:
				draw.line(win, (255, 0, 0), (100, 200), (200, 300), 4)
				draw.line(win, (255, 0, 0), (200, 200), (100, 300), 4)
			if gmap[3] == -1:
				draw.circle(win, (0,0,255), (150,250), 50, 4)



			if m[0] >= 200 and m[0] <= 300 and m[1] >= 200 and m[1] <= 300:
				if clicked:
					clicked = 0
					if char == 'КРЕСТИК':
						if gmap[4] != 1 and gmap[4] != -1:
							gmap[4] = 1
							char = 'НОЛИК'
					elif char == 'НОЛИК':
						if gmap[4] != -1 and gmap[4] != 1:
							gmap[4] = -1
							char = 'КРЕСТИК'
			if gmap[4] == 1:
				draw.line(win, (255, 0, 0), (200, 200), (300, 300), 4)
				draw.line(win, (255, 0, 0), (300, 200), (200, 300), 4)
			if gmap[4] == -1:
				draw.circle(win, (0,0,255), (250,250), 50, 4)




			if m[0] >= 300 and m[0] <= 400 and m[1] >= 200 and m[1] <= 300:
				if clicked:
					clicked = 0
					if char == 'КРЕСТИК':
						if gmap[5] != 1 and gmap[5] != -1:
							gmap[5] = 1
							char = 'НОЛИК'
					elif char == 'НОЛИК':
						if gmap[5] != -1 and gmap[5] != 1:
							gmap[5] = -1
							char = 'КРЕСТИК'
			if gmap[5] == 1:
				draw.line(win, (255, 0, 0), (300, 200), (400, 300), 4)
				draw.line(win, (255, 0, 0), (400, 200), (300, 300), 4)
			if gmap[5] == -1:
				draw.circle(win, (0,0,255), (350,250), 50, 4)










			if m[0] >= 100 and m[0] <= 200 and m[1] >= 300 and m[1] <= 400:
				if clicked:
					clicked = 0
					if char == 'КРЕСТИК':
						if gmap[6] != 1 and gmap[6] != -1:
							gmap[6] = 1
							char = 'НОЛИК'
					elif char == 'НОЛИК':
						if gmap[6] != -1 and gmap[6] != 1:
							gmap[6] = -1
							char = 'КРЕСТИК'
			if gmap[6] == 1:
				draw.line(win, (255, 0, 0), (100, 300), (200, 400), 4)
				draw.line(win, (255, 0, 0), (200, 300), (100, 400), 4)
			if gmap[6] == -1:
				draw.circle(win, (0,0,255), (150,350), 50, 4)



			if m[0] >= 200 and m[0] <= 300 and m[1] >= 300 and m[1] <= 400:
				if clicked:
					clicked = 0
					if char == 'КРЕСТИК':
						if gmap[7] != 1 and gmap[7] != -1:
							gmap[7] = 1
							char = 'НОЛИК'
					elif char == 'НОЛИК':
						if gmap[7] != -1 and gmap[7] != 1:
							gmap[7] = -1
							char = 'КРЕСТИК'
			if gmap[7] == 1:
				draw.line(win, (255, 0, 0), (200, 300), (300, 400), 4)
				draw.line(win, (255, 0, 0), (300, 300), (200, 400), 4)
			if gmap[7] == -1:
				draw.circle(win, (0,0,255), (250,350), 50, 4)



			if m[0] >= 300 and m[0] <= 400 and m[1] >= 300 and m[1] <= 400:
				if clicked:
					clicked = 0
					if char == 'КРЕСТИК':
						if gmap[8] != 1 and gmap[8] != -1:
							gmap[8] = 1
							char = 'НОЛИК'
					elif char == 'НОЛИК':
						if gmap[8] != -1 and gmap[8] != 1:
							gmap[8] = -1
							char = 'КРЕСТИК'
			if gmap[8] == 1:
				draw.line(win, (255, 0, 0), (300, 300), (400, 400), 4)
				draw.line(win, (255, 0, 0), (400, 300), (300, 400), 4)
			if gmap[8] == -1:
				draw.circle(win, (0,0,255), (350,350), 50, 4)

			draw.rect(win, (20, 0, 80), (450, 15, 40, 40), 0, 15)
			if m[0] >= 450 and m[0] <= 490 and m[1] >= 15 and m[1] <= 55:
				draw.rect(win, (40, 0, 160), (450, 15, 40, 40), 3, 15)
				if clicked:
					scene = 1
			draw.rect(win, (20, 0, 80), (400, 15, 40, 40), 0, 15)
			if m[0] >= 400 and m[0] <= 450 and m[1] >= 15 and m[1] <= 55:
				draw.rect(win, (40, 0, 160), (400, 15, 40, 40), 3, 15)
				if clicked:
					gmap = [0,0,0,0,0,0,0,0,0]
					char = 'КРЕСТИК'

		draw.rect(win, (255, 255, 255), (100, 100, 300, 300), 1)
		draw.rect(win, (255, 255, 255), (200, 100, 100, 300), 1)
		draw.rect(win, (255, 255, 255), (100, 200, 300, 100), 1)

		win.blit(text8, (10, 10))
		win.blit(text6, (458, 17))
		win.blit(playAgain, (406, 21))

		if gmap[0] == 1 and gmap[1] == 1 and gmap[2] == 1:
			draw.line(win, (255, 100, 100), (150, 150), (350, 150), 10)
			display.flip()
			time.sleep(1)
			char = 'КРЕСТИК'
			gmap = [0,0,0,0,0,0,0,0,0]
		if gmap[0] == -1 and gmap[1] == -1 and gmap[2] == -1:
			draw.line(win, (255, 100, 100), (150, 150), (350, 150), 10)
			display.flip()
			time.sleep(1)
			char = 'КРЕСТИК'
			gmap = [0,0,0,0,0,0,0,0,0]



		if gmap[3] == 1 and gmap[4] == 1 and gmap[5] == 1:
			draw.line(win, (255, 100, 100), (150, 250), (350, 250), 10)
			display.flip()
			time.sleep(1)
			char = 'КРЕСТИК'
			gmap = [0,0,0,0,0,0,0,0,0]
		if gmap[3] == -1 and gmap[4] == -1 and gmap[5] == -1:
			draw.line(win, (255, 100, 100), (150, 250), (350, 250), 10)
			display.flip()
			time.sleep(1)
			char = 'КРЕСТИК'
			gmap = [0,0,0,0,0,0,0,0,0]


		if gmap[6] == 1 and gmap[7] == 1 and gmap[8] == 1:
			draw.line(win, (255, 100, 100), (150, 350), (350,350), 10)
			display.flip()
			time.sleep(1)
			char = 'КРЕСТИК'
			gmap = [0,0,0,0,0,0,0,0,0]
		if gmap[6] == -1 and gmap[7] == -1 and gmap[8] == -1:
			draw.line(win, (255, 100, 100), (150, 350), (350, 350), 10)
			display.flip()
			time.sleep(1)
			char = 'КРЕСТИК'
			gmap = [0,0,0,0,0,0,0,0,0]




		if gmap[0] == 1 and gmap[3] == 1 and gmap[6] == 1:
			draw.line(win, (255, 100, 100), (150, 150), (150, 350), 10)
			display.flip()
			time.sleep(1)
			char = 'КРЕСТИК'
			gmap = [0,0,0,0,0,0,0,0,0]
		if gmap[0] == -1 and gmap[3] == -1 and gmap[6] == -1:
			draw.line(win, (255, 100, 100), (150, 150), (150, 350), 10)
			display.flip()
			time.sleep(1)
			char = 'КРЕСТИК'
			gmap = [0,0,0,0,0,0,0,0,0]


		if gmap[1] == 1 and gmap[4] == 1 and gmap[7] == 1:
			draw.line(win, (255, 100, 100), (250, 150), (250, 350), 10)
			display.flip()
			time.sleep(1)
			char = 'КРЕСТИК'
			gmap = [0,0,0,0,0,0,0,0,0]
		if gmap[1] == -1 and gmap[4] == -1 and gmap[7] == -1:
			draw.line(win, (255, 100, 100), (250, 150), (250, 350), 10)
			display.flip()
			time.sleep(1)
			char = 'КРЕСТИК'
			gmap = [0,0,0,0,0,0,0,0,0]


		if gmap[2] == 1 and gmap[5] == 1 and gmap[8] == 1:
			draw.line(win, (255, 100, 100), (350, 150), (350, 350), 10)
			display.flip()
			time.sleep(1)
			char = 'КРЕСТИК'
			gmap = [0,0,0,0,0,0,0,0,0]
		if gmap[2] == -1 and gmap[5] == -1 and gmap[8] == -1:
			draw.line(win, (255, 100, 100), (350, 150), (350, 350), 10)
			display.flip()
			time.sleep(1)
			char = 'КРЕСТИК'
			gmap = [0,0,0,0,0,0,0,0,0]


		if gmap[0] == 1 and gmap[4] == 1 and gmap[8] == 1:
			draw.line(win, (255, 100, 100), (150, 150), (350, 350), 10)
			display.flip()
			time.sleep(1)
			char = 'КРЕСТИК'
			gmap = [0,0,0,0,0,0,0,0,0]
		if gmap[0] == -1 and gmap[4] == -1 and gmap[8] == -1:
			draw.line(win, (255, 100, 100), (150, 150), (350, 350), 10)
			display.flip()
			time.sleep(1)
			char = 'КРЕСТИК'
			gmap = [0,0,0,0,0,0,0,0,0]


		if gmap[2] == 1 and gmap[4] == 1 and gmap[6] == 1:
			draw.line(win, (255, 100, 100), (350, 150), (150, 350), 10)
			display.flip()
			time.sleep(1)
			char = 'КРЕСТИК'
			gmap = [0,0,0,0,0,0,0,0,0]
		if gmap[2] == -1 and gmap[4] == -1 and gmap[6] == -1:
			draw.line(win, (255, 100, 100), (350, 150), (150, 350), 10)
			display.flip()
			time.sleep(1)
			char = 'КРЕСТИК'
			gmap = [0,0,0,0,0,0,0,0,0]


	display.flip()

