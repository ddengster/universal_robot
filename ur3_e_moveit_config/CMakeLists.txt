cmake_minimum_required(VERSION 3.3)
cmake_policy(SET CMP0057 NEW)
project(ur3_e_moveit_config)

find_package(ament_cmake REQUIRED)

ament_package()

#if (BUILD_TESTING)
#  find_package(ros2launch REQUIRED)
#  roslaunch_add_file_check(tests/moveit_planning_execution.xml)
#endif()

install(DIRECTORY launch DESTINATION share/${PROJECT_NAME})
install(DIRECTORY config DESTINATION share/${PROJECT_NAME})
