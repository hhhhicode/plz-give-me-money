import socket
import requests


def get_internal_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))  # Google DNS 서버를 이용
    return s.getsockname()[0]


def get_external_ip():
    response = requests.get('https://httpbin.org/ip')
    return response.json()['origin']
