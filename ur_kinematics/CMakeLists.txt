cmake_minimum_required(VERSION 3.3)
cmake_policy(SET CMP0057 NEW)
project(ur_kinematics)

add_compile_options(-std=c++11)

find_package(ament_cmake REQUIRED)

find_package(rclcpp)
find_package(geometry_msgs)
find_package(moveit_core)
find_package(moveit_kinematics)
find_package(moveit_ros_planning)
find_package(pluginlib)
find_package(tf_conversions)

find_package(Boost REQUIRED COMPONENTS system)

ament_export_dependencies(roscpp geometry_msgs moveit_core moveit_kinematics moveit_ros_planning
    pluginlib tf_conversions Boost)
ament_export_include_directories(include)
ament_export_libraries(ur3_kin ur5_kin ur10_kin ur3_moveit_plugin ur5_moveit_plugin ur10_moveit_plugin)
ament_package()


###########
## Build ##
###########

include_directories(SYSTEM ${Boost_INCLUDE_DIR})
include_directories(include ${rclcpp_INCLUDE_DIRS} ${geometry_msgs_INCLUDE_DIRS} ${moveit_core_INCLUDE_DIRS} ${moveit_kinematics_INCLUDE_DIRS} ${moveit_ros_planning_INCLUDE_DIRS} ${pluginlib_INCLUDE_DIRS} ${tf_conversions_INCLUDE_DIRS})

add_library(ur3_kin src/ur_kin.cpp)
set_target_properties(ur3_kin PROPERTIES COMPILE_DEFINITIONS "UR3_PARAMS")

add_library(ur5_kin src/ur_kin.cpp)
set_target_properties(ur5_kin PROPERTIES COMPILE_DEFINITIONS "UR5_PARAMS")

add_library(ur10_kin src/ur_kin.cpp)
set_target_properties(ur10_kin PROPERTIES COMPILE_DEFINITIONS "UR10_PARAMS")

SET(LIBS_ALL ${rclcpp_LIBRARIES} ${geometry_msgs_LIBRARIES} ${moveit_core_LIBRARIES} ${moveit_kinematics_LIBRARIES} ${moveit_ros_planning_LIBRARIES} ${pluginlib_LIBRARIES} ${tf_conversions_LIBRARIES})

add_library(ur3_moveit_plugin src/ur_moveit_plugin.cpp)
set_target_properties(ur3_moveit_plugin PROPERTIES COMPILE_DEFINITIONS "UR3_PARAMS")
target_link_libraries(ur3_moveit_plugin
  ${LIBS_ALL}
  ${Boost_LIBRARIES}
  ur3_kin)

add_library(ur5_moveit_plugin src/ur_moveit_plugin.cpp)
set_target_properties(ur5_moveit_plugin PROPERTIES COMPILE_DEFINITIONS "UR5_PARAMS")
target_link_libraries(ur5_moveit_plugin
  ${LIBS_ALL}
  ${Boost_LIBRARIES}
  ur5_kin)

add_library(ur10_moveit_plugin src/ur_moveit_plugin.cpp)
set_target_properties(ur10_moveit_plugin PROPERTIES COMPILE_DEFINITIONS "UR10_PARAMS")
target_link_libraries(ur10_moveit_plugin
  ${LIBS_ALL}
  ${Boost_LIBRARIES}
  ur10_kin)


#############
## Install ##
#############

install(TARGETS ur3_kin ur5_kin ur10_kin ur3_moveit_plugin ur5_moveit_plugin ur10_moveit_plugin
  ARCHIVE DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
  LIBRARY DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
  RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

# install header files
install(DIRECTORY include/${PROJECT_NAME}/
  DESTINATION ${CATKIN_PACKAGE_INCLUDE_DESTINATION}
)

# install moveit plugin description file
install(FILES ur_moveit_plugins.xml
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)
