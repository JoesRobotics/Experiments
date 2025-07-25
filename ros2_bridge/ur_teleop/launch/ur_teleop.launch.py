from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='ur_teleop',
            executable='ur_teleop_node',
            name='ur_teleop_node',
            output='screen'
        )
    ])

