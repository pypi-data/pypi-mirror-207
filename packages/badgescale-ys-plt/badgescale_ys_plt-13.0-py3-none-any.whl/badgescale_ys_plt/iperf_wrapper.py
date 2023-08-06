"""这是一个封装iperf server操作接口的模块。
它依赖windows二进制程序iperf3.exe。
"""

import subprocess
import threading
import psutil
import signal
import time
import os

from importlib.resources import files
iperf3_exe = files('badgescale_ys_plt').joinpath('iperf3/iperf3.exe')

class IperfWrapper(object):
    ip = ''
    port = 10802
    thread1 = None
    proc = None

    def start_server():
        if IperfWrapper.proc is None:
            IperfWrapper.ip = IperfWrapper._get_active_ip()
            print('ip:', IperfWrapper.ip)
            print('port:', IperfWrapper.port)
            
            global iperf3_exe
            IperfWrapper.proc = subprocess.Popen([iperf3_exe, '-s', '-B', '%s' % IperfWrapper.ip, '-p', '%s' % IperfWrapper.port], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            print('iper server pid:', IperfWrapper.proc.pid)
            
        return (IperfWrapper.ip, IperfWrapper.port)

    def stop_server():
        if IperfWrapper.proc:
            # print('before terminate')
            # IperfWrapper.proc.terminate()
            # print('after terminate')
            # print('before wait')
            # IperfWrapper.proc.wait()
            # print('after wait')
            subprocess.call(['taskkill', '/F', '/T', '/PID', str(IperfWrapper.proc.pid)])
            IperfWrapper.proc = None

    def _get_active_ip():
        stats = psutil.net_if_stats()
        nic = None
        for k, v in stats.items():
            if k.startswith('WLAN') and v.isup is True:
                nic = k
                break
        
        if nic:
            addrs = psutil.net_if_addrs().get(nic)
            for i in addrs:
                if i.family == 2:
                    return i.address

        return None

def signal_handler(signal, frame):
    print("You choose to stop me.")
    exit()

def main():
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    IperfWrapper.start_server()
    time.sleep(3600)
    IperfWrapper.stop_server()

if __name__ == '__main__':
    main()
