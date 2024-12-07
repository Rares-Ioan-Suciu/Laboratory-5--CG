import matplotlib.pyplot as plt
from matplotlib.widgets import Button

# Input points
points = [(1, 10), (-2, 7), (3, 8), (4, 10), (5, 7), (6, 7), (7, 11)]

# Sort points lexicographically
points = sorted(points)

# Algorithm state variables
hull = []  # Current state of the hull
steps = []  # Steps for visualization (stores hull state)

# Helper function to check if three points make a clockwise turn
def is_clockwise(p1, p2, p3):
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0]) <= 0

# Build the lower hull
for p in points:
    while len(hull) >= 2 and is_clockwise(hull[-2], hull[-1], p):
        hull.pop()
        steps.append(hull[:])  # Record the state of the hull
    hull.append(p)
    steps.append(hull[:])  # Record the state of the hull

# Save the lower hull
lower_hull = hull[:]

# Build the upper hull
for p in reversed(points):
    while len(hull) > len(lower_hull) and is_clockwise(hull[-2], hull[-1], p):
        hull.pop()
        steps.append(hull[:])  # Record the state of the hull
    hull.append(p)
    steps.append(hull[:])  # Record the state of the hull

# Remove the duplicate endpoints
hull = hull[:-1]

# Visualization setup
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.2)
ax.set_xlim(min(p[0] for p in points) - 1, max(p[0] for p in points) + 1)
ax.set_ylim(min(p[1] for p in points) - 1, max(p[1] for p in points) + 1)
ax.set_title("Convex Hull - Step by Step")
scatter = ax.scatter(*zip(*points), label="Points")  # Initial scatterplot
hull_line, = ax.plot([], [], 'r-', label="Hull")  # Line showing the hull
legend = ax.legend()
step_idx = 0

# Function to update the plot for each step
def update_plot():
    global step_idx
    ax.clear()
    ax.scatter(*zip(*points), label="Points")
    ax.set_xlim(min(p[0] for p in points) - 1, max(p[0] for p in points) + 1)
    ax.set_ylim(min(p[1] for p in points) - 1, max(p[1] for p in points) + 1)
    ax.set_title("Convex Hull - Step by Step")
    
    # Draw the current state of the hull
    if step_idx < len(steps):
        current_hull = steps[step_idx]
        ax.plot([p[0] for p in current_hull], [p[1] for p in current_hull], 'r-', label="Hull")
    legend = ax.legend()

# Button to step through the algorithm
def next_step(event):
    global step_idx
    if step_idx < len(steps):
        step_idx += 1
        update_plot()
        fig.canvas.draw()

# Button setup
ax_button = plt.axes([0.4, 0.05, 0.2, 0.075])
button = Button(ax_button, 'Next Step')
button.on_clicked(next_step)

update_plot()  # Initialize the plot
plt.show()
