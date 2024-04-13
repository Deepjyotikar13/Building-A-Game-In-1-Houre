#done JAN28
import pygame
from pygame import mixer
from random import randint
from time import sleep 
pygame.init()
path="/storage/emulated/0/FighterJetGame/Assits/" #this is my file path you should give your file path
def return_image(img_name,img_width,img_height,rotate):
	"""This function will return the image and as image rectangle  also it will scale theimage according to its width and hright and also scale it """
	image=pygame.image.load(img_name)#orignal image
	
	scaled_img=pygame.transform.scale(image,(img_width,img_height))#scaled image 
	
	rotated_image=pygame.transform.rotate(scaled_img,rotate) #rotated image 
	return rotated_image
def play_sounds(sound_name):
	"""This will play the sound effect like explosion fire"""
	sound_path="/storage/emulated/0/FighterJetGame/Sound/"+sound_name
	sound=mixer.Sound(sound_path)
	sound.set_volume(0.08)
	sound.play()
	
	
width,height=750,1500 #This is the width and height of my mobile screen 
font=pygame.font.Font("freesansbold.ttf",60)#font for my text
game_over_font=pygame.font.Font("freesansbold.ttf",100)# this is for after game is over
player_width,player_height=350,250
screen=pygame.display.set_mode((width,height))
scaled_background=return_image(path+"background.jpg",width,height,0)#This is the background image
my_bullet=return_image(path+"Bullet.png",30,70,0)#this is the bullet taht will be fiered	
my_bullet_x,my_bullet_y=150,1100#this is the initial positionof my bullet 
my_bullet_rect=pygame.Rect(my_bullet_x,my_bullet_y,30,70)# this is my bullet rectangle 

my_bullet_fire=False # so intially if its false tge bullet will not fire
enemy_bullet=return_image(path+"Bullet.png",30,70,180)#This is the enemy bullet
enemy_bullet_fire=True #so it will be true so the enemy will cobstently fire
random_x_pos=randint(60,500) # i will randomly choose get the x position for my enemy jet and bullet also placed there
enemy_bullet_x,enemy_bullet_y=random_x_pos,-800 #this is the x,y position of enemys bullet
enemy_jet_x,enemy_jet_y=random_x_pos,-800 #this is position of enemy position
enemy_bullet_rect=pygame.Rect(enemy_bullet_x+110,enemy_bullet_y+100,30,70)#so this is the bullet rectangle of enemys bullet

game_not_over=True
score_point=0 #This is the score of my player that how many enamy jets he had shot 
background_y=0 #the background staets from 0
my_jet_x,my_jet_y=40,1100#this is the initial position of my jet 
swipe_start=None 
explo_img=return_image(path+"ex_after_hit.png",650,650,0)#this is the explosion afyer my jet hit enemy jet 
my_jet=return_image(path+"fighter_jet.png",player_width,player_height,-90)#this is the jet that will fight against the enemy so lets call it "hero jet"
my_jet_rect=pygame.Rect(my_jet_x+60,my_jet_y+130,120,200)
enemy_jet=return_image(path+"enemy_jet.png",player_width,player_height,-90)
enemy_jet_rect=pygame.Rect(enemy_jet_x+60,enemy_jet_y+70,120,200)#this is the rectangle for the enemy 
my_bullet_sound=0# if its taht means play sound
enemy_bullet_sound=0
while game_not_over:
	for event in pygame.event.get():
		#i am looping through every events to find any event occared
		if event.type==pygame.QUIT:
			game_not_over=False
		elif event.type==pygame.MOUSEBUTTONDOWN:
			swipe_start = pygame.mouse.get_pos()
		elif event.type==pygame.MOUSEBUTTONUP:
			if swipe_start:
				swipe_end=pygame.mouse.get_pos()
				dx,dy=swipe_end[0]-swipe_start[0],swipe_end[1]-swipe_start[1]
				if dx>0 and abs(dx)>abs(dy):
					my_jet_x+=70
					my_jet_rect.x+=70
					if my_bullet_fire==False:
						#ensuring that the bullet doest move after i shoot it and then move the jet cause as you can see that when i am swipe left or right the bullet also chage its x position so if i fire and then move the plane the bullet will also move and if my_bullet_fire==False will only happen when thebullet is not fired
						my_bullet_x=my_jet_x+110
						my_bullet_rect.x=my_jet_x+110#bullet rectangle
				elif dx<0 and abs(dx)>abs(dy):
					my_jet_x-=70
					my_jet_rect.x-=70
					if my_bullet_fire==False:
						my_bullet_x=my_jet_x+110
						my_bullet_rect.x=my_jet_x+110 #this is the bullet rectangle
				elif abs(dx)-abs(dy)==0:
					my_bullet_fire=True # when i will tap it be true and then the bullet can move

	screen.fill((255,255,255))
	screen.blit(scaled_background,(0,background_y))#displaying the background image 
	screen.blit(scaled_background,(0,background_y-height+10))#at the end of the frist background image it will have the second background image its like a loop
	if my_bullet_fire:
		if my_bullet_sound==0:
			play_sounds("Bullet_shot.wav")
			my_bullet_sound+=1
		my_bullet_y-=30
		my_bullet_rect.y-=30
	if my_bullet_y<0:
		my_bullet_fire=False
		my_bullet_sound=0#reseting it to 0 so that i can fire it again 
		my_bullet_x=my_jet_x+110
		my_bullet_y=1100
		my_bullet_rect.x=my_jet_x+110# so repositionimg the bullet to the position of the jet
		my_bullet_rect.y=1100#this is the bullet rectangle and its repositioning it 
	enemy_jet_y+=10
	enemy_jet_rect.y=enemy_jet_y
	if enemy_jet_y>1500:
		enemy_jet_y=-800
	#pygame.draw.rect(screen,(0,255,0),my_bullet_rect)
	screen.blit(my_bullet,(my_bullet_x,my_bullet_y))
	#pygame.draw.rect(screen,(0,0,255),my_jet_rect)
	screen.blit(my_jet,(my_jet_x,my_jet_y))
	if enemy_bullet_fire:
		#so enemy_bullet_fire is true the bullet will be fired 
		if enemy_bullet_sound==0:
			play_sounds("Bullet_shot.wav")
			enemy_bullet_sound+=1
		enemy_bullet_y+=20
		enemy_bullet_rect.y+=20
	if enemy_bullet_y>1500:
		#when the bullet is out of screen then i will reposition it with the jet 
		enemy_bullet_sound=0
		enemy_bullet_y=enemy_jet_y 
		enemy_bullet_rect.y=enemy_jet_y+100#so here enemy bullet gets the position of the enemy jet
	#pygame.draw.rect(screen,(0,0,255),enemy_bullet_rect)#enemy bullet rect
	screen.blit(enemy_bullet,(enemy_bullet_x+110,enemy_bullet_y+100))
	#pygame.draw.rect(screen,(245,14,89),enemy_jet_rect)#enemy_jet_rect
	screen.blit(enemy_jet,(enemy_jet_x,enemy_jet_y))
	if enemy_jet_rect.colliderect(my_bullet_rect):
		#so this is when my bullet hits then enamy jet rectangle 
		my_bullet_sound=0#resting tl 0 after it hits the enemy jet so that i can fire it again
		screen.blit(explo_img,(enemy_jet_x-170,enemy_jet_y-120))
		play_sounds("explosion.wav")#this will play the explosion sound after its hit by the bullet or hit by the other jet itself
		rand_x_pos=randint(60,500)
		enemy_jet_x=rand_x_pos#this will randomly place it in a position
		enemy_jet_y=-800#this will playe far from screen
		enemy_jet_rect.x=rand_x_pos+60#positioning the jet rectangle at x
		enemy_jet_rect.y=-800 #positioning the jet recttange at y
		enemy_bullet_x=rand_x_pos#placing enemy bullet at random position 
		enemy_bullet_y=-800#placing bullet inage at the end
		enemy_bullet_rect.x=rand_x_pos+110#placing enemy bullet rectangle at c
		enemy_bullet_rect.y=enemy_bullet_y+100#placing enemy bullet ranctangle at y
		my_bullet_fire=False
		my_bullet_x=my_jet_x+110
		my_bullet_y=1100
		my_bullet_rect.x=my_jet_x+110
		my_bullet_rect.y=my_bullet_y
		score_point+=1
	score=font.render(" Score "+str(score_point),True,(255,255,255))
	screen.blit(score,(250,10))
	if enemy_bullet_rect.colliderect(my_jet_rect):
		#game_over_font.size=30
		game_over=game_over_font.render("Game Over",True,(0,0,0))
		screen.blit(game_over,(100,1000))
		screen.blit(explo_img,(my_jet_x-170,my_jet_y-120))
		play_sounds("explosion.wav")#this will play the explosion sound after its hit by the bullet or hit by the other jet itself
		sleep(0.5)
		game_not_over=False
	if enemy_jet_rect.colliderect(my_jet_rect):
		game_over=game_over_font.render("Game Over",True,(0,0,0))
		screen.blit(game_over,(100,1000))
		screen.blit(explo_img,(my_jet_x-170,my_jet_y-120))
		play_sounds("explosion.wav")#this will play the explosion sound after its hit by the bullet or hit by the other jet itself
		sleep(0.5)
		game_not_over=False
	if background_y>1500:
		#if the frist background image has crossed the the screen then it should start from top
		background_y=0
	pygame.display.flip()#in evry loop it will display the cahnges
	background_y+=40
pygame.quit()