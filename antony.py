import beepy as beep
import tkinter as tk
import base64


def get_check_ans():
    global question_num
    
    if question_num == 1:
        encoded='''Y2hhcmxpZQ=='''
        answer = base64.b64decode(encoded).decode()
    elif question_num == 2:
        encoded='''bmVv'''
        answer = base64.b64decode(encoded).decode()
    elif question_num == 3:
        encoded='''bWF0cml4'''
        answer = base64.b64decode(encoded).decode()
    
    guess = inputtxt.get(1.0, "end-1c")

    if guess.lower() == answer:
        if question_num == 1:
            lbl2.config(text = "Congratulations.... \n\nNEXT TASK : Get the keyword from the video played")
            inputtxt.delete('1.0', tk.END)
            question_num += 1
        elif question_num == 2:
            lbl2.config(text = "Congratulations.... \n\nDecode the 4 digit number from the image provided")
            inputtxt.delete('1.0', tk.END)
            question_num += 1
        elif question_num == 3:
            lbl2.config(text = "Congratulations.... \n\nPlay the Mario game :)")
            inputtxt.delete('1.0', tk.END)

            
    else:
        lbl2.config(text = "Uh-Oh :( \n Wrong Answer")
        for i in range(1,10): 
            beep.beep(3)
    
    print(answer)

question_num = 1

frame = tk.Tk()
frame.title("Answer Me :)")
frame.geometry('1500x800')

lbl1 = tk.Label(frame, text = "For the first task the clue is provided on the card, decode the code and enter in the prompt.(use lower case only)")
lbl1.pack()


inputtxt = tk.Text(frame,
                   height = 5,
                   width = 20,
                   )
  
inputtxt.pack()
  
printButton = tk.Button(frame,
                        text = "Submit", 
                        command=get_check_ans
                       )
printButton.pack()

lbl2 = tk.Label(frame, text = "")
lbl2.pack()

'''lbl3 = tk.Label(frame, text = "What is the capital of France?")
lbl4 = tk.Label(frame, text = "What is the name of the AI research organization that developed me?")'''

frame.mainloop()