# Architecture Overview

- **Unity** (C#) ←→ **ROS 2** (rclpy / rclcpp) via ROS‑TCP‑Connector  
- **Data logging**: In‑Unity PNG + CSV writer, ROS 2 rosbag2 recorder  
- **RL envs**: Isaac Sim & Isaac Gym templates under `/rl_envs`
