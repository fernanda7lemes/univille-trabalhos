from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, messagebox
import webbrowser

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\GEOvendas\Downloads\projeto-tk\imagens")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()

window.geometry("1280x720")
window.configure(bg="#FF8981")

canvas = Canvas(
    window,
    bg="#FF8981",
    height=720,
    width=1280,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)
canvas.create_rectangle(
    0.0,
    694.0,
    1280.0,
    721.0,
    fill="#8E2018",
    outline=""
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    635.0,
    329.0,
    image=image_image_1
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    927.5,
    288.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFF8E6",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=763.5,
    y=268.0,
    width=328.0,
    height=39.0
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    927.5,
    362.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFF8E6",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=763.5,
    y=342.0,
    width=328.0,
    height=39.0
)
entry_1.config(show="*")

def show_new_screen():
    for widget in window.winfo_children():
        widget.destroy()

    window.configure(bg="#FF8981")

    def abrir_link():
        webbrowser.open('https://www.univille.edu.br/')

    canvas = Canvas(
        window,
        bg="#FF8981",
        height=720,
        width=1280,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    canvas.place(x=0, y=0)

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    canvas.image_image_2 = image_image_2
    image_2 = canvas.create_image(
        640.0,
        360.0,
        image=image_image_2
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    canvas.button_image_3 = button_image_3
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=abrir_link,
        relief="flat"
    )
    button_3.place(
        x=130.0,
        y=207.0,
        width=131.0,
        height=31.0
    )

    canvas.create_rectangle(
        0.0,
        694.0,
        1280.0,
        721.0,
        fill="#8E2018",
        outline=""
    )

    window.resizable(False, False)

def logar():
    print('clicked')

    key = entry_1.get()
    user = entry_2.get()

    if user != 'aluno' or key != '123':
        if key == '' or user == '':
            messagebox.showerror(
                title='Erro', message='Campo(s) obrigatório(s) não preenchido(s)!')
        elif key != '123' and user == 'aluno':
            messagebox.showerror(
                title='Erro', message='Senha inválida!')
        elif key == '123' and user != 'aluno':
            messagebox.showerror(
                title='Erro', message='Usuário inválido!')
        else:
            messagebox.showerror(
                title='Erro', message='Usuário e senha inválidos!')
    else:
        messagebox.showinfo(
            title='Sucesso!', message='Login efetuado.')
        show_new_screen()

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=logar,
    relief="flat"
)
button_1.place(
    x=743.0,
    y=417.0,
    width=369.0,
    height=39.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print('button2 clicked'),
    relief="flat"
)
button_2.place(
    x=743.0,
    y=475.0,
    width=369.0,
    height=39.0
)

canvas.create_text(
    756.0,
    242.0,
    anchor="nw",
    text="Usuário",
    fill="#828282",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    756.0,
    316.0,
    anchor="nw",
    text="Senha",
    fill="#828282",
    font=("Inter", 16 * -1)
)

window.resizable(False, False)
window.mainloop()
