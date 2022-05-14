import random 


def gerador(i):
    i = int(i)
    return random.randint(1,i)


def ajuda():
    print("Podes rolar dados fazendo !roll XdY, sendo X o número de dados e Y o número de faces")
    print("Se quiseres podes adicionar um modificar -> !roll XdY+Z ou !roll XdY-Z, onde Z é o modificador")
    print("Se quiseres rolar com vantagem (o programa escolhe o maior dos dados) adiciona um > no final do comando: !roll XdY+Z>")
    print("Se quiseres rolar com desvantagem (o programa escolhe o menor dos dados) adiciona um < no final do comando: !roll XdY+Z<")
    return(main())



def roll(x):
    somar=False
    vantagem=False
    desvantagem=False
    subtrair = False
    fudge = False
    asomar=0
    dd = x[1]
    dd = dd.split("d")

    
    if ">" in dd[1] and "<" not in dd[1]:
        vantagem = True
        dd[1]=dd[1].replace(">","")
    elif "<" in dd[1] and ">" not in dd[1]:
        desvantagem = False
        dd[1]=dd[1].replace("<","")
    if "-" in dd[1]:
        dd[1]=dd[1].replace("-","+")
        subtrair=True

    if "+" in dd[1]:
        somar = True
        k = dd[1].split("+")
        asomar = int(k[1])
        if subtrair==True:
            asomar=asomar*(-1)
        dd[1] = k[0]
    else:
        pass
    if "f" in dd[1]:
        fudge=True
        dd[0]=dd[0].replace("f","3")

    


        
    dados = []
    total= 0
    for i in range(int(dd[0])):
        dados.append(gerador(dd[1]))
    for j in dados:
        total = total + j
    if somar==True:
        total = total + int(asomar)
    if vantagem==True:
        total=max(dados)+int(asomar)
    if desvantagem==True:
        total=min(dados)+int(asomar)
    totalsemsoma=total-int(asomar)

    #completar a parte do fudge
    if fudge == True:
        dados = dados.replace(3, "+")
        dados= dados.replace(2, "0")
        dados = dados.replace(1, "-")


    
    print(dados,"->", total-int(asomar), "+", asomar, "=", total)
    return(main())





def ordem (x):
    if x[0] == "!help":
        ajuda()
    elif x[0]== "!roll":
        roll(x)
    




def main(): 
    print("...")
    x = input().strip()
    x = x.split(" ")


    ordem(x)

print("---")
print("Rolador de Dados!")
print("Escolhe o que queres fazer:")
print("!help para saberes o que faço")

main()

