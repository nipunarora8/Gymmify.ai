from tkinter import *
from PIL import ImageTk, Image
import cv2
import mediapipe as mp
import imageio
import numpy as np
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
from mediapipe.python.solutions.pose import PoseLandmark
from exercises.db_press import dumbell_press
from exercises.squats import free_squats
from exercises.lateral_raise import lateral_raise
from exercises.pushups import pushups
from exercises.leg_raise import leg_raise
from exercises.biceps import bicep_curl

root = Tk()
root.attributes("-fullscreen", True)
root.geometry(f'{root.winfo_screenwidth()}x{root.winfo_screenheight()}')
# print(f'{root.winfo_screenwidth()}x{root.winfo_screenheight()}')
root["bg"] = "black"

def openinsWindow():
    
    global ins_bg, menu_btn, about_btn, research_btn, ins_window, exit_btn
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
    btn_about = Button(ins_window, text = "clickme", image = about_btn,command = openaboutWindow)
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

    exit_btn = PhotoImage(file="resources/exit_ins.png")
    btn_research = Button(ins_window, image = exit_btn, command = openthankWindow)
    btn_research["bg"]="#120B2C"
    btn_research["border"] = "0"
    btn_research.place(x=1470,y=830)

    ins_window.bind('<Key-Escape>',quit)

def openaboutWindow():

    global about_bg, menu_abt, exit_abt

    about_window = Toplevel()
  
    about_window.title("Gymmify")
    about_window.attributes("-fullscreen", True)
    
    # sets the geometry of toplevel
    about_window.geometry(f'{root.winfo_screenwidth()}x{root.winfo_screenheight()}')
    
    about_window["bg"]="#000000"
    about_bg = PhotoImage(file="resources/about_us.png")
    bg_about = Label(about_window,image=about_bg)
    bg_about.place(x=0,y=0,relwidth=1,relheight=1)

    menu_abt = PhotoImage(file="resources/menu_abt.png")
    btn_menu = Button(about_window, image = menu_abt,command = openmenuWindow)
    btn_menu["bg"]="#0A0908"
    btn_menu["border"] = "0"
    btn_menu.place(x=985,y=685)

    exit_abt = PhotoImage(file="resources/exit_abt.png")
    btn_exit = Button(about_window, image = exit_abt, command = openthankWindow)
    btn_exit["bg"]="#0A0908"
    btn_exit["border"] = "0"
    btn_exit.place(x=1140,y=685)

    about_window.bind('<Key-Escape>',quit)

def openmenuWindow():

    global menu_bg, exit_btn, back_btn, btn_1, btn_2, btn_3, btn_4, btn_5, btn_6, video_name, vidd, lb11, lb12, lb13, lb14, lb15, lb16

    menu_window = Toplevel(root)
  
    menu_window.title("Gymmify")
    menu_window.attributes("-fullscreen", True)
    
    # sets the geometry of toplevel
    menu_window.geometry(f'{root.winfo_screenwidth()}x{root.winfo_screenheight()}')
    
    menu_window["bg"]="#150F3A"
    menu_bg = PhotoImage(file="resources/menu_bg.png")
    bg_menu = Label(menu_window,image=menu_bg)
    bg_menu.place(x=0,y=0,relwidth=1,relheight=1)

    back_btn = PhotoImage(file="resources/menu_back.png")
    btn_back = Button(menu_window, image = back_btn, command = openinsWindow)
    btn_back["bg"]="#000000"
    btn_back["border"] = "0"
    btn_back.place(x=1410,y=830)

    exit_btn = PhotoImage(file="resources/menu_exit.png")
    btn_exit = Button(menu_window, image = exit_btn, command = openthankWindow)
    btn_exit["bg"]="#000000"
    btn_exit["border"] = "0"
    btn_exit.place(x=1470,y=830)

    def btn_1f():
        global n
        n=1
        opencameraWindow()

    btn_1 = PhotoImage(file="resources/shoulder_press.png")
    btn1 = Button(menu_window, image = btn_1,command = btn_1f)
    btn1["bg"]="#1C2060"
    btn1["border"] = "0"
    btn1.place(x=70,y=190)

    lb11 = PhotoImage(file="resources/should_press.png")
    lb1 = Label(menu_window,image=lb11)
    lb1["bg"]="black"
    lb1["border"] = "0"
    lb1.place(x=180,y=440)

    def change_1(e):
        global video1
        video_name = "resources/shoulder_press.mp4" #Image-path
        video1 = imageio.get_reader(video_name)
        def stream():
            try:
                image = video1.get_next_data()
                image = cv2.resize(image, (435,241))
                frame_image = Image.fromarray(image)
                frame_image=ImageTk.PhotoImage(frame_image)
                btn1.config(image=frame_image)
                btn1.image = frame_image
                btn1.after(60, lambda: stream())
            except:
                video1.close()
                change_back_1(e)
                return
        stream()

    def change_back_1(e):
        video1.close()
        btn1.config(image=btn_1)
        btn1.image = btn_1

    btn1.bind("<Enter>",change_1)
    btn1.bind("<Leave>",change_back_1)

    def btn_2f():
        global n
        n=2
        opencameraWindow()

    btn_2 = PhotoImage(file="resources/pushups.png")
    btn2 = Button(menu_window, image = btn_2,command = btn_2f)
    btn2["bg"]="#1C2060"
    btn2["border"] = "0"
    btn2.place(x=550,y=190)

    lb12 = PhotoImage(file="resources/pushup_head.png")
    lb2 = Label(menu_window,image=lb12)
    lb2["bg"]="black"
    lb2["border"] = "0"
    lb2.place(x=650,y=440)

    def change_2(e):
        global video2
        video_name = "resources/pushups.mp4" #Image-path
        video2 = imageio.get_reader(video_name)
        def stream():
            try:
                image = video2.get_next_data()
                image = cv2.resize(image, (435,241))
                frame_image = Image.fromarray(image)
                frame_image=ImageTk.PhotoImage(frame_image)
                btn2.config(image=frame_image)
                btn2.image = frame_image
                btn2.after(60, lambda: stream())
            except:
                video2.close()
                return
        stream()

    def change_back_2(e):
        video2.close()
        btn2.config(image=btn_2)
        btn2.image = btn_2

    btn2.bind("<Enter>",change_2)
    btn2.bind("<Leave>",change_back_2)

    def btn_3f():
        global n
        n=3
        opencameraWindow()

    btn_3 = PhotoImage(file="resources/lateral_raise.png")
    btn3 = Button(menu_window, image = btn_3,command = btn_3f)
    btn3["bg"]="#1C2060"
    btn3["border"] = "0"
    btn3.place(x=1030,y=190)

    lb13 = PhotoImage(file="resources/lateral_raise_head.png")
    lb3 = Label(menu_window,image=lb13)
    lb3["bg"]="black"
    lb3["border"] = "0"
    lb3.place(x=1125,y=440)

    def change_3(e):
        global video3
        video_name = "resources/lateral_raise.mp4" #Image-path
        video3 = imageio.get_reader(video_name)
        def stream():
            try:
                image = video3.get_next_data()
                image = cv2.resize(image, (435,241))
                frame_image = Image.fromarray(image)
                frame_image=ImageTk.PhotoImage(frame_image)
                btn3.config(image=frame_image)
                btn3.image = frame_image
                btn3.after(60, lambda: stream())
            except:
                video3.close()
                return
        stream()

    def change_back_3(e):
        video3.close()
        btn3.config(image=btn_3)
        btn3.image = btn_3

    btn3.bind("<Enter>",change_3)
    btn3.bind("<Leave>",change_back_3)

    def btn_4f():
        global n
        n=4
        opencameraWindow()

    btn_4 = PhotoImage(file="resources/squats.png")
    btn4 = Button(menu_window, image = btn_4,command = btn_4f)
    btn4["bg"]="#1C2060"
    btn4["border"] = "0"
    btn4.place(x=70,y=500)

    lb14 = PhotoImage(file="resources/squats_head.png")
    lb4 = Label(menu_window,image=lb14)
    lb4["bg"]="black"
    lb4["border"] = "0"
    lb4.place(x=180,y=750)

    def change_4(e):
        global video4
        video_name = "resources/squats.mp4" #Image-path
        video4 = imageio.get_reader(video_name)
        def stream():
            try:
                image = video4.get_next_data()
                image = cv2.resize(image, (435,241))
                frame_image = Image.fromarray(image)
                frame_image=ImageTk.PhotoImage(frame_image)
                btn4.config(image=frame_image)
                btn4.image = frame_image
                btn4.after(60, lambda: stream())
            except:
                video4.close()
                return
        stream()

    def change_back_4(e):
        video4.close()
        btn4.config(image=btn_4)
        btn4.image = btn_4

    btn4.bind("<Enter>",change_4)
    btn4.bind("<Leave>",change_back_4)

    def btn_5f():
        global n
        n=5
        opencameraWindow()

    btn_5 = PhotoImage(file="resources/bicep_curl.png")
    btn5 = Button(menu_window, image = btn_5,command = btn_5f)
    btn5["bg"]="#1C2060"
    btn5["border"] = "0"
    btn5.place(x=550,y=500)

    lb15 = PhotoImage(file="resources/bicep_curl_head.png")
    lb5 = Label(menu_window,image=lb15)
    lb5["bg"]="black"
    lb5["border"] = "0"
    lb5.place(x=650,y=750)

    def change_5(e):
        global video5
        video_name = "resources/bicep_curl.mp4" #Image-path
        video5 = imageio.get_reader(video_name)
        def stream():
            try:
                image = video5.get_next_data()
                image = cv2.resize(image, (435,241))
                frame_image = Image.fromarray(image)
                frame_image=ImageTk.PhotoImage(frame_image)
                btn5.config(image=frame_image)
                btn5.image = frame_image
                btn5.after(60, lambda: stream())
            except:
                video5.close()
                return
        stream()

    def change_back_5(e):
        video5.close()
        btn5.config(image=btn_5)
        btn5.image = btn_5

    btn5.bind("<Enter>",change_5)
    btn5.bind("<Leave>",change_back_5)

    def btn_6f():
        global n
        n=6
        opencameraWindow()

    btn_6 = PhotoImage(file="resources/leg_raise.png")
    btn6 = Button(menu_window, image = btn_6,command = btn_6f)
    btn6["bg"]="#1C2060"
    btn6["border"] = "0"
    btn6.place(x=1030,y=500)

    lb16 = PhotoImage(file="resources/leg_raise_head.png")
    lb6 = Label(menu_window,image=lb16)
    lb6["bg"]="black"
    lb6["border"] = "0"
    lb6.place(x=1125,y=750)

    def change_6(e):
        global video6
        video_name = "resources/leg_raise.mp4" #Image-path
        video6 = imageio.get_reader(video_name)
        def stream():
            try:
                image = video6.get_next_data()
                image = cv2.resize(image, (435,241))
                frame_image = Image.fromarray(image)
                frame_image=ImageTk.PhotoImage(frame_image)
                btn6.config(image=frame_image)
                btn6.image = frame_image
                btn6.after(60, lambda: stream())
            except:
                video6.close()
                return
        stream()

    def change_back_6(e):
        video6.close()
        btn6.config(image=btn_6)
        btn6.image = btn_6

    btn6.bind("<Enter>",change_6)
    btn6.bind("<Leave>",change_back_6)

    menu_window.bind('<Key-Escape>',quit)

def openresearchWindow():

    global research_bg, exit_btn, research_window, back_btn

    research_window = Toplevel(ins_window)
  
    research_window.title("Gymmify")
    research_window.attributes("-fullscreen", True)
    
    # sets the geometry of toplevel
    research_window.geometry(f'{root.winfo_screenwidth()}x{root.winfo_screenheight()}')
    
    
    research_window["bg"]="#000000"
    research_bg = PhotoImage(file="resources/research_bg.png")
    bg_research = Label(research_window,image=research_bg)
    bg_research.place(x=0,y=0,relwidth=1,relheight=1)


    back_btn = PhotoImage(file="resources/research_back.png")
    btn_exit = Button(research_window, image = back_btn, command = openinsWindow)
    btn_exit["bg"]="#0D0D0D"
    btn_exit["border"] = "0"
    btn_exit.place(x=469,y=570)

    exit_btn = PhotoImage(file="resources/exit.png")
    btn_exit = Button(research_window, image = exit_btn, command = openthankWindow)
    btn_exit["bg"]="#0D0D0D"
    btn_exit["border"] = "0"
    btn_exit.place(x=800,y=570)

    research_window.bind('<Key-Escape>',quit)

def opencameraWindow():
    lst = []
    global cam_bg, startt_btn, stop_btn, camera_window, imgcanvas, begin
    stop = True

    def start_camera():
        
        lvid = Label(vidcanvas)
        lvid.grid(row=0, column=0)

        lstick = Label(imgcanvas)
        lstick.grid(row=0, column=0)
        global cap
        cap = cv2.VideoCapture(0)
        # imgcanvas.create_image(0,0, anchor=NW, image=img)
        def show_frame():
            with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
                try: 
                    _, frame = cap.read()
                    frame = cv2.flip(frame, 1)
                    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    cv2image.flags.writeable = False
                    cv2image = cv2.resize(cv2image,(700,550))
                    if n==1:
                        cv2image, blank_image = dumbell_press(cv2image,pose)
                    elif n==2:
                        cv2image, blank_image = pushups(cv2image,pose)
                    elif n==3:
                        cv2image, blank_image = lateral_raise(cv2image,pose)
                    elif n==4:
                        cv2image, blank_image = free_squats(cv2image,pose)
                    elif n==5:
                        stage = None
                        cv2image, blank_image = bicep_curl(cv2image,pose)
                    elif n==6:
                        cv2image, blank_image = leg_raise(cv2image,pose)
                    
                    img = Image.fromarray(cv2image)
                    imgtk = ImageTk.PhotoImage(image=img)
                    lvid.imgtk = imgtk
                    lvid.configure(image=imgtk)

                    img_stick = Image.fromarray(blank_image)
                    imgst = ImageTk.PhotoImage(image=img_stick)
                    lstick.imgtk = imgst
                    lstick.configure(image=imgst)
                    lstick.after(20, show_frame)
                except:
                    pass
        if stop:
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
    global stop, thank_bg, cap, exit_btn, back_btn
    stop = False

    try:
        cap.release()
    except NameError:
        pass
    
    global thank_bg

    thank_window = Toplevel()
  
    thank_window.title("Gymmify")
    thank_window.attributes("-fullscreen", True)
    
    # sets the geometry of toplevel
    thank_window.geometry(f'{root.winfo_screenwidth()}x{root.winfo_screenheight()}')
    
    thank_window["bg"]="#000000"
    thank_bg = PhotoImage(file="resources/thank_you.png")
    bg_thank = Label(thank_window,image=thank_bg)
    bg_thank.place(x=0,y=0,relwidth=1,relheight=1)

    back_btn = PhotoImage(file="resources/menu_back.png")
    btn_back = Button(thank_window, image = back_btn, command = openinsWindow)
    btn_back["bg"]="#000000"
    btn_back["border"] = "0"
    btn_back.place(x=1410,y=830)

    exit_btn = PhotoImage(file="resources/menu_exit.png")
    btn_exit = Button(thank_window, image = exit_btn, command = quit)
    btn_exit["bg"]="#000000"
    btn_exit["border"] = "0"
    btn_exit.place(x=1470,y=830)

    thank_window.bind('<Key-Escape>',quit)

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
