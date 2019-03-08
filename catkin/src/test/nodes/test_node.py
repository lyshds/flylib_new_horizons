#!/usr/bin/env python
from __future__ import print_function
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge



class TestNode(object):

    def __init__(self):
        rospy.init_node('test_node')
        self.bridge = CvBridge()
        self.image_sub = rospy.Subscriber('/ca_camera_left/image_raw', Image, self.handle_image)

    def handle_image(self, data):
        print(data.header)
        cv_image = self.bridge.imgmsg_to_cv2(data,desired_encoding="passthrough")
        print(cv_image.shape)
        print()


    def run(self):
        cnt = 0
        while not rospy.is_shutdown():
            print(cnt)
            rospy.sleep(1.0)
            cnt += 1

# ----------------------------------------------------------------------------------------------------------
if __name__ == '__main__':


    node = TestNode()
    node.run()
