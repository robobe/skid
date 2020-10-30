#include <opencv2/opencv.hpp>
#include <iostream>

using namespace cv;
using namespace std;

int main()
{
    VideoCapture cap("/dev/video2");
	
    if (!cap.isOpened()) {
        cerr <<"VideoCapture not opened"<<endl;
        exit(-1);
    }

	VideoWriter writer(
		// "appsrc ! videoconvert ! video/x-raw,format=YUY2,width=640,height=480,framerate=30/1 ! jpegenc ! rtpjpegpay ! udpsink host=127.0.0.1 port=5000", 
        "appsrc ! videoconvert ! video/x-raw,format=YUY2,width=640,height=480,framerate=20/1 ! v4l2sink device=/dev/video4",
        0,		// fourcc 
		20,		// fps
		Size(640, 480), 
		true);	// isColor

    if (!writer.isOpened()) {
        cerr <<"VideoWriter not opened"<<endl;
        exit(-1);
    }

    while (true) {

        Mat frame;

        cap.read(frame);

        writer.write(frame);
    }

    return 0;
}


