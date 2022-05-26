from tkinter import *
from PIL import Image, ImageTk
import os
from tkinter import filedialog
import pytesseract
import sys

class OCRDetection:
    def __init__(self,master):
        def MainmenuFonk():
            master.update()
            master.deiconify()
            self.Quit()
            
        def writeText():
            f = open("data/file.txt", 'w')
            f.write(self.textFile)
            f.close()   
            self.fileLocation=self.textFile
        def openTextFile():
            try:
                textname=filedialog.askopenfilename(initialdir="C://", title="Lütfen Teseract Exe Seçin ",filetypes=(("EXE File", "*.exe"),("All Files", "*.*")))
                self.textFile=textname
                fileLoc.config(text=textname)
            except:
                pass

        def openFileImg():
            try:
                filename=filedialog.askopenfilename(initialdir="/img/", title="Lütfen bir Resim veya Video Dosyası Seçin",filetypes=(("JPG File", "*.jpg"),("PNG File", "*.png")))
                myImage.place_forget()
                imageFirst=Image.open(filename)
                imageLast=imageFirst.resize((450, 400),Image.ANTIALIAS)
                myImg=ImageTk.PhotoImage(imageLast)
                myImageLast=Label(self.root,image=myImg,bg="#2C073E",fg="#ffffff",width=450,height=400)
                myImageLast.image=myImg
                myImageLast.place(x=50,y=170)
                Path.config(text=filename)
                self.filename=filename
            except:
                pass
        def toText():
            try:
                myFileinp=open("data/file.txt", "r")
                dirmyFile=myFileinp.read()
                fileLoc.config(text=dirmyFile)
                myFileinp.close()
                pytesseract.pytesseract.tesseract_cmd = self.fileLocation
                a=pytesseract.image_to_string(Image.open(self.filename), lang="tur")
                OCRText.delete(1.0,END)
                OCRText.insert(INSERT,a)
            except:
                pass
              
            
            
    #<---Form Ayarları--->

        self.root = Toplevel()
        self.root.wm_iconbitmap('img/iconum.ico')
        self.root.geometry("1266x692+0+0")
        self.root.maxsize(1366,768)
        self.root.title("OCR")
        self.root.configure(background='#03994c')
        
    #</---Form Ayarları--->


    #<---Resimlerin Eklenmesi--->

        mainmenu=ImageTk.PhotoImage(Image.open(os.getcwd()+"\\img\\home2.png"))
        find=ImageTk.PhotoImage(Image.open(os.getcwd()+"\\img\\search.png"))
        noImage=ImageTk.PhotoImage(Image.open(os.getcwd()+"\\img\\noImage.png"))
        fotoImage=ImageTk.PhotoImage(Image.open(os.getcwd()+"\\img\\yazi.png"))
        save=ImageTk.PhotoImage(Image.open(os.getcwd()+"\\img\\save.png"))


    #</---Resimlerin Eklenmesi--->

    #<---Butonların Oluşturulması--->

        menu=Button(self.root,image=mainmenu,bd=0,highlightthickness=0,command=MainmenuFonk,width=150,height=50,bg="#03994c",fg="#000000")
        menu.image=mainmenu
        menu.place(x=10,y=20)

        findButton=Button(self.root,image=find,bd=0,highlightthickness=0,command=openFileImg,width=24,height=24,bg="#03994c",fg="#000000")
        findButton.image=find
        findButton.place(x=980,y=100)

        filefindButton=Button(self.root,image=find,bd=0,highlightthickness=0,command=openTextFile,width=24,height=24,bg="#03994c",fg="#000000")
        filefindButton.image=find
        filefindButton.place(x=980,y=135)

        filesaveButton=Button(self.root,image=save,bd=0,highlightthickness=0,command=writeText,width=26,height=26,bg="#03994c",fg="#000000")
        filesaveButton.image=save
        filesaveButton.place(x=1020,y=135)

        imageButton=Button(self.root,image=fotoImage,bd=0,highlightthickness=0,command=toText,bg="#03994c",fg="#ffffff")
        imageButton.image=fotoImage
        imageButton.place(x=120,y=590)


    #</---Butonların Oluşturulması--->

    #<---Labelların Oluşturulması--->

        title=Label(self.root,text="OCR (Optik Karakter Tanıma) ",font = "Arial 12 bold ",bg="#03994c",fg="#000000")
        title.place(x=463,y=30)

        fileLbl=Label(self.root,text="Dosya Yolu :",font = "Arial 10 ",bg="#03994c",fg="#000000")
        fileLbl.place(x=55,y=100)

        Path=Label(self.root,text="Lütfen Bir Dosya Seçin ...",font = "Arial 10 ",bg="#03994c",fg="#000000")
        Path.place(x=160,y=100)

        fileLocName=Label(self.root,text="Tesseract Yolu :",font = "Arial 10 ",bg="#03994c",fg="#000000")
        fileLocName.place(x=55,y=135)
        myFileinp=open("data/file.txt", "r")
        dirmyFile=myFileinp.read()
        self.fileLocation=dirmyFile
        fileLoc=Label(self.root,text=dirmyFile,bg="#03994c",fg="#000000")
        fileLoc.place(x=160,y=135)
        myFileinp.close()

        myImage=Label(self.root,image=noImage,bg="#03994c",fg="#000000",width=450,height=400)
        myImage.place(x=50,y=170)

        OCRText=Text(self.root,bg="#BDBDBD",fg="#000000",width=60,height=25)
        OCRText.place(x=650,y=170)

       

    #</---Labellerın Oluşturulması--->


        self.root.mainloop()
    
    #<---Fonksiyonların Tanımlanması--->
    
    
    def Quit(self):
        self.root.destroy()

    #</---Fonksiyonların Tanımlanması--->




    

  
