import numpy as np
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
from scipy.stats import norm

import distance_calculator as d_c

def get_z_value(x,y,segment):
    min_distance = d_c.get_distance_between_segment_point(segment[0][0][0],
             segment[0][0][1],segment[0][1][0],segment[0][1][1],x,y)
    
    for i in range(1,len(segment)):
        temp_distance = d_c.get_distance_between_segment_point(segment[i][0][0],
             segment[i][0][1],segment[i][1][0],segment[i][1][1],x,y)
        if temp_distance < min_distance:
            min_distance = temp_distance
            
    return norm.pdf(min_distance)
    
    
        
def make_wire_frame(x,y,segment):
    """
    山の標高の和を尤度とする計算を視覚化する
    x,yがLiDARから得られた点群の座標データ
    segmentがLiDARのレーザーがあたる壁の地図情報
    """
    
    #ワイヤーフレームの準備
    X, Y = np.mgrid[0:10:0.1, 0:10:0.1]
    pos = np.empty(X.shape + (2,))
    pos[:, :, 0] = X  # x座標
    pos[:, :, 1] = Y  # y座標
    Z = np.empty(X.shape)
    
    #ワイヤーフレームのz方向の値を計算
    z_shape = Z.shape
    for i in range(z_shape[0]):
        for j in range(z_shape[1]):
            Z[i][j] = get_z_value(X[i][j],Y[i][j],segment)
            
    #尤度を計算
    point_z = []
    for i in range(len(x)):
        point_z.append(get_z_value(x[i],y[i],segment))
        print("点(",x[i],",",y[i],")の尤度　",point_z[i])
    likelihood = 0
    for z_value in point_z:
        likelihood += z_value
    print("尤度の合計　",likelihood)
    
    fig = plt.figure()
    ax = Axes3D(fig)
    
    ax.plot_wireframe(X, Y, Z)
    ax.scatter(x, y,point_z,s = 300,c = "red")
    
    ax.set_xlabel(r'$x$')
    ax.set_ylabel(r'$y$')
    ax.set_zlabel(r'$z$')
    plt.savefig('wire_frame.png', dpi=144)
    plt.show()

if __name__ == "__main__":
    segment1 = [[1,1],[9,9]]
    segment2 = [[1,9],[9,1]]
    point_cloud_x = [4,6,8]
    point_cloud_y = [4,2,6]
    make_wire_frame(point_cloud_x,point_cloud_y,[segment1])
    make_wire_frame(point_cloud_x,point_cloud_y,[segment1,segment2])