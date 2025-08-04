import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped
from std_msgs.msg import Float32
from control_msgs.msg import GripperCommand


class ManusFrankaBridge(Node):
    def __init__(self):
        super().__init__('manus_franka_bridge')
        # Subscribe to Manus glove pose and pinch topics
        self.pose_sub = self.create_subscription(
            PoseStamped, '/manus_glove/pose', self.pose_callback, 10
        )
        self.pinch_sub = self.create_subscription(
            Float32, '/manus_glove/pinch', self.pinch_callback, 10
        )

        # Publishers for Franka Cartesian pose and Robotiq gripper command
        self.pose_pub = self.create_publisher(
            PoseStamped, '/franka_cartesian_pose_cmd', 10
        )
        self.gripper_pub = self.create_publisher(
            GripperCommand, '/robotiq_gripper/command', 10
        )

        # Maximum gripper width for Robotiq (meters)
        self.max_grip_width = 0.085

    def pose_callback(self, msg: PoseStamped) -> None:
        """Forward glove pose to the Franka pose command topic."""
        self.pose_pub.publish(msg)

    def pinch_callback(self, msg: Float32) -> None:
        """Map glove pinch value [0,1] to gripper width and publish."""
        pinch = max(0.0, min(1.0, msg.data))
        command = GripperCommand()
        # pinch 1.0 -> closed (width 0), pinch 0.0 -> open (max width)
        command.position = self.max_grip_width * (1.0 - pinch)
        command.max_effort = 40.0
        self.gripper_pub.publish(command)


def main(args=None):
    rclpy.init(args=args)
    node = ManusFrankaBridge()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
