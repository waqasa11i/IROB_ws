cmake_minimum_required(VERSION 3.8)
project(irob_assignment_1)

# Set C++17
set(CMAKE_CXX_STANDARD 17)

# Find necessary packages
find_package(ament_cmake REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(nav_msgs REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(std_msgs REQUIRED)
find_package(visualization_msgs REQUIRED)
find_package(rosidl_default_generators REQUIRED)
find_package(rclcpp REQUIRED)
find_package(gazebo_ros REQUIRED)
find_package(turtlebot3_gazebo REQUIRED)
find_package(rosidl_default_generators REQUIRED)


# Export dependencies
ament_export_dependencies(
  rosidl_default_runtime
  geometry_msgs
  nav_msgs
  sensor_msgs
  std_msgs
  visualization_msgs
  rclcpp
  gazebo_ros
)

# Install Python packages and scripts
ament_python_install_package(${PROJECT_NAME})

install(PROGRAMS  
  scripts/explorer.py
  scripts/collision_avoidance.py  
  DESTINATION lib/${PROJECT_NAME} 
)

# rosidl_generate_interfaces(${PROJECT_NAME}
#   "srv/GetSetpoint.srv"
#   DEPENDENCIES
#   std_msgs  # If your service depends on other messages
# )

# rosidl_generate_interfaces(${PROJECT_NAME}
#   "action/GetNextGoal.action"
#   DEPENDENCIES nav_msgs
# )

# Install launch files
install(DIRECTORY
  launch
  DESTINATION share/${PROJECT_NAME}
)

# Install config files
install(DIRECTORY
  config
  DESTINATION share/${PROJECT_NAME}
)

# Install URDF files
install(DIRECTORY
  urdf/
  DESTINATION share/${PROJECT_NAME}/urdf
  PATTERN "*" PERMISSIONS OWNER_READ OWNER_WRITE GROUP_READ WORLD_READ
)

# Install world files
install(DIRECTORY
  worlds/
  DESTINATION share/${PROJECT_NAME}/worlds
  PATTERN "*" PERMISSIONS OWNER_READ OWNER_WRITE GROUP_READ WORLD_READ
)

# Install RViz configuration
install(DIRECTORY
  rviz/
  DESTINATION share/${PROJECT_NAME}/rviz
  PATTERN "*" PERMISSIONS OWNER_READ OWNER_WRITE GROUP_READ WORLD_READ
)


ament_package()

