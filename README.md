##IROB_ws

To run the package follows these steps:

1. Clone the repo.

2. Run following to install
```
cd IROB_ws
pixi install
```

3. Open three terminals and run following commands

Terminal-1:
```
export TURTLEBOT3_MODEL=burger
pixi run simulator
```

Terminal-2:
```
pixi run navigation
```

Terminal-3:
```
pixi run start
```