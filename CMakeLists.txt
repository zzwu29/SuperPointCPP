cmake_minimum_required(VERSION 3.0 FATAL_ERROR)
project(superpoint_cpp)

# set(CMAKE_CXX_STANDARD 11)

find_package(Torch REQUIRED)
find_package(OpenCV REQUIRED)

include_directories(
    ${PROJECT_SOURCE_DIR}
    ${PROJECT_SOURCE_DIR}/include
    ${TORCH_INCLUDE_DIRS}
    ${OpenCV_LIBS}
)

# add_library(${PROJECT_NAME} SHARED   
# ERROR on Windows
# if lib do not export, it cannot be set to "SHARED"
# https://blog.csdn.net/LaineGates/article/details/108242803

add_library(${PROJECT_NAME} STATIC
    src/NetWork.cpp
    src/PointTracker.cpp
    src/SuperPointFrontend.cpp
    # include/NetWork.h
    # include/PointTracker.h
    # include/SuperPointFrontend.h
)
target_link_libraries(${PROJECT_NAME}
    ${OpenCV_LIBS}
    ${TORCH_LIBRARIES}
)

add_executable(superpoint detectPoints.cpp)
target_link_libraries(superpoint ${PROJECT_NAME})
set_property(TARGET superpoint PROPERTY CXX_STANDARD 14)
