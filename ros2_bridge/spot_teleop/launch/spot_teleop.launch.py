from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='spot_teleop',
            executable='spot_teleop_node',
            name='spot_teleop_node',
            output='screen'
        )
    ])

