class MonkeyBanana:
    def __init__(self):
        self.monkey_pos = 'A'
        self.box_pos = 'B'
        self.monkey_on_box = False
        self.has_banana = False

    def show_state(self):
        print(f"Monkey at: {self.monkey_pos}, Box at: {self.box_pos}, "
              f"On box: {self.monkey_on_box}, Has banana: {self.has_banana}")

    def go(self, place):
        print(f"🐒 Monkey walks from {self.monkey_pos} to {place}")
        self.monkey_pos = place

    def push_box(self, place):
        if self.monkey_pos == self.box_pos:
            print(f"🐒 Monkey pushes box from {self.box_pos} to {place}")
            self.box_pos = place
            self.monkey_pos = place
        else:
            print("❌ Monkey must be at the box to push it!")

    def climb_up(self):
        if self.monkey_pos == self.box_pos:
            print("🐒 Monkey climbs onto the box.")
            self.monkey_on_box = True
        else:
            print("❌ Monkey must be at the box to climb!")

    def grab_banana(self):
        if self.monkey_on_box and self.monkey_pos == 'C':
            print("🍌 Monkey grabs the banana! Success!")
            self.has_banana = True
        else:
            print("❌ Monkey can’t reach the banana yet!")

# Run the simulation
problem = MonkeyBanana()
print("🔹 Initial State:")
problem.show_state()
print()

problem.go('B')
problem.push_box('C')
problem.climb_up()
problem.grab_banana()

print("\n🔹 Final State:")
problem.show_state()
