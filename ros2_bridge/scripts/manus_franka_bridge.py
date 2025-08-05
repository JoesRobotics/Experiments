import math

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped
from control_msgs.msg import GripperCommand


class ManusFrankaBridge(Node):
    def __init__(self):
        super().__init__('manus_franka_bridge')
        # Subscribe to Manus glove pose and finger tip topics
        self.pose_sub = self.create_subscription(
            PoseStamped, '/manus_glove/pose', self.pose_callback, 10
        )
        self.thumb_sub = self.create_subscription(
            PoseStamped, '/manus_glove/thumb_tip', self.thumb_callback, 10
        )
        self.index_sub = self.create_subscription(
            PoseStamped, '/manus_glove/index_tip', self.index_callback, 10
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
        # Distance under which a pinch is considered closed (meters)
        self.pinch_threshold = 0.02
        self.thumb_pose: PoseStamped | None = None
        self.index_pose: PoseStamped | None = None

    def pose_callback(self, msg: PoseStamped) -> None:
        """Forward glove pose to the Franka pose command topic."""
        self.pose_pub.publish(msg)

    def thumb_callback(self, msg: PoseStamped) -> None:
        self.thumb_pose = msg
        self.update_pinch()

    def index_callback(self, msg: PoseStamped) -> None:
        self.index_pose = msg
        self.update_pinch()

    def update_pinch(self) -> None:
        if self.thumb_pose is None or self.index_pose is None:
            return
        dx = self.thumb_pose.pose.position.x - self.index_pose.pose.position.x
        dy = self.thumb_pose.pose.position.y - self.index_pose.pose.position.y
        dz = self.thumb_pose.pose.position.z - self.index_pose.pose.position.z
        distance = math.sqrt(dx * dx + dy * dy + dz * dz)
        pinch = max(0.0, min(1.0, (self.pinch_threshold - distance) / self.pinch_threshold))
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
