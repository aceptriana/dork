import os
from colorama import Fore,init

if os.name == "nt":
	os.system("cls")
else:
	os.system("clear")

init(convert=True)

class settings:
	y = Fore.YELLOW
	r = Fore.RED
	b = Fore.BLUE


print("""{}
  ____  _ _       _     _     _     _   _             _              [{}+{}] SiteList Hunter v1
 / ___|(_) |_ ___| |   (_)___| |_  | | | |_   _ _ __ | |_ ___ _ __   [{}+{}] Dork Maker and Scanner
 \___ \| | __/ _ \ |   | / __| __| | |_| | | | | '_ \| __/ _ \ '__|  [{}+{}] Get many sites in minutes !
  ___) | | ||  __/ |___| \__ \ |_  |  _  | |_| | | | | ||  __/ |     [{}+{}] Coded by NinjaCR3
 |____/|_|\__\___|_____|_|___/\__| |_| |_|\__,_|_| |_|\__\___|_|     [{}+{}] Contact : facebook.com/ninjacr3

 Duplicate Remover
""".format(settings.y,settings.r,settings.y,settings.r,settings.y,settings.r,settings.y,settings.r,settings.y,settings.r,settings.y))

lines_seen = set()
outfile = open('sites.txt', "a")
infile = open('sitelist.txt', "r")
for line in infile:
	if line not in lines_seen:
		outfile.write(line)
		lines_seen.add(line)
outfile.close()
infile.close()
if os.name == "nt":
	os.system("del sitelist.txt")
else:
	os.system("rm -rf sitelist.txt")
print("[{}+{}] Duplicate sites removed successfully!".format(settings.r,settings.y))
print("\n[{}+{}] Sites saved as {}sites.txt{}!".format(settings.r,settings.y,settings.b,settings.y))