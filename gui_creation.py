import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import font
import config_handler
import gui_handler




class LexGUI:



    def __init__(self, win):
    	self.master = win
    	



    def createTabs(self):
        s = ttk.Style()
        s.theme_create( "MyStyle", parent="alt", settings={
            "TNotebook": {"configure": {"tabmargins": [2, 5, 2, 0] } },
            "TNotebook.Tab": {"configure": 
                {"padding": [40, 10], "font" : ('URW Gothic L', '11', 'bold')},
            }
        })
        s.theme_use("MyStyle")
        s.configure('TButton', relief='raised', padding= 6)
        

        self.tabControl = ttk.Notebook(self.master)
        
        self.tab1 = ttk.Frame(self.tabControl)
        self.tab2 = ttk.Frame(self.tabControl)
        self.tab3 = ttk.Frame(self.tabControl)
        self.tab4 = ttk.Frame(self.tabControl)

        self.tabControl.add(self.tab1, text = 'Generate Pairs')
        self.tabControl.add(self.tab2, text = 'Merge Pairs')      
        self.tabControl.add(self.tab3, text = 'Recycle')
        self.tabControl.add(self.tab4, text = 'Settings')


        #display tabs
        self.tabControl.pack(expand = 1, fill = "both")

    

    
    def processText1(self):
        if(self.filepath41.get() and self.filepath42.get() and self.filepath11.get()):
            gui_handler.processTab1(self.filepath41.get(), self.filepath42.get(), self.filepath11.get())
        else:
            messagebox.showwarning("Error", "Empty output or settings")


    def dirDialog11(self):
        self.filename11 = filedialog.askdirectory()
        if (self.filename11):
            self.filepath11.set(self.filename11)
            cf = config_handler.ConfigHandler()
            cf.set_config_value(cf.RECENT_OUTPUT_DIR,self.filename11)   
    
    def createTab1(self):
      
        #TAB NO 1  SECTION 0
        self.labelFrame1 = ttk.LabelFrame(self.tab1, text= 'Select a clean map file:', borderwidth = 1,  relief="raised")
        self.labelFrame1.grid(column=0, row=0, padx = 20, pady = 20)
        #STYLE SETTINGS
        style = ttk.Style()
        style.configure('TLabelframe.Label', font='arial 11 bold')
        style.configure('TEntry', font = ('Courier', 24), padding = 4)


        #TAB NO-1 SECTION NO-1======================================================================
        #label 
        self.label11 = ttk.Label(self.labelFrame1, text="Generation Output Folder:")
        self.label11.grid(column = 0, row = 1,  padx = 20, pady = 0, sticky = "w")

        self.filepath11 = tk.StringVar()
        #load config value
        cf = config_handler.ConfigHandler()
        value = cf.get_config_value(cf.RECENT_OUTPUT_DIR)
        self.filepath11.set(value) 
        self.path11 = ttk.Entry(self.labelFrame1, width=90, textvariable = self.filepath11)
        self.path11.grid(column = 0, row = 2, padx = (20, 0), pady = 10, sticky = "w")
   

        #button 11
        self.button11 = ttk.Button(self.labelFrame1, text = "Browse...", command=self.dirDialog11)
        self.button11.grid(column = 1, row = 2, padx = (0, 20) , pady = 10, sticky = "w")
  


        #TAB NO-1 SECTION NO-2======================================================================
        #label 11
        self.label12 = ttk.Label(self.labelFrame1, text="Click button to start generating word pairs:")
        self.label12.grid(column = 0, row = 3, padx = 20, pady = (20,0) , sticky = "w")
        
        #button 12        
        self.button12 = ttk.Button(self.labelFrame1, text = "START PROCESS", command=self.processText1)
        self.button12.grid(column = 0, row = 4, padx = 20, pady = (0, 20))

    #----------------------------------------------------------------------
    #STARTING TAB 2 FUNCTIONS AND GUID ELEMENTS
    #----------------------------------------------------------------------

    def dirDialog21(self):
        self.filename21 = filedialog.askdirectory()
        if (self.filename21):
            self.filepath21.set(self.filename21) #set the textbox to the file path        
            cf = config_handler.ConfigHandler()
            cf.set_config_value(cf.RECENT_OUTPUT_DIR2,self.filename21)

    def processText2(self):
        if(self.filepath43.get() and self.filepath21.get()):
            gui_handler.processTab2 (self.filepath43.get(), self.filepath21.get())
        else:
            messagebox.showwarning("Error", "Missing input or output folder")


  
    def createTab2(self):

        #TAB 2 ----SECTION 0------------------------------------------------------------------------------
        self.labelFrame2 = ttk.LabelFrame(self.tab2, text= 'Output Directory:',  borderwidth = 1,  relief="raised")
        self.labelFrame2.grid(column=0, row=0, padx = 20, pady = 20)


        #TAB 2 ----SECTION 1------------------------------------------------------------------------------
        #label 21
        self.label21 = ttk.Label(self.labelFrame2, text="Select output director for merged file:")
        self.label21.grid(column = 0, row = 0,  padx = 20, pady = 0, sticky = "w")
        
        self.filepath21 = tk.StringVar()
        #load config value
        cf = config_handler.ConfigHandler()
        value = cf.get_config_value(cf.RECENT_OUTPUT_DIR2)
        self.filepath21.set(value) 
        self.path21 = ttk.Entry(self.labelFrame2, width=90, textvariable = self.filepath21)
        self.path21.grid(column = 0, row = 1, sticky = "w", padx=(20, 0), pady = 20)
        
        #button 21
        self.button21 = ttk.Button(self.labelFrame2, text = "Browse Folder", command=self.dirDialog21)
        self.button21.grid(column = 1, row = 1, sticky = "w", padx = (0, 20), pady = 20)
  
        #label 22
        self.label22 = ttk.Label(self.labelFrame2, text="Click button to start merging:")
        self.label22.grid(column = 0, row = 2, sticky = "w", padx = 20, pady = (20, 0) )
        
        #button no 22
        self.button22 = ttk.Button(self.labelFrame2, text = "START PROCESS", command=self.processText2)
        self.button22.grid(column = 0, row = 3, padx = 20, pady = (0, 20) )

    #----------------------------------------------------------------------
    #STARTING TAB 3 FUNCTIONS AND GUID ELEMENTS
    #----------------------------------------------------------------------

    def fileDialog31(self):
        self.filename31 = filedialog.askopenfilename(initialdir = "E:/FULLTEXT/PAIR/CLEANMERGE", 
            title = "Select standard word list", filetypes = (("Text files", "*.txt"), ("all files", "*.*")))
        if (self.filename31):
            self.filepath31.set(self.filename31)
            cf = config_handler.ConfigHandler()
            cf.set_config_value(cf.RECENT_OPEN_FILE3,self.filename31)


    def processText3(self):
        if(self.filepath31.get() and self.filepath21.get() and self.filepath43.get()):
            gui_handler.processTab3 (self.filepath31.get(), self.filepath21.get(), self.filepath43.get())
        else:
            messagebox.showwarning("Error", "Missing input or output folder")


    def createTab3(self):
        #TAB 3 ----SECTION 0------------------------------------------------------------------------------
        self.labelFrame3 = ttk.LabelFrame(self.tab3, text= 'Recycle Marged File:',  borderwidth = 1,  relief="raised")
        self.labelFrame3.grid(column=0, row=0, padx = 20, pady = 20)


        #TAB 3 ----SECTION 1------------------------------------------------------------------------------
        #label 31
        self.label31 = ttk.Label(self.labelFrame3, text="Select manually cleaned merged file:")
        self.label31.grid(column = 0, row = 0,  padx = 20, pady = 0, sticky = "w")


        #textbox 31
        self.filepath31 = tk.StringVar()
        #load defaults
        cf = config_handler.ConfigHandler()
        value = cf.get_config_value(cf.RECENT_OPEN_FILE3)
        self.filepath31.set(value)


        self.path31 = ttk.Entry(self.labelFrame3, width=90, textvariable = self.filepath31)
        self.path31.grid(column = 0, row = 1, padx = (20, 0), pady = 10, sticky = "w")

        #button 31
        self.button31 = ttk.Button(self.labelFrame3, text = "Browse File", command=self.fileDialog31)
        self.button31.grid(column = 1, row = 1, padx = (0, 20), pady = 10, sticky = "w")
        #TAB 3 ----SECTION 2------------------------------------------------------------------------------
  
       #label 32
        self.label32 = ttk.Label(self.labelFrame3, text="Click button to start recycling:")
        self.label32.grid(column = 0, row = 2, sticky = "w", padx = 20, pady = (20, 0) )
        
        #button no 32
        self.button32 = ttk.Button(self.labelFrame3, text = "START PROCESS", command=self.processText3)
        self.button32.grid(column = 0, row = 3, padx = 20, pady = (0, 20) )


    #----------------------------------------------------------------------
    #STARTING TAB 4 FUNCTIONS AND GUID ELEMENTS
    #----------------------------------------------------------------------

    def fileDialog41(self):
        self.filename41 = filedialog.askopenfilename(initialdir = "E:/FULLTEXT/DICTIONARY/LOWERCASE", 
            title = "Select standard word list", filetypes = (("Text files", "*.txt"), ("all files", "*.*")))
        if (self.filename41):
            self.filepath41.set(self.filename41) #set the textbox to the file path
            cf = config_handler.ConfigHandler()
            cf.set_config_value(cf.RECENT_OPEN_FILE,self.filename41)

    def fileDialog42(self):
        self.filename42 = filedialog.askopenfilename(initialdir = "E:/FULLTEXT/DICTIONARY/LOWERCASE", 
            title = "Select custom word list", filetypes = (("Text files", "*.txt"), ("all files", "*.*")))
        if (self.filename42):
            self.filepath42.set(self.filename42) 
            cf = config_handler.ConfigHandler()
            cf.set_config_value(cf.RECENT_OPEN_FILE2,self.filename42)

    def dirDialog43(self):
        self.filename43 = filedialog.askdirectory()
        if (self.filename43):
            self.filepath43.set(self.filename43)
            cf = config_handler.ConfigHandler()
            cf.set_config_value(cf.RECENT_OUTPUT_DIR3,self.filename43)


    def createTab4(self):

        #TAB 4 ----SECTION 0------------------------------------------------------------------------------
        self.labelFrame4 = ttk.LabelFrame(self.tab4, text= "Word-List Paths",  borderwidth = 1,  relief="raised")
        self.labelFrame4.grid(column=0, row=0, padx = 20, pady = 20)    

        #TAB 4 ----SECTION 1------------------------------------------------------------------------------
        #label 41
        self.label41 = ttk.Label(self.labelFrame4, text="Standard Word List:")
        self.label41.grid(column = 0, row = 0,  padx = 20, pady = 0, sticky = "w")


        #textbox 41
        self.filepath41 = tk.StringVar()
        #load defaults
        cf = config_handler.ConfigHandler()
        value = cf.get_config_value(cf.RECENT_OPEN_FILE)
        self.filepath41.set(value)
        s = ttk.Style()
        s.configure('TEntry', font = ('Courier', 24), padding = 4)


        self.path41 = ttk.Entry(self.labelFrame4, width=90, textvariable = self.filepath41)
        self.path41.grid(column = 0, row = 1, padx = (20, 0), pady = 10, sticky = "w")

        #button 41
        self.button41 = ttk.Button(self.labelFrame4, text = "Browse File", command=self.fileDialog41)
        self.button41.grid(column = 1, row = 1, padx = (0, 20), pady = 10, sticky = "w")

        #TAB 4 ----SECTION 2------------------------------------------------------------------------------
        #label 42
        self.label42 = ttk.Label(self.labelFrame4, text="Custom Word List:")
        self.label42.grid(column = 0, row = 2,  padx = 20, pady = 0, sticky = "w")

        #textbox 42
        self.filepath42 = tk.StringVar()
        #load defaults
        cf = config_handler.ConfigHandler()
        value = cf.get_config_value(cf.RECENT_OPEN_FILE2)
        self.filepath42.set(value)


        self.path42 = ttk.Entry(self.labelFrame4, width=90, textvariable = self.filepath42)
        self.path42.grid(column = 0, row = 3, padx = (20, 0) , pady = 10, sticky = "w")

        #button 41
        self.button42 = ttk.Button(self.labelFrame4, text = "Browse File", command=self.fileDialog42)
        self.button42.grid(column = 1, row = 3, padx = (0,20), pady = 10, sticky = "w")
        
        #TAB 4 ----SECTION 3------------------------------------------------------------------------------
        #label 43
        self.label43 = ttk.Label(self.labelFrame4, text="Select recyle folder:")
        self.label43.grid(column = 0, row = 4,  padx = 20, pady = 0, sticky = "w")
        
        self.filepath43 = tk.StringVar()
        #load config value
        cf = config_handler.ConfigHandler()
        value = cf.get_config_value(cf.RECENT_OUTPUT_DIR3)
        self.filepath43.set(value) 
        self.path43 = ttk.Entry(self.labelFrame4, width=90, textvariable = self.filepath43)
        self.path43.grid(column = 0, row = 5, sticky = "w", padx=(20, 0), pady = 20)
        
        #button 43
        self.button43 = ttk.Button(self.labelFrame4, text = "Browse Folder", command=self.dirDialog43)
        self.button43.grid(column = 1, row = 5, sticky = "w", padx = (0, 20), pady = 20)



    def createGUI(self):
        self.createTabs()    
        self.createTab1()
        self.createTab2()
        self.createTab3()
        self.createTab4()
   