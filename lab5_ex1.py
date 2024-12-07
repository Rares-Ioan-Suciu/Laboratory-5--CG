import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

def graham_scan(points):
   
    def cross_product(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
    
  
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


def visualize_convex_hull(points, hull):
 
    x, y = zip(*points)
    hull_x, hull_y = zip(*(hull + [hull[0]]))  
    
    plt.figure(figsize=(8, 8))
    plt.scatter(x, y, label="Points")
    plt.plot(hull_x, hull_y, 'r-', label="Convex Hull")
    
 
    plt.scatter(hull_x, hull_y, color="red")
    
  
    plt.gca().add_patch(Polygon(hull, closed=True, fill=True, color='lightblue', alpha=0.3))
    
    plt.legend()
    plt.xlabel("X-coordinate")
    plt.ylabel("Y-coordinate")
    plt.title("Graham Scan - Convex Hull")
    plt.grid()
    plt.show()

if __name__ == "__main__":
   
    sample_points = [(30, 60), (15, 25), (0, 30), (70, 30), (50, 40), (50, 10), (20, 0), (55, 20)]
    
    
    convex_hull = graham_scan(sample_points)
    
    visualize_convex_hull(sample_points, convex_hull)
