find_package(OpenCV REQUIRED)
include_directories(
        ${PROJECT_SOURCE_DIR}
        include
        ${OpenCV_INCLUDE_DIRS}
        )

link_libraries(
        ${OpenCV_LIBRARIES}
        )


add_executable(cv_cpp cv/cv_cpp.cpp)
target_link_libraries(cv_cpp ${OpenCV_LIBRARIES})

add_executable(cv_gst_sender cv/cv_gst_sender.cpp)
target_link_libraries(cv_gst_sender ${OpenCV_LIBRARIES})

add_executable(cv_gst_reader cv/cv_gst_reader.cpp)
target_link_libraries(cv_gst_reader ${OpenCV_LIBRARIES})

