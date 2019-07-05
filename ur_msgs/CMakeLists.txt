cmake_minimum_required(VERSION 3.3)
cmake_policy(SET CMP0057 NEW)
project(ur_msgs)

find_package(ament_cmake REQUIRED)
find_package(std_msgs REQUIRED)
find_package(rosidl_default_generators REQUIRED)


## Generate messages and services with any dependencies listed here
rosidl_generate_interfaces(
   ${PROJECT_NAME}
   msg/Analog.msg
   msg/Digital.msg
   msg/IOStates.msg
   msg/RobotStateRTMsg.msg
   msg/MasterboardDataMsg.msg
   msg/RobotModeDataMsg.msg
   msg/ToolDataMsg.msg
   srv/SetPayload.srv
   srv/SetIO.srv
   DEPENDENCIES
   std_msgs
)

ament_export_dependencies(rosidl_default_runtime std_msgs)
ament_package()
