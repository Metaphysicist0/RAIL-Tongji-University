import cv2
import numpy as np
 

# 四元数转欧拉角
from scipy.spatial.transform import Rotation as R
 
def quaternion2euler(quaternion):
    r = R.from_quat(quaternion)
    euler = r.as_euler('xyz', degrees=True)
    return euler
 
quaternion = [0.03551,0.21960,-0.96928, 0.10494]
print(quaternion2euler(quaternion))
 
# 输出
# [ -24.90053735    6.599459   -169.1003646 ]

# 欧拉角转四元数
from scipy.spatial.transform import Rotation as R
 
 
def euler2quaternion(euler):
    r = R.from_euler('xyz', euler, degrees=True)
    quaternion = r.as_quat()
    return quaternion
 
 
euler = [-24.90053735, 6.599459, -169.1003646]
print(euler2quaternion(euler))
 
# 输出
# [ 0.03550998  0.21959986 -0.9692794   0.10493993]
