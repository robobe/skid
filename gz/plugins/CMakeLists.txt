find_package(gazebo REQUIRED)
find_package(OpenCV REQUIRED)
pkg_check_modules(GST REQUIRED gstreamer-1.0>=1.8)
include_directories(
        ${PROJECT_SOURCE_DIR}
        include
        ${GAZEBO_INCLUDE_DIRS}
        ${OpenCV_INCLUDE_DIRS}
        ${GSTREAMER_INCLUDE_DIRS}
        )

link_libraries(
        ${GAZEBO_LIBRARIES}
        ${OpenCV_LIBRARIES}
        ${GSTREAMER_LIBRARIES}
        ${GLIB_LDFLAGS}
        gobject-2.0
        )
        
add_library(ArduPilotPlugin SHARED ardupilot/ArduPilotPlugin.cc)
target_link_libraries(ArduPilotPlugin ${GAZEBO_LIBRARIES})
install(TARGETS ArduPilotPlugin DESTINATION ${PROJECT_SOURCE_DIR}/bin)

add_library(gst_camera_plugin SHARED gst_camera/gst_camera_plugin.cpp)
target_include_directories(gst_camera_plugin PRIVATE ${GST_INCLUDE_DIRS})
target_link_libraries(gst_camera_plugin ${GAZEBO_LIBRARIES} ${GST_LIBRARIES} ${OpenCV_LIBRARIES}) 
install(TARGETS gst_camera_plugin DESTINATION ${PROJECT_SOURCE_DIR}/bin)
