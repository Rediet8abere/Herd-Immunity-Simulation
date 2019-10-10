import unittest
import simulation

class TestSimulationMethods(unittest.TestCase):

    # def test_simulation_instance(self):
    #     virus = simulation.Virus('Ebola', 0.25, 0.70)
    #     sim = simulation.Simulation(100000, 0.90, virus, 10)
    #     # assertIsInstance(a, b)
    # # assert sim
    def setUp(self):
        self.virus = simulation.Virus('Ebola', 0.25, 0.70)
        self.sim = simulation.Simulation(100000, 0.90, self.virus, 10)

    def tearDown(self):
        pass

    def test__create_population(self):
        create_population = self. sim._create_population(10)
        for index in range(len(create_population)):
            if index < 10:
                person = create_population[index]
                self.assertEqual(person._id, index)
                self.assertTrue(person.is_alive)
                self.assertFalse(person.is_vaccinated)
                self.assertIsNotNone(person.infection)
            elif 10 <= index <= (10008):
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
        # for i in range(100):
        simulation_should_continue = self. sim._simulation_should_continue()
        self.assertTrue(simulation_should_continue)
        self. sim.vaccinated = 50
        self. sim.total_dead = 40
        if self.sim.vaccinated + self.sim.total_dead >= self.sim.pop_size:
            self.assertFalse(simulation_should_continue)
            # assert simulation_should_continue == False
        elif self. sim.vaccinated + self. sim.total_dead < self. sim.pop_size:
            self.assertTrue(simulation_should_continue)
            # assert simulation_should_continue == True
    def test_run(self):
        pass


    def test_random_person(self):
        for _ in range(100):
            self.assertIsNotNone(self.sim._random_person(5))

if __name__ == '__main__':
    unittest.main()
