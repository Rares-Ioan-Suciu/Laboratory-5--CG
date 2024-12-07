import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import numpy as np

def cross_product(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])


def graham_scan(points):
   
    points = sorted(points)
    

    upper = []
    for p in points:
        while len(upper) >= 2 and cross_product(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    
    
    lower = []
    for p in reversed(points):
        while len(lower) >= 2 and cross_product(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    
  
    return upper[:-1] + lower[:-1]


def points_on_hull(points, hull):
    hull_set = set(hull)
    return sum(1 for p in points if p in hull_set)

def visualize(points, hull, lambda_value):
    x, y = zip(*points)
    hull_x, hull_y = zip(*(hull + [hull[0]])) 
    
    plt.figure(figsize=(8, 8))
    plt.scatter(x, y, label="Points")
    plt.plot(hull_x, hull_y, 'r-', label="Convex Hull")
    
    
    for point in hull:
        plt.scatter(*point, color="red")
        plt.text(point[0] + 0.1, point[1] + 0.1, f"{point}", fontsize=9)
    
    plt.title(f"Convex Hull (λ = {lambda_value})")
    plt.legend()
    plt.grid()
    plt.show()


def main(lambda_value):
    
    A = (3, -3)
    B = (3, 3)
    C = (-3, -3)
    D = (-3, 3)
    
    M = (-2 + lambda_value, 3 - lambda_value)
    
  
    points = [A, B, C, D, M]
    
  
    hull = graham_scan(points)
    

    count_on_hull = points_on_hull(points, hull)
    

    print(f"Points on the convex hull: {count_on_hull}")
    print(f"Convex hull vertices: {hull}")
    #visualize(points, hull, lambda_value)


if __name__ == "__main__":
     for lambda_value in np.arange(-3, 10, 0.2):  
        print(f"lambd: {lambda_value}\n")
        main(lambda_value)
