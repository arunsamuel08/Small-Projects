from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube
from tkinter import messagebox

Folder_Name = ""

# function for location of folder
def Browse():
    global Folder_Name
    Folder_Name = filedialog.askdirectory()
    if(len(Folder_Name)>1):
        browse_error.config(text=Folder_Name, fg='green')
    
    else:
        browse_error.config(text='Please Choose Folder!', fg='red')
    download_path.set(Folder_Name)

# function for downloading th video
def Download():
    choice = input_quality.get()
    url = input_link.get()

    if(len(url)>1):
        label1_error.config(text="")
        yt = YouTube(url)

        if(choice == choices[0]):
            select = yt.streams.filter(progressive=True).first()

        elif(choice == choices[1]):
            select = yt.streams.filter(progressive=True, file_extension='mp4').last()

        elif(choice == choices[2]):
            select = yt.streams.filter(only_audio=True).first()

        else:
            label1_error.config(text="Paste Link again", fg='red')


    # download function
    select.download(Folder_Name)
    label1_error.config(text="Download Completed", fg='green')
    messagebox.showinfo('Download Completed', 'File Downloaded Successfully in\n'
                           + Folder_Name)



# making the gui window
root = Tk()
# giving geometry
root.geometry('370x500')
# made the window not resizeable
root.resizable(False, False)
# gave window title
root.title('Youtube Downloader')
# background color black
root.configure(bg='#222')


# ========================================= Entry box for link input ===============================================

# gave string value to the video link variable
video_link = StringVar()

# label for link entry box
label1 = Label(root, text="  Enter the YouTube Link  ", font=('Helvetica', 15, 'bold'), bg='black', fg='red')
label1.grid(columnspan=2, row=0, column=0, pady=20, padx=60)

# entry box for link
input_link = Entry(root, width=40, font=('helvetica', 10), textvariable=video_link, relief='sunken')
input_link.grid(columnspan=2, padx=40)

# label for error msg
label1_error = Label(root, text="Enter YouTube URL", fg='red', font=('helvetica', 10))
label1_error.grid(columnspan=2, pady=10)

# =========================================== Entry box for quality =================================================

# label for quality
label2 = Label(root, text="Select Quality", font=('helvetica', 15, 'bold'), bg='black', fg='red')
label2.grid(columnspan=2, pady=20, padx=60)

# entry box for quality and choice
choices = ["720p","144p","Only Audio"]
input_quality = ttk.Combobox(root, values=choices)
input_quality.grid(columnspan=2, row=4, column=0, padx=60)

# =========================================== Entry Box for dwnld destination ========================================

# string value to download path variable
download_path = StringVar()

# label for download destination
label3 = Label(root, text="Enter Download Destination", font=('Helvetica', 15, 'bold'), fg='red', bg='black')
label3.grid(pady=30, columnspan=2)

# entry box for download destination
input_dwnld_dest = Entry(root, width=30, font=('helvetica',10), textvariable=download_path, relief='sunken')
input_dwnld_dest.grid(row=6, column=0)

# button for browsing file directory
browse_btn = Button(text="Browse", font=('helvetica', 10, 'bold'), fg='white', bg='red', relief='raised', command=Browse)
browse_btn.grid(row=6, column=1)

# error label for wrong path input
browse_error = Label(root, text='Please choose folder', fg='red', font=('helvetica', 10))
browse_error.grid(columnspan=7, pady=10)

# ============================================= Progress Bar =========================================================

# ========================================== Download Button ==========================================================

# button for downloading
download_btn = Button(root, text="Download", font=('helvetica', 16, 'bold'), fg='white', bg='red', command= Download)
download_btn.place(x=125, y=400)






root.mainloop()