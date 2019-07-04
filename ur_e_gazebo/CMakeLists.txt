cmake_minimum_required(VERSION 3.3)
cmake_policy(SET CMP0057 NEW)
project(ur_e_gazebo)

find_package(ament_cmake REQUIRED)

ament_package()

#if (BUILD_TESTING)
#  find_package(ros2launch REQUIRED)
#  roslaunch_add_file_check(tests/roslaunch_test.xml)
#endif()

install(DIRECTORY launch controller DESTINATION share/${PROJECT_NAME})
