# import tkinter as tk
# from PIL import Image

# root = tk.Tk()
# root.title("Displaing Gif")
# root.config(bg = 'gray12')
# file = "D:\\loading-loading-forever.gif"
# info = Image.open(file)

# frames = info.n_frames  # number of frames

# photoimage_objects = []
# for i in range(frames):
#     obj = tk.PhotoImage(file=file, format=f"gif -index {i}")
#     photoimage_objects.append(obj)


# def animation(current_frame=0):
#     global loop
#     image = photoimage_objects[current_frame]

#     gif_label.configure(image=image)
#     current_frame = current_frame + 1

#     if current_frame == frames:
#         current_frame = 0

#     loop = root.after(50, lambda: animation(current_frame))


# def stop_animation():
#     root.after_cancel(loop)


# gif_label = tk.Label(root, image="", bg = 'gray12')
# gif_label.pack()

# start = tk.Button(root, text="Start", command=lambda: animation(current_frame=0))
# start.pack()

# stop = tk.Button(root, text="Stop", command=stop_animation)
# stop.pack()

# root.mainloop()

print('иди нахуй'.count('нах'))

# response = requests.get('https://raw.githubusercontent.com/danakt/russian-words/master/russian.txt')

# text = response.content.decode('cp1251')

# with open('russian.txt', 'wb') as ru:
#     ru.write(text.encode('utf-8'))

# response = requests.get('https://raw.githubusercontent.com/danakt/russian-words/master/russian_surnames.txt')

# text = response.content.decode('cp1251')

# with open('russian_surnames.txt', 'wb') as ru:
#     ru.write(text.encode('utf-8'))