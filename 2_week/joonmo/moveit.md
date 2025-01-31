# MoveIt 파이프라인 노드 구성 정리

## 전체 구조 개요

### 핵심 노드/구성 요소

1. **move_group 노드**  
   - MoveIt의 중심 노드.  
   - 요청받은 플래닝, 충돌 검사, 실행 관리를 통합적으로 수행.  
   - 내부에서 `PlanningSceneMonitor`, `Trajectory Execution Manager`, 각종 플래너(OMPL, STOMP, CHOMP 등) 플러그인을 사용.

2. **robot_state_publisher 노드**  
   - URDF를 참조해 로봇의 링크와 조인트를 TF 트리(Transform)를 통해 퍼블리싱.  
   - 주로 로봇의 현재 관절 값(joint_states)을 받아 TF를 갱신.

3. **joint_state_publisher 노드**  
   - 실제 하드웨어가 없는 환경에서, 관절 값을 퍼블리시하거나 GUI를 통해 관절 상태를 변경 가능케 해줌.  
   - 시뮬레이션/테스트 환경에서 많이 사용.

4. **ROS Controller / 드라이버 노드**  
   - 실제 로봇 하드웨어와 통신하거나, Gazebo 시뮬레이터 등과 연동해 관절 제어를 수행.  
   - 예: `controller_manager`, 특정 로봇용 드라이버 패키지 등.  
   - MoveIt은 이 노드(혹은 액션 서버)에 `FollowJointTrajectory` 액션 등을 통해 경로를 전달.

5. **Rviz MoveIt Plugin** (별도 노드라기보다는 플러그인)
   - Rviz에서 Interactive Marker 등을 통해 목표 상태(End-effector pose, Joint value)를 설정하고, move_group과 상호 작용.  
   - 사용자는 RViz 플러그인을 통해 경로 요청, 결과 시각화 가능.

이외에도 **센서 데이터**(Depth 카메라, LiDAR 등)를 받아 환경 장애물을 모델링하는 `moveit_ros_perception` 계열 패키지나, 플래닝 알고리즘을 추가하는 여러 플러그인들이 있지만, 기본적으로는 `move_group` 노드를 중심으로 구성됩니다.

---

## 1. 로봇 상태/환경 정보 획득

1. **robot_state_publisher 노드**  
   - **URDF**를 바탕으로 로봇의 링크-조인트 구조(TF 트리)를 퍼블리싱.  
   - **joint_state_publisher 노드**나 하드웨어 드라이버 노드로부터 받은 `JointState` 메시지를 토대로 로봇의 TF 상태를 계속 갱신.

2. **move_group 노드** 내부의 `PlanningSceneMonitor`  
   - **TF**, **센서 데이터**, **JointState** 등을 받아 **PlanningScene**(로봇+환경 모델)을 동기화.  
   - 충돌 검사 시 이 PlanningScene을 활용해 로봇과 장애물 사이를 계산.

3. **joint_state_publisher 노드**(필요시)  
   - 실제 하드웨어가 없을 경우, GUI나 파라미터를 통해 임의 관절 값을 퍼블리시.  
   - 시뮬레이션이나 테스트 환경에서 사용.

---

## 2. 목표 상태 정의

- 사용자가 Rviz MoveIt Plugin(인터페이스)을 사용하거나, **move_group** API(ROS Action/Service/Topic 호출)로 원하는 **End-effector pose**나 **joint angles**를 설정.
- 별도의 독립 노드 없이도, **Rviz 플러그인** 또는 **moveit_cpp / MoveGroupInterface**(C++/Python 라이브러리) 등을 통해 **move_group** 노드에 목표 상태를 전달.

---

## 3. 플래닝 요청 (Planning Request) 전달

1. **사용자 측** (Rviz, Custom Node, MoveGroupInterface)  
   - 목표 위치(또는 Joint State), 플래너 타입(OMPL, STOMP, CHOMP 등), 제약조건 등을 입력해 `move_group`에 플래닝 요청(서비스/액션 호출).

2. **move_group 노드**  
   - 내부 **Planning Pipeline**을 통해 경로 탐색 수행.  
   - OMPL, STOMP 등 다양한 플래너는 플러그인으로 동작하며, `move_group`이 이를 호출.  
   - 결과 경로(trajectory)와 함께 충돌 여부, 성공/실패 상태를 반환.

---

## 4. 충돌 검사 (Collision Checking)

1. **move_group 노드** 내부의 `PlanningSceneMonitor`  
   - 로봇 모델, 환경 모델(센서로 추정된 장애물 포함)을 참조.  
   - 경로 상 충돌이 있는지 실시간으로 확인하며, 충돌 시 대안 경로를 탐색하도록 플래너에 피드백.

2. 센서 데이터 연동 시  
   - `moveit_ros_perception` 계열 노드(OctoMap 등)를 통해 장애물 데이터가 `PlanningScene`에 업데이트됨.  
   - 업데이트된 장면 정보로 충돌 검사를 수행.

---

## 5. 실행 (Execution)

1. **move_group 노드** 내부의 `Trajectory Execution Manager`  
   - 플래닝된 안전 경로(trajectory)를 실제 로봇 제어기로 전달하는 과정 관리.  
   - 계획된 경로를 **ROS 컨트롤러 노드(또는 FollowJointTrajectory 액션 서버)**에 전송.

2. **ROS Controller / 드라이버 노드**  
   - 전달받은 trajectory를 하드웨어에 맞게 실제로 모터/관절을 구동하거나, 시뮬레이터(Gazebo)와 연결해 움직임을 재현.  
   - MoveIt Controller Manager를 통해 여러 종류의 컨트롤러와 연동할 수 있음.

---

## 6. 피드백 / 상태 모니터링

1. **move_group 노드**  
   - 실행 중 하드웨어(또는 시뮬레이터)에서 올라오는 joint_states, 액션 결과, 센서 데이터를 계속 수신.  
   - 실제 로봇 또는 시뮬레이터 상태가 계획대로 이동 중인지, 충돌이 발생했는지 등을 실시간 모니터링.

2. **Rviz MoveIt Plugin**  
   - 사용자 시각화 측면에서, 로봇의 실제 움직임(또는 가상 움직임)을 모니터링할 수 있도록 화면에 갱신.  
   - 경로 실행 도중의 상태를 시각적으로 확인.

---

## 요약: 단계별 노드/구성 요소 매핑

| 단계                                   | 주요 노드/구성 요소                                   | 역할                                                                                   |
|----------------------------------------|--------------------------------------------------------|-----------------------------------------------------------------------------------------|
| 1. 로봇 상태/환경 정보 획득           | - robot_state_publisher <br> - joint_state_publisher <br> - move_group(PlanningSceneMonitor) | - 로봇 TF(Transform) 퍼블리시 <br> - 센서/관절 정보 수집 <br> - PlanningScene 갱신         |
| 2. 목표 상태 정의                      | - 사용자(Rviz Plugin) 또는 move_group API             | - 목표 pose/Joint 설정 <br> - move_group에 목표 상태 전달                              |
| 3. 플래닝 요청(Planning Request) 전달 | - move_group 노드                                      | - 내부 플래닝 파이프라인 (OMPL 등 플러그인) 호출 <br> - 경로 생성                        |
| 4. 충돌 검사(Collision Checking)       | - move_group(PlanningSceneMonitor) <br> - 센서 처리 노드(선택) | - 로봇+환경 장애물 정보 기반 충돌 검사 <br> - 충돌 발생 시 재플래닝                      |
| 5. 실행(Execution)                     | - move_group(Trajectory Execution Manager) <br> - ROS Controller 노드 | - 결정된 경로를 로봇 제어기로 전달 <br> - 하드웨어(또는 시뮬레이터) 구동                |
| 6. 피드백/상태 모니터링               | - move_group <br> - Rviz MoveIt Plugin <br> - ROS Controller 노드  | - 로봇 움직임, 충돌 여부, 상태 정보 실시간 수신 <br> - Rviz 등 시각화                   |

---
