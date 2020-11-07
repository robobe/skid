from threading import Thread
import traceback
import logging
import cv2


class GstStream(Thread):
    def __init__(self):
        super(GstStream,self).__init__(name="video", daemon=True, target=self.run)
        self.__port = 5000
        self.__open_stream()
        self.__frame = None
        self.__grabbed = False

    def __open_stream(self):
        pipe = self.__get_pipe()
        try:
            self.__cap = cv2.VideoCapture(pipe, cv2.CAP_GSTREAMER)
        except:
            raise

    def __get_pipe(self):
        pipe = f"udpsrc port={self.__port} \
        ! application/x-rtp,media=video,payload=26,clock-rate=90000,encoding-name=JPEG,framerate=20/1 \
        ! rtpjpegdepay \
        ! jpegdec \
        ! videoconvert \
        ! appsink"

        return pipe

    def run(self):
        while True:
            self.__grabbed, self.__frame = self.__cap.read()

    def read(self):
        return self.__grabbed, self.__frame
