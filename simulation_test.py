import unittest
import simulation
import person
import virus

class TestSimulationMethods(unittest.TestCase):

    def setUp(self):
        self.virus = simulation.Virus('Ebola', 0.25, 0.70)
        self.sim = simulation.Simulation(100, 0.90, self.virus, 10)
        self.dysentery = virus.Virus("Dysentery", 0.7, 0.2)
        self.person = person.Person(2, True, self.dysentery)
        self.random_person_1 = person.Person(2, True)
        self.random_person_2 = person.Person(2, False)
        self.random_person_3 = person.Person(2, False, self.dysentery)

    def test__create_population(self):
        create_population = self. sim._create_population(10)
        for index in range(len(create_population)):
            if index < 10:
                person = create_population[index]
                self.assertEqual(person._id, index)
                self.assertTrue(person.is_alive)
                self.assertFalse(person.is_vaccinated)
                self.assertIsNotNone(person.infection)
            elif 10 <= index < (19):
                person = create_population[index]
                self.assertEqual(person._id, index)
                self.assertTrue(person.is_alive)
                self.assertFalse(person.is_vaccinated)
                self.assertIsNone(person.infection)
            else:
                person = create_population[index]
                self.assertEqual(person._id, index)
                self.assertTrue(person.is_alive)
                self.assertTrue(person.is_vaccinated)
                self.assertIsNone(person.infection)

    def test_simulation_should_continue(self):

        self.sim.vaccinated = 7
        self.sim.total_dead = 9
        self.sim.total_dead = 0
        if self.sim.vaccinated + self.sim.total_dead >= self.sim.pop_size:
            print("simulation should end")
            self.assertFalse(self.sim._simulation_should_continue())
        elif self.sim.total_dead == 0:
            print("all dead")
            self.assertFalse(self.sim._simulation_should_continue())
        elif self. sim.vaccinated + self. sim.total_dead < self. sim.pop_size:
            print("simulation should continue")
            self.assertTrue(self.sim._simulation_should_continue())


        self.sim.vaccinated = 7
        self.sim.total_dead = 94
        if self.sim.vaccinated + self.sim.total_dead >= self.sim.pop_size:
            self.assertFalse(self.sim._simulation_should_continue())
        elif self.sim.vaccinated + self. sim.total_dead < self. sim.pop_size:
            self.assertTrue(self.sim._simulation_should_continue())

    def test_time_step(self):
        self.sim.time_step()
        self.assertTrue(self.sim.vaccinated > 10 and self.sim.total_dead > 0)

    def test_random_person(self):
        for _ in range(100):
            self.assertIsNotNone(self.sim._random_person(5))

    def test_interaction(self):
        if self.random_person_1:
            self.sim.interaction(self.person, self.random_person_1)
            self.assertFalse(self.sim.total_infected > 10)
        if self.random_person_2:
            self.sim.interaction(self.person, self.random_person_2)
            self.assertTrue(self.sim.total_infected > 10)
        if self.random_person_3:
            self.sim.interaction(self.person, self.random_person_3)
            self.assertTrue( self.sim.already_infected > 0)

    def test_infect_newly_infected(self):
        self.sim._infect_newly_infected()
        self.assertTrue(self.sim.newly_infected == [])




if __name__ == '__main__':
    unittest.main()
