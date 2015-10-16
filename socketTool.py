#!/usr/bin/env python
#coding=utf-8
__author__ = 'wangxiaochuang from China'
__date__ = '2015-10-16'


import socket
import Tkinter
from Tkinter import Frame, Button, Text, Entry, Label, Tk

class MySocket():
    def __init__(self, ip, port, flag):
        self.ip = ip
        self.port = int(port)
        self.flag = flag
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.ip, self.port))

    def shortLink(self, data):
        self.sock.sendall(data)
        rcvdata = self.sock.recv(2048)
        return rcvdata

    def longLink(self, data):
        self.sock.sendall(data)
        rcvdata = self.sock.recv(2048)
        return rcvdata
    
class MyApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title('socket tools in *nix')

        #Frame setting
        frame_left = Frame(width=170, height=400)
        frame_right_top = Frame(width=380, height=200, bg='white')
        frame_right_center = Frame(width=380, height=180, bg='white')
        frame_right_bottom = Frame(width=380, height=40)

        #Button and Text
        self.text_send = Text(frame_right_top)
        self.text_send.grid()
        self.text_recv = Text(frame_right_center)
        self.text_recv.grid()

        #set ip and port
        Label(frame_left, text='ip').grid()
        self.ip = Entry(frame_left)
        self.ip.grid()
        Label(frame_left, text='port').grid()
        self.port = Entry(frame_left)
        self.port.grid();

        button_senddata = Button(frame_right_bottom, text='send', command=self.send).grid(sticky=Tkinter.W)

        #Grid
        frame_left.grid(row=0, column=0, rowspan=3, padx=2, pady=2)
        frame_right_top.grid(row=0, column=1, padx=2, pady=5)
        frame_right_center.grid(row=1, column=1, padx=2, pady=5)
        frame_right_bottom.grid(row=2, column=1)

        frame_right_top.grid_propagate(0)
        frame_right_center.grid_propagate(0)
        frame_right_bottom.grid_propagate(0)

    def send(self):
        sip = self.ip.get()
        sport = self.port.get()
        sctxt = self.text_send.get('0.0', Tkinter.END)

        if sip == '' or sport == '' or sctxt == '':
            self.text_recv.insert('0.0', 'please input some thing ip port content')
            return

        sock = MySocket(sip, sport)
        if self.flag == '0':
            recvData = sock.shortLink(sctxt)
            self.sock.close()
            self.text_recv.insert('0.0', recvData)
        else:
            while 1:
                recvData = sock.shortLink(sctxt)
                self.text_recv.insert('0.0', recvData)
            self.sock.close()

if __name__ == '__main__':
    MyApp().mainloop()

