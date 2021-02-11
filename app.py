from tkinter import *
root = Tk()

# send button functionality
def send():
    send="Me => "+e.get()
    txt.insert(END,"\n"+send)
    
    # Adding replyies to chatbot
    if(e.get()=='Hello'):
        txt.insert(END,"\n" + "Clair => Welcome to Clare The Chatbot")
        txt.insert(END,"\n" + "Clair => How can I assist?")
    elif(e.get()=='hello'):
        txt.insert(END,"\n" + "Clair => Welcome to Clare The Chatbot")
        txt.insert(END,"\n" + "Clair => How can I assist?")
    elif(e.get()=='Greetings Clair'):
        txt.insert(END,"\n" + "Clair => Heyyyy Orion.... what's up?")
    elif(e.get()=='Greetings'):
        txt.insert(END,"\n" + "Clair => Heyyyy Orion.... what's up?")
    elif(e.get()=='greetings clair'):
        txt.insert(END,"\n" + "Clair => Heyyyy Orion.... what's up?")
    elif(e.get()=='Clair'):
        txt.insert(END,"\n" + "Clair => How can I help? Are you ok?")
    e.delete(0,END)
    
txt=Text(root)
txt.grid(row=0, column=0, columnspan=2)
root.title('Clair The Chatbot')
e=Entry(root, width=100)
send=Button(root, text="Send", command=send).grid(row=1,column=1)
e.grid(row=1,column=0)
root.mainloop()



