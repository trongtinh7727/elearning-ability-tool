__version__ = '0.1.0'
from time import sleep
import webbrowser
from selenium import webdriver
import sys
import os
import tkinter as tk
import tkinter.filedialog
from pathlib import Path
import lib as account
window = tk.Tk()
# Path to asset files for this GUI window.
ASSETS_PATH = Path(__file__).resolve().parent / "assets"

# Required in order to add data files to Windows executable
path = getattr(sys, '_MEIPASS', os.getcwd())
os.chdir(path)

output_path = ""


def btn_clicked():
    chrome_options = webdriver.ChromeOptions()
    prefs = {
        "profile.managed_default_content_settings.images": 1
    }
    chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(
        executable_path="C:\elearning_ability_tool\chromedriver.exe", options=chrome_options)

    user = username_entry.get()
    pwd = "'" + password_entry.get() + "'"
    url = class_entry.get()

    if not user:
        tk.messagebox.showerror(
            title="Empty Fields!", message="Please enter User.")
        return
    if not pwd:
        tk.messagebox.showerror(
            title="Empty Fields!", message="Please enter User.")
        return
    if not url:
        tk.messagebox.showerror(
            title="Empty Fields!", message="Please enter URL.")
        return
    account.login(driver, user, pwd)
    account.lessonSkip(driver, url)

    tk.messagebox.showinfo(
        "Success!", f"Successfully!.")


def btn_cookie():
    chrome_options = webdriver.ChromeOptions()
    prefs = {
        "profile.managed_default_content_settings.images": 1
    }
    chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(
        executable_path="C:\elearning_ability_tool\chromedriver.exe", options=chrome_options)
    url = class_entry.get()

    if not url:
        tk.messagebox.showerror(
            title="Empty Fields!", message="Please enter URL.")
        return
    account.loginCookie(driver)
    sleep(0.5)
    account.lessonSkip(driver, url)

    tk.messagebox.showinfo(
        "Success!", f"Successfully!.")


def know_more_clicked(event):
    instructions = (
        "https://github.com/trongtinh7727/elearning-ability-tool/issues")
    webbrowser.open_new_tab(instructions)


def make_label(master, x, y, h, w, *args, **kwargs):
    f = tk.Frame(master, height=h, width=w)
    f.pack_propagate(0)  # don't shrink
    f.place(x=x, y=y)
    label = tk.Label(f, *args, **kwargs)
    label.pack(fill=tk.BOTH, expand=1)
    return label


def destroy():
    canvas.delete('all')
    generate_btn.destroy()
    username_entry.destroy()
    password_entry.destroy()
    loginBY.destroy()


def restart_program(event):
    python = sys.executable
    os.execl(python, python, * sys.argv)


def login_token(event):
    destroy()
    canvas.place(x=0, y=0)
    canvas.create_rectangle(431, 0, 431 + 431, 0 + 519,
                            fill="#FCFCFC", outline="")
    canvas.create_rectangle(40, 160, 40 + 60, 160 + 5,
                            fill="#FCFCFC", outline="")

    canvas.create_text(
        490.0, 156.0+60, text="Class URL", fill="#515486",
        font=("Arial-BoldMT", int(13.0)), anchor="w")

    canvas.create_text(
        646.5, 428.5+60, text="Generate",
        fill="#FFFFFF", font=("Arial-BoldMT", int(13.0)))
    canvas.create_text(
        573.5, 88.0, text="Enter the details.",
        fill="#515486", font=("Arial-BoldMT", int(22.0)))

    generate_btn = tk.Button(
        image=generate_btn_img, borderwidth=0, highlightthickness=0,
        command=btn_cookie, relief="flat")
    class_entry.place(x=490.0, y=137+25+60, width=321.0, height=35)
    generate_btn.place(x=557, y=200+60, width=180, height=55)

    loginBY = tk.Label(
        text="Click here for login by account.",
        bg="#FFFFFF", fg="black", cursor="hand2")
    loginBY.place(x=557, y=200+60+60)
    loginBY.bind('<Button-1>', restart_program)


if __name__ == '__main__':

    logo = tk.PhotoImage(file=ASSETS_PATH / "iconbitmap.gif")
    window.call('wm', 'iconphoto', window._w, logo)
    window.title("Elearning ability")

    window.geometry("862x519")
    window.configure(bg="#3A7FF6")
    canvas = tk.Canvas(
        window, bg="#3A7FF6", height=519, width=862,
        bd=0, highlightthickness=0, relief="ridge")
    canvas.place(x=0, y=0)
    canvas.create_rectangle(431, 0, 431 + 431, 0 + 519,
                            fill="#FCFCFC", outline="")
    canvas.create_rectangle(40, 160, 40 + 60, 160 + 5,
                            fill="#FCFCFC", outline="")

    text_box_bg = tk.PhotoImage(file=ASSETS_PATH / "TextBox_Bg.png")
    username_entry_img = canvas.create_image(650.5, 167.5, image=text_box_bg)
    password_entry_img = canvas.create_image(650.5, 248.5, image=text_box_bg)

    username_entry = tk.Entry(bd=0, bg="#F6F7F9", highlightthickness=0)
    username_entry.place(x=490.0, y=137+25, width=321.0, height=35)
    username_entry.focus()
    password_entry = tk.Entry(bd=0, bg="#F6F7F9", highlightthickness=0)
    password_entry.place(x=490.0, y=218+25, width=321.0, height=35)

    class_entry_img = canvas.create_image(650.5, 329.5, image=text_box_bg)
    class_entry = tk.Entry(bd=0, bg="#F6F7F9", highlightthickness=0)
    class_entry.place(x=490.0, y=299+25, width=321.0, height=35)

    canvas.create_text(
        490.0, 234.5+81, text="Class URL", fill="#515486",
        font=("Arial-BoldMT", int(13.0)), anchor="w")
    canvas.create_text(
        490.0, 156.0, text="Username", fill="#515486",
        font=("Arial-BoldMT", int(13.0)), anchor="w")
    canvas.create_text(
        490.0, 234.5, text="Password", fill="#515486",
        font=("Arial-BoldMT", int(13.0)), anchor="w")

    canvas.create_text(
        646.5, 428.5, text="Generate",
        fill="#FFFFFF", font=("Arial-BoldMT", int(13.0)))
    canvas.create_text(
        573.5, 88.0, text="Enter the details.",
        fill="#515486", font=("Arial-BoldMT", int(22.0)))

    title = tk.Label(
        text="Elearning ability", bg="#3A7FF6",
        fg="white", font=("Arial-BoldMT", int(20.0)))
    title.place(x=27.0, y=120.0)

    info_text = tk.Label(
        text="A special tool for TDTUers.\n"
        "Just used, don't share!!",
        bg="#3A7FF6", fg="white", justify="left",
        font=("Georgia", int(16.0)))

    info_text.place(x=27.0, y=200.0)

    know_more = tk.Label(
        text="Click here for instructions",
        bg="#3A7FF6", fg="white", cursor="hand2")
    know_more.place(x=27, y=400)
    know_more.bind('<Button-1>', know_more_clicked)

    global loginBY
    loginBY = tk.Label(
        text="Click here for login by token.",
        bg="#FFFFFF", fg="black", cursor="hand2")
    loginBY.place(x=557, y=403+60)
    loginBY.bind('<Button-1>', login_token)

    generate_btn_img = tk.PhotoImage(file=ASSETS_PATH / "generate.png")
    generate_btn = tk.Button(
        image=generate_btn_img, borderwidth=0, highlightthickness=0,
        command=btn_clicked, relief="flat")
    generate_btn.place(x=557, y=401, width=180, height=55)
    window.resizable(False, False)
    window.mainloop()
