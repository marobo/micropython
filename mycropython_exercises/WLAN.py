import machine, time, socket, network

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('Catalpa', 'kafemalirin')
wlan.isconnected()

def http_get(url):
    _, _, host, path = url.split('/', 3)
    if ':' in host:
        host, port = host.split(':')
        port = int(port)
    else:
        port = 80
    address = socket.getaddrinfo(host, port)[0][-1]
    the_socket = socket.socket()
    the_socket.connect(address)
    the_socket.send(bytes('GET /%s HTTP/1.0\r\n\Host:%s\r\n\r\n' % (path, host), 'utf8'))
    while True:
        data = the_socket.recv(100)
        if data:
            print(str(data, 'utf8'), end='')
        else:
            break
    the_socket.close()
