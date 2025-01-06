import tkinter as tk

window = tk.Tk()
window.title("Python Wordle")
window.geometry('600x200')

def getInput():
    inputValue=text.get("1.0", "end-1c")
    print(inputValue)
    return inputValue

def checkInput(inputValue, word):
    listWord = list(word)
    listVal = list(inputValue)

    result = ['','','','','']

    for i in range(5):
        if (listWord[i] == listVal[i]):
            result[i] = '+'
        else:
            result[i] = '!'
    
    result = "".join(result)

    if (result == "+++++"):
        print("Congratulations!")
        return "Congratulations!"

    return result

copylabel = tk.Label(window, text="")

label = tk.Label(window, text="Check your letters!")
text = tk.Text(window, height=1, width=10)
button = tk.Button(window, text="Submit", command=lambda: copylabel.configure(text=checkInput(getInput(), "stair")))

label.pack()
text.place(x=255, y=100)
button.place(x=265, y=150)
copylabel.pack()

window.mainloop()
