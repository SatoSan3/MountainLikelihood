import numpy as np

def get_slope_and_intercept(x1,y1,x2,y2):
    slope = (y1-y2)/(x1-x2)
    intercept = y1 - slope * x1
    return slope , intercept

def get_intersection_point(a1,b1,a2,b2):
    x = (b2 - b1)/(a1 - a2)
    y = (a2*b1 - a1*b2)/(a2 - a1)
    return x , y
    
def get_distance_between_segment_point(x1,y1,x2,y2,px,py):
    """
    x1,y1,x2,y2は線分の端点の座標を表す。
    px,pyは点の座標を表す。
    """
    a1 , b1 = get_slope_and_intercept(x1,y1,x2,y2)
    
    #線分の傾きに垂直で(px,py)を通る直線の傾きと切片を求める
    a2 = -1.0/a1
    b2 = py - a2*px
    
    x , y = get_intersection_point(a1,b1,a2,b2)
    
    mean_x = (x1 + x2)/2 
    mean_y = (y1 + y2)/2
    #傾きa2,切片b2の直線が線分と交点を持つ場合
    if np.linalg.norm([mean_x - x2,mean_y - y2]) > np.linalg.norm([mean_x - x , mean_y - y]):
        return np.linalg.norm([x - px,y - py])
    
    #点(x1,y1)と点(px,py)の距離、点(x2,y2)と点)(px,py)の距離で短いものを返す
    if np.linalg.norm([x1 - px,y1 - py]) < np.linalg.norm([x2 - px,y2 - py]):
        return np.linalg.norm([x1 - px,y1 - py])
    return np.linalg.norm([x2 - px,y2 - py])
    
if __name__ == "__main__":
    print(get_slope_and_intercept(1,1,0,0))
    print(get_slope_and_intercept(0.5,2,0,1))
    print(get_distance_between_segment_point(1,1,2,2,3,4))
    
    