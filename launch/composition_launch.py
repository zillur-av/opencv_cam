"""
Dynamically compose OpencvCamNode and ImageSubscriberNode in a component_container.

Limitations of this container:
 -- stdout is not set to flush after each line, so the most recent log messages may be delayed
"""

import launch
from launch_ros.actions import ComposableNodeContainer
from launch_ros.descriptions import ComposableNode


def generate_launch_description():
    camera_info_path = '/home/zillur/ros2_ws/src/opencv_cam/config/camera_info.yaml'

    container = ComposableNodeContainer(
        name='my_container',
        namespace='',
        package='rclcpp_components',
        executable='component_container',
        composable_node_descriptions=[
            ComposableNode(
                package='opencv_cam',
                plugin='opencv_cam::OpencvCamNode',
                name='image_publisher',
                parameters=[{
                    'file': False,
                    'filename': "",
                    'index': 2,
                    'camera_frame_id': 'traffic_light_left_camera/camera_link',
                    'camera_info_path': camera_info_path,
                }],
                remappings=[
                     ('/image_raw', '/sensing/camera/camera6/image_raw'),
                     ('/camera_info', '/sensing/camera/camera6/camera_info')
                ],
                extra_arguments=[{'use_intra_process_comms': True}],
            ),
        ],
        output='screen',
    )

    return launch.LaunchDescription([container])
