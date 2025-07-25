#include <memory>
#include "rclcpp/rclcpp.hpp"
#include "geometry_msgs/msg/twist.hpp"

class URTeleopNode : public rclcpp::Node
{
public:
  URTeleopNode() : Node("ur_teleop_node")
  {
    using std::placeholders::_1;
    sub_ = this->create_subscription<geometry_msgs::msg::Twist>(
      "cmd_vel", 10, std::bind(&URTeleopNode::twist_callback, this, _1));
    pub_ = this->create_publisher<geometry_msgs::msg::Twist>("cmd_vel_out", 10);
  }

private:
  void twist_callback(const geometry_msgs::msg::Twist::SharedPtr msg)
  {
    RCLCPP_INFO(this->get_logger(), "Received cmd_vel: linear=%.2f angular=%.2f",
                msg->linear.x, msg->angular.z);
    pub_->publish(*msg);
  }

  rclcpp::Subscription<geometry_msgs::msg::Twist>::SharedPtr sub_;
  rclcpp::Publisher<geometry_msgs::msg::Twist>::SharedPtr pub_;
};

int main(int argc, char **argv)
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<URTeleopNode>());
  rclcpp::shutdown();
  return 0;
}
