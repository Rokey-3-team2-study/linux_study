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

- 개념
  - ROS 2를 구성하는 가장 작은 실행 단위 중 하나.
  - 노드는 특정 기능을 담당
  - 노드는 네트워크 상에서 서로 토픽, 서비스, 액션을 통해 통신하여 협업

### 1. run
ROS 2 패키지 내부의 지정된 실행 파일(노드)을 실행하는 명령어
- 패키지: 특정 기능, 노드, 메세지, 서비스, 액션 등 관련 리소르를 하나로 묶어 관리하기 위한 디렉토리 단위
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
현재 실행 중인 모든 ROS 2 노드의 이름을 나열하는 명령어
```bash
ros2 node list
```
<p align="center">
<img src="./img/turtlesim_terminal.png" style="width: 500;"></img>
<img src="./img/turtle_teleop_key_terminal.png" style="width: 500;"></img>
<img src="./img/node_list.png" style="width: 500;"></img>
</p>

#### 2.1 remapping
실행 시 노드 이름을 <new name>으로 변경
```bash
ros2 run <package name> <executable name> --ros-args --remap __node:=<new name>
```
```bash
ros2 run turtlesim turtlesim_node --ros-args --remap __node:=my_turtle
```

<p align="center">
<img src="./img/turtlesim_remapping_terminal.png" style="width: 500;"></img>
<img src="./img/turtlesim_remapping.png" style="width: 300;"></img>
<img src="./img/node_list_remapping.png" style="width: 500;"></img>
</p>

### 3. node info
노드가 사용중인 Publisher, Subscriber, Service, Action에 대한 상세 정보 표시
```bash
ros2 node info /<node name>
```
```bash
ros2 node info /my_turtle
```

<p align="center">
<img src="./img/node_info.png" style="width: 500;"></img>
</p>

### Summary
1. 노드는 로봇 시스템에서 단일 및 모듈 용도로 사용되는 ROS 2의 기본 요소
2. 노드 *turtlesim* 및 *turtlesim_key*를 실행하여 *turtlesim* 패키지에서 생성된 노드를 활용
3. 활성 노드 이름을 검색하기 위해 *ros2 noed list*를 사용하고, 단일 노드를 관찰하기 위해 *ros2 node info*를 사용하는 방법을 배움

## ✅ Topic
<img src="./img/Topic-MultiplePublisherandMultipleSubscriber.gif"></img>

- 개념
  - 토픽은 **Publisher**와 **Subscriber** 간 **비동기성 데이터 스트리밍** 방식이다.
  - 한 노드에서 메시지를 특정 토픽으로 퍼블리시하면, 해당 토픽을 구독 중인 다른 노드들이 이를 수신한다. = **One-to-Many 통신**
- 특징
  - 주기적이고 연속적인 데이터 교환에 적합
  - Publisher는 보내기만 할 뿐, 메시지 수신여부를 확인하지 않음
  - Subscriber는 들어오는 메세지를 받아 처리리

### 1. rqt_graph
ROS 시스템 내의 노드, 토픽, 서비스 간의 연결 관계를 시각적으로 그래프 형태로 표시해주는 도구
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
현재 활성화된 모든 ROS 2 토픽의 이름을 나열
```bash
ros2 topic list
```

<p align="center">
<img src="./img/topic_list.png" style="width: 500;"></img>
</p>

현재 활성화된 모든 ROS 2 토픽의 이름과 각 토픽이 사용하는 메시지 타입을 함께 나열
```bash
ros2 topic list -t
```
<p align="center">
<img src="./img/topic_list-t.png" style="width: 500;"></img>
</p>

### 3. topic echo
지정한 ROS 2 토픽에서 퍼블리시되는 메시지를 실시간으로 화면에 출력
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
지정한 ROS 2 토픽의 퍼블리셔, 서브스크라이버, 메시지 타입 등 상세 정보를 표시
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
지정한 ROS 2 **메시지 타입**의 필드와 구조를 화면에 표시
- 메세지 타입: 노드 간에 주고받는 데이터의 구조와 형식을 정의하는 데이터 구조
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
지정한 토픽에 특정 메시지 타입의 메시지를 발행
```bash
ros2 topic pub <topic_name> <msg_type> '<args>'
```

노드 **/_ros2cli_21956** 이 /turtle1/cmd_vel로 메세지 발행
```bash
ros2 topic pub /turtle1/cmd_vel geometry_msgs/msg/Twist \
"{linear: {x: 2.0, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 1.8}}"
```

<p align="center">
<img src="./img/topic_pub_terminal.png" style="width: 500;"></img>
<img src="./img/topic_pub_turtlesim.png" style="width: 300;"></img>
<img src="./img/topic_pub_rqt_graph.png" style="width: 500;"></img>
</p>


토픽 **/turtle1/pose**이 turtle1의 자세 정보를 받고 보냄
```bash
ros2 topic echo /turtle1/pose
```

<p align="center">
<img src="./img/topic_pub_pose_rqt_graph.png" style="width: 500;"></img>
</p>


### 7. topic hz
지정한 ROS 2 토픽에서 메시지가 퍼블리시되는 빈도(Hz)를 실시간으로 측정
```bash
ros2 topic hz <topic name>
```
```bash
ros2 topic hz /turtle1/pose
```

<p align="center">
<img src="./img/topic_hz_terminal.png" style="width: 500;"></img>
</p>

메세지 퍼블리싱 빈도를 초당 1번으로 설정
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
지정한 ROS 2 토픽의 데이터 전송 대역폭을 실시간으로 측정
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
특정 메시지 타입을 사용하는 모든 ROS 2 토픽의 이름을 검색하여 나열
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
1. 노드는 토픽에 대한 정보를 게시하여 다른 노드들이 해당 정보를 구독하고 액세스할 수 있게 함
2. rqt_graph를 사용하여 토픽을 통해 여러 노드 간의 연결을 학습

## ✅ Services
<img src="./img/Service-MultipleServiceClient.gif"></img>

- 개념
  - 서비스는 **Request**와 **Response**를 기반으로 한 **동기 통신 방식**
  - **Service Client**: 클라이언트가 서비스를 요청
  - **Service Server**: 서버가 요청을 처리하고 응답
- 특징
  - 요청을 보낸 시점에 응답이 필요한 경우 사용
  - 요청이 들어올 때만 작업. 따라서, 지속적인 데이터 스트리밍이 필요하지 않은 곳에 사용

### 1. service list
현재 활성화된 모든 ROS 2 서비스의 이름을 나열
```bash
ros2 service list
```

<p align="center">
<img src="./img/service_list_terminal.png" style="width: 500;"></img>
</p>

### 2. service type
지정한 ROS 2 서비스의 **서비스 타입**을 표시
- 서비스 타입
  - Request, Response로 구성
  - 여러 필드로 구성, 특정 데이터 타입을 가짐짐
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
활성화된 모든 ROS 2 서비스의 이름과 각 서비스가 사용하는 서비스 타입을 함께 나열
```bash
ros2 service list -t
```

<p align="center">
<img src="./img/service_list_t.png" style="width: 500;"></img>
</p>

### 3. service find
특정 타입을 사용하는 모든 ROS 2 서비스의 이름을 나열
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
지정한 ROS 2 **인터페이스(메시지, 서비스, 액션) 타입**의 필드와 구조를 화면에 표시
- 인터페이스 타입: 노드들이 데이터를 주고 받을 때 사용하는 데이터 구조와 형식을 정의
  - 메시지 타입: 토픽을 통해 데이터를 주고 받을 때 사용
  - 서비스 타입: 요청과 응답 기반의 통신에 사용
  - 액션 타입: 목표, 피드백, 결과를 포함한 장기적이고 비동기적인 통신에 사용용
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
지정한 ROS 2 서비스에 특정 서비스 타입의 요청을 보내고 응답을 받는 명령어
- arguments는 필수 아님
```bash
ros2 service call <service name> <service type> <arguments>
```
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
2. **Unlike a topic** - a one way communication pattern where a node publishes information that can be consumed by one or more subscribers - a service is a request/response pattern where a client makes a request to a node providing the service and the service processes the request and generates a response.
1. 노드는 ROS 2의 서비스를 사용하여 통신할 수 있습니다.
2. 노드가 하나 이상의 구독자가 사용할 수 있는 정보를 게시하는 단방향 통신 패턴인 **토픽과 달리**, 서비스는 클라이언트가 서비스를 제공하는 노드에 요청을 하고 서비스가 요청을 처리하여 응답을 생성하는 요청/응답 패턴입니다.

## ✅ Parameters

- 개념
  - 노드에서 사용할 수 있는 설정값
  - 런타임, 런치 시점에 값을 조정할 필요가 있을 때 사용

### 1. param list
지정한 ROS 2 노드의 모든 파라미터 이름을 나열
```bash
ros2 param list
```

<p align="center">
<img src="./img/param_list.png" style="width: 500;"></img>
</p>

### 2. param get
특정 ROS 2 노드에서 지정한 파라미터의 값을 조회
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
특정 ROS 2 노드의 지정된 파라미터 값을 설정 또는 업데이트
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
지정한 ROS 2 노드의 모든 파라미터를 YAML 파일로 내보내는 명령어
- try it in working directory
```bash
ros2 param dump <node_name>
```
```bash
ros2 param dump /turtlesim > turtlesim.yaml
```

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
YAML 파일에서 지정한 ROS 2 노드로 파라미터를 불러와 적용
- Read-only parameters can only be modified at startup and not afterwards, that is why there are some warnings for the “qos_overrides” parameters. 
```bash
ros2 param load <node name> <parameter file>
```
```bash
ros2 param load /turtlesim turtlesim.yaml
```

<p align="center">
<img src="./img/param_load.png" style="width: 500;"></img>
</p>

### 6. Load parameter file on node startup
지정한 패키지의 실행 파일을 파라미터 파일과 함께 실행
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
1. 노드는 기본 구성 값을 정의할 수 있는 매개변수를 가지고 있습니다.
2. 명령줄에서 매개변수 값을 가져오고 설정할 수 있습니다.
3. 매개변수 설정을 파일에 저장하여 향후 세션에서 다시 로드할 수도 있습니다.

## ✅ Actions
<img src="./img/Action-SingleActionClient.gif"></img>

- 개념
  - 오래 걸리는 작업, 중간 피드백, 취소가 필요한 작업을 처리하기 위한 **비동기 통신 방식**
  - **Action Client**: Goal을 전송, Feedbask 수신, 필요하면 작업 취소
  - **Action Server**: Goal을 수신받아 작업을 수행
- 특징
  - 이동, 제어 등 시간이 오래 걸리는 작업에 유용
  - 액션 서버는 Goal을 수락한 후, 작업을 진행하며 주기적으로 Feedback을 전송, 최종적으로 Result 반환
  - 액션 클라이언트는 작업 중간에 Cancel을 호출해 작업을 중단시킬 수 있다.

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
현재 활성화된 모든 ROS 2 액션의 이름을 나열
```bash
ros2 action list
```

<p align="center">
<img src="./img/action_list.png" style="width: 500;"></img>
</p>

#### 3.1 action list -t
활성화된 모든 ROS 2 액션의 이름과 각 액션이 사용하는 액션 타입을 함께 나열
```bash
ros2 action list -t
```

<p align="center">
<img src="./img/action_list_t.png" style="width: 500;"></img>
</p>

### 4. action info
지정한 ROS 2 액션의 Publisher, Subscriber, 액션 타입 등 상세 정보를 표시
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
지정한 ROS 2 액션 타입의 Goal, Result, Feedback 메시지 구조를 화면에 표시
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
지정한 ROS 2 액션에 특정 액션 타입의 목표(goal)를 보내고, 응답을 받는 명령어
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
지정한 액션에 목표를 전송하고, 작업의 진행 상황에 대한 피드백을 실시간으로 수신
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
1. 작업은 장기적으로 실행되는 작업을 수행하고 정기적인 피드백을 제공하며 취소할 수 있는 서비스와 같다.
2. 로봇 시스템은 내비게이션에 액션을 사용. 액션 목표는 로봇에게 특정 위치로 이동하도록 지시. 로봇이 위치로 이동하는 동안 도중에 업데이트(예: 피드백)를 보내고, 목적지에 도착하면 최종 결과 메시지를 보낼 수 있다.

## ✅ Colcon
> Concept of Libraries for Compilers Installation
- 개념: Colcon은 ROS 2에서 패키지를 빌드하고 관리하기 위한 **빌드 도구**

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
- 개념
  - 워크스페이스는 ROS 2 패키지들이 모여 있는 디렉토리 구조
  - 하나의 워크스페이스 안에는 여러 패키지, 소스 코드, 빌드 파일 등이 포함
  - 워크스페이스는 ROS 2 개발 환경을 설정하고, 패키지를 빌드하며, 실행하는 데 사용

### 1. Make new directory
In build terminal = underlay terminal
```bash
source /opt/ros/humble/setup.bash
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

- rosdep install -i --from-path src --rosdistro humble -y
  ```bash
  sudo rosdep init
  rosdep update
  ```

### 4. Build workspace by colon
```bash
colcon build
```

### 5. Overlay
In new terminal = overlay terminal
```bash
cd ros_ws2
source /opt/ros/humble/setup.bash   # underlay source
source install/local_setup.bash     # overlay source
ros2 run turtlesim turtlesim_node
```

- qt.qpa.plugin: Could not find the Qt platform plugin "wayland" in "",

  ```bash
  export QT_QPA_PLATFORM=xcb
  ```

- symbol lookup error: /snap/core20/current/lib/x86_64-linux-gnu/libpthread.so.0: undefined symbol: __libc_pthread_init, version GLIBC_PRIVATE

  - Try it in terminal. <U>**Not in VSC terminal**</U>

### 6. Modify Overlay
```bash
cd ~/ros_ws2/src/ros_tutorials/turtlesim/src
```
52 line in turtle_frame.cpp : TurtleSim -> MyTurtleSim

In build terminal
```bash
colcon build
```

In overlay terminal
```bash
ros2 run turtlesim turtlesim_node
```