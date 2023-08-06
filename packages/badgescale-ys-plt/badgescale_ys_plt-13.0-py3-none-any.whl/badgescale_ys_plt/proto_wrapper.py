"""这是一个封装串口通信接口、私有串口消息通信的模块。
它依赖pyserial模块。
"""

import serial
from serial.tools.list_ports import *
from threading import Thread, Lock, Event
import re
import time

class ProtoWrapper:
    def __init__(self, port, baud, bytesize, stopbits, parity, auto_port=True):
        self.port = [port]
        self.baud = int(baud)
        self.bytesize = None
        if bytesize == '8':
           self.bytesize = serial.EIGHTBITS 
        self.stopbits = None
        if stopbits == '1':
            self.stopbits = serial.STOPBITS_ONE
        self.parity = None
        if parity == 'N':
            self.parity = serial.PARITY_NONE
        elif parity == 'E':
            self.parity = serial.PARITY_EVEN
        elif parity == 'O':
            self.parity = serial.PARITY_ODD
        else:
            pass
        self.auto_port = auto_port

        self.thread1 = None
        self.fd = None
        self.fd_rw_lock = Lock()
        
        self.result_map = { }
        
        self.event1 = Event()
        self.event2 = Event()
        self.event3 = Event()
        self.event4 = Event()
        self.event5 = Event()
        self.event6 = Event()
        self.event7 = Event()
        self.event8 = Event()
        self.event9 = Event()
        self.event10 = Event()
        self.event11 = Event()

        self.stopped = False

    def start_read(self):
        if self.thread1 is None:
            self.thread1 = Thread(target = self._read_entry, name='start read thread')
            self.thread1.start()
            self.stopped = False

    def stop_read(self):
        self.stopped = True
        if self.thread1:
            self.thread1.join()
            self.thread1 = None
            
    def _read_entry(self):
        
        while self.stopped is False:
            if not self.fd:
                if self.auto_port:
                    self.port = self.get_com_list()
                    self.port = sorted(self.port, reverse=True)
                    print('port:', self.port)
        
                for p in self.port:
                    try:
                        self.fd_rw_lock.acquire()
                        self.fd = serial.Serial(p, self.baud, self.bytesize, self.parity, self.stopbits, timeout = 0.2)
                        if self.fd.isOpen():
                            break
                    except serial.SerialException as e:
                        print('error:', e)
                        self.fd = None
                    finally:
                        self.fd_rw_lock.release()
                
            while self.fd and self.fd.isOpen() and self.stopped is False:
                str_line = ''
                try:
                    self.fd_rw_lock.acquire()
                    # readline return byte-formatted data
                    data = self.fd.readline()
                    str_line = data.decode(encoding='utf-8', errors='ignore')
                    str_line = str_line.strip()
                except serial.SerialTimeoutException as e:
                    print('timeout:', e)
                except serial.SerialException as e:
                    print('error:', e)
                    self.fd.close()
                    self.fd = None
                finally:
                    self.fd_rw_lock.release()

                if len(str_line) > 0:
                    print('str_line:', str_line)

                    '''match each pattern against line just readed.'''
                    m = re.match(r'.*?functiontest return (\d)', str_line)
                    if m:
                        self.response_functiontest_start(m.groups()[0])
                    
                    m = re.match(r'.*?functiontest ble return (.+)', str_line)
                    if m:
                        self.response_functiontest_ble_start(m.groups()[0])
                    
                    m = re.match(r'.*?functiontest wifi set return (\d)', str_line)
                    if m:
                        self.response_functiontest_wifi_set(m.groups()[0])
                    
                    m = re.match(r'.*?functiontest wifi return TX (.+?)Mb/s', str_line)
                    if m:
                        self.response_functiontest_wifi_start(m.groups()[0])
                    
                    m = re.match(r'.*?functiontest record return (.+)', str_line)
                    if m:
                        #print('note record matched')
                        self.response_functiontest_record_start(m.groups()[0])
                    
                    m = re.match(r'.*?functiontest 3dsensor return (\d)', str_line)
                    if m:
                        self.response_functiontest_3dsensor_start(m.groups()[0])
                    
                    m = re.match(r'.*?functiontest charging return (\d)', str_line)
                    if m:
                        self.response_functiontest_charging_start(m.groups()[0])
                    
                    m = re.match(r'.*?functiontest speaker return (\d)', str_line)
                    if m:
                        self.response_functiontest_speaker_start(m.groups()[0])
                    
                    m = re.match(r'.*?functiontest buzzer return (\d)', str_line)
                    if m:
                        self.response_functiontest_buzzer_start(m.groups()[0])
                    
                    m = re.match(r'.*?functiontest 3key return (\d)', str_line)
                    if m:
                        self.response_functiontest_3key_start(m.groups()[0])
                    
                    m = re.match(r'.*?functiontest return (\d)', str_line)
                    if m:
                        self.response_functiontest_stop(m.groups()[0])
            
            time.sleep(2)

    def writeline(self, str):
        ret = False
        self.fd_rw_lock.acquire()
        if self.fd:
            try:
                self.fd.write(''.join([str, '\r\n']).encode('utf-8'))
                ret = True
            except serial.SerialException as e:
                print('error:', e)
                self.fd = None
        self.fd_rw_lock.release()

        return ret

    @staticmethod
    def get_com_list():
        coms = []
        plist = list(comports())
        for port in plist:
            msg =list(port)
            coms.append(msg[0])
        return coms
    
    def request_functiontest_start(self):
        self.event1.clear()

        if self.writeline('functiontest start'):
            if self.event1.wait(10):
                ret = self.result_map['functiontest_start'][0]
                return int(ret)
            else:
                return 1
        
        return 1

    def response_functiontest_start(self, *args):
        self.result_map['functiontest_start'] = args
        self.event1.set()

    def request_functiontest_ble_start(self):
        self.event2.clear()

        if self.writeline('functiontest ble start'):
            self.event2.wait(10)
            if self.event2.isSet():
                ret = self.result_map['functiontest_ble_start'][0]
                return ret
            else:
                return ''
        
        return ''

    def response_functiontest_ble_start(self, *args):
        self.result_map['functiontest_ble_start'] = args
        self.event2.set()
        
    def request_functiontest_wifi_set(self, ssid, password):
        self.event3.clear()

        if self.writeline('functiontest wifi set %s %s' % (ssid, password)):
            self.event3.wait(20)
            if self.event3.isSet():
                ret = self.result_map['functiontest_wifi_set'][0]
                return int(ret)
            else:
                return 1
        
        return 1

    def response_functiontest_wifi_set(self, *args):
        self.result_map['functiontest_wifi_set'] = args
        self.event3.set()

    def request_functiontest_wifi_start(self, ip, port):
        self.event4.clear()

        if self.writeline('functiontest wifi start %s %s' % (ip, port)):
            self.event4.wait(20)
            if self.event4.isSet():
                ret = self.result_map['functiontest_wifi_start'][0]
                return float(ret)
            else:
                return 0.0
        
        return 0.0

    def response_functiontest_wifi_start(self, *args):
        self.result_map['functiontest_wifi_start'] = args
        self.event4.set()

    def request_functiontest_record_start(self, ip, port):
        self.event5.clear()

        if self.writeline('functiontest record start %s %s' % (ip, port)):    
            self.event5.wait(20)
            if self.event5.isSet():
                #print('note wait true')
                ret = self.result_map['functiontest_record_start'][0]
                return ret
            else:
                return ''
        
        return ''

    def response_functiontest_record_start(self, *args):
        self.result_map['functiontest_record_start'] = args
        self.event5.set()
        #print('note set true')
    
    def request_functiontest_3dsensor_start(self):
        self.event6.clear()

        if self.writeline('functiontest 3dsensor start'):    
            self.event6.wait(10)
            if self.event6.isSet():
                ret = self.result_map['functiontest_3dsensor_start'][0]
                return int(ret)
            else:
                return 1
        
        return 1

    def response_functiontest_3dsensor_start(self, *args):
        self.result_map['functiontest_3dsensor_start'] = args
        self.event6.set()

    def request_functiontest_charging_start(self):
        self.event7.clear()

        if self.writeline('functiontest charging start'):
            self.event7.wait(10)
            if self.event7.isSet():
                ret = self.result_map['functiontest_charging_start'][0]
                return int(ret)
            else:
                return 1
        
        return 1

    def response_functiontest_charging_start(self, *args):
        self.result_map['functiontest_charging_start'] = args
        self.event7.set()

    def request_functiontest_speaker_start(self, url):
        self.event8.clear()

        if self.writeline('functiontest speaker start %s' % (url)):
            self.event8.wait(20)
            if self.event8.isSet():
                ret = self.result_map['functiontest_speaker_start'][0]
                return int(ret)
            else:
                return 1
        
        return 1

    def response_functiontest_speaker_start(self, *args):
        self.result_map['functiontest_speaker_start'] = args
        self.event8.set()

    def request_functiontest_buzzer_start(self):
        self.event9.clear()

        if self.writeline('functiontest buzzer start'):
            self.event9.wait(10)
            if self.event9.isSet():
                ret = self.result_map['functiontest_buzzer_start'][0]
                return int(ret)
            else:
                return 1
        
        return 1

    def response_functiontest_buzzer_start(self, *args):
        self.result_map['functiontest_buzzer_start'] = args
        self.event9.set()

    def request_functiontest_3key_start(self):
        self.event10.clear()

        if self.writeline('functiontest 3key start'):
            self.event10.wait(20)
            if self.event10.isSet():
                ret = self.result_map['functiontest_3key_start'][0]
                return int(ret)
            else:
                return 4
        
        return 4

    def response_functiontest_3key_start(self, *args):
        self.result_map['functiontest_3key_start'] = args
        self.event10.set()

    def request_functiontest_stop(self):
        self.event11.clear()

        if self.writeline('functiontest stop'):
            self.event11.wait(10)
            if self.event11.isSet():
                ret = self.result_map['functiontest_stop'][0]
                return int(ret)
            else:
                return 1
        
        return 1

    def response_functiontest_stop(self, *args):
        self.result_map['functiontest_stop'] = args
        self.event11.set()

if __name__ == "__main__":
    proto = ProtoWrapper('', 115200, '8', '1', 'N', True)
    proto.start_read()
    
    print('result:', proto.request_functiontest_start())
    time.sleep(1)

    print('result:', proto.request_functiontest_ble_start())
    time.sleep(1)
    
    while True:
        time.sleep(1)