"""这是一个封装WAV音频播放的模块。
它依赖软件包 pyaudio。
"""
import time
import os
import sys
import pyaudio
import wave
import asyncio
from uuid import uuid1
from datetime import datetime

class AudioPlayback(object):
    """Open speaker device.
    Then play the stream data.
    """
    def __init__(self):
        self._local_path = ''
        self._wf = None
        self._p = None
        self._stream = None

    @property
    def local_path(self):
        return self._local_path

    @local_path.setter
    def local_path(self, path):
        self._local_path = path
        
    def start_playback(self):
        self._wf = wave.open(self._local_path, 'rb')
        self._p = pyaudio.PyAudio()

        self._stream = self._p.open(format=self._p.get_format_from_width(self._wf.getsampwidth()),
                        channels=self._wf.getnchannels(),
                        rate=self._wf.getframerate(),
                        output=True,
                        stream_callback=self._stream_callback)
        
        self._stream.start_stream()
        return True

    def stop_playback(self):
        while self._stream.is_active():
            time.sleep(0.1)
        
        self._stream.stop_stream()
        self._stream.close()
        self._wf.close()
        self._p.terminate()
        return True

    def _stream_callback(self, in_data, frame_count, time_info, status):
        data = self._wf.readframes(frame_count)
        return data, pyaudio.paContinue


if __name__ == "__main__":
    ap = AudioPlayback()

    from importlib.resources import files
    ap.local_path = files('badgescale_ys_plt').joinpath('mic_utils/vibration.wav').__str__()
    print(ap.local_path)

    ap.start_playback()
    ap.stop_playback()