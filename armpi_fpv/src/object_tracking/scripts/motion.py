import atexit
import sys
import time

sys.path.append("/home/pi/ArmPi/")

import HiwonderSDK.Board as Board  # noqa
import ArmIK.ArmMoveIK as arm_ik  # noqa
import ArmIK.Transform as transform  # noqa


def set_rgb(color: str):
    """
    set the color of the RGB with passed in variable
    """
    match color:
        case "red":
            Board.RGB.setPixelColor(0, Board.PixelColor(255, 0, 0))
            Board.RGB.setPixelColor(1, Board.PixelColor(255, 0, 0))
        case "green":
            Board.RGB.setPixelColor(0, Board.PixelColor(0, 255, 0))
            Board.RGB.setPixelColor(1, Board.PixelColor(0, 255, 0))
        case "blue":
            Board.RGB.setPixelColor(0, Board.PixelColor(0, 0, 255))
            Board.RGB.setPixelColor(1, Board.PixelColor(0, 0, 255))
        case _:
            Board.RGB.setPixelColor(0, Board.PixelColor(0, 0, 0))
            Board.RGB.setPixelColor(1, Board.PixelColor(0, 0, 0))

    Board.RGB.show()


def buzz(duration: float):
    """
    run the buzzer for a specified time
    """
    # Start the buzzer
    Board.setBuzzer(0)
    Board.setBuzzer(1)
    time.sleep(duration)

    # Stop the buzzer
    Board.setBuzzer(0)


class Pose:
    """position and rotation"""

    x: float
    y: float
    rotation: float


class Motion:
    """interface for controlling the arm"""

    # Coordinates for each respective block
    _block_coordinates = {
        "red": (-15 + 0.5, 12 - 0.5, 1.5),
        "green": (-15 + 0.5, 6 - 0.5, 1.5),
        "blue": (-15 + 0.5, 0 - 0.5, 1.5),
    }

    # Default position of servo 1
    _default_jaws_angle = 500

    def __init__(self) -> None:
        """Create a new control interface for the arm."""
        self.ik = arm_ik.ArmIK()
        self.unreachable = True

        self.reset_pose()
        atexit.register(self.reset_pose)

    def reset_pose(self):
        """Reset the position of the arm to its default pose."""
        Board.setBusServoPulse(1, Motion._default_jaws_angle - 50, 300)
        Board.setBusServoPulse(2, 500, 500)
        self.ik.setPitchRangeMoving((0, 10, 10), -30, -30, -90, 1500)

    def move(
        self,
        pose: Pose,
        first_move: bool,
        start_pickup: bool,
        detect_color: str,
        track: bool,
    ) -> bool:
        """
        Move the arm according to the desired current task.
        This method moves the arm according to whether it should be executing a
        pick-and-place task or a tracking task. If performing pick-and-place, this
        method performs the full pick-and-place procedure according to the detected
        location and the object's pre-assigned target place position.
        Args:
            pose (Pose): The current pose of the object.
            first_move (bool): Indicates whether or not this is the first time that
                the manipulator has moved for this task.
            start_pickup (bool): Indicates whether or not the manipulator should start
                the pickup process.
            detect_color (str): The color of the detected object.
            track (bool): Indicates whether or not the manipulator should be tracking
                the pose of the object.
        Returns:
            bool: Indicates whether or not the arm has completed the task.
        """
        finished = False

        set_rgb(detect_color)

        if first_move and start_pickup:
            buzz(0.1)

            result = self.ik.setPitchRangeMoving((pose.x, pose.y - 2, 5), -90, -90, 0)

            # Keep track of whether or not the object is reachable
            if not result:
                self.unreachable = True
            else:
                self.unreachable = False

            time.sleep(result[2] / 1000)

            first_move = False
            finished = True

        elif not first_move and not self.unreachable:
            # The robot is tracking the state of the object
            if track:
                self.ik.setPitchRangeMoving((pose.x, pose.y - 2, 5), -90, -90, 0, 20)
                time.sleep(0.02)
                track = False

            # Start the pickup process
            if start_pickup:
                finished = False

                # Open the jaws
                Board.setBusServoPulse(1, Motion._default_jaws_angle - 280, 500)

                # Rotate the gripper
                Board.setBusServoPulse(
                    2, transform.getAngle(pose.x, pose.y, pose.rotation), 500
                )
                time.sleep(0.8)

                # Move the arm down
                self.ik.setPitchRangeMoving((pose.x, pose.y, 2), -90, -90, 0, 1000)
                time.sleep(2)

                # Close the jaws
                Board.setBusServoPulse(1, Motion._default_jaws_angle, 500)
                time.sleep(1)

                # Move the arm back up
                Board.setBusServoPulse(2, 500, 500)
                self.ik.setPitchRangeMoving((pose.x, pose.y, 12), -90, -90, 0, 1000)
                time.sleep(1)

                # Sort the objects according to their respective colors
                result = self.ik.setPitchRangeMoving(
                    (
                        Motion._block_coordinates[detect_color][0],
                        Motion._block_coordinates[detect_color][1],
                        12,
                    ),
                    -90,
                    -90,
                    0,
                )
                time.sleep(result[2] / 1000)

                Board.setBusServoPulse(
                    2,
                    transform.getAngle(
                        Motion._block_coordinates[detect_color][0],
                        Motion._block_coordinates[detect_color][1],
                        -90,
                    ),
                    500,
                )
                time.sleep(0.5)

                self.ik.setPitchRangeMoving(
                    (
                        Motion._block_coordinates[detect_color][0],
                        Motion._block_coordinates[detect_color][1],
                        Motion._block_coordinates[detect_color][2] + 3,
                    ),
                    -90,
                    -90,
                    0,
                    500,
                )
                time.sleep(0.5)

                self.ik.setPitchRangeMoving(
                    (Motion._block_coordinates[detect_color]), -90, -90, 0, 1000
                )
                time.sleep(0.8)

                Board.setBusServoPulse(1, Motion._default_jaws_angle - 200, 500)
                time.sleep(0.8)

                self.ik.setPitchRangeMoving(
                    (
                        Motion._block_coordinates[detect_color][0],
                        Motion._block_coordinates[detect_color][1],
                        12,
                    ),
                    -90,
                    -90,
                    0,
                    800,
                )
                time.sleep(0.8)

                # Reset the arm after completing the place step
                self.reset_pose()
                time.sleep(1.5)

                # Disable the RGB
                set_rgb()
                finished = True
            else:
                time.sleep(0.01)

        return finished