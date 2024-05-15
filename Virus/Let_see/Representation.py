import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

# create a new CustomTkinter window
root = tk.Tk()

# create a new figure
fig = Figure(figsize=(5, 4), dpi=100)

# create a subplot
ax = fig.add_subplot(111)

# define the data to be plotted
x = ['A', 'B', 'C', 'D']
y = [3, 5, 2, 7]

# create a bar graph
ax.bar(x, y)

# set the axis labels and title
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_title('Bar Graph')

# create a canvas to display the graph in the CustomTkinter window
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack()

# run the CustomTkinter event loop
tk.mainloop()
