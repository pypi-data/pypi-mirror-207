import socket
import requests


def get_machine_ip():
    """获取本机ip"""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 1))
    return s.getsockname()[0]


def get_geo_info(ip):
    """获取地理ip"""
    url = f'http://whois.pconline.com.cn/ipJson.jsp'
    params = {'json': 'true', 'ip': ip}
    rsp = requests.get(url, params=params)
    if rsp.status_code == 200:
        return rsp.json()
    else:
        return {}
