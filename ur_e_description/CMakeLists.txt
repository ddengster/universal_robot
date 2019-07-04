cmake_minimum_required(VERSION 3.3)
cmake_policy(SET CMP0057 NEW)
project(ur_e_description)

find_package(ament_cmake REQUIRED)
ament_package()

install(DIRECTORY launch DESTINATION share/${PROJECT_NAME})
install(DIRECTORY urdf DESTINATION share/${PROJECT_NAME})
install(DIRECTORY meshes DESTINATION share/${PROJECT_NAME})
