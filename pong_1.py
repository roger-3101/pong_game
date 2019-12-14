'''

It's a little Pong game program, for a single player. 
I let you discover all the functionalities I put in it, enjoy ;)
Some are explained in when you run it, but here are others :
In the start menu :
	1 = change user
	2 = del the user in the users dict
	3 = change the ball color
	4 = change the bar color

'''

import pygame as pg
import random
import tkinter as tk
from usrs_hscs_dict import usrs_hsc

pg.init()

win = pg.display.set_mode((600,600))
pg.display.set_caption('Pong for a single player')

colors = {'white':(255,255,255),'red':(255,0,0),'green':(0,255,0),'blue':(0,0,255),'pink':(255,0,255),'yellow':(255,255,0),'cian':(0,255,255)}
score, space, right, left, x, y, color_ball, color_bar, lose = 0, 0, 0, 0, 250, 580 ,colors['white'],colors['white'], 0
r, xb, yb, cx ,cy = 20, 300, 300, 1, 1
font = pg.font.Font('freesansbold.ttf', 30)

def fct():
	vx, vy = 0, 0
	while abs(vx + vy) != 15:
		vx, vy = random.randint(-10,0), random.randint(-10,0)
	return [vx,vy]
vx,vy = fct()
def interface():
	from usrs_hscs_dict import usrs_hsc
	import tkinter as tk
	def user_name():
		def valider():
			global nam
			nam = txt.get()
			win.destroy()

		win = tk.Tk()
		val = tk.StringVar()
		val.set("")
		label = tk.Label(win,text='Type your name')
		label.pack()
		txt = tk.Entry(win,textvariable=val,width=20)
		txt.pack()
		botton = tk.Button(win,text="OK",command=valider)
		botton.pack()

		win.tk.mainloop()

		return nam

	name = user_name()

	if name in usrs_hsc != True:
		h_score = usrs_hsc[name]

	elif name == 'del':
		name_del = user_name()
		del(usrs_hsc[name_del])

	else:
		usrs_hsc[name] = 0

	file = open('usrs_hscs_dict.py','w')
	file.write('usrs_hsc = ' + str(usrs_hsc))
	file.close()

	pg.display.set_caption(name)

	return name
name = interface()
h_score = usrs_hsc[name]
def intitialisation():
	pg.time.delay(30)
	win.fill((0,0,0))

	pg.draw.circle(win, color_ball, (xb,yb),r)
	pg.draw.rect(win, color_bar, (x,y,100,10))

	txt_score, txt_rect = font.render(str(score), 1, colors['white']), (10,10)
	win.blit(txt_score, txt_rect)
	txt_h_score, txt_rect = font.render(str(h_score),1, colors['white']), (560,10)
	win.blit(txt_h_score, txt_rect)

	if space == 0:
		txt_start, txt_rect_start = font.render('PRESS SPACE TO START',1, colors['white']), (115,75)
		win.blit(txt_start, txt_rect_start)
def sure():
	def destroy():
		win.destroy()
	win = tk.Tk()
	label = tk.Label(win,text='Are you sure ?')
	label.pack() 
	botton = tk.Button(win,text="Yes",command=destroy)
	botton.pack()

	win.tk.mainloop()

	return 1
def colour():
	def valider():
		global c
		c = txt.get()
		win.destroy()

	win = tk.Tk()
	val = tk.StringVar()
	val.set("")
	label = tk.Label(win,text='Which color ?')
	label.pack()
	txt = tk.Entry(win,textvariable=val,width=20)
	txt.pack()
	botton = tk.Button(win,text="OK",command=valider)
	botton.pack()

	win.tk.mainloop()

	return c

while 1:
	if lose == 0:
		intitialisation()
		for event in pg.event.get():
			if event.type == pg.KEYDOWN:
				if space == 1:
					if event.key == pg.K_RIGHT and x + 100 < 600:
						right, left = 1, 0
					if event.key == pg.K_LEFT and x > 0:
						right, left = 0, 1

			if event.type == pg.KEYUP:
				if event.key == pg.K_RIGHT or event.key == pg.K_LEFT:
					right, left = 0, 0
				if event.key == pg.K_SPACE:
					space = 1
				if space == 0:
					if event.key == pg.K_1:
						name = interface()
						h_score = usrs_hsc[name]
						color_ball, color_bar = colors['white'],colors['white']
					if event.key == pg.K_2:
						if sure() == 1:
							del usrs_hsc[name]
							name = interface()
							h_score = usrs_hsc[name]
							color_ball, color_bar = colors['white'],colors['white']
					if event.key == pg.K_3:
						color_ball = colors[str(colour())]
					if event.key == pg.K_4:
						color_bar = colors[str(colour())]

			if event.type == pg.QUIT:
				pg.quit()
				quit()

		if right == 1:
			x += 15
		if left == 1:
			x -= 15

		if x < 0 or x + 100 > 600:
			right, left = 0, 0

		if space == 1:
			xb += vx * cx
			yb += vy * cy
		if xb + r >= 600:
			cx *= -1
		if xb - r <= 0:
 			cx *= -1
		if yb + r >= 605:
			xb, yb = 300,300
			lose = 1
		if yb - r <= 0:
			cy *= -1

		if yb + r >= y and xb + r >= x and xb - r <= x + 100:
			cy *= -1
			score += 1
			if score > h_score:
				h_score += 1

		if score != 0 and score % 3 == 0 and yb + r >= y and xb + r >= x and xb - r <= x + 100:
			vx -= 1
			vy -= 1
	else:
		txt_perdu, txt_rect = font.render(str('You lose ! Press return to continue...'),1, colors['white']), (30,75)
		win.blit(txt_perdu, txt_rect)

		if h_score > usrs_hsc[name]:
			usrs_hsc[name] = h_score
		file = open('usrs_hscs_dict.py','w')
		file.write('usrs_hsc = ' + str(usrs_hsc))
		file.close()

		for event in pg.event.get():
			if event.type == pg.KEYUP:
				if event.key == pg.K_RETURN:
					lose,score,space,cx,cy = 0,0,0,1,1
					vx,vy = fct()
					x,y = 250, 580
					intitialisation()
			if event.type == pg.QUIT:
				pg.quit()
				quit()

	pg.display.update()
#	THE END !!!