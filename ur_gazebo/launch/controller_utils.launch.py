import launch
import launch.actions 
import launch.substitutions 
import launch_ros.actions
import os

from launch_ros.actions import Node

def generate_launch_description():
  
  return launch.LaunchDescription([
    Node(package='robot_state_publisher', node_executable='robot_state_publisher',
          arguments=['--help'],
          output='screen'),
  ])
