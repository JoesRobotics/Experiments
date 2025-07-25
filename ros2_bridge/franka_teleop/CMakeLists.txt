cmake_minimum_required(VERSION 3.5)
project(franka_teleop)

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(std_msgs REQUIRED)

add_executable(franka_teleop_node src/franka_teleop_node.cpp)
ament_target_dependencies(franka_teleop_node
  rclcpp sensor_msgs geometry_msgs std_msgs
)
target_compile_features(franka_teleop_node PUBLIC cxx_std_17)
install(TARGETS franka_teleop_node
  DESTINATION lib/${PROJECT_NAME}
)
install(DIRECTORY launch DESTINATION share/${PROJECT_NAME})


ament_package()
