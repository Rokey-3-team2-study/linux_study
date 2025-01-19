# ✨ Linux & ROS 2

## ⚙️ Environment
### <U>[Rufus & Dual Boot](https://webnautes.tistory.com/2119)</U>
- Rufus
- Linux(Ubuntu)
- BIOS boot setting
### <U>[Ubuntu](https://webnautes.tistory.com/2120)</U>
- Ubuntu setting
### <U>[ROS 2](https://velog.io/@i_robo_u/%ED%98%84%EC%A7%81%EC%9E%90%EA%B0%80-%EC%95%8C%EB%A0%A4%EC%A3%BC%EB%8A%94-ROS2-%EB%AA%85%EB%A0%B9%EC%96%B4-%EB%8F%84%EA%B5%ACCommand-Line-interface-tools-1)</U>
- turtlesim
- rqt
### Summary
1. Rufus : Linux(Ubuntu) > USB
2. BIOS Setting
3. Ubunt Basic Setting

## ✅ Nodes
<img src="./img/Nodes-TopicandService.gif"></img>

### 1. run
```bash
ros2 run <package name> <executable name>
```
```bash
ros2 run turtlesim turtlesim_node
```

<p align="center">
    <img src="./img/turtlesim.png" style="width: 300;"></img>
</p>

### 2. node list
```bash
ros2 node list
```
<p align="center">
<img src="./img/turtlesim_terminal.png" style="width: 500;"></img>
<img src="./img/turtle_teleop_key_terminal.png" style="width: 500;"></img>
<img src="./img/node_list.png" style="width: 500;"></img>
</p>

#### 2.1 remapping
```bash
ros2 run turtlesim turtlesim_node --ros-args --remap __node:=my_turtle
```

<p align="center">
<img src="./img/turtlesim_remapping_terminal.png" style="width: 500;"></img>
<img src="./img/turtlesim_remapping.png" style="width: 300;"></img>
<img src="./img/node_list_remapping.png" style="width: 500;"></img>
</p>

### 3. node info
```bash
ros2 node info /my_turtle
```

<p align="center">
<img src="./img/node_info.png" style="width: 500;"></img>
</p>

### Summary
1. node is a fundamental ROS 2 element that serves a single, modular purpose in a robotics system.
2. We utilized nodes created in the *turtlesim* package by running the executalbes *turtlesim* and *turtlesim_key*.
3. We learned how to use *ros2 noed list* to discover active node names and *ros2 node info* to introspect a single node. These tools are vital to understanding the flow of data in a complex, real-world robot system.

## ✅ Topic
<img src="./img/Topic-MultiplePublisherandMultipleSubscriber.gif"></img>

### 1. rqt_graph
```bash
rqt_graph
```
<p align="center">
<img src="./img/rqt_graph.png" style="width: 500;"></img>
</p>

- **node** : /teleop_turtle, /turtlesim
- **topic** : /turtle1/cmd_vel
- /teleop_turtle(**publish**) -> message -> /turtle1/cmd_vel -> message -> /turtlesim(**subscribe**)

### 2. topic list
```bash
ros2 topic list
```

<p align="center">
<img src="./img/topic_list.png" style="width: 500;"></img>
</p>

```bash
ros2 topic list -t
```
<p align="center">
<img src="./img/topic_list-t.png" style="width: 500;"></img>
</p>

### 3. topic echo
```bash
ros2 topic echo <topic name>
```
```bash
ros2 topic echo /turtle1/cmd_vel
```

<p align="center">
<img src="./img/topic_echo_turtlesim.png" style="width: 300;"></img>
<img src="./img/topic_echo_terminal.png" style="width: 500;"></img>
</p>

### 4. topic info
```bash
ros2 topic info <topic name>
```
```bash
ros2 topic info /turtle1/cmd_vel
```

<p align="center">
<img src="./img/topic_info.png" style="width: 500;"></img>
</p>

### 5. interface show
```bash
ros2 interface show <message type>
```
```bash
ros2 interface show geometry_msgs/msg/Twist
```

<p align="center">
<img src="./img/interface_show.png" style="width: 500;"></img>
</p>

- message structure

### 6. topic pub
```bash
ros2 topic pub <topic_name> <msg_type> '<args>'
```
- We can publish message directly from command line

```bash
ros2 topic pub /turtle1/cmd_vel geometry_msgs/msg/Twist \
"{linear: {x: 2.0, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 1.8}}"
```

<p align="center">
<img src="./img/topic_pub_turtlesim.png" style="width: 300;"></img>
<img src="./img/topic_pub_terminal.png" style="width: 500;"></img>
<img src="./img/topic_pub_rqt_graph.png" style="width: 500;"></img>
</p>

- **/_ros2cli_21956** publish message to /turtle1/cmd_vel

```bash
ros2 topic echo /turtle1/pose
```

<p align="center">
<img src="./img/topic_pub_pose_rqt_graph.png" style="width: 500;"></img>
</p>

- topic **/turtle1/pose** receive and send pose information of turtle1

### 7. topic hz
```bash
ros2 topic hz <topic name>
```
```bash
ros2 topic hz /turtle1/pose
```

<p align="center">
<img src="./img/topic_hz_terminal.png" style="width: 500;"></img>
</p>

- average rate : number of messages per second

```bash
ros2 topic pub --rate 1 /turtle1/cmd_vel geometry_msgs/msg/Twist \
"{linear: {x: 2.0, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 1.8}}"
```
```bash
ros2 topic hz /turtle1/cmd_vel
```

<p align="center">
<img src="./img/topic_pub_rate_1_terminal.png" style="width: 500;"></img>
<img src="./img/topic_hz_rate_1.png" style="width: 500;"></img>
</p>

### 8. topic bw
```bash
ros2 topic bw <topic name>
```
```bash
ros2 topic bw /turtle1/pose
```

<p align="center">
<img src="./img/topic_bw_terminal.png" style="width: 500;"></img>
</p>

### 9. topic find
```bash
ros2 topic find <topic_type>
```
```bash
ros2 topic find geometry_msgs/msg/Twist
ros2 topic find turtlesim/msg/Pose
```

<p align="center">
<img src="./img/topic_find_terminal.png" style="width: 500;"></img>
</p>

### Summary
1. Nodes publish information over topics, which allows any number of other nodes to subscribe to and access that information.
2. We learned connection between sevral nodes over topics using rqt_graph

## ✅ Services
<img src="./img/Service-MultipleServiceClient.gif"></img>

### 1. service list
```bash
ros2 service list
```

<p align="center">
<img src="./img/service_list_terminal.png" style="width: 500;"></img>
</p>

### 2. service type
```bash
ros2 service type <service name>
```
```bash
ros2 service type /clear
```

<p align="center">
<img src="./img/service_type.png" style="width: 500;"></img>
</p>

#### 2.1 service list -t
```bash
ros2 service list -t
```

<p align="center">
<img src="./img/service_list_t.png" style="width: 500;"></img>
</p>

### 3. service find
```bash
ros2 service find <type name>
```
```bash
ros2 service find std_srvs/srv/Empty
```

<p align="center">
<img src="./img/service_find.png" style="width: 500;"></img>
</p>

### 4. interface show
```bash
ros2 interface show <type_name>
```
```bash
ros2 interface show std_srvs/srv/Empty
ros2 interface show turtlesim/srv/Spawn
```

<p align="center">
<img src="./img/service_interface.png" style="width: 500;"></img>
</p>

### 5. service call
```bash
ros2 service call <service name> <service type> <arguments>
```

- arguments is optional

```bash
ros2 service call /clear std_srvs/srv/Empty
```

<p align="center">
<img src="./img/service_call_turtlesim_b.png" style="width: 300;"></img>
<img src="./img/service_call_clear.png" style="width: 500;"></img>
<img src="./img/service_call_turtlesim_A.png" style="width: 300;"></img>
</p>

```bash
ros2 service call /spawn turtlesim/srv/Spawn \
"{x: 2, y: 2, theta: 0.2, name: ''}"
```

<p align="center">
<img src="./img/service_call_spawn_b.png" style="width: 300;"></img>
<img src="./img/service_call_spawn_terminal.png" style="width: 500;"></img>
<img src="./img/service_call_spawn_a.png" style="width: 300;"></img>
</p>

### Summary
1. Nodes can communicate using services in ROS 2.
2. **Unlike a topic** - a one way communication pattern where a node publishes information that can be consumed by one or more subscribers - a service is a request/response pattern where a client makes a request to a node providing the service and the service processes the request and generates a response.

## ✅ Parameters

### 1. param list
```bash
ros2 param list
```

<p align="center">
<img src="./img/param_list.png" style="width: 500;"></img>
</p>

### 2. param get
```bash
ros2 param get <node_name> <parameter_name>
```
```bash
ros2 param get /turtlesim background_g
ros2 param get /turtlesim background_r
ros2 param get /turtlesim background_b
```

<p align="center">
<img src="./img/param_get.png" style="width: 500;"></img>
</p>

### 3. param set
```bash
ros2 param set <node_name> <parameter_name> <value>
```
```bash
ros2 param set /turtlesim background_r 150
```

<p align="center">
<img src="./img/param_set.png" style="width: 500;"></img>
<img src="./img/param_set_turtlesim.png" style="width: 300;"></img>
</p>

### 4. param dump
```bash
ros2 param dump <node_name>
```
```bash
ros2 param dump /turtlesim > turtlesim.yaml
```
- try it in working directory

<p align="center">
<img src="./img/param_dump.png" style="width: 500;"></img>
</p>

```yaml
/turtlesim:
  ros__parameters:
    background_b: 255
    background_g: 86
    background_r: 150
    qos_overrides:
      /parameter_events:
        publisher:
          depth: 1000
          durability: volatile
          history: keep_last
          reliability: reliable
    use_sim_time: false
```

### 5. param load
```bash
ros2 param load <node name> <parameter file>
```
```bash
ros2 param load /turtlesim turtlesim.yaml
```

<p align="center">
<img src="./img/param_load.png" style="width: 500;"></img>
</p>

- Read-only parameters can only be modified at startup and not afterwards, that is why there are some warnings for the “qos_overrides” parameters.

### 6. Load parameter file on node startup
```bash
ros2 run <package name> <executable name> --ros-args --params-file <file name>
```
```bash
ros2 run turtlesim turtlesim_node --ros-args --params-file turtlesim.yaml --remap __node:=param_load
```

<p align="center">
<img src="./img/param_load_startup_terminal.png" style="width: 500;"></img>
<img src="./img/param_load_startup_turtlesim.png" style="width: 300;"></img>
</p>

### Summary
1. Nodes have parameters to define their default configuration values.
2. You can get and set parameter values from the command line.
3. You can also save the parameter settings to a file to reload them in a future session.

## ✅ Actions
<img src="./img/Action-SingleActionClient.gif"></img>

### 1. user actions

<p align="center">
<img src="./img/user_action.png" style="width: 500;"></img>
</p>

- G: 터틀봇의 방향을 0도(오른쪽)로 설정합니다.
- B: 터틀봇의 방향을 180도(왼쪽)로 설정합니다.
- V: 터틀봇의 방향을 90도(위쪽)로 설정합니다.
- C: 터틀봇의 방향을 270도(아래쪽)로 설정합니다.
- D: 터틀봇의 방향을 45도(대각선 위 오른쪽)로 설정합니다.
- E: 터틀봇의 방향을 135도(대각선 위 왼쪽)로 설정합니다.
- R: 터틀봇의 방향을 225도(대각선 아래 왼쪽)로 설정합니다.
- T: 터틀봇의 방향을 315도(대각선 아래 오른쪽)로 설정합니다.
- F: 현재 설정된 회전을 취소할 수 있습니다.
- Q: 프로그램이 종료됩니다.

### 2. node info
```bash
ros2 node info /turtlesim
ros2 node info /teleop_turtle
```

<p align="center">
<img src="./img/action_node_info_turtlesim.png" style="width: 500;"></img>
<img src="./img/action_node_info_teleop_turtle.png" style="width: 500;"></img>
</p>

- Action **Servers** : /turtlesim
- Action **Clients** : /teleop_turtle

### 3. action list
```bash
ros2 action list
```

<p align="center">
<img src="./img/action_list.png" style="width: 500;"></img>
</p>

#### 3.1 action list -t
```bash
ros2 action list -t
```

<p align="center">
<img src="./img/action_list_t.png" style="width: 500;"></img>
</p>

### 4. action info
```bash
ros2 action info <action name>
```
```bash
ros2 action info /turtle1/rotate_absolute
```

<p align="center">
<img src="./img/action_info.png" style="width: 500;"></img>
</p>

### 5. interface show
```bash
ros2 interface show <action type>
```
```bash
ros2 interface show turtlesim/action/RotateAbsolute
```

<p align="center">
<img src="./img/action_interface_show.png" style="width: 500;"></img>
</p>

### 6. action sned_goal
```bash
ros2 action send_goal <action name> <action type> <values>
```
```bash
ros2 action send_goal /turtle1/rotate_absolute \
turtlesim/action/RotateAbsolute \
"{theta: 1.57}"
```

<p align="center">
<img src="./img/action_send_goal.png" style="width: 500;"></img>
</p>

#### 6.1 action send_goal --feedback
```bash
ros2 action send_goal /turtle1/rotate_absolute \
turtlesim/action/RotateAbsolute \
"{theta: -1.57}" --feedback
```

<p align="center">
<img src="./img/action_send_goal_feedback_1.png" style="width: 500;"></img>
<img src="./img/action_send_goal_feedback_2.png" style="width: 500;"></img>
</p>

### Summary
1. Actions are like services that allow you to execute long running tasks, provide regular feedback, and are cancelable.
2. A robot system would likely use actions for navigation. An action goal could tell a robot to travel to a position. While the robot navigates to the position, it can send updates along the way (i.e. feedback), and then a final result message once it’s reached its destination.

## ✅ Colcon
> Concept of Libraries for Compilers Installation

### 1. Install colcon
```bash
sudo apt install python3-colcon-common-extensions
```

### 2. Create a workspace
```bash
mkdir <root directory name>/src
cd <root directory name>
```

### 3. Add some sources
```bash
git clone https://github.com/ros2/examples src/examples -b humble
```

### 4. Source an underlay
- source an underlay: 우리가 ROS2를 설치했을 때 ROS2의 기본 작업환경을 .bashrc 파일에 "source /opt/ros/humble/setup.bash" 형태로 source했던 것을 일반적으로 "underlay를 source했다"고 한다.
- source an overlay: ROS2의 기본 작업 환경을 source했으면 우리 개인이 만드는 (상대적으로 작은 규모의) 작업환경을 source하는 것을 "overlay를 source 한다"라고 표현한다.

이렇게 작업환경들을 source하는 이유는 서로 의존성이 있을 수 있는 파일들에게 "야 너가 지금 쓰려고 하는거 저기 다른 작업환경에 있어"라는 식으로 알려줄 수 있기 때문이다.

### 5. Build the workspace
```bash
colcon build --symlink-install
```

### 6. Run tests
```bash
colcon test
```

### 7. Sources the environment
```bash
source install/setup.bash
```

### 8. Try a demo
```bash
ros2 run examples_rclcpp_minimal_subscriber subscriber_member_function
ros2 run examples_rclcpp_minimal_publisher publisher_member_function
```

<p align="center">
<img src="./img/demo_publisher.png"></img>
<img src="./img/demo_subscriber.png"></img>
</p>

## ✅ Workspace

### 1. Make new directory
```bash
mkdir ros_ws2/src
cd ros_ws2/src
```

### 2. Copy sample repository
```bash
git clone https://github.com/ros/ros_tutorials.git -b humble
```
### 3. Check dependency
```bash
cd ..
rosdep install -i --from-path src --rosdistro humble -y
```

> if rosdep install -i --from-path src --rosdistro humble -y
```bash
sudo rosdep init
rosdep update
```

### 4. Build workspace by colon
```bash
colcon build
```

### 5. Overlay
> In new terminal
```bash
cd ros_ws2
source /opt/ros/humble/setup.bash
source install/local_setup.bash
ros2 run turtlesim turtlesim_node
```
> if qt.qpa.plugin: Could not find the Qt platform plugin "wayland" in "",
```bash
sudo apt install qtwayland5
```
> if QSocketNotifier: Can only be used with threads started with QThread
```bash

```
