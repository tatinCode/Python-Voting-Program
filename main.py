#
#
#   This program simulates a voting application
#   using tkinter and makes a gui interface
#
#
import tkinter
import tkinter.messagebox
import tkinter.font

class Voter:
    def __init__(self):
        self.main_window = tkinter.Tk()

        #the fonts
        myfont = tkinter.font.Font(family = 'Times', size = 20, weight = 'bold')
        myfont2 = tkinter.font.Font(family = 'Times', size = 15, weight = 'bold')

        #Create the frames
        self.myName_frame = tkinter.Frame(self.main_window)
        self.id_frame = tkinter.Frame(self.main_window)
        self.name_frame =  tkinter.Frame(self.main_window)
        self.radio_frame = tkinter.Frame(self.main_window)
        self.check_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)

        #Create and pack the widgets for id number
        self.myName_label = tkinter.Label(self.myName_frame, \
                            text = "Tenorio's Suffrage Software", \
                            font = myfont)
        self.myName_label.pack(side = 'left')
        
        self.id_label = tkinter.Label(self.id_frame, \
                        text = 'Enter Your ID Number:',\
                        font = myfont)
        self.id_entry = tkinter.Entry(self.id_frame, \
                                      width = 20, font = myfont2)
        self.id_label.pack(side = 'left')
        self.id_entry.pack(side = 'left')

        #Create and pack the widgets for name box
        self.name_label = tkinter.Label(self.name_frame, \
                            text = 'Enter your Name:', \
                            font = myfont)
        self.name_entry = tkinter.Entry(self.name_frame, \
                                        width = 20, font = myfont2)
        self.name_label.pack(side = 'left')
        self.name_entry.pack(side = 'left')

        #Create an IntVar object to use with
        #the radiobuttons
        self.radio_var = tkinter.IntVar()

        #Set the intvar object to
        self.radio_var.set(0)

        #Create the radiobutton widgets
        self.rb_yes = tkinter.Radiobutton(self.radio_frame, \
                        text = 'In Favor Prop A', variable = self.radio_var, \
                        font = myfont, value = 1)
        self.rb_no = tkinter.Radiobutton(self.radio_frame, \
                        text = 'Against Prop A', variable = self.radio_var, \
                        font = myfont, value = 2)

        #Packs the radiobuttons
        self.rb_yes.pack()
        self.rb_no.pack()

        #Create three IntVar objects to use with checkbuttons
        self.cb_varB = tkinter.IntVar()
        self.cb_varC = tkinter.IntVar()

        #Set the intVar objects to 0
        self.cb_varB.set(0)
        self.cb_varC.set(0)

        #Create the checbutton widgets in the top_frame
        self.cbB = tkinter.Checkbutton(self.check_frame,\
                                       text = 'Candidate B', \
                                       variable = self.cb_varB, \
                                       font = myfont)
        self.cbC = tkinter.Checkbutton(self.check_frame, \
                                       text = 'CandidateC', \
                                       variable = self.cb_varC, \
                                       font = myfont)

        #Pack the checkbuttons
        self.cbB.pack()
        self.cbC.pack()

        #Create and pack the button widgets
        self.vote_button = tkinter.Button(self.button_frame, \
                                          text = 'Your Vote', font = myfont, \
                                          command = self.cast_vote)
        self.quit_button = tkinter.Button(self.button_frame, \
                                          text = 'Cast Vote and Quit', font = myfont, \
                                          command = self.main_window.destroy)
        self.vote_button.pack(side = 'left')
        self.quit_button.pack(side = 'left')

        #Pack the frames
        self.myName_frame.pack()
        self.id_frame.pack()
        self.name_frame.pack()
        self.radio_frame.pack()
        self.check_frame.pack()
        self.button_frame.pack()

        #Start the main loop
        tkinter.mainloop()

    #Displays the result window
    def cast_vote(self):
        prop_A = self.radio_var.get()
        self.textBox = "You didn't vote on Proposition A"

        if prop_A == 1:
            self.textBox = 'You voted for Proposition A'
        elif prop_A ==2:
            self.textBox = 'You voted against Proposition A'

        if self.cb_varB.get() == 1:
            self.textBox = self.textBox + ' and you voted for candidate B.'
        if self.cb_varC.get() == 1:
            self.textBox = self.textBox + ' and you voted for candidate C.'
        if self.cb_varB.get() == 1 and self.cb_varC.get() == 1:
            self.textBox = 'You can only vote for one of the two candidates!'

        tkinter.messagebox.showinfo('Selection', self.textBox)

voter = Voter()
