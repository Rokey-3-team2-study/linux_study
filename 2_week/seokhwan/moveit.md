[링크](https://moveit.picknik.ai/main/doc/tutorials/quickstart_in_rviz/quickstart_in_rviz_tutorial.html#)

**목차**   
- [Step 1: Launch the Demo and Configure the Plugin](#step-1-launch-the-demo-and-configure-the-plugin)
- [Step 2: Play with the Visualized Robots](#step-2-play-with-the-visualized-robots)
- [Step 3: Interact with the Kinova Gen 3](#step-3-interact-with-the-kinova-gen-3)
- [Step 4: Use Motion Planning with the Kinova Gen 3](#step-4-use-motion-planning-with-the-kinova-gen-3)

## Step 1: Launch the Demo and Configure the Plugin

launch 파일 실행

```bash
ros2 launch moveit2_tutorials demo.launch.py
```

1. 디스플레이의 fixed frame을 /base_link로 변경
→ 내 경우 world가 맞는 것 같음
2. Display에서 MotionPlanning의 **RobotDescription**을 `robot_description`으로 변경
3. **Planning Scene Topic**를 `/monitored_planning_scene`로 변경
4. **Planned Path**의 **Trajectory Topic**을 `/display_planned_path`로 변경
5. **Planning Request**의 **Planning Group**를 `manipulator`로 변경
→ 나는 panda_arm에서 변경 안함

## Step 2: Play with the Visualized Robots

![image.png](attachment:17483872-76d6-4112-8191-f3ef866ccfbb:image.png)

로봇에는 4개의 오버래핑되는 시각화가 있다

1. `/monitored_planning_scene`설정 내의 계획된 환경
2. 로봇이 지나갈 경로
3. Green: 모션 의 시작점
4. Orange: 모션의 도착점

각 시각화는 켜거나 끌 수 있다

1. Planning Scene(환경을 말하는 듯)는 Scene Robot 트리 메뉴의 Show Robot Visual 체크박스
2. 로봇이 지나갈 경로는 Planned Path 트리 메뉴의 Show Robot Visual 체크박스
3. 시작점은 Planned Path 트리 메뉴의 Query Start State 체크박스
4. 도착점은 Planned Path 트리 메뉴의 Query Goal State 체크박스

## Step 3: Interact with the Kinova Gen 3

1. Planned Path트리 메뉴의 Show Robot Visual 체크박스 체크
2. Scene Robot 트리 메뉴의 Show Robot Visual 체크박스 해제
3. Planning Request 트리 메뉴의 Query Goal State 체크박스 체크
4. Planning Request 트리 메뉴의 Query Start State 체크박스 체크

![image.png](attachment:1d59468e-7208-4e4a-843c-b5e7b2917d7d:image.png)

오렌지색이 도착점 초록색이 시작점

![image.png](attachment:0a39956d-ed50-4d6c-874b-3f54adc760c1:image.png)

### Moving into collision

계획된 경로와 목표를 숨긴다

로봇팔이 충돌하게 움직여 봐라

충돌 확인이 어려우면 Planning 탭의 Use Collision-Aware IK 체크박스를 체크 하면 된다.

### Moving out of Reachable Workspace

로봇팔로 이동 가능한곳을 넘어가면 다시 돌아온다

![image.png](attachment:6844ccff-837d-4e40-94c3-69c76eff39f6:image.png)

### **Moving Joints or in Null Space**

Joints 탭으로 각 관절을 움직일 수 있다

null space exploration 슬라이더도 움직여봐라 → 왜인지 안움직임

![image.png](attachment:66564b8d-d7e9-4374-ae57-44c3984c7532:image.png)

## Step 4: Use Motion Planning with the Kinova Gen 3

