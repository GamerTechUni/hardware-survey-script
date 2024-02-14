import subprocess
import platform
import os
import uuid
import tkinter as tk
from tkinter import messagebox

MACHINE_ID = uuid.getnode()


def grab_hardware_info():
    output_file = f"output-{MACHINE_ID}.doc"
    try:
        with open(output_file, 'w', encoding="utf-8") as f:
            print(MACHINE_ID, file=f)
            print(f"{platform.system()} \n", file=f)
            x = subprocess.run(['inxi', '-Fx'], capture_output=True,
                               check=True, text=True)
            print(x.stdout, file=f)
            messagebox.showinfo(
                message=f"The information has been collected successfully!\nFile has been saved to: {os.path.abspath(output_file)}", title="Success!")
    except subprocess.CalledProcessError:
        print("That command wasn't found")
        messagebox.showerror(
            message="Couldn't collect information\n Maybe the inxi script isn't installed. \n Check the README.md on Github:\n https://github.com/GamerTechUni/hardware-survey-script", title="Failed to collect info. ")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Hardware Info Program")
    program_label = tk.Label(root, font=('Arial', 30),
                             text="Hardware Info Program")
    program_label.pack()
    empty_label = tk.Label(
        root, text="Click the button below to collect system information")
    empty_label.pack()
    start_button = tk.Button(root, text="Start",
                             command=grab_hardware_info)
    start_button.pack()
    root.mainloop()
