# 1.  Package build & create

## 1.1 Underlay & Overlay
| **구분**               | **오버레이 (Overlay)**                                  | **언더레이 (Underlay)**                                  |
|-----------------------|-------------------------------------------------------|--------------------------------------------------------|
| **정의**              | 개발자가 직접 작업하는 공간. 소스 빌드된 패키지가 위치.  | 기반이 되는 공간. 일반적으로 `apt-get`으로 설치된 ROS2 환경. |
| **우선순위**           | **높음** (동일한 패키지가 있을 때 오버레이의 패키지가 우선 사용됨) | **낮음** (오버레이에 패키지가 없을 때만 사용됨)                   |
| **환경 설정 방법**     | `source install/local_setup.bash` (오버레이만 설정)      | `source /opt/ros/<distro>/setup.bash` (언더레이 설정)     |
|                       | `source install/setup.bash` (오버레이 + 언더레이 설정)   |                                                         |
| **수정 여부** | **가능** (소스 코드 직접 수정 후 재빌드)                   | **불가능** (바이너리 설치이므로 코드 변경 불가)                   |
| **빌드 명령**          | `colcon build` 또는 `colcon build --symlink-install`     | 필요 없음 (`apt-get`으로 이미 설치됨)                          |
| **의존성 관리**        | 오버레이의 패키지가 언더레이에 의존 가능                     | 언더레이는 오버레이에 영향을 주지 않음                          |
| **사용 목적**          | 개발, 테스트, 커스터마이징                               | 안정적인 기본 환경 제공                                    |
| **예시 경로**          | `~/ros2_ws` (사용자 작업 공간)                          | `/opt/ros/humble` (공식 패키지 설치 경로)                     |

---
- 환경 설정 시 오버레이와 언더레이에 **동일한 패키지 존재 시 충돌**
- 충돌 발생 시 오버레이와 언더레이 패키지 이름을 다르게 하거나 local_setup.bash로 재소싱.

## 1.2 Comands
### - install
```bash
sudo apt install python3-colcon-common-extensions
```
### - 종속성 확인
```bash
rosdep install -i --from-path src --rosdistro humble -y
```
### - build method
```bash
# 기본적인 빌드 
colcon build
# 패키지 + 종속성 빌드 - 전체 작업 공간 빌드 X (시간 절약)
colcon build --packages-up-to
# 코드 수정 시 즉시 빌드 없이 즉시 반영 but, 배포용으로 권장 X
colcon build --symlink-install
# log를 보여줌
colcon build --event-handlers console_direct+
# 병렬 처리 (패키지 하나씩)
colcon build --executor sequential
# 패키지 하나만 빌드
colocn build --packages-select <package_name>
```
### pkg create
```bash
# python
ros2 pkg create --build-type ament_python --license Apache-2.0 <package_name>
# c++
ros2 pkg create --build-type ament_cmake --license Apache-2.0 <package_name>
```
### pkg file structure
```bash
# python
my_package/
      package.xml # *** -> 패키지 정보
      resource/my_package
      setup.cfg
      setup.py
      my_package/
# c++
my_package/
     CMakeLists.txt # *** -> code build method
     include/my_package/
     package.xml
     src/
```