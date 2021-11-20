from tkinter import Tk,Menu,filedialog,Label,messagebox
from PIL import Image, ImageTk,ImageGrab
import os

def open_file():
    filetypes = (
        ('Jpeg', '*.jpg'),
        ('Png', '*.png')
    )
    filename = filedialog.askopenfilename(parent=tk,initialdir=os.getcwd(),filetypes=filetypes)
    img = Image.open(filename)
    imgwidth, imgheight = img.size
    if imgheight > 800 or imgwidth > 500:
        chkheight=imgheight//800
        chkweight=imgwidth//500
        img = img.resize((imgwidth//chkheight, imgheight//chkheight)) if chkheight > chkweight else img.resize((imgwidth//chkweight,imgheight//chkweight ))

    if 'watermark' in filename:
        inputImage.inputImg(img,watermark=True)
    else:
        inputImage.inputImg(img)

def save_file():
    filetypes = (
        ('Jpeg', '*.jpg'),
        ('Png', '*.png')
    )
    filename=filedialog.asksaveasfile(mode='w',defaultextension=".png",filetypes=filetypes)
    if filename:
        x = tk.winfo_rootx()
        y = tk.winfo_rooty()
        height = tk.winfo_height() + y
        width = tk.winfo_width() + x

        ImageGrab.grab().crop((x, y, width, height)).save(filename)

class imginput():
    def __init__(self):
        self.photo=None
    def inputImg(self,img, watermark=False):
        if watermark:
            if self.photo:
                # 浮水印
                finalImg=self.photo.copy()
                finalImg.paste(img, (10, 10))
                photo = ImageTk.PhotoImage(finalImg)
                labelimg.image = photo
                final=Label(tk, image=photo)
                final.place(x=0, y=0)
                tk.geometry(f"{finalImg.size[0]}x{finalImg.size[1]}")
            else:
                messagebox.showinfo(title="Error", message="請先新增要製作浮水印的圖片，檔名需要包含watermark.")
        else:
            self.photo= img
            photo = ImageTk.PhotoImage(img)
            # 設定labelimg為圖片作顯示
            labelimg.configure(image=photo, highlightthickness=0, borderwidth=1, padx=0, pady=0)
            labelimg.image = photo
            labelimg.place(x=0, y=0)

if __name__ == "__main__":
    tk = Tk()
    #設定視窗的長寬
    tk.geometry("800x500")
    inputImage=imginput()
    #建立選單欄
    filemenu=Menu(tk)
    labelimg = Label(tk, image="")
    tk.config(menu=filemenu)
    menu1=Menu(filemenu,tearoff=0) #tearoff=0 表移除虛線
    menu1.add_command(label='開啟檔案',command=open_file)
    menu1.add_command(label='儲存檔案',command=save_file)
    menu1.add_command(label='離開',command=tk.quit)
    tk.wm_attributes("-transparentcolor")
    filemenu.add_cascade(label='檔案',menu=menu1) #命名父選單名稱，綁定menu1的項目

    tk.mainloop()

