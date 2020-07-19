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

def clean():
	lines_seen = set()
	outfile = open('dorks.txt', "a")
	infile = open('dorkstest.txt', "r")
	for line in infile:
		if line not in lines_seen:
			outfile.write(line)
			lines_seen.add(line)
	outfile.close()
	infile.close()
	if os.name == "nt":
		os.system("del dorkstest.txt")
	else:
		os.system("rm -rf dorkstest.txt")
	print("[{}+{}] Duplicate dorks removed successfully!".format(settings.r,settings.y))
	print("\n[{}+{}] Dorks saved as {}dorks.txt{}!".format(settings.r,settings.y,settings.b,settings.y))


print("""{}
  ____  _ _       _     _     _     _   _             _              [{}+{}] SiteList Hunter v1
 / ___|(_) |_ ___| |   (_)___| |_  | | | |_   _ _ __ | |_ ___ _ __   [{}+{}] Dork Maker and Scanner
 \___ \| | __/ _ \ |   | / __| __| | |_| | | | | '_ \| __/ _ \ '__|  [{}+{}] Get many sites in minutes !
  ___) | | ||  __/ |___| \__ \ |_  |  _  | |_| | | | | ||  __/ |     [{}+{}] Coded by NinjaCR3
 |____/|_|\__\___|_____|_|___/\__| |_| |_|\__,_|_| |_|\__\___|_|     [{}+{}] Contact : facebook.com/ninjacr3

 Dork Maker
""".format(settings.y,settings.r,settings.y,settings.r,settings.y,settings.r,settings.y,settings.r,settings.y,settings.r,settings.y))

print("="*60)
text = raw_input("\n[{}*{}] Please input any text : ".format(settings.r,settings.y))
words = text.split(" ")
print("[{}+{}] ".format(settings.r,settings.y) + str(len(words)) + " text verified! Now let's make some dorks!\n")
print("="*60)
print("\n[{}1{}] WordPress".format(settings.r,settings.y))
print("[{}2{}] Joomla".format(settings.r,settings.y))
print("[{}3{}] OpenCart".format(settings.r,settings.y))
cms = raw_input("\n[{}*{}] Which CMS dorks do you want to make? : ".format(settings.r,settings.y))
if cms == "1":
	print("[{}+{}] Prepared dorks:".format(settings.r,settings.y) + "\n")
	wpdorks = {'("Comment on Hello world!")',
			   '("Comentarios en Hello world!")',
			   '("author/admin")',
			   '("uncategorized/hello-world")',
			   '("category/sin-categoria")',
			   '("uncategorized")',
			   '("Proudly powered by WordPress")',
			   '("Welcome to WordPress. This is your first post.")',
			   '("Just another WordPress site")',
			   '("Mr WordPress on Hello world!")',
			   '("/wp/hello-world/")'}
	for wpdork in wpdorks:
		for word in words:
			print(wpdork + word)
			try:
				with open("dorkstest.txt","a") as f:
					f.write(wpdork + word + "\n")
			except:
				pass
	input("\n[{}*{}] Please enter to remove duplicate dorks...".format(settings.r,settings.y))
	clean()

elif cms == "2":
	print("[{}+{}] Prepared dorks:".format(settings.r,settings.y) + "\n")
	jmdorks = {'index.php?option=com_users ',
			   'index.php?option=com_jce ',
			   '("com_user")'}
	for jmdork in jmdorks:
		for word in words:
			print(jmdork + word)
			try:
				with open("dorkstest.txt","a") as f:
					f.write(jmdork + word + "\n")
			except:
				pass
	input("\n[{}*{}] Please enter to remove duplicate dorks...".format(settings.r,settings.y))
	clean()

elif cms == "3":
	print("[{}+{}] Prepared dorks:".format(settings.r,settings.y) + "\n")
	ocdorks = {'index.php?route=product ',
			   'index.php?route='}
	for ocdork in ocdorks:
		for word in words:
			print(ocdork + word)
			try:
				with open("dorkstest.txt","a") as f:
					f.write(ocdork + word + "\n")
			except:
				pass
	input("\n[{}*{}] Please hit enter to remove duplicate dorks...".format(settings.r,settings.y))
	clean()

else:
	print("[{}-{}] Invalid Optionn! Tool closed!".format(settings.r,settings.y))