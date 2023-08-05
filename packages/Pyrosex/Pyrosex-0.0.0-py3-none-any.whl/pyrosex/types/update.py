import pyrosex


class Update:
    def stop_propagation(self):
        raise pyrosex.StopPropagation

    def continue_propagation(self):
        raise pyrosex.ContinuePropagation
