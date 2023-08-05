try:
   import tkinter as tk
   from tkinter.messagebox import showerror, showinfo
   import tkinter as tk
   from tkinter import ttk
   from tkinter import*
   import cv2
   import numpy as np
   from PIL import Image, ImageTk 
   import PDFVisor.funcsVisorPDF as vPDF
except Exception as e:
      print(f"This error occured while importing neccesary modules or library {e}")   

nombre = ""
lenguaje = ""
bandaFrame = None
marcovisor = None
opcion = ""
image_on_canvas = None


class Visor(tk.Frame):
     def __init__(self, master=None):
         #tk.Toplevel.__init__(self, master)
         tk.Frame.__init__(self, master)
         global btnEstado
         global bandaFrame
         global marcovisor
         global pdf_location
         global btnAvance
         global btnRetro
         global opcion
         global image_on_canvas
         global auto

         estilo = ttk.Style(self)
         estilo.configure("Emergency.TLabel", borderwidth= 0, relief="flat")
         estilo.layout('GDocument.TLabel', 
                                [('Label.border',  {'sticky': 'nswe', 'border': '0',
                                  'children': [('Label.padding', {'sticky': 'nswe', 'border': '0',
                                  'children': [('Label.label', {'sticky': 'nswe'})]
                                 })]
                              }
                           )])

     
         pdf_location = self.master.getvar(name="PDFDOC")
         auto = self

         self.master.configure(height=675, width= 770, bg= "#1a5e92")
         #self.config(height=529, width= 330, bg= "#1a5e92")
         self.grid_rowconfigure(0, weight= 60)
         self.grid_rowconfigure(1, weight= 120)
         self.place()
         
         bandaFrame = tk.Frame(self.master, bg="#2596be", height=80, width= 770)
         bandaFrame.grid(row= 0, column= 0, padx=2, sticky="nw")
         bandaFrame.grid_columnconfigure(0, weight=50)
         bandaFrame.grid_columnconfigure(1, weight=150)
         bandaFrame.grid_columnconfigure(2, weight=50)
         bandaFrame.place_configure(x=0, y=0)

         marcovisor = tk.LabelFrame(self.master, width= 770, height= 605, borderwidth= 2, bg= "#2596be", relief= "raised")
         marcovisor.grid(row=1, column=0, padx= 2, pady= 2, sticky="se")
         marcovisor.place_configure(x=0, y=80, bordermode="outside")
        
         btnEstado = vPDF.defEstado(self.master.getvar(name="PDFDOC"))
         archEstados = btnEstado["imagStates"]
         estados = btnEstado["Estado"]
         self.imgAvance = ImageTk.PhotoImage(file= archEstados[0])
         btnAvance = ttk.Label(bandaFrame, image= self.imgAvance, state= estados[0], width= 106, border=0, background=None)
         btnAvance.config(style= "Emergency.TLabel")
         btnAvance.grid(row=0, column=0, ipadx=0, ipady=0)
         btnAvance.place()

         metaDataDoc = vPDF.metaDataPDF(self.master.getvar(name="PDFDOC"))
         rotulo = Canvas(bandaFrame, width=330, height=60, highlightthickness=0, bg="#2596be", bd=0, borderwidth= 0)
         rotulo.grid(row=0, column=1, ipady=0, ipadx=5)
         metadatosPDF = "{}\n{}".format(metaDataDoc.get("Titulo"), metaDataDoc.get("Fecha_creacion"))
         x = vPDF.centraTexto(metaDataDoc.get("Titulo"), bandaFrame.cget('width'))
         lblInformacion = rotulo.create_text(x, 28, justify="center", text= metadatosPDF, fill="white", font= ("Times New Roman", 12, "bold"))

         btnEstado = vPDF.defEstado(self.master.getvar(name="PDFDOC"))
         archEstados = btnEstado["imagStates"]  #estados[1]
         estados = btnEstado["Estado"]
         self.imgRetro = ImageTk.PhotoImage(file= archEstados[1]) 
         btnRetro = ttk.Label(bandaFrame, image= self.imgRetro, state= "normal", width= 106)  
         btnRetro.config(style= "Emergency.TLabel")
         btnRetro.grid(row=0, column=2)
         btnRetro.place()

         vPDF.desglosaPDF(self.master.getvar(name="PDFDOC"))
         nomFile = self.master.getvar(name="PDFDOC")
         nomFile = nomFile[0:-4] + "_Page-0.jpg"
         img = Image.open(nomFile)
         img = img.resize((752,577), Image.Resampling.LANCZOS)
         imgk = ImageTk.PhotoImage(img)
         visorPDF = tk.Label(marcovisor, image= imgk, width=752, height=577, borderwidth= 0, bg= "white")
         visorPDF.grid(row=0, column= 0, ipadx= 2, ipady=2, sticky= "sw")
         visorPDF.place_configure(x=0, y=85, bordermode="outside")

         vPDF.grid_by_column(bandaFrame, 3)
         
         self.gestorEventos()

     def on_enter(self, parOpcion, opcion, fileflecha):
         global btnEstado
             
         btnEstado = vPDF.defEstado(pdf_location)
         print("Llega a 'on_enter'")  
         print(parOpcion)

         if btnEstado[opcion] == 'normal':
             imgFlecha = ImageTk.PhotoImage(file= fileflecha)
             bandaFrame.children[parOpcion].__setattr__('image', imgFlecha)


     def on_leave(self, parOpcion, opcion, fileflecha):
         btnEstado = vPDF.defEstado(auto.master.getvar(name="PDFDOC"))
         print("Llega a 'on_leave'")      

         if btnEstado["Estado"][opcion] != btnAvance.cget("state"):
            imgFlecha = ImageTk.PhotoImage(file= fileflecha)
            bandaFrame.children[parOpcion].__setattr__('image', imgFlecha)

     def on_press(self, parOpcion, opcion, fileflecha):
         global btnEstado
         global estados

         btnEstado = vPDF.defEstado(pdf_location)
         
         if btnEstado[opcion] == 'normal':
             imgFlecha = ImageTk.PhotoImage(file= fileflecha)
             bandaFrame.children[parOpcion].__setattr__('image', imgFlecha)
         else:
             return    

         nomFilePag = pdf_location[:-4]           
         nomFilePag = nomFilePag[8:] + ".pdf"
         boolEstados = {}
         archEstados = {"avancePressed.png", "retroPressed.png"}

         reader = vPDF.PdfReader(pdf_location, "rb")
         if len(reader.pages) == 1:
               archEstados = {r"./img/avanceDeshabilitado.png", r"./img/retroDeshabilitado.png"}
               estados = ["disabled", "disabled"]

               imgFlecha = ImageTk.PhotoImage(file= archEstados[0])
               bandaFrame.children['!label'].__setattr__('image', imgFlecha)
               bandaFrame.children['!label'].__setattr__('state', "normal")
               imgFlecha = ImageTk.PhotoImage(file= archEstados[1])
               bandaFrame.children['!label2'].__setattr__('image', imgFlecha)
               bandaFrame.children['!label2'].__setattr__('state', "normal")
               opcion = -1
               reader = None
         elif len(reader.pages) == 2:
              archEstados = {r"./img/avanceNormal.png", r"./img/retroDeshabilitado.png"} 
              estados = ["normal", "disabled"]

              imgFlecha = ImageTk.PhotoImage(file= archEstados[0])
              bandaFrame.children['!label'].__setattr__('image', imgFlecha)
              bandaFrame.children['!label'].__setattr__('state', "normal")
              imgFlecha = ImageTk.PhotoImage(file= archEstados[1])
              bandaFrame.children['!label2'].__setattr__('image', imgFlecha)
              bandaFrame.children['!label2'].__setattr__('state', "normal")
              reader = None
              return
         elif len(reader.pages) < 1:
             opcion = -1
             return 


     def on_release(self, parOpcion, opcion, fileflecha):
         global btnEstado
         global image_on_canvas
             
         btnEstado = vPDF.defEstado(pdf_location)

         if btnEstado[opcion] == 'normal':
             imgFlecha = ImageTk.PhotoImage(file= fileflecha)
             bandaFrame.children[parOpcion].__setattr__('image', imgFlecha)
         else:
             return 

         nomFile = self.master.getvar(name="PDFDOC")
         nomFile = nomFile[0:-4] + "_Page-{}.jpg".format(opcion)
         imgk = Image.open(nomFile)
         imgk = imgk.resize((752,577), Image.Resampling.LANCZOS)
         marcovisor.children['!label'].__setattr__('image', imgk)
         
         
     def gestorEventos(self):    
         archEstados = btnEstado["imagStates"]
         
         bandaFrame.children['!label'].bind("<Enter>", lambda event: auto.on_enter('!label', 0, r"./img/avanceHighlight.png"))                    
         bandaFrame.children['!label2'].bind("<Enter>", lambda event: auto.on_enter('!label2', 1, r"./img/retroHighlight.png") )                                   
         bandaFrame.children['!label'].bind("<Leave>", lambda event: auto.on_leave('!label',  0, archEstados[0]))
         bandaFrame.children['!label2'].bind("<Leave>", lambda event: auto.on_leave('!label2', 1, archEstados[1]))
         bandaFrame.children['!label'].bind("<ButtonPress-1>", lambda event: self.on_press('!label',  r"./img/avanceHighlightPressed.png"))                    
         bandaFrame.children['!label2'].bind("<ButtonPress-1>", lambda event: self.on_press('!label2', r"./img/retroHighlightPressed.png") )                                   
         bandaFrame.children['!label'].bind("<ButtonRelease-1>", lambda event: self.on_release('!label',  0, r"./img/avanceHighlight.png"))
         bandaFrame.children['!label2'].bind("<ButtonRelease-1>", lambda event: self.on_release('!label2', 1, r"./img/retroHighlight.png"))