from tkinter import* 

import socket 

Pen = Tk()
Pen.geometry("330x500")
Pen.title("ACIK PORT TARAMA ")

Pen.resizable(FALSE,FALSE)

arkaplanResimi = PhotoImage(file="img2.png")

lblarkaplan = Label(Pen,image= arkaplanResimi)
lblarkaplan.place(x=0, y=0)



lblurl =  Label(Pen, text="URL VEYA IP ADRESI", font= "Verdana 12 bold", fg="blue")
lblurl.place(x=60, y=20)
listsonuc =  Listbox(Pen, font="Verdana 12 bold", width="25", height="17",fg=  "white", bg = "black")

listsonuc.place(x=27 , y=140)
entur1  = Entry(Pen, font= "Verdana 12 bold" ,  fg="blue")

entur1.place(x=50 , y= 50 )
def trama():
    s1 = str(entur1.get())
    liste = [21,22,23,25,80,139,443,445,3389]
    try:
        for port in liste :
            sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
            result = sock.connect_ex((s1,port))
            if result == 0 :
                listsonuc.insert(1,"port{} Acik ".format(port))
            else:
                listsonuc.insert(1,"port{} Acik ".format(port))
            sock.close()
    except socket.error:
        print("Bilgisayara Ulasilamiyor ")

btntra = Button(Pen, text= "PORTLARI TARA" , font= "Verdana" , fg= "white" , bg  = "black" , command=trama)

btntra.place(x= 80 , y=90)
Pen.mainloop()

