from tkinter import *

root = Tk()

root.title("Fibonacci")
root.geometry("400x400")

label_series = Label(root, text="Fibonacci Series:     ")
label_flower = Label(root)
label_spiral = Label(root)



def Fibonacci():
    num = int(Entry(root))
    no1 = 0
    no2 = 1
    sum = 0
    count = 1
    while (count <= num):
        label_series["text"] += str(sum) + " "
        count = count + 1
        no1 = no2
        no2 = sum
        sum = no1 + no2
    label_flower["text"] = "Flower is fully bloomed."
    label_spiral["text"] = "Sprials in the right direction are " + str(no1) + " and spirals in the left direction are " + str(no2) + "\n. Total number of spirals are " + str(sum)
    
btn = Button(root, text="Show Fibonacci series", command=Fibonacci)
btn.pack()
label_series.pack()
label_flower.pack()
label_spiral.pack()

root.mainloop()
 
