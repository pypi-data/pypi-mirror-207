"""这是一个封装http file 上传和下载服务接口的模块。
它依赖simple_http_server模块。
"""

import subprocess
import threading
import psutil
import signal
import shutil, os
import time

class HttpFileUploadDownloadWrapper(object):
    ip = ''
    port = 10801
    proc = None

    def start_server():
        if HttpFileUploadDownloadWrapper.proc is None:
            HttpFileUploadDownloadWrapper.ip = HttpFileUploadDownloadWrapper._get_active_ip()
            print('ip:', HttpFileUploadDownloadWrapper.ip)
            print('port:', HttpFileUploadDownloadWrapper.port)
            
            HttpFileUploadDownloadWrapper.proc = subprocess.Popen(['python', '-m', 'badgescale_ys_plt.simple_http_server', '-b', '%s' % HttpFileUploadDownloadWrapper.ip, '%s' % HttpFileUploadDownloadWrapper.port], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print('http file server pid:', HttpFileUploadDownloadWrapper.proc.pid)

            from importlib.resources import files
            speaker_sample_file = files('badgescale_ys_plt').joinpath('speaker_sample.wav')
            print('speaker sample:', speaker_sample_file)
            src_basename = os.path.basename(speaker_sample_file)
            dest_file = os.path.join(os.path.abspath('.'), src_basename)

            if os.path.exists(speaker_sample_file):
                shutil.copyfile(speaker_sample_file, dest_file)

        return (HttpFileUploadDownloadWrapper.ip, HttpFileUploadDownloadWrapper.port)

    def stop_server():
        if HttpFileUploadDownloadWrapper.proc:
            # print('before terminate')
            # HttpFileUploadDownloadWrapper.proc.terminate()
            # print('after terminate')
            # print('before wait')
            # HttpFileUploadDownloadWrapper.proc.wait()
            # print('after wait')
            subprocess.call(['taskkill', '/F', '/T', '/PID', str(HttpFileUploadDownloadWrapper.proc.pid)])
            HttpFileUploadDownloadWrapper.proc = None

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

    HttpFileUploadDownloadWrapper.start_server()
    time.sleep(3600)
    HttpFileUploadDownloadWrapper.stop_server()

if __name__ == '__main__':
    main()
