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

### 6. service echo
```bash
ros2 service echo <service_name | service_type> <arguments>
```
```bash
ros2 service echo <service_name | service_type> <arguments>
```

<p align="center">
<img src="./img" style="width: 500;"></img>
</p>

### Summary
1. a
2. b
3. c

## ✅ Parameters

## ✅ Actions
<img src="./img/Action-SingleActionClient.gif"></img>

## ✅ Colcon
> Concept of Libraries for Compilers Installation

