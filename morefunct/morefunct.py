try:
    import tkinter
except ImportError:
    import Tkinter as tkinter


def parabola(x):
    y = x * x / 100
    return y


def draw_axis(canvas):  # in real life, try to keep local and global variables differently named
    canvas.update()
    x_origin = canvas.winfo_width() / 2
    y_origin = canvas.winfo_height() / 2
    canvas.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))
    canvas.create_line(-x_origin, 0, x_origin, 0, fill="red")
    canvas.create_line(0, y_origin, 0, -y_origin, fill="red")
    print(locals())


def plot(canvas, x, y):
    canvas.create_line(x, y, x + 1, y + 1, fill="white")


main_window = tkinter.Tk()

main_window.title("Parabola")
main_window.geometry("640x480")

canvas = tkinter.Canvas(main_window, width=320, height=480)
canvas.grid(row=0, column=0)

canvas2 = tkinter.Canvas(main_window, width=320, height=480, background="blue")
canvas2.grid(row=0, column=1)



draw_axis(canvas)
draw_axis(canvas2)


for x in range(-100, 100):
    y = parabola(x)
    plot(canvas, x, -y)

main_window.mainloop()