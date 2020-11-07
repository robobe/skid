
        
add_library(ArduPilotPlugin SHARED ardupilot/ArduPilotPlugin.cc)
target_link_libraries(ArduPilotPlugin ${GAZEBO_LIBRARIES})
install(TARGETS ArduPilotPlugin DESTINATION ${PROJECT_SOURCE_DIR}/bin)

add_library(gst_camera_plugin SHARED gst_camera/gst_camera_plugin.cpp)
target_include_directories(gst_camera_plugin PRIVATE ${GST_INCLUDE_DIRS})
target_link_libraries(gst_camera_plugin ${GAZEBO_LIBRARIES} ${GST_LIBRARIES} ${OpenCV_LIBRARIES}) 
install(TARGETS gst_camera_plugin DESTINATION ${PROJECT_SOURCE_DIR}/bin)

add_library(RealSensePlugin SHARED real_sense/RealSensePlugin.cc)
target_link_libraries(RealSensePlugin ${GAZEBO_libraries})
install(TARGETS RealSensePlugin DESTINATION ${PROJECT_SOURCE_DIR}/bin)