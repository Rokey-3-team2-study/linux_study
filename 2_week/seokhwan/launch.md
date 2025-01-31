[링크](https://docs.ros.org/en/humble/Tutorials/Intermediate/Launch/Creating-Launch-Files.html)

**목차**
- [1. Launch 파일이란? ](#1-launch-파일이란)
- [2. Launch 파일 생성 및 위치 ](#2-launch-파일-생성-및-위치)
- [3. Launch 파일 작성 및 사용법 ](#3-launch-파일-작성-및-사용법)

### 1. Launch 파일이란?

launch system은 **실행과 관련된 시스템의 구성**을 저장하여 ros2의 실행을 간단하게 한다

시스템의 구성

- 어떤 프로그램(node)를 실행할 지
- 어디서 실행할 지
- 어떤 argument를 넘겨줄 지(= 사용할 지)
- …

이러한 시스템의 구성을 미리 기록하여 간단하게 실행 할 수 있도록한다

### 2. Launch 파일 생성 및 위치

- workspace 내부에 launch 폴더 생성
- 생성된 launch 폴더에 ~~~_launch.py  파일 생성

→ `/ros2_ws/launch/~~~_launch.py` 

### 3. Launch 파일 작성 및 사용법

LaunchDescription 클래스를 리턴하는 generate_launch_description()의 함수를 정의하여 작성한다

**사용법 1 - launch 파일 생성 후 ros2 launch 명령어로 실행**

- example_launch.py

```bash
# 필요한 모듈 import
from launch import LaunchDescription
from launch_ros.actions import Node

# generate_laucnh_description 함수로 launch가 실행됨
# 실행할 node 들의 패키지와 노드 이름등을 입력해야 한다

def generate_launch_description():

    # generate_launch_description함수
    # 실행으로 반환할 값 = LaunchDescription 클래스
    return LaunchDescription(
        [
            # 노드1
            Node(
                package="turtlesim",
                namespace="turtlesim1",
                executable="turtlesim_node",
                name="sim",
            ),
            # 노드2
            Node(
                package="turtlesim",
                namespace="turtlesim2",
                executable="turtlesim_node",
                name="sim",
            ),
            # 노드3
            Node(
                package="turtlesim",
                executable="mimic",
                name="mimic",
                remappings=[
                    ("/input/pose", "/turtlesim1/turtle1/pose"),
                    ("/output/cmd_vel", "/turtlesim2/turtle1/cmd_vel"),
                ],
            ),
        ]
    )

```

**실행 -  terminal 창에서** 

```bash
ros2 launch exmaple_launch.py
```

**사용법 2 - ros2 launch 환경 세팅 후 python으로 실행**

- launch_run.py

```bash
# 필요한 모듈 import
import launch
from launch import LaunchDescription
from launch_ros.actions import Node

# generate_laucnh_description 함수로 launch가 실행됨
# 실행할 node 들의 패키지와 노드 이름등을 입력해야 한다

def generate_launch_description():

    # generate_launch_description함수
    # 실행으로 반환할 값 = LaunchDescription 클래스
    return LaunchDescription(
        [
            # 노드1
            Node(
                package="turtlesim",
                namespace="turtlesim1",
                executable="turtlesim_node",
                name="sim",
            ),
            # 노드2
            Node(
                package="turtlesim",
                namespace="turtlesim2",
                executable="turtlesim_node",
                name="sim",
            ),
            # 노드3
            Node(
                package="turtlesim",
                executable="mimic",
                name="mimic",
                remappings=[
                    ("/input/pose", "/turtlesim1/turtle1/pose"),
                    ("/output/cmd_vel", "/turtlesim2/turtle1/cmd_vel"),
                ],
            ),
        ]
    )

# 이 부분이 중요
def main():
    # 런치 서비스 생성
    launch_service = launch.LaunchService()

    # 런치 파일에서 LaunchDescription 가져오기
    launch_description = generate_launch_description()

    # 런치 서비스에 LaunchDescription 추가
    launch_service.include_launch_description(launch_description)

    # 런치 실행
    launch_service.run()

if __name__ == "__main__":
    main()

```

**실행 -  terminal 창에서** 

```bash
python3 launch_run.py
```