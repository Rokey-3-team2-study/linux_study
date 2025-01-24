[링크](https://docs.ros.org/en/humble/Tutorials/Beginner-CLI-Tools/Understanding-ROS2-Services/Understanding-ROS2-Services.html)

## Table of Contents
1. [서비스란?](#1-서비스란)
2. [ros2 service list](#2-ros2-service-list)
3. [ros2 service type](#3-ros2-service-type)
   - [ros2 service list -t](#3_1-ros2-service-list--t)
4. [ros2 service find](#4-ros2-service-find)
5. [ros2 interface show](#5-ros2-interface-show)
6. [ros2 service call](#6-ros2-service-call)
7. [요약](#요약)

### 1. 서비스란?

서비스는 node가 ros 그래프 안에서 통신하는 다른 방법이다

서비스는 call-and-response 모델을 바탕으로 한다

(토픽은 publisher-subscriber 모델로 동작)

토픽: 지속적으로 데이터 스트림을 통해 subscribe, 지속적으로 업데이트

서비스: 클라이언트가 요청했을 때만 데이터 생성

서비스 1개에

클라이언트는 여러 개 가능, 서버는 1개

### 2. ros2 service list

서비스 리스트 출력

**`ros2 service list` 명령어를 통해 서비스 리스트 출력이 가능하다**

```bash
# turtlesim과 teleopkey 노드 실행 시 확인 가능한 서비스 리스트
/clear
/kill
/reset
/spawn
/teleop_turtle/describe_parameters
/teleop_turtle/get_parameter_types
/teleop_turtle/get_parameters
/teleop_turtle/list_parameters
/teleop_turtle/set_parameters
/teleop_turtle/set_parameters_atomically
/turtle1/set_pen
/turtle1/teleport_absolute
/turtle1/teleport_relative
/turtlesim/describe_parameters
/turtlesim/get_parameter_types
/turtlesim/get_parameters
/turtlesim/list_parameters
/turtlesim/set_parameters
/turtlesim/set_parameters_atomically
```

두 노드가 공통적으로 parameter에 관한 6개의 서비스가 있다

ros2의 노드 거의 대부분은 매개변수 기반으로 구축된 인프라 서비스가 있다

### 3. ros2 sevice type

**서비스의 request값, response 값의 타입 출력**

서비스의 타입은 topic 타입과 비슷하게 정의된다.

```bash
# 형식
ros2 service type <service_name>

# 예시
ros2 service type /clear

# 결과
std_srvs/srv/Empty
```

여기서 empty 타입은 sevice call 시 no data 요청, no data 응답을 의미한다

### 3_1. ros2 sevice list -t

모든 서비스의 type 한번에 확인

```bash
# 입력
ros2 service list -t
```

### 4. ros2 service find

**특정한 타입의 모든 서비스를 찾을 수도 있다**

```bash
# 형식
ros2 service find <type_name>

# 예시
ros2 service find std_srvs/srv/Empty

# 결과
/clear
/reset
```

### 5. ros2 interface show

**서비스의 입력 구조 확인**

```bash
# 형식
ros2 interface show <type_name>

# 예시 1
ros2 interface show std_srvs/srv/Empty

# 예시 2
ros2 interface show turtlesim/srv/Spawn
```

예시 1 결과

```bash
---
```

--- 기준으로 위는 입력 아래는 리턴

std_srvs/srv/Empty 타입은 둘다 비어있다

예시 2 결과

```bash
float32 x
float32 y
float32 theta
string name # Optional.  A unique name will be created and returned if this is empty
---
string name
```

### 6. ros2 service call

터미널에서 서비스를 직접 call 할 수 있다

```bash
# 형식
ros2 service call <service_name> <service_type> <arguments>

# 예시 1
# 경로를 clear함
ros2 service call /clear std_srvs/srv/Empty 

# 예시 2
# 거북이를 spawn함
ros2 service call /spawn turtlesim/srv/Spawn "{x: 2, y: 2, theta: 0.2, name: ''}"
```

예시 2 결과

```bash
requester: making request: turtlesim.srv.Spawn_Request(x=2.0, y=2.0, theta=0.2, name='')

response:
turtlesim.srv.Spawn_Response(name='turtle2')
```

### 요약

- 서비스는 클라이언트가 요청, 서버가 리스폰스 해준다
- 클라이언트는 여러 개 가능, 서버는 1개만 가능
- 서비스 리스트 확인
→ 서비스 형식 확인
→ 서비스 요청
순으로 사용 하면 된다