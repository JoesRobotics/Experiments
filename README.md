# Experiments

## Overview
This repo hosts:
- **unity/**: Unity 2021.3 LTS project scaffold (scene “TeleopDemo”)
- **ros2_bridge/**: ROS 2 Humble packages to bridge teleop for Spot, Franka, UR, TurtleBot
- **rl_envs/**: Basic Python gym environments and training examples
- **docs/**: Architecture & setup guides

## Getting Started
1. Clone:
   ```bash
   git clone https://github.com/JoesRobotics/Experiments.git
   ```
2. Unity:
   - Open `Experiments/unity` with Unity 2021.3 LTS.
3. ROS 2:
   ```bash
 cd Experiments/ros2_bridge
 colcon build
 ```
4. RL Environments:
   ```bash
   cd Experiments/rl_envs
   python3 example_train.py
   ```
5. Launch a teleop node:
   ```bash
   ros2 launch spot_teleop spot_teleop.launch.py
   ```
   Publish commands from another terminal:
   ```bash
   python3 ros2_bridge/scripts/publish_cmd_vel.py
   ```
6. See `/docs/architecture.md` for details.

