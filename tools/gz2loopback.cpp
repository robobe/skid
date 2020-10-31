// https://answers.gazebosim.org//question/14619/how-to-convert-gazebos-constimagestamped-to-cvmat/
#include <string>
#include <vector>

#include <gazebo/gazebo_config.h>
#include <gazebo/gazebo_client.hh>
#include <gazebo/msgs/msgs.hh>
#include <gazebo/transport/transport.hh>

#include <opencv2/opencv.hpp>
#include <opencv2/core/core.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/features2d/features2d.hpp>

#define IMAGE_TOPIC "/gazebo/default/skid/rover_ardupilot/cam_link/chase_cam/image"

std::string device;
cv::VideoWriter writer;

std::string getCmdOption(int argc, char* argv[], 
    const std::string& option,
    const std::string& value)
{
    std::string cmd = value;
     for( int i = 0; i < argc; ++i)
     {
          std::string arg = argv[i];
          if(0 == arg.find(option))
          {
               std::size_t found = arg.find_last_of(option);
               cmd =arg.substr(found + 1);
               return cmd;
          }
     }
     return cmd;
}

void cb(ConstImageStampedPtr &msg)
{
    // std::cout << msg->image().width() << std::endl;
    // std::cout << msg->image().height() << std::endl;
    // std::cout << msg->image().pixel_format() << std::endl;
    // std::cout << std::endl;

    int width;
    int height;
    char *data;

    width = (int) msg->image().width();
    height = (int) msg->image().height();
    data = new char[msg->image().data().length() + 1];

    memcpy(data, msg->image().data().c_str(), msg->image().data().length());
    cv::Mat image(height, width, CV_8UC3, data);
    writer.write(image);
    cv::imshow(device, image);
    cv::waitKey(1);
    delete data;  // DO NOT FORGET TO DELETE THIS, 
                  // ELSE GAZEBO WILL TAKE ALL YOUR MEMORY
}


int main(int argc, char **argv)
{
    gazebo::client::setup(argc, argv);
    gazebo::transport::NodePtr node(new gazebo::transport::Node());
    gazebo::transport::SubscriberPtr sub;

    std::string topic = getCmdOption(argc, argv, "-topic=", IMAGE_TOPIC);
    device = getCmdOption(argc, argv, "-device=", "/dev/video4");
    // setup
    node->Init();
    sub = node->Subscribe(topic, cb);

    /*
    gst-launch-1.0 udpsrc port=5000 \
    ! application/x-rtp,media=video,payload=26,clock-rate=90000,encoding-name=JPEG,framerate=20/1 \
    ! rtpjpegdepay \
    ! jpegdec \
    ! videoconvert \
    ! autovideosink
    */
    writer = cv::VideoWriter(
		"appsrc ! videoconvert ! video/x-raw,format=YUY2,width=640,height=480,framerate=20/1 ! jpegenc ! rtpjpegpay ! udpsink host=127.0.0.1 port=5000", 
        //"appsrc ! videoconvert ! video/x-raw,format=YUY2,width=640,height=480,framerate=20/1 ! v4l2sink device=/dev/video4",
        0,		// fourcc 
		20,		// fps
		cv::Size(640, 480), 
		true);	// isColor
    
    if (!writer.isOpened()) {
        std::cerr <<"VideoWriter not opened"<<std::endl;
        exit(-1);
    }

    // loop
    while (true) {
        gazebo::common::Time::MSleep(10);
    }

    // clean up
    gazebo::client::shutdown();

    return 0;
}