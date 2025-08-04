#!/usr/bin/env python3
import argparse

REAL_FRANKA_TOPIC = "/franka/command"
FAKE_FRANKA_TOPIC = "/mujoco/franka/command"


def parse_args():
    parser = argparse.ArgumentParser(description="Teleoperate the Franka arm using Vive controllers")
    parser.add_argument(
        "--franka-topic",
        type=str,
        default=None,
        help="ROS topic used to command the Franka arm",
    )
    parser.add_argument(
        "--use-fake-hw",
        action="store_true",
        help="Use the MuJoCo/fake-hardware endpoint instead of the real robot",
    )
    args = parser.parse_args()

    if args.franka_topic:
        franka_topic = args.franka_topic
    else:
        franka_topic = FAKE_FRANKA_TOPIC if args.use_fake_hw else REAL_FRANKA_TOPIC

    mode = "fake hardware" if args.use_fake_hw else "real robot"
    print(f"Starting Franka Vive teleop in {mode} mode using topic '{franka_topic}'")
    return args, franka_topic


def main():
    _, _ = parse_args()
    # Placeholder for actual teleoperation logic.


if __name__ == "__main__":
    main()
