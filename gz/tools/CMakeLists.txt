add_library(image_converter SHARED image_converter.cpp image_converter.hpp)
target_link_libraries(image_converter ${OpenCV_LIBRARIES})
install(TARGETS image_converter DESTINATION ${PROJECT_SOURCE_DIR}/bin)


add_executable(test_convert test.cpp)
target_link_libraries(test_convert  ${OpenCV_LIBRARIES} image_converter)