
import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.actions import AppendEnvironmentVariable
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

TURTLEBOT3_MODEL = os.environ['TURTLEBOT3_MODEL']

def generate_launch_description():
    use_sim_time = LaunchConfiguration('use_sim_time', default='true')
    # world_file_name = 'turtlebot3_worlds/' + 'burger.model'
    # world = os.path.join(get_package_share_directory('turtlebot3_gazebo'),
    #                      'worlds', world_file_name)
    launch_file_dir = os.path.join(get_package_share_directory('turtlebot3_gazebo'), 'launch')
    
    ros_gz_sim = get_package_share_directory('ros_gz_sim')

    pkg_irob_assignment_1 = get_package_share_directory('irob_assignment_1')
    pkg_slamtoolbox_ros = get_package_share_directory('slam_toolbox')

    use_sim_time = LaunchConfiguration('use_sim_time', default='true')
    x_pose = LaunchConfiguration('x_pose', default='-2.0')
    y_pose = LaunchConfiguration('y_pose', default='-0.5')

    world = os.path.join(
        get_package_share_directory('turtlebot3_gazebo'),
        'worlds',
        'turtlebot3_world.world'
    )

    gzserver_cmd = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(ros_gz_sim, 'launch', 'gz_sim.launch.py')
        ),
        launch_arguments={'gz_args': f'-r -s -v2 {world}', 'on_exit_shutdown': 'true'}.items()
    )

    gzclient_cmd = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(ros_gz_sim, 'launch', 'gz_sim.launch.py')
        ),
        launch_arguments={'gz_args': '-g -v2 ', 'on_exit_shutdown': 'true'}.items()
    )

    robot_state_publisher_cmd = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(launch_file_dir, 'robot_state_publisher.launch.py')
        ),
        launch_arguments={'use_sim_time': use_sim_time}.items()
    )

    spawn_turtlebot_cmd = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_irob_assignment_1, 'launch', 'spawn_turtlebot3.launch.py')
        ),
        launch_arguments={
            'x_pose': x_pose,
            'y_pose': y_pose
        }.items()
    )

    set_env_vars_resources = AppendEnvironmentVariable(
            'GZ_SIM_RESOURCE_PATH',
            os.path.join(
                get_package_share_directory('turtlebot3_gazebo'),
                'models'))

    # --- RViz Launch ---
    rviz = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        arguments=[
            '-d', os.path.join(pkg_irob_assignment_1, 'rviz', 'view.rviz'),
        ],
        parameters=[{'use_sim_time': True}],
        output='screen'
    )

    return LaunchDescription([
        gzserver_cmd,
        gzclient_cmd,
        spawn_turtlebot_cmd,
        robot_state_publisher_cmd,
        set_env_vars_resources,
        rviz,
        IncludeLaunchDescription(      
            PythonLaunchDescriptionSource(
                    os.path.join(pkg_slamtoolbox_ros, 'launch', 'online_async_launch.py')
                ),
                launch_arguments={'use_sim_time': use_sim_time}.items(),
        ),
    ])


