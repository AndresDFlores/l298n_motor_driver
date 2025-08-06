from dc_motor import *

import pygame

import time
import sys


class MotorDriver():

	def __init__(self):
		
		
		# Initialize pygame
		self.pg = pygame
		self.pg.init()


		# Set up display (required for handling events in pygame)
		screen = self.pg.display.set_mode((50, 50))
		self.pg.display.set_caption("Key Press Reader")
		

		# run status to define if a session is active
		self.running = True
		
		
		# define pins, initialize motors
		self.motorA = DCMotor(
			in1=23,
			in2=24,
			en=25
		)

		self.motorB = DCMotor(
			in1=17,
			in2=27,
			en=22
		)

		self.motor_effort=100
		
		
	def drive(self):
		
		for event in self.pg.event.get():

			if event.type == self.pg.KEYDOWN:  # Check for key press
				pressed_key = self.pg.key.name(event.key)  # Output the key pressed

				if pressed_key == 'up':
					print('FORWARD')

					self.motorA.set_motor_effort(effort=self.motor_effort)
					self.motorA.set_motor_direction(direction=True)
					self.motorA.drive_motor()

					self.motorB.set_motor_effort(effort=self.motor_effort)
					self.motorB.set_motor_direction(direction=True)
					self.motorB.drive_motor()
					
					
				elif pressed_key == 'down':
					print('REVERSE')

					self.motorA.set_motor_effort(effort=self.motor_effort)
					self.motorA.set_motor_direction(direction=False)
					self.motorA.drive_motor()

					self.motorB.set_motor_effort(effort=self.motor_effort)
					self.motorB.set_motor_direction(direction=False)
					self.motorB.drive_motor()
					
					
				elif pressed_key == 'left':
					print('LEFT')

					self.motorA.set_motor_effort(effort=self.motor_effort)
					self.motorA.set_motor_direction(direction=False)
					self.motorA.drive_motor()

					self.motorB.set_motor_effort(effort=self.motor_effort)
					self.motorB.set_motor_direction(direction=True)
					self.motorB.drive_motor()
					
					
				elif pressed_key == 'right':
					print('RIGHT')

					self.motorA.set_motor_effort(effort=self.motor_effort)
					self.motorA.set_motor_direction(direction=True)
					self.motorA.drive_motor()

					self.motorB.set_motor_effort(effort=self.motor_effort)
					self.motorB.set_motor_direction(direction=False)
					self.motorB.drive_motor()
					
					
				elif pressed_key == 'space' or pressed_key == 'escape':
					print('SESSION TERMINATED')
					self.running = False

					self.motorA.set_motor_effort(effort=0)
					self.motorA.set_motor_direction(direction=True)
					self.motorA.stop_motor()

					self.motorB.set_motor_effort(effort=0)
					self.motorB.set_motor_direction(direction=True)
					self.motorB.stop_motor()
					
				else:
					print(f'{pressed_key}: NO DEFINED ACTION')
					
					
			elif event.type == self.pg.KEYUP:
				print('NO PRESSED KEY')

				self.motorA.set_motor_effort(effort=0)
				self.motorA.set_motor_direction(direction=True)
				self.motorA.stop_motor()

				self.motorB.set_motor_effort(effort=0)
				self.motorB.set_motor_direction(direction=True)
				self.motorB.stop_motor()
                
				
			if event.type == self.pg.QUIT:  # Exit condition
				print('SESSION TERMINATED')           
				self.running = False

				self.motorA.set_motor_effort(effort=0)
				self.motorA.set_motor_direction(direction=True)
				self.motorA.stop_motor()

				self.motorB.set_motor_effort(effort=0)
				self.motorB.set_motor_direction(direction=True)
				self.motorB.stop_motor()

		
			
	def main(self):
		while self.running:
			self.drive()

	
