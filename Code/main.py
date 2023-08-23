import os
import keras
import customtkinter
import numpy as np
from PIL import ImageTk, Image
from tkinter import filedialog
import tkinter as tk

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Autism Detection")
        self.geometry("800x400")
        self.grid_columnconfigure((0,2), weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame1 = customtkinter.CTkFrame(master=self)
        self.frame1.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsew", )

        self.frame2 = customtkinter.CTkFrame(master=self)
        self.frame2.grid(row=0, column=2, padx=10, pady=(10, 0), sticky="nsew",rowspan=4)
        self.frame2.configure(fg_color="transparent")

        self.logo = customtkinter.CTkImage(light_image=Image.open("AUTISM DETECTION-.png"),
                                           dark_image=Image.open("AUTISM DETECTION-.png"),
                                           size=(120, 120))
        self.label1 = customtkinter.CTkLabel(master=self.frame2, image=self.logo, text="")
        self.label1.pack()

        self.label2 = customtkinter.CTkLabel(master=self.frame2, text="The driving force behind this project is\n"\
                                                                      "a deep-seated desire to enhance care \n"\
                                                                      "and awareness for autistic.", width=250,
                                                                      font=('Century Gothic', 12), justify="center")
        self.label2.pack(pady=10)

        self.label3 = customtkinter.CTkLabel(master=self.frame2, text="Upload the image of your child, and the \n"\
                                                                      "model will detect if the child has any signs \n"\
                                                                      "of autism.", width=250,
                                             font=('Century Gothic', 12), justify="center")
        self.label3.pack(pady=10)

        self.label4 = customtkinter.CTkLabel(master=self.frame2, text="\n\nThe result will appear below: \n", width=250,
                                             font=('Century Gothic', 16), justify="center")
        self.label4.pack(pady=10)

        self.image = customtkinter.CTkImage(
            light_image=Image.open("Image.jpeg"),
            dark_image=Image.open("Image.jpeg"),
            size=(270, 270))

        self.image_label = customtkinter.CTkLabel(master=self.frame1, text="", image=self.image)
        self.image_label.pack(pady=50, padx=50)

        self.button = customtkinter.CTkButton(master=self, text="Upload", command=self.action)
        self.button.grid(row=3, column=0, padx=10, pady=10, sticky="ew", columnspan=2)

    def action(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
        if file_path:
            self.image= customtkinter.CTkImage(
                light_image=Image.open(file_path),
                dark_image=Image.open(file_path),
                size=(270, 270))
            self.image_label.configure(image=self.image)

            os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
            saved_model = keras.models.load_model("model7861.keras")

            img = keras.utils.load_img(file_path, target_size=(224, 224))

            input_arr = keras.utils.img_to_array(img)
            input_arr = np.array([input_arr])
            predict = saved_model.predict(input_arr)
            print(predict)
            predicted_label = 1 if predict < 0.5 else 0

            if predicted_label:
                self.label4.configure(text="\n\nThe result will appear below: \ntheir is signs of autistic")
            else:
                self.label4.configure(text="\n\nThe result will appear below: \nno signs")


app = App()
app.mainloop()
