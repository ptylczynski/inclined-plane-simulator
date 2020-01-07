from maths.simulator import Simulator


def main():
    step: int = 0.01
    iterations: int = 3000
    start: int = 90
    end: int = 200
    save_place: str = "plots/"

    s = Simulator(
        step=step,
        iterations=iterations,
        start_point=start,
        end_point=end,
        save_palace=save_place)
    s.set_friction_expression("0.01")
    s.set_gravity_expression("10")
    s.set_plane_expression('-1/10000 * (t-100)**3')
    s.simulate()




if __name__ == "__main__":
    main()
