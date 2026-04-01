
import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    use_sim_time = LaunchConfiguration('use_sim_time', default='true')
    
    pkg_nav2_ros = get_package_share_directory('nav2_bringup')
    pkg_slamtoolbox_ros = get_package_share_directory('slam_toolbox')

    return LaunchDescription([
        Node(
            package='irob_assignment_1',
            executable='explorer',
            name='explorer',
            output='screen'
        )
    ])
