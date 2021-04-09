from random import randint, getrandbits
import sys

class Hurensohn:
	def __init__(self, name: str, hurensohn_level: int, kamel: bool):
		self.name = name
		self.hs_lvl = hurensohn_level
		self.kamel = kamel
	
	def to_lesbar(self) -> str:
		return "Hallo, ich bin " + self.name + ", " + ("ein" if self.kamel else "kein") + " Kamel, mit einem hs level von " + str(self.hs_lvl) + "!"
		

hses = [Hurensohn("Klaus", 5, True), Hurensohn("Peter", 15, False), Hurensohn("Lennart", 0, True), Hurensohn("Nolram", 5000, False)]


for iglu in range (18000000):
	hses.append(Hurensohn(f"Mennsch Nr. {iglu}", randint(0, 5000), bool(getrandbits(1))))

for hs in hses:
	print(hs.to_lesbar(), end="Der nächste Schwuchtel ist: ")
sys.exit(42)
