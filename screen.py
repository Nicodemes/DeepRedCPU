from common import *
from cpu_ref import *
class Screen(LinkedComponent):
	def __init__(self,**f):
		self.frames=f['frames']
		LinkedComponent.__init__(self,self.frames[0])
		self.iCursor=f["iCursor"]
		self.cursor=f["cursor"]
		self.tmpcursor=f['tmpcursor']
		self.iChar=f['iChar']
		self.charpivot=f['charpivot']
		self.snapStart=f['snapstart']

		self.powerOn=f['powerOn']
		self.powerOff=f['powerOff']
		self.openArea=f['openArea']
		self.hiddenArea=f['hiddenArea']
		self.anchor=f['anchor']
	def clearAction(self):
		return "/fill {} {} {}".format(self.tmpcursor.dest,self.iChar.getEndOfOrigin(),Pear.resetBlock)
	def char(self,i):
		a=Point(self.snapStart[0][0],self.snapStart[0][1]-i+1,self.snapStart[0][2])
		b=Point(self.snapStart[1][0],self.snapStart[1][1]-i+1,self.snapStart[1][2])
		return self.cursor.execute("/clone {} {} ~ ~ ~".format(a,b))
	def action(self,i):
		CHARSIZE=(6,8)
		if i <=4:
			return self.cursor.moveX(CHARSIZE[0]*(2**i))
		else:
			return self.cursor.moveZ(CHARSIZE[1]*(2**(i-5)))
	
	def charselect(self,i):
		if i<=3:
			return self.charpivot.moveZ(2**i)
		else:
			return self.charpivot.moveX(-(2**(i-4)))
	def __getitem__(self,i):
		return self.frames[i]
	def printc(self):
		return self.charpivot.signal()
	def spawnFrame(self,x,y,z,char="0"):
		fx=-77
		fy=11
		fz=-42
		fx+=x
		fy-=y
		fz+=z
		fx=str(fx)
		fy=str(fy)
		fz=str(fz)
		return "/summon ItemFrame "+fx+" "+fy+" "+fz+" {TileX:"+fx+",TileY:"+fy+",TileZ:"+fz+",Facing:0,Item:{id:358,Damage:"+str(ord(char))+",Count:1}}"
screen=Screen(
	snapstart=((-199,104,-162),(-194,104,-155)),
	frames=[
		Pear("-202 12 -189"),
		Pear("-201 12 -189"),
		Pear("-198 12 -189")
	],
	iCursor=Pear("-202 14 -192",8),
	tmpcursor=Pear("-202 11 -192",8),
	iChar=Pear("-202 11 -191",8),
	charpivot=pRefrence("SCREEN_CHARPIVOT",Point("-194 12 -180")),
	cursor=pRefrence("CURSOR",Point("-192 11 -192")),
	
	powerOn=Pear("-80 2 -34"),
	powerOff=Pear("-82 9 -42"),
	openArea="-227 23 -189 -208 17 -167",
	hiddenArea="-227 16 -189 -208 11 -167",
	anchor=Point("-80 10 -47")
	)
