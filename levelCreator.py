import pygame
from note import Don, Kat, DDon, DKat, Roll
from level import Level
import creatorUI
import time
import pygame

level = Level('Yoru ni Kakeru', [], 281, 'easy')
level.addNote(Don(3, 3.2))
