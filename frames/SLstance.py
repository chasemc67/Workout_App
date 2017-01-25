import tkinter as tk

from buttons.NextButton import NextButton
from buttons.BackButton import BackButton
from buttons.QuitButton import QuitButton

class SLstance(tk.Frame):

   def focus_next_window(self, event):
       event.widget.tk_focusNext().focus()
       return("break")

   def focus_last_window(self, event):
       event.widget.tk_focusPrev().focus()
       return("break")

   def __init__(self, parent, controller):
       tk.Frame.__init__(self, parent)
       self.controller = controller

       self.SLStance = tk.Label(self)
       self.SLStance["text"] = "Single Leg Stance Test"
       self.SLStance.grid(row=0, column=0)

       self.SLOpenLeft = tk.Label(self)
       self.SLOpenLeft["text"] = "Eyes Open Left(sec.): "
       self.SLOpenLeft.grid(row=1, column=0)

       self.SLOpenLeftText = tk.Text(self)
       self.SLOpenLeftText["height"] = 1
       self.SLOpenLeftText["width"] = 5
       self.SLOpenLeftText.bind("<Tab>", self.focus_next_window)
       self.SLOpenLeftText.bind("<Shift-Tab>", self.focus_last_window)
       self.SLOpenLeftText.grid(row=1, column=1)

       self.SLOpenRight = tk.Label(self)
       self.SLOpenRight["text"] = "Eyes Open Right(sec.): "
       self.SLOpenRight.grid(row=1, column=2)

       self.SLOpenRightText = tk.Text(self)
       self.SLOpenRightText["height"] = 1
       self.SLOpenRightText["width"] = 5
       self.SLOpenRightText.bind("<Tab>", self.focus_next_window)
       self.SLOpenRightText.bind("<Shift-Tab>", self.focus_last_window)
       self.SLOpenRightText.grid(row=1, column=3)

       self.SLCloseLeft = tk.Label(self)
       self.SLCloseLeft["text"] = "Eyes Closed Left(sec.): "
       self.SLCloseLeft.grid(row=2, column=0)

       self.SLCloseLeftText = tk.Text(self)
       self.SLCloseLeftText["height"] = 1
       self.SLCloseLeftText["width"] = 5
       self.SLCloseLeftText.bind("<Tab>", self.focus_next_window)
       self.SLCloseLeftText.bind("<Shift-Tab>", self.focus_last_window)
       self.SLCloseLeftText.grid(row=2, column=1)

       self.SLCloseRight = tk.Label(self)
       self.SLCloseRight["text"] = "Eyes Closed Right(sec.): "
       self.SLCloseRight.grid(row=2, column=2)

       self.SLCloseRightText = tk.Text(self)
       self.SLCloseRightText["height"] = 1
       self.SLCloseRightText["width"] = 5
       self.SLCloseRightText.bind("<Tab>", self.focus_next_window)
       self.SLCloseRightText.bind("<Shift-Tab>", self.focus_last_window)
       self.SLCloseRightText.grid(row=2, column=3)

       self.Next = NextButton(self, controller, self.saveData)
       self.Next.grid(row=3, column=0)

       self.Back = BackButton(self, controller)
       self.Back.grid(row=3, column=1)

       self.Quit = QuitButton(self, controller)
       self.Quit.grid(row=3, column=2)

   def loadData(self, person):

       self.SLOpenLeftText.delete(1.0, tk.END)
       self.SLOpenLeftText.insert(tk.END, person.SLOpenLeft)

       self.SLOpenRightText.delete(1.0, tk.END)
       self.SLOpenRightText.insert(tk.END, person.SLOpenRight)

       self.SLCloseLeftText.delete(1.0, tk.END)
       self.SLCloseLeftText.insert(tk.END, person.SLCloseLeft)

       self.SLCloseRightText.delete(1.0, tk.END)
       self.SLCloseRightText.insert(tk.END, person.SLCloseRight)

   def saveData(self, person):
       person.SLOpenLeft = self.SLOpenLeftText.get(1.0, tk.END)
       person.SLOpenRight = self.SLOpenRightText.get(1.0, tk.END)
       person.SLCloseLeft = self.SLCloseLeftText.get(1.0, tk.END)
       person.SLCloseRight = self.SLCloseRightText.get(1.0, tk.END)
