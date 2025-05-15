import shapely
from shapely.geometry import Polygon


def bbox_iou_eval(box1, box2):
    poly1 = Polygon(box1).convex_hull  # 将第一个多边形的点集转换为凸多边形
    poly2 = Polygon(box2).convex_hull  # 将第二个多边形的点集转换为凸多边形

    if not poly1.intersects(poly2):  # 如果两个多边形不相交
        iou = 0
    else:
        try:
            inter_area = poly1.intersection(poly2).area  # 计算相交面积
            iou = float(inter_area) / (poly1.area + poly2.area - inter_area)  # 计算 iou
        except shapely.geos.TopologicalError:
            print('shapely.geos.TopologicalError occurred, iou set to 0')
            iou = 0
    return iou


# 示例用法
box3 = [(525.4407289884148, 61.4921828082869), (685.3858404806961, 60.49252007641505),
        (691.3837821616567, 218.43923171216548), (523.4414150947613, 218.43923171216548)]  # 第一个多边形的点坐标列表
box4 = [(520.0715275399681, 217.67655605168207), (693.7619220511173, 218.92613446652183),
        (688.7636373169836, 128.9564885980564), (523.8202410905684, 137.703537501935)]  # 第二个多边形的点坐标列表

iou = bbox_iou_eval(box3, box4)
print(iou)


def calculate_polygon_iou(polygon1, polygon2):
    poly1 = Polygon(polygon1)
    poly2 = Polygon(polygon2)

    if not poly1.intersects(poly2):
        iou = 0
    else:
        intersection = poly1.intersection(poly2).area
        union = poly1.union(poly2).area
        iou = intersection / union

    return iou


# 示例用法
polygon1 = [(525.4407289884148, 61.4921828082869), (685.3858404806961, 60.49252007641505),
            (691.3837821616567, 218.43923171216548), (523.4414150947613, 218.43923171216548)]
polygon2 = [(524.4410720415881, 135.46722496680292), (523.4414150947613, 353.39370051486367),
            (699.3810377362707, 352.39403778299186), (688.3848113211764, 134.4675622349311)]

print(calculate_polygon_iou(polygon1, polygon2))

if __name__ == '__main__':
    bbox_iou_eval(box3, box4)
    calculate_polygon_iou(polygon1, polygon2)
