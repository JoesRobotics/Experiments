# ROS 2 Teleop Bridge

This folder contains ROS 2 packages that act as simple bridges for controlling different robots from Unity. Each package exposes a node that subscribes to the `cmd_vel` topic and republishes the message on `cmd_vel_out` after logging the received command.

Packages:
- **spot_teleop**
- **franka_teleop**
- **turtlebot_teleop**
- **ur_teleop**

## Building
```bash
cd ros2_bridge
colcon build --symlink-install
```

## Example Usage
Launch a teleop node (e.g. Spot):
```bash
ros2 launch spot_teleop spot_teleop.launch.py
```

Then in a separate terminal publish test velocity commands:
```bash
python3 scripts/publish_cmd_vel.py
```
Each teleop package has an equivalent launch file.

### Franka Vive Teleop Script

For direct control of a Franka arm with Vive controllers, a helper script is
available:

```bash
python3 scripts/franka_vive_teleop.py [--use-fake-hw] [--debug]
```

By default the script connects to the real robot topic. Pass `--use-fake-hw`
to target the MuJoCo/fake-hardware endpoint instead. Use `--debug` to enable
additional logging that can help diagnose issues.

