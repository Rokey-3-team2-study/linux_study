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
