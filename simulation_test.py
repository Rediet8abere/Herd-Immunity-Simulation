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
    sim = simulation.Simulation(100000, 0.90, virus, 10)
    create_population = sim._create_population(10)
    for index in range(len(create_population)):
        if index < 10:
            person = create_population[index]
            assert person._id == index
            assert person.is_alive == True
            assert person.is_vaccinated == False
            assert person.infection == virus
        elif 10 <= index <= (10008):
            person = create_population[index]
            assert person._id == index
            assert person.is_alive == True
            assert person.is_vaccinated == False
            assert person.infection == None
        else:
            person = create_population[index]
            assert person._id == index
            assert person.is_alive == True
            assert person.is_vaccinated == True
            assert person.infection == None

def test_simulation_should_continue():
    virus = simulation.Virus('Ebola', 0.25, 0.70)
    sim = simulation.Simulation(100, 0.90, virus, 10)
    for i in range(100):
        simulation_should_continue = sim._simulation_should_continue()
        assert simulation_should_continue == True
    # person_list = []
    # for num in range(100):
    #     if num < 10:
    #         person = Person(num, False, self.virus)
    #         person_list.append(person)
    #     elif 10 <= num <= (20):
    #         person = Person(num, False)
    #         person_list.append(person)
    #     else:
    #         person = Person(num, True)
    #         person_list.append(person)
