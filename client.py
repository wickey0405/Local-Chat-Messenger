import socket
import sys
from message import Message

# TCP/IPソケット(通信を可能にするためのエンドポイント)を作成
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

# サーバが待ち受けている特定の場所にソケットを接続する(本来はIPアドレスとポート)
server_address = '../socket_file'
print('connecting to {}'.format(server_address))

# サーバ接続をトライ
# エラーが起こった場合は、メッセージを表示してプログラムを停止する。
try:
    sock.connect(server_address)
except socket.error as err:
    print(err)

    sys.exit(1)

# サーバに接続できたら、ユーザー入力のメッセージを送信、もしくはServerからのメッセージを受信。
print("----------------------------------------------------------------------------")
print("If you input the word inculded 'name', you would get a random name.")
print("If you input the word inculded 'address', you would get a random adress.")
print("If you input the word inclulded without name and address, you would get a random text.")
while True:
    # 送信
    message = input('-----input your comment----\n')
    if(message == 'exit'): break
    sock.sendall(message.encode())

    # 受信
    data = sock.recv(4096)
    print(data.decode())
    print("-------------------------------------------")
