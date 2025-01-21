# GAZEBO & Rviz

## [GAZEBO](https://gazebosim.org/docs/fortress/getstarted/)

### 1. Install

```bash
sudo apt-get update
sudo apt-get install lsb-release gnupg
```

```bash
sudo curl https://packages.osrfoundation.org/gazebo.gpg --output /usr/share/keyrings/pkgs-osrf-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/pkgs-osrf-archive-keyring.gpg] http://packages.osrfoundation.org/gazebo/ubuntu-stable $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/gazebo-stable.list > /dev/null
sudo apt-get update
sudo apt-get install ignition-fortress
```

### 2. Run
```bash
ign gazebo shapes.sdf
```

### 3. ROS 2 Integration
```bash
sudo apt-get install ros-${ROS_DISTRO}-ros-gz
```

## [Rviz](https://moveit.picknik.ai/main/doc/tutorials/getting_started/getting_started.html)

### 1. Install rosdep
```bash
sudo apt install python3-rosdep
```

### 2. Install colcon with mixin
```bash
sudo apt install python3-colcon-common-extensions
sudo apt install python3-colcon-mixin
colcon mixin add default https://raw.githubusercontent.com/colcon/colcon-mixin-repository/master/index.yaml
colcon mixin update default
```

### 3. Install vsctool
```bash
sudo apt install python3-vcstool
```

### 4. Create Workspace
```bash
mkdir ws_moveit
mkdir ws_moveit/src
```

### 5. Download Source Code
```bash
cd ws_moveit/src
git clone -b humble https://github.com/moveit/moveit2_tutorials
vcs import --recursive < moveit2_tutorials/moveit2_tutorials.repos
```

### 6. Build colcon workspace
```bash
sudo apt remove ros-$ROS_DISTRO-moveit*
sudo apt update && rosdep install -r --from-paths . --ignore-src --rosdistro $ROS_DISTRO -y
```

```bash
cd ..
colcon build --mixin release
```

### 7. Setup your colcon workspace
```bash
cd ..
source ws_moveit/install/setup.bash
echo 'source ws_moveit/install/setup.bash' >> ~/.bashrc
```

## Moveit
```bash
ros2 launch moveit2_tutorials demo.launch.py
```

## ROS 2 - Gazebo - Rviz
```bash
sudo apt install ros-humble-ros-ign
sudo apt install ros-humble-gazebo-ros-pkgs ros-humble-gazebo-ros2-control
```

ros2 - gazebo bidictional communication
```bash
ros2 run ros_ign_bridge parameter_bridge /example/topic@std_msgs/msg/String@ignition.msgs.StringMsg
ros2 run ros_gz_bridge parameter_bridge /TOPIC@ROS_MSG@IGN_MSG
```

setting environment
```bash
source /usr/share/gazebo/setup.sh
source /opt/ros/humble/setup.bash
export IGN_GAZEBO_SYSTEM_PLUGIN_PATH=/usr/lib/x86_64-linux-gnu/ign-gazebo-6/plugins
export IGN_GAZEBO_RESOURCE_PATH=/usr/share/ignition/ignition-gazebo6
```

### turtlebot 4 simulator
```bash
sudo apt install ros-humble-turtlebot4-simulator ros-humble-irobot-create-nodes
sudo apt install ros-dev-tools
```

```bash
mkdir turtlebot4_ws/src
cd turtlebot4_ws/src
git clone https://github.com/turtlebot/turtlebot4_simulator.git -b humble
cd ..
rosdep install --from-path src -yi
colcon build --symlink-install
```

```bash
ros2 launch turtlebot4_ignition_bringup turtlebot4_ignition.launch.py
```