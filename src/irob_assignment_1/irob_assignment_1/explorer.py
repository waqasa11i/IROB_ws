#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from nav_msgs.msg import OccupancyGrid
from geometry_msgs.msg import PoseStamped
from nav2_msgs.action import NavigateToPose
from rclpy.action import ActionClient
import numpy as np


class ExplorerNode(Node):
    def __init__(self):
        # TODO: Initialize the node with name 'explorer'.
        # TODO: Create a subscription to the occupancy grid map topic (e.g., '/map'),
        #       with queue size 10, and register self.map_callback.
        # TODO: Create an ActionClient for Nav2's NavigateToPose on 'navigate_to_pose'.
        # TODO: Create a set to store visited frontier cells (row, col).
        # TODO: Initialize storage for the latest map (self.map_data = None).
        # TODO: Initialize the robot's grid position (self.robot_position), to be
        #       updated by localization (placeholder values are fine for now).
        # TODO: Create a periodic timer (e.g., every 5.0 seconds) that calls self.explore().
        pass

    def map_callback(self, msg):
        """
        TODO: Store the latest occupancy grid message in self.map_data.
              Optionally log that a new map was received.
        """
        pass

    def navigate_to(self, x, y):
        """
        TODO: Construct a PoseStamped goal in the 'map' frame at coordinates (x, y).
              - Set header.stamp using the node clock.
              - Set orientation (e.g., w = 1.0).
        TODO: Wrap that in a NavigateToPose.Goal and send it with the ActionClient.
        TODO: Wait for the action server to be available.
        TODO: Attach self.goal_response_callback to the future returned by send_goal_async().
        """
        pass

    def goal_response_callback(self, future):
        """
        TODO: Check whether the goal was accepted or rejected.
        TODO: If accepted, request the result and attach self.navigation_complete_callback
              to the result future (goal_handle.get_result_async()).
        """
        pass

    def navigation_complete_callback(self, future):
        """
        TODO: Handle completion of the navigation action.
              - If successful, log/record the result.
              - On failure, log the exception or error.
        """
        pass

    def find_frontiers(self, map_array):
        """
        TODO: Detect frontier cells in the occupancy grid.
              Definition: a frontier is a FREE cell (value == 0)
              that has at least one UNKNOWN neighbor (value == -1)
              in its 8-neighborhood.

              Steps:
              - Iterate over interior cells (avoid the outermost border).
              - For each free cell, check the 3x3 neighborhood.
              - If any neighbor is unknown, add (row, col) to a list of frontiers.
              - Return the list of (row, col) frontier cells.
        """
        pass

    def choose_frontier(self, frontiers):
        """
        TODO: Choose the closest frontier to the robot's current grid position.
              - Skip frontiers already present in self.visited_frontiers.
              - Compute Euclidean distance in grid coordinates.
              - Keep the minimum; return (row, col) or None if none available.
              - Add the chosen frontier to self.visited_frontiers.
        """
        pass

    def explore(self):
        """
        TODO: Main exploration routine:
              - If no map yet, return early.
              - Convert the flat map data to a 2D numpy array with shape
                (height, width).
              - Call find_frontiers(map_array) to get candidates.
              - If none, optionally log "exploration complete" and return.
              - Call choose_frontier(frontiers); if None, return.
              - Convert the chosen (row, col) to world (x, y) using:
                    x = col * resolution + origin.position.x
                    y = row * resolution + origin.position.y
              - Call navigate_to(x, y).
        """
        pass


def main(args=None):
    # TODO: Standard ROS 2 boilerplate:
    # - Initialize rclpy
    # - Create the ExplorerNode
    # - Spin
    # - On shutdown, destroy node and call rclpy.shutdown()
    pass