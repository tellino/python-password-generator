def generate():
	pass_widget.config(state = "normal")
	pass_widget.delete(1.0, tk.END)
	password_choice = []
	
	if num_check.get():
		password_nums = "0123456789"
		for i in range(len(password_nums)):
			password_choice.append(password_nums[i])
	
	if char_check.get():
		password_char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
		for i in range(len(password_char)):
			password_choice.append(password_char[i])
	
	if spec_check.get():
		password_spec = "!£$%&/()=?^-_*+.,:;|"
		for i in range(len(password_spec)):
			password_choice.append(password_spec[i])
	

	password = ""
	try:
		for i in range(int(variable.get())):
			password += random.choice(password_choice)

	
	except IndexError:
		pass_widget.insert(tk.END, chars = "Select the type of characters.")

	
	pass_widget.insert(tk.END, chars = password)
	pass_widget.config(state = "disabled")





import tkinter as tk
import random

number_of_character = []

for i in range(33):
	number_of_character.append(str(i))

del number_of_character[0]

window = tk.Tk()
num_check = tk.IntVar()
char_check = tk.IntVar()
spec_check = tk.IntVar()

onvalue_1 = None
offvalue_1 = None
onvalue_2 = None
offvalue_2 = None
onvalue_3 = None
offvalue_3 = None



window.geometry("300x150")
window.title("Password Generator")
window.iconbitmap("icon.ico")
window.resizable(False, False)
window.configure(bg = "grey20")

num_tick = tk.Checkbutton(window, text = "Numbers", variable = num_check, bg = "grey20", bd = 0, fg = "grey99", selectcolor = "grey30", onvalue = onvalue_1, offvalue = offvalue_1) 
num_tick.place(x = 0, y = 0)

char_tick = tk.Checkbutton(window, text = "Characters", variable = char_check, bg = "grey20", bd = 0, fg = "grey99", selectcolor = "grey30", onvalue = onvalue_2, offvalue = offvalue_2)
char_tick.place(x = 0, y = 20)

spec_tick = tk.Checkbutton(window, text = "Special Characters", variable = spec_check, bg = "grey20", bd = 0, fg = "grey99", selectcolor = "grey30", onvalue = onvalue_2, offvalue = offvalue_2)
spec_tick.place(x = 0, y = 40)

pass_widget = tk.Text()
pass_widget.place(x = 15, y = 125, height = 20, width = 270)
pass_widget.config(state = "disabled")

generate_button = tk.Button(text = "GENERATE", bd = 0, fg = "green", font = ("Quinta", 12, "bold"), bg = "grey20", command = generate)
generate_button.place(x = 95, y = 100, height = 20, width = 110)

char_text = tk.Label(text = "Characters", bg = "grey20", fg = "grey99")
char_text.place(x = 190, y = 0)

variable = tk.StringVar()
variable.set(number_of_character[0])
option = tk.OptionMenu(window, variable, *number_of_character)
option.place(x = 253, y = 0, height = 20, width = 47)


window.mainloop()