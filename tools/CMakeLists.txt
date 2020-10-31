find_package(gazebo REQUIRED)
find_package(OpenCV REQUIRED)

include_directories(
    ${GAZEBO_INCLUDE_DIRS}
    ${OpenCV_INCLUDE_DIRS}
    )
link_directories(
    ${GAZEBO_LIBRARY_DIRS}
    ${OpenCV_LIBRARIES}
    )

list(APPEND CMAKE_CXX_FLAGS "${GAZEBO_CXX_FLAGS}")

add_executable(gz2loopback gz2loopback.cpp)
target_link_libraries(gz2loopback ${GAZEBO_LIBRARIES} ${OpenCV_LIBRARIES} pthread)
install(TARGETS gz2loopback DESTINATION ${PROJECT_SOURCE_DIR}/bin)