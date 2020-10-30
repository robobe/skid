#include <opencv2/opencv.hpp>
#include <iostream>

using namespace std;
using namespace cv;

int main()
{
    // "udpsrc port=5000 ! application/x-rtp,media=video,payload=26,clock-rate=90000,encoding-name=JPEG,framerate=30/1 ! rtpjpegdepay ! jpegdec ! videoconvert ! appsink"
    string pipe = "videotestsrc ! videoconvert ! appsink";
	VideoCapture cap(pipe, CAP_GSTREAMER);
    
	if (!cap.isOpened()) {
        cerr <<"VideoCapture not opened"<<endl;
        exit(-1);
    }
    
    while (true) {

        Mat frame;

        cap.read(frame);

        imshow("receiver", frame);

        if (waitKey(1) == 27) {
            break;
        }
    }

    return 0;
}
