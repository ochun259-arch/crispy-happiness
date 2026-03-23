import numpy as np
import math
from math import radians, sin, cos, sqrt, asin


# 1. 欧式距离
def euclidean_distance(x, y):
    """欧式距离：两点之间的直线距离"""
    return np.sqrt(np.sum((np.array(x) - np.array(y)) ** 2))


# 2. 曼哈顿距离
def manhattan_distance(x, y):
    """曼哈顿距离：坐标差的绝对值之和"""
    return np.sum(np.abs(np.array(x) - np.array(y)))


# 3. 切比雪夫距离
def chebyshev_distance(x, y):
    """切比雪夫距离：坐标差的最大值（国际象棋中的国王移动距离）"""
    return np.max(np.abs(np.array(x) - np.array(y)))


# 4. 余弦相似度
def cosine_similarity(x, y):
    """
    余弦相似度：向量夹角的余弦值
    返回范围 [-1, 1]，值越大表示越相似
    """
    x = np.array(x)
    y = np.array(y)
    dot_product = np.dot(x, y)
    norm_x = np.linalg.norm(x)
    norm_y = np.linalg.norm(y)
    if norm_x == 0 or norm_y == 0:
        return 0
    return dot_product / (norm_x * norm_y)


# 5. 汉明距离
def hamming_distance(x, y):
    """汉明距离：两个等长字符串对应位置不同字符的个数"""
    if len(x) != len(y):
        raise ValueError("两个序列长度必须相等")
    return sum(1 for i, j in zip(x, y) if i != j)


# 6. 闵可夫斯基距离
def minkowski_distance(x, y, p):
    """
    闵可夫斯基距离：欧式距离和曼哈顿距离的推广
    p = 1 时为曼哈顿距离
    p = 2 时为欧式距离
    p = ∞ 时为切比雪夫距离
    """
    if p == float('inf'):
        return chebyshev_distance(x, y)
    return np.sum(np.abs(np.array(x) - np.array(y)) ** p) ** (1 / p)


# 7. Jaccard指数
def jaccard_index(set1, set2):
    """
    Jaccard指数（杰卡德相似系数）：两个集合交集与并集的比例
    返回范围 [0, 1]，值越大表示越相似
    """
    set1 = set(set1)
    set2 = set(set2)
    intersection = len(set1 & set2)
    union = len(set1 | set2)
    if union == 0:
        return 0
    return intersection / union


def jaccard_distance(set1, set2):
    """Jaccard距离：1 - Jaccard指数，值越小表示越相似"""
    return 1 - jaccard_index(set1, set2)


# 8. 半正矢距离（球面距离）
def haversine_distance(point1, point2, radius=6371):
    """
    半正矢距离：球面上两点之间的最短距离（大圆距离）

    参数:
        point1, point2: (纬度, 经度) 元组，单位为度
        radius: 球体半径，默认地球平均半径 6371 公里
    返回:
        距离，单位与半径相同
    """
    lat1, lon1 = point1
    lat2, lon2 = point2

    # 转换为弧度
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

    # 半正矢公式
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))

    return radius * c


# ==================== 使用示例 ====================
if __name__ == "__main__":
    # 示例数据
    a = [0, 0]
    b = [3, 4]

    print("=== 距离/相似度计算示例 ===\n")
    print(f"点 A: {a}, 点 B: {b}")
    print(f"1. 欧式距离: {euclidean_distance(a, b):.4f}")
    print(f"2. 曼哈顿距离: {manhattan_distance(a, b)}")
    print(f"3. 切比雪夫距离: {chebyshev_distance(a, b)}")

    # 向量
    v1 = [1, 2, 3]
    v2 = [4, 5, 6]
    print(f"\n向量 V1: {v1}, 向量 V2: {v2}")
    print(f"4. 余弦相似度: {cosine_similarity(v1, v2):.4f}")

    # 字符串/序列
    s1 = "101010"
    s2 = "111000"
    print(f"\n字符串 S1: {s1}, S2: {s2}")
    print(f"5. 汉明距离: {hamming_distance(s1, s2)}")

    # 闵可夫斯基距离
    print(f"\n6. 闵可夫斯基距离:")
    print(f"   p=1 (曼哈顿): {minkowski_distance(a, b, 1)}")
    print(f"   p=2 (欧式): {minkowski_distance(a, b, 2):.4f}")
    print(f"   p=inf (切比雪夫): {minkowski_distance(a, b, float('inf'))}")

    # Jaccard
    set_a = {1, 2, 3, 4}
    set_b = {3, 4, 5, 6}
    print(f"\n集合 Set A: {set_a}, Set B: {set_b}")
    print(f"7. Jaccard 指数: {jaccard_index(set_a, set_b):.4f}")
    print(f"   Jaccard 距离: {jaccard_distance(set_a, set_b):.4f}")

    # 半正矢距离（地球表面）
    beijing = (39.9042, 116.4074)  # 北京
    shanghai = (31.2304, 121.4737)  # 上海
    distance_km = haversine_distance(beijing, shanghai)
    print(f"\n8. 半正矢距离（北京-上海）: {distance_km:.2f} 公里")