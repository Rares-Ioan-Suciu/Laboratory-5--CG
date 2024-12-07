import matplotlib.pyplot as plt
from matplotlib.widgets import Button


# Function to compute orientation
def orientation(p, q, r):
    """
    Compute the orientation of the triplet (p, q, r).
    Returns:
        > 0 if counterclockwise
        < 0 if clockwise
        == 0 if collinear
    """
    return (q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0])


# Visualization
class StepByStepVisualizer:
    def __init__(self, points):
        self.points = points
        self.hull = []
        self.step = 0
        self.is_complete = False
        self.p = None  # Current point on the hull
        self.fig, self.ax = plt.subplots(figsize=(8, 8))
        self.ax.set_title("Jarvis March Visualization (Step-by-Step)")
        self.ax.grid(True)
        self.update_plot()
        self.button_ax = self.fig.add_axes([0.7, 0.05, 0.2, 0.075])
        self.button = Button(self.button_ax, 'Next Step')
        self.button.on_clicked(self.next_step)

    def update_plot(self):
        self.ax.clear()
        self.ax.set_title("Jarvis March Visualization (Step-by-Step)")
        self.ax.grid(True)

        # Plot all points
        x, y = zip(*self.points)
        self.ax.scatter(x, y, label="Points", color="blue")

        # Plot the convex hull so far
        if self.step > 0:
            for i in range(len(self.hull) - 1):
                self.ax.plot(
                    [self.hull[i][0], self.hull[i + 1][0]],
                    [self.hull[i][1], self.hull[i + 1][1]],
                    color="red",
                    label="Convex Hull" if i == 0 else None,
                )
            # Close the hull if complete
            if self.is_complete:
                self.ax.plot(
                    [self.hull[-1][0], self.hull[0][0]],
                    [self.hull[-1][1], self.hull[0][1]],
                    color="red",
                )

        # Highlight points on the hull
        for i, point in enumerate(self.hull):
            self.ax.scatter(*point, color="red")
            self.ax.text(point[0] + 0.1, point[1] + 0.1, f"P{i + 1}", fontsize=10, color="red")

        self.ax.legend()
        plt.draw()

    def next_step(self, event):
        if self.is_complete:
            return  # Stop further processing if the hull is complete

        if self.step == 0:
            # Start the algorithm
            leftmost = min(self.points, key=lambda p: p[0])
            self.hull.append(leftmost)
            self.p = leftmost
        else:
            q = self.points[0]  # Initial assumption for the next point in the hull
            for r in self.points:
                if r == self.p:  # Skip the same point
                    continue
                # Choose the most counterclockwise point
                if orientation(self.p, q, r) > 0 or (orientation(self.p, q, r) == 0 and r != q):
                    q = r
            self.p = q  # Move to the next point
            if self.p == self.hull[0]:
                # Hull is complete
                self.is_complete = True
            else:
                self.hull.append(q)

        self.step += 1
        self.update_plot()

    def show(self):
        plt.show()


# Main Function to initialize the visualization
def main():
    points = [(2, -1), (1, 3), (4, 0), (4, 3), (5, 2)]  # Input points
    visualizer = StepByStepVisualizer(points)
    visualizer.show()


if __name__ == "__main__":
    main()
