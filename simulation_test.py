import pytest
import random
import simulation

def test_simulation_instance():
    # Test instantiation without error
    #python3 simulation.py Ebola 0.25 0.70 100000 0.90 10
    virus = simulation.Virus('Ebola', 0.25, 0.70)
    sim = simulation.Simulation(100000, 0.90, virus, 10)
    assert sim
def test__create_population():

    virus = simulation.Virus('Ebola', 0.25, 0.70)
    person = simulation.Person(1999, False, self.virus)
    sim = simulation.Simulation(100000, 0.90, virus, 10)
    assert person._id
