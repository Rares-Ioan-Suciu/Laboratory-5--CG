import math
import matplotlib.pyplot as plt
from matplotlib.widgets import Button

def sort_points_angularly(points):
    """Sort points angularly around their centroid."""
    centroid_x = sum(p[0] for p in points) / len(points)
    centroid_y = sum(p[1] for p in points) / len(points)
    centroid = (centroid_x, centroid_y)

    def angle_with_centroid(point):
        return math.atan2(point[1] - centroid_y, point[0] - centroid_x)

    sorted_points = sorted(points, key=angle_with_centroid)
    return sorted_points, centroid


# Points to be sorted
points = [(4, 2), (7, -1), (3, -5), (-3, 6), (-4, 4), (-1, -1), (-2, -6)]

# Sort the points and get the centroid
sorted_points, centroid = sort_points_angularly(points)

# Set up the plot
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.2)  # Adjust space for the button

# Initial empty plot
scat = ax.scatter(*zip(*points), color="blue", label="Original Points")
centroid_scat = ax.scatter(*centroid, color="red", label="Centroid", zorder=5)
polygon_line, = ax.plot([], [], color="green", label="Polygon", linestyle='--')
ax.legend()
ax.set_title("Polygon Construction (Step-by-Step)")
ax.grid()

# Keep track of current step
current_step = [0]  # Mutable so it updates with button callback


def update_polygon(event):
    """Update the polygon construction step-by-step."""
    step = current_step[0]
    if step < len(sorted_points):
        # Get the current step of the polygon
        polygon_line.set_data(
            *zip(*sorted_points[: step + 1], sorted_points[0])  # Close the loop
        )
        current_step[0] += 1
        fig.canvas.draw()


# Add button for "Next Step"
ax_button = plt.axes([0.4, 0.05, 0.2, 0.075])  # Position: [left, bottom, width, height]
button = Button(ax_button, "Next Step")
button.on_clicked(update_polygon)

# Show the plot
plt.show()
