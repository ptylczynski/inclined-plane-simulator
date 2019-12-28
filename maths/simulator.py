import math

from matplotlib import animation
from matplotlib.axis import Axis
from matplotlib.figure import Figure
from matplotlib.pyplot import subplots, figure, axes, show, plot, savefig, xlabel, ylabel

from math import cos, sin

from maths.functions import Plane, Angle, Acceleration, Friction, Gravity


class Simulator:
    def __init__(self, step: float, iterations: int, start_point: float,  end_point: float):
        self.step: float = step
        self.xPos: float = start_point
        self.start_x = start_point
        self.end_x: float = end_point
        self.iterations: int = iterations
        self.total_speed = 0
        self.fig: Figure = figure()
        self.axes: Axis = axes()
        self.lines = None
        self.title = None
        self.last_point = [0, 0]
        self.x_graph = list()
        self.friction_graph = list()
        self.gravity_graph = list()
        self.angle_graph = list()
        self.total_speed_graph = list()
        self.speed_diff_graph = list()
        self.acceleration_graph = list()
        self.plane: Plane = Plane('1')
        self.friction: Friction = Friction('1')
        self.gravity: Gravity = Gravity('1')
        self.angle: Angle = Angle(self.plane)
        self.acceleration: Acceleration = Acceleration(self.gravity, self.friction, self.angle)

    def simulate(self):
        anim = animation.FuncAnimation(self.fig, self.make_plot, init_func=self.init_plot,
                                       frames=self.iterations, interval=10, blit=False)

        anim.save("plot.mp4")

        self.fig, self.axes = subplots(1, 1)
        self.axes.set_title("Total Speed")
        ylabel("Speed")
        xlabel("Position")
        plot(self.x_graph, self.total_speed_graph)
        savefig("total_speed_graph.png")

        self.fig, self.axes = subplots(1, 1)
        self.axes.set_title("Friction coefficient")
        ylabel("Friction coeff")
        xlabel("Position")
        plot(self.x_graph, self.friction_graph)
        savefig("friction_graph.png")

        self.fig, self.axes = subplots(1, 1)
        self.axes.set_title("Gravity coefficient")
        ylabel("Gravity corff")
        xlabel("Position")
        plot(self.x_graph, self.gravity_graph)
        savefig("gravity_graph.png")

        self.fig, self.axes = subplots(1, 1)
        self.axes.set_title("Angle")
        ylabel("Angle (degrees)")
        xlabel("Position")
        plot(self.x_graph, self.angle_graph)
        savefig("angle_graph.png")

        self.fig, self.axes = subplots(1, 1)
        self.axes.set_title("Speed difference")
        ylabel("Speed diff")
        xlabel("Position")
        plot(self.x_graph, self.speed_diff_graph)
        savefig("speed_diff_graph.png")

        self.fig, self.axes = subplots(1, 1)
        self.axes.set_title("Net acceleration")
        ylabel("Net Acceleration")
        xlabel("Position")
        plot(self.x_graph, self.acceleration_graph)
        savefig("acceleration_graph.png")

    def init_plot(self):
        now = self.xPos
        iteration = 0
        slope = list()
        max_slope = -math.inf
        min_slope = math.inf

        while iteration < self.iterations and now < self.end_x:
            self.x_graph.append(now)
            slope.append(self.plane[now])
            self.friction_graph.append(self.friction[now])
            self.gravity_graph.append(self.gravity[now])
            self.angle_graph.append(self.angle[now] * 360 / (2 * 3.14))

            max_slope = max(self.plane[now], max_slope)
            min_slope = min(self.plane[now], min_slope)
            now += self.step
            iteration += 1

        self.axes = axes(
            xlim=(0.9 * self.start_x, 1.1 * min(now, self.end_x)),
            ylim=(0.9 * min_slope, 1.1 * max_slope)
        )
        self.lines = [plot([], [])[0], plot([], [], marker="X")[0]]

        self.last_point = [self.x_graph[0], slope[0]]
        self.lines[0].set_data(self.x_graph, slope)
        self.lines[1].set_data([], [])

        self.x_graph = list()

        return self.lines

    def make_plot(self, i):
        print("Iteration: {}/{}".format(
            i, self.iterations
        ))

        self.x_graph.append(self.xPos)

        acceleration = self.acceleration[self.xPos]
        self.acceleration_graph.append(acceleration)

        angle = self.angle[self.xPos]

        speed_diff = acceleration * self.step
        self.speed_diff_graph.append(speed_diff)

        self.total_speed += speed_diff
        # clamping speed
        self.total_speed = max(self.total_speed, 0) if angle > 0 else min(self.total_speed, 0)
        self.total_speed_graph.append(self.total_speed)

        distance_covered = self.total_speed * self.step

        print("Acceleration: {}\nSpeed: {}\nAngle: {}\nDistance in one move: {}"
              "\nGravity: {}\nFriction {}\nPosition (x,y) {}, {}\n"
              "dx: {}\ndy: {}\n\n\n".format(
                acceleration,
                self.total_speed,
                angle * 360 / (2 * 3.14),
                distance_covered,
                self.gravity,
                self.friction,
                self.last_point[0], self.last_point[1],
                distance_covered * cos(-angle),
                distance_covered * sin(-angle),
        ))

        self.last_point[0] += distance_covered * cos(-angle)
        self.last_point[1] += distance_covered * sin(-angle)

        self.xPos += distance_covered * cos(angle)
        self.axes.set_title("Frame: {}/{}".format(i, self.iterations))

        self.lines[1].set_data([self.last_point[0]], [self.last_point[1]])

        return self.lines, self.title

    def set_plane_expression(self, expression: str):
        self.plane.set_expression(expression)

    def set_friction_expression(self, expression: str):
        self.friction.set_expression(expression)

    def set_gravity_expression(self, expression: str):
        self.gravity.set_expression(expression)

    def color(self):
        colors = ["red", "blue", "green", "cyan", "magenta", "yellow", "black"]
        idx = 0
        while True:
            yield colors[idx]
            idx = idx + 1 if idx < len(colors) - 1 else 0


if __name__ == "__main__":
    s = Simulator(0.01, 3000, 90, 200)
    s.set_friction_expression('0.01')
    s.set_gravity_expression('10')
    s.set_plane_expression('-1/10000 * (t-100)**3')
    s.simulate()
