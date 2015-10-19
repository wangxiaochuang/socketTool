#!/usr/bin/env python
#coding=utf-8
__author__ = {'name':'wangxiaochuang',
              'mail':'jackstrawxiaoxin@gmail.com',
              'QQ':'932698529',
              'created':'2015-10-16'}

import pdb
import socket, Tkinter
from Tkinter import Toplevel, Frame, Button, Text, Entry, Label, Tk, Radiobutton, Menubutton, Menu, IntVar

class MySocket():
    def __init__(self):
        '''
        self.ip = ip
        self.port = int(port)
        '''
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def sendData(self, data):
        self.sock.sendall(data)
        rcvdata = self.sock.recv(2048)
        return rcvdata

class MyApp(Tk):
    def open_file(self):
        filewin = Tkinter.Toplevel()
        button = Button(filewin, text='do nothing button')
        button.pack()

    def __init__(self):
        Tk.__init__(self)
        self.title('socket tools in *nix')

        #Frame setting
        top_mbar = self.winfo_toplevel()

        frame_left = Frame(self)
        frame_right_top = Frame(self)
        frame_right_center = Frame(self)
        frame_right_bottom = Frame(self, height=40)

        #menu
        mbFile = Menu(top_mbar)
        top_mbar['menu'] = mbFile
        mbFile.subMenu = Menu(mbFile)
        mbFile.add_cascade(label='File', menu=mbFile.subMenu)
        mbFile.subMenu.add_command(label='open', command=self.open_file)
        mbFile.subMenu.entryconfig(0, state=Tkinter.DISABLED)

        #Button and Text
        self.text_send = Text(frame_right_top)
        self.text_send.grid()
        self.text_recv = Text(frame_right_center)
        self.text_recv.grid()

        #set ip and port
        ipf = Frame(frame_left, padx=10, pady=15)
        Label(ipf, text='ip', relief=Tkinter.RAISED, borderwidth=2, width=8).pack(side='left')
        self.ip = Entry(ipf)
        self.ip.pack(side='left')
        ipf.pack()

        portf = Frame(frame_left, padx=10, pady=5)
        Label(portf, text='port', relief=Tkinter.RAISED, borderwidth=2, width=8).pack(side='left')
        self.port = Entry(portf)
        self.port.pack(side='left')
        portf.pack()
        #set short and long link
        linkf = Frame(frame_left, padx=10, pady=15, relief=Tkinter.SUNKEN, borderwidth=2)
        self.flag = IntVar()
        Radiobutton(linkf, text="短链接", 
                value=0, variable=self.flag, 
                relief=Tkinter.RAISED)\
                        .pack(side=Tkinter.LEFT)
        Radiobutton(linkf, text="长链接", 
                value=1, variable=self.flag, 
                relief=Tkinter.RAISED)\
                        .pack(side=Tkinter.LEFT)
        linkf.pack()

        button_senddata = Button(frame_right_bottom, text='send', command=self.send).grid(sticky=Tkinter.W)

        #Grid
        frame_left.pack(side='left', anchor=Tkinter.N)
        frame_right_top.pack(side='top')
        frame_right_center.pack(side='top')
        frame_right_bottom.pack(side='top', anchor=Tkinter.E)
        
    def send(self):
        sip = self.ip.get()
        sport = self.port.get()
        flag = self.flag.get()
        sctxt = self.text_send.get('0.0', Tkinter.END)
        recvData = ''

        if sip == '' or sport =='' or sctxt == '':
            self.text_recv.insert('0.0', 'please input data what you want to send with specific addr')
            return

        #pdb.set_trace()
        if not hasattr(self,'conn'):
            self.conn = MySocket()
            self.conn.sock.connect((sip, int(sport)))

        if flag == 0:
            conn = MySocket()
            conn.sock.connect((sip, int(sport)))

            recvData = conn.sendData(sctxt)
            self.text_recv.insert('0.0', recvData)
            conn.sock.close()
        else:
            recvData = self.conn.sendData(sctxt)
            self.text_recv.insert('0.0', recvData)
            
if __name__ == '__main__':
    MyApp().mainloop()

