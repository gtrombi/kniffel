import random as rdn
import pandas as pd

class partita:
def __init__(self, players):
self.players = players
self.rows = ['ones', 'twos', 'threes', 'fours', 'fives', 'sixes', 'upperBonus', 'tris', 'poker', 'full', 'chance', 'short_streight', 'long_streight', 'kniffel','punti']
self.df = pd.DataFrame([[ 0 for p in self.players] for i in self.rows], columns=[p.getNome() for p in self.players], index = self.rows)
self.shadow_df = self.df
for p in self.players:
p.entraInPartita(self)

def checkNumber(self,player,number):
return player.getValoreTiro().count(number) >= 3

def checkTrisPoker(self,player,number):
for n in range(1,7):
if player.getValoreTiro().count(n) >= number:
return True
return False


class dado:
def __init__(self):
self.value = 0
self.tienilo = False

def tira(self):
if not self.tienilo:
self.tienilo = False
self.value = rdn.randint(1,6)

def tieni(self):
self.tienilo = True

def getValore(self):
return self.value

class player:
def __init__(self, nome):
self.punti = 0
self.nome = nome
self.dadi = []
for i in range(0,5):
self.dadi.append(dado())
self.tiro = 1
self.turno = 0
self.partita = None

def entraInPartita(self,partita):
self.partita

def getNome(self):
return self.nome

def nuovoTurno(self):
self.turno += 1
self.tiraDadi()

def tiraDadi(self):
for d in self.dadi:
d.tira()
self.scegli()

def getValoreTiro(self):
return [v.getValore() for v in self.dadi]

def opziona(self):
ehi = 12

def scegli(self):
self.opziona()
