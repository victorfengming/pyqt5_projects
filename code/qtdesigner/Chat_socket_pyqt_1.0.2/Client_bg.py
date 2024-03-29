
import socket
import threading
import main
message_content = "init_content"

class Connect:
    def socket_init(self,ip):

        # 创建socket对象
        self.s = socket.socket()
        # 连接远程主机
        self.s.connect((ip, 6666))
        def read_from_server(s):
            global message_content
            while True:
                mes = s.recv(2048).decode('utf-8')
                message_content += mes
                print("message_content--->",message_content)
                # main.form.set_label_content()


        # 客户端启动线程不断地读取来自服务器的数据
        threading.Thread(target=read_from_server, args=(self.s, )).start()


    def input_chat_content(self,line):
        # line = input('')
        if line is None or line == 'exit':
            return
        # 将用户的键盘输入内容写入socket
        self.s.send(line.encode('utf-8'))
