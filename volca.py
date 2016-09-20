
f = open("input.in", "r") #abre o arquivo de entradas
w_mod = int(f.readline()) #le o |w|
p = int(f.readline())     #le o p
W = {}                    #cria o dicionario W
v_max = {}                #cria o dicionario v_max
v_min = {}                #cria o dicionario v_min
v_class = {}              #cria o dicionario v_class
limit = w_mod-w_mod*p     #inicializa a variável limit

for linha in f:
    pass

for i in v_max:
    if v_max[i] > limit:
        v_class[i] = "sell"
    if v_min[i] > limit:
        v_class[i] = "buy"

f.close()                 #fecha o arquivo de entrada
