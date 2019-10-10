import unittest
import logger

class TestLoggerMethods(unittest.TestCase):

     def setUp(self):
         self.log = logger.Logger('test.txt')

     # def tearDown(self):
     #     pass
     #
     def test__write_metadata(self):
         write_metadata = self.log.write_metadata(100, 0.50, "Chicken Pox", 0.10, 0.20)
         file  = open('test.txt', 'r')
         # contents =file.read()
         for line in file:
             self.assertEqual(line, "Input data for the simulation: \n")
             self.assertEqual(line, "\n")
             self.assertEqual(line, "       Population size = 100 \n")
             self.assertEqual(line, "       percent vaccinated = 0.50 \n")
             self.assertEqual(line, "       virus name: Chicken Pox \n")
             self.assertEqual(line, "       mortality_rate = 0.10 \n")
             self.assertEqual(line, "       reproductive rate = 0.20 \n")



     # def test_simulation_should_continue(self):
     #     # for i in range(100):
     #     simulation_should_continue = self. sim._simulation_should_continue()
     #     self.assertTrue(simulation_should_continue)
     #     self. sim.vaccinated = 50
     #     self. sim.total_dead = 40
     #     if self.sim.vaccinated + self.sim.total_dead >= self.sim.pop_size:
     #         self.assertFalse(simulation_should_continue)
     #         # assert simulation_should_continue == False
     #     elif self. sim.vaccinated + self. sim.total_dead < self. sim.pop_size:
     #         self.assertTrue(simulation_should_continue)
     #         # assert simulation_should_continue == True
     # def test_run(self):
     #     pass
     #
     #
     # def test_random_person(self):
     #     for _ in range(100):
     #         self.assertIsNotNone(self.sim._random_person(5))

if __name__ == '__main__':
     unittest.main()
