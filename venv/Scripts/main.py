import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
import control


class DCMotor:

    def __init__(self, voltage, resistance,
                 inductance, inertia,
                 friction, electromotive_force,
                 torque):
        self.V = voltage
        self.R = resistance
        self.L = inductance
        self.J = inertia  # moment of inertia of the rotor
        self.b = friction  # viscous friction constant
        self.Ke = electromotive_force  # electromotive force constant
        self.Km = torque  # motor torque constant

        numerator = [self.Ke]  # no load, so motor torque equals electromotive force
        denominator = [self.J*self.L, self.J*self.R+self.L*self.b, self.R*self.b + self.Ke*self.Ke]
        self.transfer_function = signal.TransferFunction(numerator, denominator)

    def plot_step_response(self):
        t, y = signal.step2(self.transfer_function)
        plt.plot(t, y)
        plt.show()

    def test_noise(self):
        sim_length = 1000

        sig_val = 1
        sig = []
        for s in range(sim_length):
            sig.append(sig_val)

        input_noise = np.random.normal(0, 0.05, sim_length)
        input_signal = sig + input_noise

        time = []
        for time_sample in range(sim_length):
            time.append(time_sample)

        t, y, x = signal.lsim(self.transfer_function, input_signal, time)
        output_noise = np.random.normal(0, 0.01, sim_length)

        plt.plot(t, y)
        output = y + output_noise
        #plt.plot(t, output)
        plt.show()


def __main__():
    print("Hello World!")
    motor = DCMotor(voltage=1, resistance=0.5, inductance=0.01, inertia=0.1,
                    friction=0.01, torque=0.01, electromotive_force=0.01)
    motor.test_noise()


if __name__ == "__main__":
    __main__()


