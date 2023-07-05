# Anthill, the tree-based web crawler.

print("                                                                                 \n                                                                                 \n                                         hh                    lllll    llll     \n                               tt        hh              ii       ll      ll     \n    aaaaaa      nn nnnnnn    ttttttttt   hh hhhhhh                ll      ll     \n  aaa    aaa    nnn     nnn    tt        hhh     hhh     ii       ll      ll     \n         aaa    nn      nnn    tt        hh      hhh     ii       ll      ll     \n  aaaaaaaaaa    nn      nnn    tt        hh      hhh     ii       ll      ll     \n aaa     aaa    nn      nnn    tt        hh      hhh     ii       ll      ll     \n  aaaaaaaaaa    nn      nnn    ttttttt   hh      hhh     iiiii    lllll   llllll \n                                                                                 \n \n                         Anthill, the tree-based web crawler. \n \n                                         **                                      \n                             ,*%#%(##,((%#%,**,(%,//(,*,/                        \n                       %**,%%%(#%%%%&%#(,/*(/#//,*/(/%/#%/#/(                    \n                    */,(*#,%%&%%&%%%%%#(*/(/(,/,#%%**/,,.,,,*,*(                 \n                 .*,#*..,*.*(%*(#,/#,,/*,,(%(*(/#,#(,.(/,*(#%%#%%%#              \n             ,,,(*,#**/.#/,*,#((/#*##/*/*,%%#((%%((#%%&#%*(%%#&*,(%%%%           \n         ,,/.*,,*/,*//***&,((/,%/(,#%%&#(//#**#%%(#%%#*&//##%%%%%%&%%%%&%#       \n      *,(*,,(*.,*(*(#/&/*/,/.*%*%((#&&%%(%%(%/&(%%,&%,%#%%&&&%%%##%%%#&#%%#%#    \n  (,,,*//,*.*###,,./(%//(/*/*%/#*,*(%%#(&((/*#%,*/,((#%&%#%&##&&%%&##%#%%&#%&%*  \n ,,*.,,**/*//%(,*,((#*,*#(##%%,*%#,#&/,###(%#,%,(*(%%#*(#*#(###/%%&%#%&&%&%%%%,* \n  *//#(/*%(#,#((,*,.,*,(*%%*%##%/%*,&*/(#%#*(,//(*%###&#, %&#&%/*&##&%&&%%&%%#/  \n  (((*##(//*##/,///*/#%(/,/(##&/##,#,/*/#(,,%#(.%%/,(%&,%&,%,#%#*%%*&%%,%(,(*    \n   &*,%*%%%%,#/**/**##*/*#(,,#,,#/#//(#&((#%#//#(,*/*/#,#,%/(#&*#&%#%#**         \n            &*#*(,,*(,%((((,*%//%(*,*&./%*(&(,%%#&%/#&(%%*%#&(%*/%               \n                             %.*//,#**##*  *//#,#,(#,##,,                       ")

cfg = {}

trees = []

# Class for defining URL trees
class Tree:
	def __init__(this, name, url):
		this.name = str(name).lower().replace(" ", "_")
		this.data = {}
		dlfc = 0

	def __str__(this):
		return this.name
	
	def __repr__(this):
		return "Tree of name " + this.name

print("\nImporting html from lxml...", end="")
try:
	from lxml import html
except:
	print("\u001b[31mERROR\u001b[0m\nQuiting!")
	quit()
print("\u001b[32mOK\u001b[0m\nImporting requests...", end="")
try:
	import requests
except:
	print("\u001b[31mERROR\u001b[0m\nQuiting!")
	quit()
print("\u001b[32mOK\u001b[0m\nLoading default settings...", end="")
try:
	cfgFile = open("anthillDefs.cfg", "r").read()
	cfgFile = cfgFile.replace(" ", "").split("\n")
	for x in cfgFile:
		y = x.split("=")
		if len(y) > 2:
			raise FileError
		cfg[y[0]] = eval(y[1])
	
except:
	print("\u001b[31mERROR\u001b[0m\nQuiting!")
	quit()

print("\u001b[32mOK\u001b[0m\n\nSettings:")

print("do not "*(not cfg["showtitle"]) + "show page titles")
print("do not "*(not cfg["showurl"]) + "show URLs")
print("do not "*(cfg["showtitle"]) + "rescan links\n")

def 

def tokenSplit(inp):
	ts = inp.split(" ")
	ts = [i for i in ts if i!=""]
	return ts

active = "anthill"
indentationLevel = 0

while True:
	cmd = input(active + "> ")
	c = tokenSplit(cmd)

	if c[0] == "echo":
		print(" ".join(c[1:]))
	elif c[0] == "begintree":
		try:
			-trees.append(Tree(c[1], c[2]))
			print("Tree established. Type 'crawl " + str(trees[-1]).lower().replace(" ", "_") + " 1' to crawl it 1 layer deep.")
		except IndexError:
			print("Missing argument(s)")
	elif c[0] == "crawl":
		
def crawl(url):
    page = requests.get(url)
    webpage = html.fromstring(page.content)
    
    return webpage.xpath('//a/@href')

initial = "http://" + input("URL: http://")

#MARK
lst = []
lst2 = crawl(initial)

#MARK
newsrc = ""
mostRecentWithResults = "*NO*"
linksFound = []

#MARK
while True:
    try:
        for x in tuple(lst2):
            if x[0] == "/":
                lst2.remove(x)
        if len(lst2) != 0:
            newsrc = random.choice(lst2)
        else:
            newsrc = random.choice(lst)
        newsrc = newsrc[:newsrc.find("#")]

        if not excludeFound:
            for z in lst2:
                if z in linksFound:
                    lst2.remove(z)
        
        for y in lst2:
            if simplified == True:
                try:
                    print(html.fromstring(requests.get(y).content).xpath("//title")[0].text)
                except:
                    print("No page name")
            else:
                print(y)
        lst = lst2
        lst2 = crawl(newsrc)
    except:
        print(" ---- NO LINKS ON PAGE, RESTARTING FROM INITIAL URL ----")
        newsrc = initial
        lst = []
        lst2 = crawl(initial)
