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

    # big_stick = superheroes.Weapon("Overwhelming Stick", 200)
    # test_runs = 100
    # for _ in range(0, test_runs):
    #     attack = big_stick.attack()
    #     assert attack <= 200 and attack >= 100


    virus = simulation.Virus('Ebola', 0.25, 0.70)
    person = simulation.Person(1999, False, virus)
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
            
