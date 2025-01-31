# ✨ Integrate ROS 2, Gazebo, MoveIt

### 📜 Index

1. [ROS 2](#-ros-2)
2. [Gazebo](#-gazebo)
3. [RViz](#-rviz)
4. [MoveIt](#-moveit)
5. [Integrate](#-integrate)

## ✅ ROS 2

### 🏷 Link
- [Installation](https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debs.html)
- [Beginner: Client libraries](https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries.html)
    - [Configuring environment](https://docs.ros.org/en/humble/Tutorials/Beginner-CLI-Tools/Configuring-ROS2-Environment.html)
    - [Using turtlesim, ros2, and rqt](https://docs.ros.org/en/humble/Tutorials/Beginner-CLI-Tools/Introducing-Turtlesim/Introducing-Turtlesim.html)
    - [Understanding nodes](https://docs.ros.org/en/humble/Tutorials/Beginner-CLI-Tools/Understanding-ROS2-Nodes/Understanding-ROS2-Nodes.html)
    - [Understanding topics](https://docs.ros.org/en/humble/Tutorials/Beginner-CLI-Tools/Understanding-ROS2-Topics/Understanding-ROS2-Topics.html)
    - [Understanding services](https://docs.ros.org/en/humble/Tutorials/Beginner-CLI-Tools/Understanding-ROS2-Services/Understanding-ROS2-Services.html)
    - [Understanding parameters](https://docs.ros.org/en/humble/Tutorials/Beginner-CLI-Tools/Understanding-ROS2-Parameters/Understanding-ROS2-Parameters.html)
    - [Understanding actions](https://docs.ros.org/en/humble/Tutorials/Beginner-CLI-Tools/Understanding-ROS2-Actions/Understanding-ROS2-Actions.html)
    - [Using rqt_console to view logs](https://docs.ros.org/en/humble/Tutorials/Beginner-CLI-Tools/Using-Rqt-Console/Using-Rqt-Console.html)
    - [Launching nodes](https://docs.ros.org/en/humble/Tutorials/Beginner-CLI-Tools/Launching-Multiple-Nodes/Launching-Multiple-Nodes.html)
    - [Recording and playing back data](https://docs.ros.org/en/humble/Tutorials/Beginner-CLI-Tools/Recording-And-Playing-Back-Data/Recording-And-Playing-Back-Data.html)
- [Beginner: CLI tools](https://docs.ros.org/en/humble/Tutorials/Beginner-CLI-Tools.html)
    - [Using colcon to build packages](https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries/Colcon-Tutorial.html)
    - [Creating a workspace](https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries/Creating-A-Workspace/Creating-A-Workspace.html)
    - [Creating a package](https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries/Creating-Your-First-ROS2-Package.html)
- [Intermediate](https://docs.ros.org/en/humble/Tutorials/Intermediate.html)
    - [Launch](https://docs.ros.org/en/humble/Tutorials/Intermediate/Launch/Launch-Main.html)

## ✅ Gazebo

### 🏷 Link
- [Installation](https://gazebosim.org/docs/fortress/install_ubuntu/)
- [Tutorials](https://gazebosim.org/docs/fortress/tutorials/)
    - Basic
        - [Building your own robot](https://gazebosim.org/docs/fortress/building_robot/)
        - [Moving the robot](https://gazebosim.org/docs/fortress/moving_robot/)
        - [SDF worlds](https://gazebosim.org/docs/fortress/sdf_worlds/)
        - [Sensors](https://gazebosim.org/docs/fortress/sensors/)
        - [Actors](https://gazebosim.org/docs/fortress/actors/)
    - GUI
        - [Understanding the GUI](https://gazebosim.org/docs/fortress/gui/)
        - [Manipulating Models](https://gazebosim.org/docs/fortress/manipulating_models/)
        - [Model Insertion from Fuel](https://gazebosim.org/docs/fortress/fuel_insert/)
        - [Gazebo Keyboard Shortcuts](https://gazebosim.org/docs/fortress/hotkeys/)
    - ROS Integration
        - [Spawn URDF](https://gazebosim.org/docs/fortress/spawn_urdf/)
        - [ROS 2 Integration via bridge](https://gazebosim.org/docs/fortress/ros2_integration/)
        - [ROS 2 Interoperablity](https://gazebosim.org/docs/fortress/ros2_interop/)
        - [ROS 2 Integration Template]()
- [Setting up a robot simulation](https://docs.ros.org/en/humble/Tutorials/Advanced/Simulators/Gazebo/Gazebo.html)

### SDF
> Gazebo에서 로봇 + 환경을 모두 풍부하게 표현할 수 있도록 만들어진 XML 형식.
```xml
<sdf version="1.9">
    <world name="my_world">

        <physics name="1ms" type="ignored">
            <!-- attributes -->
        </physics>

        <plugin
            filename="ignition-gazebo-physics-system"
            name="ignition::gazebo::systems::Physics">
            <!-- attributes -->
        </plugin>
        <!-- more pluginss -->

        <scene>
            <!-- attributes -->
        </scene>
            
        <gui fullscreen="false">
            <!-- attributes -->
        </gui>

        <light type="directional" name="sun">
            <!-- attributes -->
        </light>

        <model name="my_robot">

            <link name="base_link">
                <!-- 링크(본체) 관련 물리 파라미터, 시각/충돌 메쉬, 센서 등 -->
            </link>

            <link name="wheel_link">
                <!-- 바퀴 링크 -->
            </link>

            <joint name="wheel_joint" type="revolute">
                <parent>base_link</parent>
                <child>wheel_link</child>
                <!-- 조인트의 축(axis), 물리 파라미터 등 -->
            </joint>

            <!-- 필요하다면 다른 링크, 조인트 추가 ... -->

            <plugin name="my_plugin" filename="libmy_plugin.so">
                <!-- 플러그인 파라미터(플러그인마다 달라요!) -->
            </plugin>
        </model>
        <!-- more models -->

        <include>
            <uri>
                <!-- insert model uri from https://app.gazebosim.org/fuel/models -->
            </uri>
        </include>
    </world>
</sdf>
```

### URDF
> ROS에서 로봇을 정의할 때 주로 사용되는 XML 형식입니다.

### Sensors
- IMU
    > Inertial Measurement Unit, 관성 측정 장치
    - 가속도(acceleration), 각속도(angular velocity), 자기장(magnetometer) 등을 측정해 로봇이나 드론, 차량 등의 자세(orientation)와 움직임을 파악하는 데 사용하는 핵심 센서 모듈
    - 가속도계(Accelerometer) : 물체가 움직이거나 기울어질 때 발생하는 가속도(선형가속도)를 측정합니다.
    - 자이로스코프(Gyroscope) : 물체의 회전 각속도(roll, pitch, yaw 축 기준)를 측정합니다.
    - 자력계(Magnetometer) : 지구 자기장 방향을 측정하여, 방향 정보를 더욱 정확히 보정할 수 있도록 합니다.
- Depth Camera
    > 깊이 카메라
    - 다양한 방식
        - 구조화 광(Structured Light) : 패턴이 있는 광을 환경에 투사하고, 왜곡된 패턴을 카메라가 수신해 3D 정보를 복원
        - 스테레오 카메라 : 좌우 두 개의 카메라로 사물을 촬영해 시차를 기반으로 깊이 계산
- Lidar
    > Light Detection and Ranging, 빛 감지 및 거리 측정
    - 일반적으로 360도 또는 180도 범위를 수평으로 스캔하며, 고속으로 주변 환경의 밀도 높은 점군(point cloud) 데이터를 생산합니다.
    - 시간비행(ToF, Time of Flight) 카메라 : 광 펄스를 발사하고 돌아오는 시간을 측정해 픽셀별 거리 계산

## ✅ RViz

### 🏷 Link
- [RViz](https://docs.ros.org/en/humble/Tutorials/Intermediate/RViz/RViz-Main.html)
    - [RViz User Guide](https://docs.ros.org/en/humble/Tutorials/Intermediate/RViz/RViz-User-Guide/RViz-User-Guide.html)

## ✅ MoveIt

### 🏷 Link
- [Getting Started](https://moveit.picknik.ai/main/doc/tutorials/getting_started/getting_started.html)
- [MoveIt Quickstart in Rviz](https://moveit.picknik.ai/main/doc/tutorials/quickstart_in_rviz/quickstart_in_rviz_tutorial.html)
    - [Getting Started](https://moveit.picknik.ai/main/doc/tutorials/quickstart_in_rviz/quickstart_in_rviz_tutorial.html#getting-started)
    - [Step 1: Launch the Demo and Configure the Plugin](https://moveit.picknik.ai/main/doc/tutorials/quickstart_in_rviz/quickstart_in_rviz_tutorial.html#step-1-launch-the-demo-and-configure-the-plugin)
    - [Step 2: Play with the Visualized Robots](https://moveit.picknik.ai/main/doc/tutorials/quickstart_in_rviz/quickstart_in_rviz_tutorial.html#step-2-play-with-the-visualized-robots)
    - [Step 3: Interact with the Kinova Gen 3](https://moveit.picknik.ai/main/doc/tutorials/quickstart_in_rviz/quickstart_in_rviz_tutorial.html#step-3-interact-with-the-kinova-gen-3)
    - [Step 4: Use Motion Planning with the Kinova Gen 3](https://moveit.picknik.ai/main/doc/tutorials/quickstart_in_rviz/quickstart_in_rviz_tutorial.html#step-4-use-motion-planning-with-the-kinova-gen-3)

## ✅ Integrate
