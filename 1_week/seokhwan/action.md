[링크](https://docs.ros.org/en/humble/Tutorials/Beginner-CLI-Tools/Understanding-ROS2-Actions/Understanding-ROS2-Actions.html)

## Table of Contents
1. [Action 이란?](#1-action-이란)
2. [Use actions](#2-use-actions)
3. [Ros2 node info](#3-ros2-node-info)
4. [ros2 action list](#4-ros2-action-list)
   - [ros2 action list -t](#41-ros2-action-list--t)
5. [ros2 action info](#5-ros2-action-info)
6. [ros2 interface show](#6-ros2-interface-show)
7. [ros2 action send_goal](#7-ros2-action-send_goal)
8. [요약](#요약)

### 1. Action 이란?

- Action은 오랜시간 동작하는 task를 위한 커뮤니케이션 방법이다.
- Goal, Feedback, Result 3가지 파트로 구성된다.
- action은 취소할 수 있다는 것을 제외하면 service와 기능이 비슷하다
- Action Client 노드는 Action Server에 Goal을 보낸다
서버는 Goal을 인식하고 결과를 feedback 해준다

= Client → Server에 goal전달, goal까지 동작 완료 후 Server → Client로 응답

### 2. Use actions

turtlesim 패키지에서 teleopkey를 사용하면 아래 결과를 볼 수 있는데 두번째 줄이 action에 대한 내용이다.

```bash
Use arrow keys to move the turtle.
Use G|B|V|C|D|E|R|T keys to rotate to absolute orientations. 'F' to cancel a rotation.
```

**Goal 특징**

- Goal은 클라이언트나 서버 측 둘 다 취소가 가능하다
- Goal 완료 전 다음 Goal이 들어왔을 때
1) 이전 Goal 취소 및 새로운 Goal 설정
2) 이전Goal 완료  후 새로운 Goal 설정
3) 새로운 Goal 무시
셋 다 가능하다

### 3. Ros2 node info

**node 정보 출력**

```bash
# 노드 출력 명령어
ros2 node info /turtlesim
```

```bash
# 결과
/turtlesim
  Subscribers:
    /parameter_events: rcl_interfaces/msg/ParameterEvent
    /turtle1/cmd_vel: geometry_msgs/msg/Twist
  Publishers:
    /parameter_events: rcl_interfaces/msg/ParameterEvent
    /rosout: rcl_interfaces/msg/Log
    /turtle1/color_sensor: turtlesim/msg/Color
    /turtle1/pose: turtlesim/msg/Pose
  Service Servers:
    /clear: std_srvs/srv/Empty
    /kill: turtlesim/srv/Kill
    /reset: std_srvs/srv/Empty
    /spawn: turtlesim/srv/Spawn
    /turtle1/set_pen: turtlesim/srv/SetPen
    /turtle1/teleport_absolute: turtlesim/srv/TeleportAbsolute
    /turtle1/teleport_relative: turtlesim/srv/TeleportRelative
    /turtlesim/describe_parameters: rcl_interfaces/srv/DescribeParameters
    /turtlesim/get_parameter_types: rcl_interfaces/srv/GetParameterTypes
    /turtlesim/get_parameters: rcl_interfaces/srv/GetParameters
    /turtlesim/list_parameters: rcl_interfaces/srv/ListParameters
    /turtlesim/set_parameters: rcl_interfaces/srv/SetParameters
    /turtlesim/set_parameters_atomically: rcl_interfaces/srv/SetParametersAtomically
  Service Clients:

  Action Servers:
    /turtle1/rotate_absolute: turtlesim/action/RotateAbsolute
  Action Clients:
```

결과를 보면 마지막에 `Action Servers`에서 

`/turtle1/rotate_absolute` 액션을  확인할 수 있다
turtlesim 노드가 `/turtle1/rotate_absolute` 액션에 대해서 

teleopkey노드는 해당내용을 Action Servers에서가지고 있다

### 4. ros2 action list

**액션 리스트 출력**

```bash
# 입력
ros2 action list

# 출력
/turtle1/rotate_absolute
```

### 4.1 ros2 action list -t

**액션의 타입 출력**

액션도 topic이나 service 처럼 타입이 있다

list에서 -t 옵션을 사용해서 타입까지 출력 가능하다

타입을 사용해서 Command line이나 코드에서 액션 실행이 가능하다

```bash
# 입력
ros2 action list -t

# 출력
/turtle1/rotate_absolute [turtlesim/action/RotateAbsolute]
```

### 5. ros2 action info

**액션 정보 출력**

```bash
# 입력
ros2 action info /turtle1/rotate_absolute

# 출력
Action: /turtle1/rotate_absolute
Action clients: 1
    /teleop_turtle
Action servers: 1
    /turtlesim
```

액션이 뭐가 있는지

액션의 client, server의 수와 이름이 나온다

### 6. ros2 interface show

**action의 구조 확인**

action을 실행하기 전에 필요한 정보를 알 수 있다

services에서 request와 response 확인하는 것과 같다

```bash
# 입력
ros2 interface show turtlesim/action/RotateAbsolute

# 출력
# The desired heading in radians
float32 theta
---
# The angular displacement in radians to the starting position
float32 delta
---
# The remaining rotation in radians
float32 remaining
```

--- 를 기준으로 순서대로

goal request

goal result

feed back

로 구별된다

두번째가 결과고 세번째가 feed back이다

### 7. ros2 action send_goal

**command line에서 직접 action의 goal 입력**

```bash
# 형식
ros2 action send_goal <action_name> <action_type> <values>

# 예시1
ros2 action send_goal /turtle1/rotate_absolute turtlesim/action/RotateAbsolute "{theta: 1.57}"

# 예시2, feedback option 추가
ros2 action send_goal /turtle1/rotate_absolute turtlesim/action/RotateAbsolute "{theta: -1.57}" --feedback
```

`<values>`는 YAML형식이 필요하다

결과를 보면 각 goal은 unique id를 가지고 있다

```bash
Waiting for an action server to become available...
Sending goal:
   theta: 1.57

Goal accepted with ID: f8db8f44410849eaa93d3feb747dd444

Result:
  delta: -1.568000316619873

Goal finished with status: SUCCEEDED
```

feed back도 보고 싶으면 --feedback 옵션을 추가하면 된다

### 요약

Action은 Service와 거의 유사하다

Service: Request 전송 → 완료 후 Response 응답

Action: Goal 전송 → 동작 중에 feed back 응답 → 완료 후 Goal 응답

사용예시

로봇이 목적지 까지 이동할 때 Action의 Goal은 목적지를 설정할 수 있다

그리고 이동하는 중에 현재 위치를 update할 수 있다