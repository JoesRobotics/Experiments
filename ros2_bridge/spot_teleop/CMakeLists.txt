cmake_minimum_required(VERSION 3.5)
project(spot_teleop)

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(std_msgs REQUIRED)

add_executable(spot_teleop_node src/spot_teleop_node.cpp)
ament_target_dependencies(spot_teleop_node
  rclcpp sensor_msgs geometry_msgs std_msgs
)

install(TARGETS spot_teleop_node
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()
