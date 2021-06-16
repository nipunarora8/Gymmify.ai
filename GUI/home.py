from tkinter import *
from PIL import ImageTk, Image
import cv2

root = Tk()
root.attributes("-fullscreen", True)
root.geometry(f'{root.winfo_screenwidth()}x{root.winfo_screenheight()}')
# print(f'{root.winfo_screenwidth()}x{root.winfo_screenheight()}')
root["bg"] = "black"

def openinsWindow():
    
    global ins_bg, menu_btn, about_btn, research_btn, ins_window
    # Toplevel object which will 
    # be treated as a new window
    ins_window = Toplevel(root)
  
    ins_window.title("Gymmify")
    ins_window.attributes("-fullscreen", True)
    
    # sets the geometry of toplevel
    ins_window.geometry(f'{root.winfo_screenwidth()}x{root.winfo_screenheight()}')
    
    ins_window["bg"]="#150F3A"
    ins_bg = PhotoImage(file="resources/page_2.png")
    bg_ins = Label(ins_window,image=ins_bg)
    bg_ins.place(x=0,y=0,relwidth=1,relheight=1)

    #buttons
    about_btn = PhotoImage(file="resources/about.png")
    btn_about = Button(ins_window, text = "clickme", image = about_btn,command = opencameraWindow)
    btn_about["bg"]="#1C2060"
    btn_about["border"] = "0"
    btn_about.place(x=1100,y=140)

    menu_btn = PhotoImage(file="resources/menu.png")
    btn_menu = Button(ins_window, text = "clickme", image = menu_btn,command = openmenuWindow)
    btn_menu["bg"]="#1C2060"
    btn_menu["border"] = "0"
    btn_menu.place(x=1100,y=240)

    research_btn = PhotoImage(file="resources/research.png")
    btn_research = Button(ins_window, text = "clickme", image = research_btn, command = openresearchWindow)
    btn_research["bg"]="#1C2060"
    btn_research["border"] = "0"
    btn_research.place(x=1100,y=340)

    ins_window.bind('<Key-Escape>',quit)

def openaboutWindow():

    pass

def openmenuWindow():

    pass

def openresearchWindow():

    pass    

def opencameraWindow():

    global cam_bg, startt_btn, stop_btn, camera_window, imgcanvas, begin

    def start_camera():
        
        lmain = Label(vidcanvas)
        lmain.grid(row=0, column=0)

        cap = cv2.VideoCapture(0)
        # imgcanvas.create_image(0,0, anchor=NW, image=img)
        def show_frame():
            _, frame = cap.read()
            frame = cv2.flip(frame, 1)
            cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
            cv2image = cv2.resize(cv2image,(700,550))
            img = Image.fromarray(cv2image)
            imgtk = ImageTk.PhotoImage(image=img)
            lmain.imgtk = imgtk
            lmain.configure(image=imgtk)
            lmain.after(10, show_frame) 

        show_frame()
    
    # Toplevel object which will 
    # be treated as a new window
    camera_window = Toplevel(ins_window)

    camera_window.title("Gymmify")
    camera_window.attributes("-fullscreen", True)
    
    # sets the geometry of toplevel
    camera_window.geometry(f'{root.winfo_screenwidth()}x{root.winfo_screenheight()}')
    
    cam_bg = PhotoImage(file="resources/camera_bg.png")
    bg_cam = Label(camera_window,image=cam_bg)
    bg_cam.place(x=0,y=0,relwidth=1,relheight=1)

    imgcanvas = Canvas(camera_window,width=700, height=550, bg="black", highlightthickness=3, highlightbackground="white")
    imgcanvas.place(x=40,y=140)
    begin = PhotoImage(file="resources/begin.png")
    labell = Label(imgcanvas,image=begin)
    labell["bg"]="black"
    labell["border"] = "0"
    labell.place(x=110,y=220)

    vidcanvas = Canvas(camera_window,width=700, height=550, bg="black", highlightthickness=3, highlightbackground="white")
    vidcanvas.place(x=800,y=140)
    labelr = Label(vidcanvas,image=begin)
    labelr["bg"]="black"
    labelr["border"] = "0"
    labelr.place(x=110,y=220)

    #buttons
    startt_btn = PhotoImage(file="resources/start_video.png")
    btn_startt = Button(camera_window, image = startt_btn, command = start_camera)
    btn_startt["bg"]="#2A2D2C"
    btn_startt["border"] = "0"
    btn_startt.place(x=300,y=725)

    stop_btn = PhotoImage(file="resources/stop_video.png")
    btn_stop = Button(camera_window, image = stop_btn, command = openthankWindow)
    btn_stop["bg"]="#232525"
    btn_stop["border"] = "0"
    btn_stop.place(x=1000,y=725)

    camera_window.bind('<Key-Escape>',quit)

def openthankWindow():

    global thank_bg

    thank_window = Toplevel(camera_window)
  
    thank_window.title("Gymmify")
    thank_window.attributes("-fullscreen", True)
    
    # sets the geometry of toplevel
    thank_window.geometry(f'{root.winfo_screenwidth()}x{root.winfo_screenheight()}')
    
    thank_window["bg"]="#000000"
    thank_bg = PhotoImage(file="resources/thank_you.png")
    bg_thank = Label(thank_window,image=thank_bg)
    bg_thank.place(x=0,y=0,relwidth=1,relheight=1)

bg = PhotoImage(file = "resources/main_screen.png")

bg_img = Label(root,image=bg)
bg_img.place(x=0,y=0,relwidth=1,relheight=1)

start_btn = PhotoImage(file="resources/Start Button.png")
btn_start = Button(root, text = "clickme", image = start_btn,command = openinsWindow)
btn_start["bg"]="#202020"
btn_start["border"] = "0"
btn_start.place(x=670,y=470)




root.bind('<Key-Escape>',quit)

root.mainloop()
