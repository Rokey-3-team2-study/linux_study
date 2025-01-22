# GAZEBO & Rviz

## ✅ [GAZEBO](https://gazebosim.org/docs/fortress/getstarted/)

- 개념
  - 고급 로봇 시뮬레이션 환경
  - 로봇의 동작을 실제 환경과 유사한 물리적 조건에서 테스트하고 개발
  - ROS 2와 긴밀하게 통합
  - 다양한 센서, 액추에이터, 물리 엔진 등을 지원
- 특징
  - 물리 시뮬레이션: 중력, 마찰, 충돌 등 실제 물리 법칙을 기반으로 한 정교한 시뮬레이션을 제공합니다.
  - 센서 시뮬레이션: 카메라, LiDAR, IMU 등 다양한 센서를 가상으로 구현하여 로봇의 센서 데이터를 테스트할 수 있습니다.
  - 멀티로봇 지원: 여러 대의 로봇을 동시에 시뮬레이션할 수 있어 복잡한 시나리오를 구현할 수 있습니다.
  - 확장성: 플러그인을 통해 새로운 기능을 쉽게 추가할 수 있습니다.
  - 고해상도 환경: 실제 환경과 유사한 고해상도의 모델과 맵을 사용할 수 있습니다.

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

## ✅ [Rviz](https://moveit.picknik.ai/main/doc/tutorials/getting_started/getting_started.html)

- 개념
  - ROS 2에서 제공하는 3D 시각화 도구
  - 로봇의 상태, 센서 데이터, 환경 정보를 시각적으로 표현
  - 개발자가 로봇의 동작을 직관적으로 이해하고 디버깅
- 특징
  - 다양한 시각화 도구: 포인트 클라우드, 메시지, 로봇 모델, 경로 등 다양한 데이터 타입을 시각화할 수 있습니다.
  - 인터랙티브 환경: 3D 뷰어를 통해 카메라 위치를 자유롭게 조정하고, 관심 있는 영역을 자세히 관찰할 수 있습니다.
  - 플러그인 아키텍처: 새로운 시각화 도구를 플러그인 형태로 쉽게 추가할 수 있습니다.
  - 실시간 데이터 업데이트: ROS 2 토픽, 서비스, 액션 등의 실시간 데이터를 즉각적으로 반영합니다.
  - 사용자 정의 설정: 다양한 설정을 통해 시각화 방식을 맞춤 설정할 수 있습니다.

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

### 8. Moveit
```bash
ros2 launch moveit2_tutorials demo.launch.py
```

## ✅ ROS 2 - Gazebo - Rviz
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

### [turtlebot 4 simulator](https://turtlebot.github.io/turtlebot4-user-manual/software/turtlebot4_simulator.html)
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