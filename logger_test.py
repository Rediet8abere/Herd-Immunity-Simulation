import unittest
import logger
import person
import virus

class TestLoggerMethods(unittest.TestCase):

     def setUp(self):
         self.log = logger.Logger('test.txt')
         self.dysentery = virus.Virus("Dysentery", 0.7, 0.2)
         self.person = person.Person(4, True, self.dysentery)
         self.random_person_1 = person.Person(2, True, self.dysentery)
         self.random_person_2 = person.Person(2, True)
         self.random_person_3 = person.Person(2, False)
         self.current_infected = 2
         self.total_dead = 5
         self.pop_size = 20
         self.saved = 15
         self.total_infected = 3
         self.total_percentage = str(round((self.total_dead/self.pop_size)*100))

     def test_write_metadata(self):
         self.log.write_metadata(100000, 0.90, 'Ebola', 0.70, 0.25)

         with open('test.txt') as f:
             content = f.read().split("\n")
             # print(content)
             self.assertEqual(content[0], 'Input data for the simulation: ')
             self.assertEqual(content[1], '')
             self.assertEqual(content[2], '       Population size = 100000 ')
             self.assertEqual(content[3], '       percent vaccinated = 0.9 ')
             self.assertEqual(content[4], '       virus name: Ebola ')
             self.assertEqual(content[5], '       mortality_rate = 0.7 ')
             self.assertEqual(content[6], '       reproductive rate = 0.25 ')

     # log_infection_survival called before log_interaction
     def test_log_infection_survival(self):
         self.log.log_infection_survival(self.person, True)
         with open('test.txt') as f:
             content = f.read().split("\n")
             # print("In log infection survival: ", content)
             self.assertEqual(content[7], '4 died from infection')

     def test_log_interaction(self):

         self.log.log_interaction(self.person, self.random_person_1, random_person_sick=True)
         with open('test.txt') as f:
             content = f.read().split("\n")
             # print("In log interaction already sick: ", content)
             self.assertEqual(content[8], '4 did not infect 2 because already sick ')

         self.log.log_interaction(self.person, self.random_person_2, random_person_vacc=True)
         with open('test.txt') as f:
             content = f.read().split("\n")
             # print("In log interaction vaccinated: ", content)
             self.assertEqual(content[9], '4 did not infect 2 because vaccinated ')

         self.log.log_interaction(self.person, self.random_person_3, did_infect=True)
         with open('test.txt') as f:
            content = f.read().split("\n")
            # print("In log interaction infect: ", content)
            self.assertEqual(content[10], '4 infects 2 ')




if __name__ == '__main__':
     unittest.main()
