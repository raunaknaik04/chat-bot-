from tkinter import *
import openai

# Set your OpenAI API key here
openai.api_key = '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'

# Function to handle user input and generate responses
def send():
    message = entry.get()
    if message.strip():
        txt.config(state=NORMAL)
        txt.insert(END, "You: " + message + "\n")
        txt.config(state=DISABLED)
        entry.delete(0, END)

        # Call the OpenAI API to generate responses
        response = generate_response(message)

        txt.config(state=NORMAL)
        txt.insert(END, "Bot: " + response + "\n")
        txt.config(state=DISABLED)

# Function to generate responses using the OpenAI GPT-3 API
def generate_response(message):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=message,
        max_tokens=50
    )
    return response.choices[0].text

root = Tk()
root.title("Chatbot")

# Define colors and fonts
BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"
FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

# Create UI elements
label = Label(root, bg=BG_COLOR, fg=TEXT_COLOR, text="Welcome", font=FONT_BOLD, pady=10)
label.grid(row=0, column=0, columnspan=2)

txt = Text(root, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, height=10, width=40)
txt.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
txt.config(state=DISABLED)  # Disable the Text widget initially

scrollbar = Scrollbar(root, command=txt.yview)
scrollbar.grid(row=1, column=2, sticky="ns")
txt.config(yscrollcommand=scrollbar.set)

entry = Entry(root, bg="white", fg="black", font=FONT, width=30)
entry.grid(row=2, column=0, padx=10, pady=10)

send_button = Button(root, text="Send", font=FONT_BOLD, bg=BG_GRAY, command=send)
send_button.grid(row=2, column=1, padx=10, pady=10)

root.geometry("600x400")  # Set the window dimensions

root.mainloop()