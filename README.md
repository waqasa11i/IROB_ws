##IROB_ws

To run the package follows these steps:

1. Clone the repo.

2. Run following to install
```
cd IROB_ws
pixi shell
colcon build
```

3. Open three terminals and run following commands

Terminal-1:
```
source install/setup.bash
export TURTLEBOT3_MODEL=burger
pixi run simulator
```

Terminal-2:
```
source install/setup.bash
pixi run navigation
```

Terminal-3:
```
source install/setup.bash
pixi run start
```