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

add_subdirectory(tools)
add_subdirectory(plugins)
