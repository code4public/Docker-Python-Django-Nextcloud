
from django.views.generic import View
from django.shortcuts import HttpResponse
import socket
import docker

dport = 8080
def checkport( port ):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex(('127.0.0.1',port))
        while((result) == 0):
                port = port + 1
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                result = sock.connect_ex(('127.0.0.1',port))
        return port

class TestView(View):
    def get(self, request, *args, **kwargs):
        open_port = checkport(dport)
        client = docker.from_env()
        opstr = "Nextcloud instance started on Port Number # " + str(open_port)
        container = client.containers.run("nextcloud:latest", ports={80:open_port}, detach=True)
        return HttpResponse(opstr)