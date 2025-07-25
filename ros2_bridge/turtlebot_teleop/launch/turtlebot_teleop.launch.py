from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='turtlebot_teleop',
            executable='turtlebot_teleop_node',
            name='turtlebot_teleop_node',
            output='screen'
        )
    ])

