'''Module note
'''
import PySimpleGUI as sg
import logging
import threading
import time
import sys
from urllib import request

from . import sn_csv_table_wrapper, resource
from .sn_csv_table_wrapper import SNCSVTableWrapper
from . import ble_wrapper, proto_wrapper
from .ble_wrapper import BLEWrapper
from .proto_wrapper import ProtoWrapper

from . import http_file_server_wrapper, iperf_wrapper
from .http_file_server_wrapper import HttpFileUploadDownloadWrapper
from .iperf_wrapper import IperfWrapper

class MainWindow(object):
    def __init__(self):
        self._scan_qrcode_thread = None
        self._scan_qrcode_stop_event = None
        self._window = None
        self._relation_file = None
        self._timer1 = None
        self._timeout_sum = 0
        self._speaker_sample = 'speaker_sample.wav'
        self._thread1 = None
        self._event1 = threading.Event()
        self._proto = None
        self._http_file_server_addr = ()
        self._iperf_server_addr = ()

    def make_layout(self):
        #sg.set_options(icon=None, font='Helvitica 12', element_padding = (4,4))
        sg.set_options(font='Helvitica 12') 

        input_size1 = (400, 10)
        input_size2 = (250, 10)
        text_test_name_size = (17,0)
        multiline_about_size = (50,5)

        from importlib.resources import files
        icon1_file = files('badgescale_ys_plt').joinpath('bidirectional_convert_icon.png')
        print('icon1:', icon1_file)

        tab1= [
                [sg.Text('导入前壳二维码和后壳SN的表格文件')],
                [sg.Input('此处显示选择的文件全路径', disabled=True, enable_events=True, key='-relation_file-'), sg.FileBrowse('上传', key='-upload-')],
                [sg.Sizer(0, 30)],
                [
                    sg.Column([
                        [sg.Text('扫描前壳二维码字符串(注：键盘调到英文输入法)')],
                        [sg.Input('', enable_events=True, key='-front_housing_qrcode-', text_color='red', focus=True)],
                    ]), 
                    sg.Column([[sg.Image(filename=icon1_file)]]), 
                    sg.Column([
                        [sg.Text('自动查询到的模组二维码字符串')],
                        [sg.Input('', disabled=True, key='-module_qrcode-', disabled_readonly_text_color='green'), sg.Button('复制', enable_events=True, key='-copy-')],
                        [sg.Text('自动查询到的模组二维码十六进制')],
                        [sg.Input('', disabled=True, key='-module_qrcode_hex-', disabled_readonly_text_color='blue'), sg.Button('复制', enable_events=True, key='-copy_hex-')],
                    ])
                ],
        ]


        tab2 = [[sg.Text('WIFI热点名称和密码')],
            [sg.Input('此处填写名称', enable_events=True, key='-wifi_ssid-'), sg.Input('此处填写密码', enable_events=True, key='-wifi_pwd-')],
            [sg.Text('模组SN号(注：键盘调到英文输入法)')],
            [sg.Input('', key='-module_sn-', text_color='green')],
            [sg.Text('功能测试')],
            [sg.Text('1.BLE扫描', size = text_test_name_size), sg.Input('此处显示测试结果', readonly=True, key='-ble_test_result-')],
            [sg.Text('2.WIFI上行', size = text_test_name_size), sg.Input('此处显示测试结果', readonly=True, key='-wifi_test_result-')],
            [sg.Text('3.麦克风一致性', size = text_test_name_size), sg.Input('此处显示测试结果', readonly=True, key='-mic_test_result-')],
            [sg.Text('4.三轴加速度计', size = text_test_name_size), sg.Input('此处显示测试结果', readonly=True, key='-3d_sensor_test_result-')],
            [sg.Text('5.充电', size = text_test_name_size), sg.Input('此处显示测试结果', readonly=True, key='-charging_test_result-')],
            [sg.Text('6.上键，下键和OK键', size = text_test_name_size), sg.Input('请人工辅助按压按键', readonly=True, key='-3keys_test_result-')] ,
            [sg.Text('7.喇叭', size = text_test_name_size), sg.Input('请人工听检，然后填写结果', readonly=True, key='-speaker_test_result-'), sg.Radio('合格', 'choice7', default=False, enable_events=True, key='-choice7_pass-'), sg.Radio('不合格', 'choice7', default=True, enable_events=True, key='-choice7_fail-')],
            [sg.Text('8.蜂鸣器', size = text_test_name_size), sg.Input('请人工听检，然后填写结果', readonly=True, key='-buzzer_test_result-'), sg.Radio('合格', 'choice8', default=False, enable_events=True, key='-choice8_pass-'), sg.Radio('不合格', 'choice8', default=True, enable_events=True, key='-choice8_fail-')],
            [sg.Text('9.墨水屏', size = text_test_name_size), sg.Input('请人工目检，然后填写结果', readonly=True, key='-sink_screen_test_result-'), sg.Radio('合格', 'choice9', default=False, enable_events=True, key='-choice9_pass-'), sg.Radio('不合格', 'choice9', default=True, enable_events=True, key='-choice9_fail-')],
            [sg.Text('10.电池', size = text_test_name_size), sg.Input('请人工目检，然后填写结果', readonly=True, key='-battery_test_result-'), sg.Radio('合格', 'choice10', default=False, enable_events=True, key='-choice10_pass-'), sg.Radio('不合格', 'choice10', default=True, enable_events=True, key='-choice10_fail-')],
            [sg.Button('开始测试', enable_events=True, key='-start_test-'), sg.Button('停止测试', enable_events=True, key='-stop_test-', disabled=True)],
            [sg.Text('累计测试报告')],
            [sg.Input('此处显示测试报告', readonly=True, key='-test_report-'), sg.Button('下载报告', enable_events=True, key='-download-')]]
        
        tab3 = [[sg.Text('软件介绍')],
            [sg.Multiline(default_text='此处...', disabled=True, key='-intro-', size = multiline_about_size)],
            [sg.Text('版权声明')],
            [sg.Multiline(default_text='此处...', disabled=True, key='-copyright-', size = multiline_about_size)],
            [sg.Text('联系我们')],
            [sg.Multiline(default_text='此处...', disabled=True, key='-contact-', size = multiline_about_size)]]

        tabgroup1 = sg.TabGroup([[sg.Tab('扫二维码', tab1, key='-tab1-'), 
            sg.Tab('功能测试', tab2, key='-tab2-'),
            sg.Tab('关于', tab3, key='-tab3-')]],
            key='-tabgroup1-', 
            tab_location='lefttop',
            enable_events = True)

        layout = [[tabgroup1]]

        return layout
    
    def copy_module_qrcode(self):
        qrcode = self._window['-module_qrcode-'].get()
        sg.clipboard_set(qrcode)
    
    def copy_module_qrcode_hex(self):
        qrcode_hex = self._window['-module_qrcode_hex-'].get()
        sg.clipboard_set(qrcode_hex)
    

    def get_relation_file(self, file_path):
        '''保存对照表格'''
        self._relation_file = file_path
        print('relation file:%s\n' % (self._relation_file))

    def get_front_housing_qrcode(self, qrcode):
        pass

    def handle_timeout(self, timeout):
        t = self._window['-front_housing_qrcode-'].get()
        sn = self._window['-module_qrcode-'].get()

        if len(t) > 0 and len(sn) == 0 and self._relation_file is not None and len(self._relation_file) > 0:
                '''获取前壳二维码字符串，自动查找对应的SN号二维码'''
                table = SNCSVTableWrapper(self._relation_file)
                sn = table.get_sn(t)
                if sn is None:
                    self._window['-module_qrcode-'].update('未找到对应的SN号！！')
                    self._window['-module_qrcode_hex-'].update('未找到对应的SN号！！')
                else:
                    self._window['-module_qrcode-'].update(sn)
                    
                    hex_str = sn.encode('utf-8').hex()
                    self._window['-module_qrcode_hex-'].update(hex_str)
        
        if len(t) > 0 and len(sn) > 0:
            self._timeout_sum = self._timeout_sum + timeout
        
        '''连续N秒没有长码值变化时，清空'''
        if self._timeout_sum > 6 * 1000:
            self._window['-module_qrcode-'].update('')
            self._window['-module_qrcode_hex-'].update('')
            self._window['-front_housing_qrcode-'].update('')
            self._timeout_sum = 0
        
    def jpg2base64(self):
        from base64 import b64encode, b64decode
        with open('bothlent_corporation_logo.jpg', 'rb') as f:
            base64_data = b64encode(f.read())  # b64encode是编码
        return base64_data
    
    def _function_test_flow_entry(self):
        upload_speed_threshold = 1 # Mb/s

        while True:
            prior = self._proto.request_functiontest_start()
            print('prior ret:', prior)

            ret = self._proto.request_functiontest_ble_start()
            
            ble = BLEWrapper()
            ret = ble.do_connect(ret, '')
            if prior==0 and ret:
                self._window['-ble_test_result-'].update(value='Pass')
            else:
                self._window['-ble_test_result-'].update(value='Fail')

            ssid = self._window['-wifi_ssid-'].get()
            pwd = self._window['-wifi_pwd-'].get()
            ret = self._proto.request_functiontest_wifi_set(ssid.strip(), pwd.strip())
            if ret == 0:
                ret1 = self._proto.request_functiontest_wifi_start(self._iperf_server_addr[0], self._iperf_server_addr[1])
                #print('note tx speed:', ret1)
                if prior==0 and ret1 >= upload_speed_threshold:
                    self._window['-wifi_test_result-'].update(value='Pass')
                else:
                    self._window['-wifi_test_result-'].update(value='Fail')
            else:
                self._window['-wifi_test_result-'].update(value='Fail')

            ret = self._proto.request_functiontest_record_start(self._http_file_server_addr[0], self._http_file_server_addr[1])
            if prior==0 and len(ret) > 0:
                # process_alg(ret)
                self._window['-mic_test_result-'].update(value='Pass')
            else:
                self._window['-mic_test_result-'].update(value='Fail')    
            
            ret = self._proto.request_functiontest_3dsensor_start()
            if prior==0 and ret == 0:
                self._window['-3d_sensor_test_result-'].update(value='Pass')
            else:
                self._window['-3d_sensor_test_result-'].update(value='Fail')
            
            ret = self._proto.request_functiontest_charging_start()
            if prior==0 and ret == 0:
                self._window['-charging_test_result-'].update(value='Pass')
            else:
                self._window['-charging_test_result-'].update(value='Fail')
            
            ret = self._proto.request_functiontest_3key_start()
            if prior==0 and ret == 0:
                self._window['-3keys_test_result-'].update(value='Pass')
            else:
                self._window['-3keys_test_result-'].update(value='Fail')

            url = 'http://%s:%d/%s' % (self._http_file_server_addr[0], self._http_file_server_addr[1], self._speaker_sample)
            ret = self._proto.request_functiontest_speaker_start(url)

            ret = self._proto.request_functiontest_buzzer_start()

            ret = self._proto.request_functiontest_stop()

            break

        self._event1.set()

    def start_test(self):
        self._event1.clear()

        self._window['-ble_test_result-'].update(value='')
        self._window['-wifi_test_result-'].update(value='')
        self._window['-mic_test_result-'].update(value='')
        self._window['-3d_sensor_test_result-'].update(value='')
        self._window['-charging_test_result-'].update(value='')
        self._window['-3keys_test_result-'].update(value='')
        self._window['-speaker_test_result-'].update(value='')
        self._window['-buzzer_test_result-'].update(value='')
        self._window['-sink_screen_test_result-'].update(value='')
        self._window['-battery_test_result-'].update(value='')

        self._window['-choice7_pass-'].update(value=False)
        self._window['-choice8_pass-'].update(value=False)
        self._window['-choice9_pass-'].update(value=False)
        self._window['-choice10_pass-'].update(value=False)
        
        self._window['-choice7_fail-'].update(value=True)
        self._window['-choice8_fail-'].update(value=True)
        self._window['-choice9_fail-'].update(value=True)
        self._window['-choice10_fail-'].update(value=True)
        
        self._thread1 = threading.Thread(target = self._function_test_flow_entry, name='function test flow thread')
        self._thread1.start()

        self._window['-start_test-'].update(disabled=True)
        self._window['-stop_test-'].update(disabled=False)

    def stop_test(self):
        self._event1.wait()

        if self._window['-ble_test_result-'].get() == 'Pass' and \
            self._window['-wifi_test_result-'].get() == 'Pass' and \
            self._window['-mic_test_result-'].get() == 'Pass' and \
            self._window['-3d_sensor_test_result-'].get() == 'Pass' and \
            self._window['-charging_test_result-'].get() == 'Pass' and \
            self._window['-3keys_test_result-'].get() == 'Pass' and \
            self._window['-speaker_test_result-'].get() == 'Pass' and \
            self._window['-buzzer_test_result-'].get() == 'Pass' and \
            self._window['-sink_screen_test_result-'].get() == 'Pass' and \
            self._window['-battery_test_result-'].get() == 'Pass':
            
            sg.popup_ok('功能测试:Pass')
        else:
            sg.popup_ok('功能测试:Fail')
        
        self._window['-start_test-'].update(disabled=False)
        self._window['-stop_test-'].update(disabled=True)
    
    def run(self):
        self._http_file_server_addr = HttpFileUploadDownloadWrapper.start_server()
        self._iperf_server_addr = IperfWrapper.start_server()
        self._proto = ProtoWrapper('', 115200, '8', '1', 'N', True)
        self._proto.start_read()

        layout = self.make_layout()
        self._window = sg.Window('badgescale_ys_plt', layout)

        while True:
            '''空闲timer累积N毫秒，触发timer事件'''
            timeout_set = 1000
            event, values = self._window.read(timeout=timeout_set, timeout_key=sg.TIMEOUT_KEY)
            #print(event, values, '\n')
            if event == sg.WIN_CLOSED:
                break
            elif event == '-copy-':
                self.copy_module_qrcode()
            elif event == '-copy_hex-':
                self.copy_module_qrcode_hex()
            elif event == '-relation_file-':
                self.get_relation_file(values['-relation_file-'])
            elif event == '-front_housing_qrcode-':
                self.get_front_housing_qrcode(values['-front_housing_qrcode-'])
            elif event == sg.TIMEOUT_KEY:
                self.handle_timeout(timeout_set)
            elif event == '-start_test-':
                self.start_test()
                pass
            elif event == '-stop_test-':
                self.stop_test()
                pass
            elif event == '-choice7_pass-':
                self._window['-speaker_test_result-'].update(value='Pass')
            elif event == '-choice8_pass-':
                self._window['-buzzer_test_result-'].update(value='Pass')
            elif event == '-choice9_pass-':
                self._window['-sink_screen_test_result-'].update(value='Pass')      
            elif event == '-choice10_pass-':
                self._window['-battery_test_result-'].update(value='Pass')
            elif event == '-choice7_fail-':
                self._window['-speaker_test_result-'].update(value='Fail')
            elif event == '-choice8_fail-':
                self._window['-buzzer_test_result-'].update(value='Fail')
            elif event == '-choice9_fail-':
                self._window['-sink_screen_test_result-'].update(value='Fail')
            elif event == '-choice10_fail-':
                self._window['-battery_test_result-'].update(value='Fail')
            
        self._window.close()
        self._proto.stop_read()
        HttpFileUploadDownloadWrapper.stop_server()
        IperfWrapper.stop_server()

def sample():
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)-15s %(name)-8s %(levelname)s: %(message)s",
    )

    app = MainWindow()
    app.run()


if __name__ == "__main__":
    sample()