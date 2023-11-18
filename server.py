import socket
import sys
import os
import time
from message import Message

# メッセージクラスをインスタンス化
message = Message()

# UNIXソケットをストリームモードで作成
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

# このサーバが接続を待つUNIXソケットのパスを設定する(本来はIPアドレスとポート)
server_address = '../socket_file'

# 以前の接続が残っていた場合に備えて、サーバアドレスをアンリンク(削除)する。
try:
    os.unlink(server_address)
# サーバアドレスが存在しない場合(=望んでいる状態)、例外を無視
except FileNotFoundError:
    pass

print('Starting up on {}'.format(server_address))

# サーバアドレスのソケットをバインド（接続）します
sock.bind(server_address)

# ソケットが接続要求を待機するようにする
sock.listen(1)

flag = True
# 無限ループでクライアントからの接続を待つ
while flag:
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)

        while True:
            data = connection.recv(4096)
            data_str = data.decode('utf-8')

            message.setRecievedMessage(data_str)
            message.choiceMessage()

            if data_str == 'exit':
                print("Clothing current connection")
                connection.close()
                break

            if data:
                response = message.getSendMessage()
                connection.sendall(response.encode())
    finally:
        print("Clothing current connection")
        connection.close()

    flag = False

