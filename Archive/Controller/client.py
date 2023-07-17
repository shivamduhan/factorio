import socket

def client():
  host = socket.gethostname()  # get local machine name
  port = 8080  # Make sure it's within the > 1024 $$ <65535 range

  print(f"loalHost Name: {host} @ port#: {port}")

  s = socket.socket()
  s.connect((host, port))

  message = input('-> ')
  while message != 'quit()':
    s.send(message.encode('utf-8'))
    data = s.recv(1024).decode('utf-8')
    print('Received from server: ' + data)
    message = input('==> ')
    #KEY_EVENT_TIME

  s.close()


if __name__ == '__main__':
    client()
