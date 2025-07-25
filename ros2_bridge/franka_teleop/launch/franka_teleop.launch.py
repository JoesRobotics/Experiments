from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='franka_teleop',
            executable='franka_teleop_node',
            name='franka_teleop_node',
            output='screen'
        )
    ])

