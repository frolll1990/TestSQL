####IRM rule generator 
####v001

print("\nWelcome to IRM config generator!\n")
f = open("file_with_rule.txt", "w")


exc = input("Execution?\n Market = 1\n Instant = 2\n Instant+Market = 3\n")

if exc == '1':
    exc = 'market;'
    print(exc)
elif exc == '2':
    exc = str('instant;')
else:
    exc = str('market,instant;')


symb = input("Symbol?\n EURUSD = 1\n GBPUSD = 2\n or type symbolname \n")

if symb == '1':
    symb = str('Forex\EURUSD;')
elif symb == '2':
    symb = str('Forex\GBPUSD;')
else:
    symb = str(symb) + ";"


gr = input("Groups?\n * = 1\n or type groupname \n")

if gr == '1':
    gr = str('*;')
else:
    gr = str(gr) + ";"


lgns = input("Logins?\n * = 1\n or type logins\n")


if lgns == '1' and gr == '*;':    
	lgns = str(';')
elif lgns == '1':
    lgns = str('*;')
else:
    lgns = str(lgns) + ";"
    
#print("\n\n" + exc + symb + gr + lgns + vol + type + "\n\n")

vol = input("Add exact volume or volume - range\n")+";"

type = input("\n Type?\n open,close = 1\n limit,stop = 2\n tp,sl,stopout = 3 \n all = 0\n")
if type == '1':
    type = str('open,close;')
elif type == '2':
    type = str('limit,stop;')
elif type == '3':
    type = str('tp,sl,stopout;')
elif type == '0':
    type = str('open,close,stop_limit,tp,sl,stopout;')
else:
    type = str(type) + ";"
#print("\n\n" + exc + symb + gr + lgns + vol + type + "\n\n")

delay = input("\n Delay?\n\n in milliseconds: ")+";"


po = input("\n Price Options?\n wp = 1\n bp = 2\n fp = 3 \n np = 4\n op = 5 \n dp = 6 \n")


if po == '1':
    po = str('wp;')
elif po == '2':
    po = str('bp;')
elif po == '3':
    po = str('fp;')
elif po == '4':
    po = str('np;')
elif po == '5':
    po = str('op;')
elif po == '6':
    po = str('dp;')
else:
    po = str(po) + ";"





prdiv = input("\n Price Deviation?\n\n in pips: ")+";"

muv = input("\n Max Unchanged Volume?\n\n in lots x100: ")+";"

ovm = input("\n Open Volume Multiplier?\n\n :")


rule = exc + symb + gr + lgns + vol + type + delay + po + prdiv + muv + ovm
print("\n\n" + rule + "\n\n")
f = open("file_with_rule.txt", "w")
f.write(rule)
f.close