#labels
from tkinter import *
import requests
import bs4
from operator import itemgetter


def exibe():

    valor2=240
    valor3=0

    sites=Label(root, fg="blue", text="Selecione o s sites :")
    sites.place(x=10,y=210)
    
    c_filme_1.place(x=1000,y=1000)
    c_filme_2.place(x=1000,y=1000)
    c_filme_3.place(x=1000,y=1000)
    c_filme_4.place(x=1000,y=1000)
    
    
    c_livro_1.place(x=1000,y=1000)
    c_livro_2.place(x=1000,y=1000)
    c_livro_3.place(x=1000,y=1000)
    c_livro_4.place(x=1000,y=1000)

    
    
    #Aparece o top 10 selecionado no listbox
    clicked_items = lb.curselection()
    soh_o_num=clicked_items[0]
    a1=lb.get(soh_o_num)

    

    if a1=="Top filmes online":

        valor3=120
        
        c_filme_1.config(text="Adoro cinema", var=v1, bg="orange",fg="blue")
        c_filme_1.place(x=10,y=valor2)
        
        c_filme_2.config (text="The pirate filmes online", var=v2, bg="orange",fg="blue")
        c_filme_2.place(x=10,y=(valor2+30))
        
        c_filme_3.config(text="Ultra cine filmes",var=v3, bg="orange",fg="blue")
        c_filme_3.place(x=10,y=(valor2+60))
        
        c_filme_4.config(text="Top filmes",var=v4, bg="orange",fg="blue")
        c_filme_4.place(x=10,y=(valor2+90))

        

    elif a1=="Top livros online":

        valor3=120
        
        c_livro_1.config(text="Amazon",var=v1, bg="orange",fg="blue")
        c_livro_1.place(x=10,y=valor2)
        
        c_livro_2.config(text="Livraria Cultura", var=v2, bg="orange",fg="blue")
        c_livro_2.place(x=10,y=(valor2+30))
        
        c_livro_3.config(text="Veja", var=v3, bg="orange", fg="blue")
        c_livro_3.place(x=10,y=(valor2+60))
        
        c_livro_4.config(text="Publish News", var=v4, bg="orange", fg="blue")
        c_livro_4.place(x=10,y=(valor2+90))


    #Aparece botão exibir
    butt2.config(text="Exibir", command=print_me)
    butt2.place(x=10,y=(valor2+valor3))

    
    return

def print_me():
    clicked_items = lb.curselection()
    soh_o_num=clicked_items[0]
    a1=lb.get(soh_o_num)
    
    Dicio={}
    Dicio_2=[]
    Lista=[]
    variavel=0
    mano_do_ceu=[]
    variula=0
    vv1=["1","2","3","4","5","6","7","8","9","0"]
    
    if a1=="Top filmes online":
        variavel_1=0
        variavel_2=0
        listFilmes_4_1={}
        Top_10={}
        vv1=["1","2","3","4","5","6","7","8","9","0"]
        titulo = "Filmes online mais assistidos entre os sites escolhidos"
        site_1 = requests.get("http://www.adorocinema.com/vod/populares/")
        site_2 = requests.get("https://thepiratefilmesonline.org/")
        site_4 = requests.get("https://ultracinefilmes.com/")
        site_5 = requests.get("https://topfilmes.co/")

        if v1.get()==1:
            #site_1.raise_for_status()
            objectSoup = bs4.BeautifulSoup(site_1.text,features="lxml")
            listFilmes_1 = objectSoup.find_all(class_="meta-title-link")
            for eachA in listFilmes_1:
                dicio=eachA.getText().replace('VOD','').strip()
                Lista.append(dicio)
       
        if v2.get()==1:        
            #site_2.raise_for_status()
            objectSoup = bs4.BeautifulSoup(site_2.text,features="lxml")
            listFilmes_2 = objectSoup.select('a')
            for eachA in listFilmes_2:
                if "HD" in eachA.getText():
                    for a in range(0,10,1):
                        if vv1[a] in eachA.getText():
                            hue=eachA.getText().strip()
                            if hue[0]==vv1[a]:
                                dicio=hue.replace('Dublado','').replace('Online','').replace('HD','').replace('720p','').replace('Completo','').replace(vv1[a],'').strip()
                                Lista.append(dicio)

        if v3.get()==1:                    
            #site_4.raise_for_status()
            objectSoup = bs4.BeautifulSoup(site_4.text,features="lxml")
            listFilmes_4 = objectSoup.select('h2')
            for eachA in listFilmes_4: 
                Lista.append(eachA.getText().strip())
                variavel_1=variavel_1+1
                if(variavel_1>=10):
                    break

        if v4.get()==1:    
            #site_5.raise_for_status()
            objectSoup = bs4.BeautifulSoup(site_5.text,features="lxml")
            listFilmes_5 = objectSoup.select('p')
            for eachA in listFilmes_5: 
                Lista.append(eachA.getText().strip().capitalize())
                variavel_2=variavel_2+1
                if variavel_2>=10:
                    break



    elif a1=="Top livros online":
        titulo = "Livros mais procurados entre os sites escolhidos"

        livro_1 = requests.get("https://www.amazon.com.br/b?ie=UTF8&node=16271670011")
        livro_2 = requests.get("https://www.livrariacultura.com.br/maisvendidos")
        livro_4 = requests.get("https://veja.abril.com.br/livros-mais-vendidos/")
        livro_8 = requests.get("https://www.publishnews.com.br/ranking")
        
            
        if v1.get()==1:    
            #livro_1.raise_for_status()
            objectSoup = bs4.BeautifulSoup(livro_1.text,features="lxml")
            listLivros_1 = objectSoup.find_all(class_="a-size-medium s-inline s-access-title a-text-normal")
            for eachA in listLivros_1:
                dicio = eachA.getText().capitalize()
                Lista.append(dicio)

        if v2.get()==1:   
            #livro_2.raise_for_status()
            objectSoup = bs4.BeautifulSoup(livro_2.text,features="lxml")
            listLivros_2 = objectSoup.find_all(class_="product-font-new product-title-new")
            for eachA in listLivros_2:
                dicio = eachA.getText().capitalize()
                Lista.append(dicio)

        if v3.get()==1:
            #livro_4.raise_for_status()
            objectSoup = bs4.BeautifulSoup(livro_4.text,features="lxml")
            listLivros_4 = objectSoup.find_all(class_="titulo")
            for eachA in listLivros_4:
                dicio = eachA.getText().capitalize()
                Lista.append(dicio)

        if v4.get()==1:
            #livro_8.raise_for_status()
            objectSoup = bs4.BeautifulSoup(livro_8.text,features="lxml")
            listLivros_8 = objectSoup.find_all(class_="pn-ranking-livro-nome")
            for eachA in listLivros_8:
                dicio = eachA.getText().capitalize().strip()
                Lista.append(dicio)
                   


    for b in Lista:
        valor=Lista.count(b)
        if b not in Dicio:
            Dicio[b]=int(valor)


    for chave,valor in sorted(Dicio.items(),key=itemgetter(1),reverse=True):
        Dicio_2.append(chave)
        variavel=variavel+1
        if variavel==10:
            break       

    Titulo.config(width=45, height=1, bg='#500', fg="white", text=titulo)
    Titulo.place(x=200,y=10)
    
    Primeiro.config(width=45, height=1, bg="#500", fg="white", text="1. "+Dicio_2[0])
    Primeiro.place(x=200,y=40)

    Segundo.config(width=45, height=1, bg="#500", fg="white", text="2. "+Dicio_2[1])
    Segundo.place(x=200,y=70)

    Terceiro.config(width=45, height=1, bg="#500", fg="white", text="3. "+Dicio_2[2])
    Terceiro.place(x=200,y=100)

    Quarto.config(width=45, height=1, bg="#500", fg="white", text="4. "+Dicio_2[3])
    Quarto.place(x=200,y=130)

    Quinto.config(width=45, height=1, bg="#500", fg="white", text="5. "+Dicio_2[4])
    Quinto.place(x=200,y=160)

    Sexto.config(width=45, height=1, bg="#500", fg="white", text="6. "+Dicio_2[5])
    Sexto.place(x=200,y=190)

    Setimo.config(width=45, height=1, bg="#500", fg="white", text="7. "+Dicio_2[6])
    Setimo.place(x=200,y=220)

    Oitavo.config(width=45, height=1, bg="#500", fg="white", text="8. "+Dicio_2[7])
    Oitavo.place(x=200,y=250)

    Nono.config(width=45, height=1, bg="#500", fg="white", text="9. "+Dicio_2[8])
    Nono.place(x=200,y=280)

    Decimo.config(width=45, height=1, bg="#500", fg="white", text="10. "+Dicio_2[9])
    Decimo.place(x=200,y=310)
    

    return

#Nome da janela        
root = Tk()
v1 = IntVar(root)
v2 = IntVar(root)
v3 = IntVar(root)
v4 = IntVar(root)
#caracteristicas da scrollbar
scrollbar = Scrollbar(root, orient=VERTICAL)
scrollbar.pack(side=RIGHT, fill=Y)
#Inciando listbox
lb = Listbox(root)
lb.pack()
#Inserindo nomes na listobox
lb.insert(0,"Top filmes online","Top livros online")
#Scrollbar da listabox lb
lb.config(yscrollcommand=scrollbar.set)
#Lugar da listbox lb
lb.place(x=10,y=10)



#Definido label, lugar e suas caracteristicas
#Label das variaveis dos sites escolhidos
l = Label(root)

#
Titulo=Label(root)
#Primeiro Lugar
Primeiro=Label(root)
#Segundo Lugar
Segundo=Label(root)
#Terceiro Lugar
Terceiro=Label(root)
#Quarto
Quarto=Label(root)
#Quinto
Quinto=Label(root)
#Sexto
Sexto=Label(root)
#Setimo
Setimo=Label(root)
#Oitavo
Oitavo=Label(root)
#Nono
Nono=Label(root)
#Decimo
Decimo=Label(root)


#botão exibir
butt2 = Button(root)


#caixa de marcar para cada pagina da web

c_filme_1 = Checkbutton(root)

c_filme_2 = Checkbutton(root)

c_filme_3 = Checkbutton(root)

c_filme_4 = Checkbutton(root)



c_livro_1 = Checkbutton(root)

c_livro_2 = Checkbutton(root)

c_livro_3 = Checkbutton(root)

c_livro_4 = Checkbutton(root)


scrollbar.config(command=lb.yview)

butt1=Button(root, text="GO", command=exibe)
butt1.place(x=10,y=175)

root.geometry("700x700")
root.title("Nome do projeto")

Descricao=Label(root, fg="blue", text="Selecione o top 10 e aperte GO.")
Descricao.place(x=10,y=500)

mainloop()
