import random, sys
random.seed(42)
from person import Person
from logger import Logger
from virus import Virus



class Simulation(object):
    ''' Main class that will run the herd immunity simulation program.
    Expects initialization parameters passed as command line arguments when file is run.

    Simulates the spread of a virus through a given population.  The percentage of the
    population that are vaccinated, the size of the population, and the amount of initially
    infected people in a population are all variables that can be set when the program is run.
    '''
    def __init__(self, pop_size, vacc_percentage, virus, initial_infected=1):
        ''' Logger object logger records all events during the simulation.
        Population represents all Persons in the population.
        The next_person_id is the next available id for all created Persons,
        and should have a unique _id value.
        The vaccination percentage represents the total percentage of population
        vaccinated at the start of the simulation.
        You will need to keep track of the number of people currently infected with the disease.
        The total infected people is the running total that have been infected since the
        simulation began, including the currently infected people who died.
        You will also need to keep track of the number of people that have die as a result
        of the infection.

        All arguments will be passed as command-line arguments when the file is run.
        HINT: Look in the if __name__ == "__main__" function at the bottom.
        '''
        self.pop_size = pop_size # Int
        self.next_person_id = 0 # Int

        self.virus = virus # Virus object
        self.initial_infected = initial_infected # Int
        self.total_infected = initial_infected # Int
        self.current_infected = 0 # Int

        self.vacc_percentage = vacc_percentage # float between 0 and 1
        self.total_dead = 0 # Int

        self.file_name = f"{self.virus.name}_simulation_pop_{self.pop_size}_vp_{self.vacc_percentage}_infected_{self.initial_infected}.txt"
        self.newly_infected = []
        self.logger = Logger(self.file_name)
        self.population = self._create_population(self.initial_infected) # List of Person objects
        self.vaccinated = round((self.pop_size - self.initial_infected) * self.vacc_percentage)
        self.saved = 0
        self.already_infected = 0



    def _create_population(self, initial_infected):
        '''This method will create the initial population.
            Args:
                initial_infected (int): The number of infected people that the simulation
                will begin with.

            Returns:
                list: A list of Person objects.

        '''
        self.vaccinated  = round((self.pop_size - initial_infected) * self.vacc_percentage)
        unvaccinated = round((self.pop_size - initial_infected) - self.vaccinated)
        person_list = []
        for num in range(self.pop_size):
            if num < initial_infected:
                self.next_person_id += 1
                person = Person(num, False, infection=self.virus)
                person_list.append(person)
            elif initial_infected <= num < (unvaccinated + initial_infected):
                self.next_person_id += 1
                person = Person(num, False)
                person_list.append(person)
            else:
                self.next_person_id += 1
                person = Person(num, True)
                person_list.append(person)
        return person_list

    def _simulation_should_continue(self):
        ''' The simulation should only end if the entire population is dead
        or everyone is vaccinated.

            Returns:
                bool: True for simulation should continue, False if it should end.
        '''
        if self.vaccinated + self.total_dead >= self.pop_size:
            print(self.current_infected)
            self.logger.write_currentinfect_and_dead(self.total_dead, self.pop_size, self.saved, self.current_infected)
            return False
        return True

    def run(self):
        ''' This method should run the simulation until all requirements for ending
        the simulation are met.
        '''
        time_step_counter = 0
        while self._simulation_should_continue():
            self.time_step()
            time_step_counter += 1
            self.logger.log_time_step(time_step_counter)

    def time_step(self):
        ''' This method should contain all the logic for computing one time step
        in the simulation.

        This includes:
            1. 100 total interactions with a randon person for each infected person
                in the population
            2. If the person is dead, grab another random person from the population.
                Since we don't interact with dead people, this does not count as an interaction.
            3. Otherwise call simulation.interaction(person, random_person) and
                increment interaction counter by 1.
            '''
        self.logger.write_metadata(self.pop_size, self.vacc_percentage, self.virus.name, self.virus.mortality_rate, self.virus.repro_rate)
        for person in self.population:
            if person.infection and person.is_alive:
                for num in range(100):
                    random_person = self._random_person(person._id)
                    self.interaction(person, random_person)
                survive = person.did_survive_infection()
                self.logger.log_infection_survival(person, survive)
                if not survive:
                    self.total_dead += 1
                else:
                    self.vaccinated += 1
                print(self.current_infected)
                self.current_infected -= 1
                print(self.current_infected)
        self._infect_newly_infected()

    def _random_person(self, person_id):
        ''' This method should return a random person from population
            to interact with an infected person.
        '''
        while True:
            random_person = random.choice(self.population)
            survive = random_person.is_alive and random_person._id != person_id
            if survive:
                return random_person

    def interaction(self, person, random_person):
        '''This method should be called any time two living people are selected for an
        interaction. It assumes that only living people are passed in as parameters.

        Args:
            person1 (person): The initial infected person
            random_person (person): The person that person1 interacts with.
        '''
        assert person.is_alive == True
        assert random_person.is_alive == True
        if random_person.is_vaccinated:
            self.logger.log_interaction(person, random_person, random_person_vacc=True)
            self.saved += 1
        elif random_person.infection:
            self.logger.log_interaction(person, random_person, random_person_sick=True)
            self.already_infected += 1
        elif random_person.infection is None and not random_person.is_vaccinated:
            rand_num = random.random()
            if rand_num  <= person.infection.repro_rate:
                self.newly_infected.append(random_person._id)
                self.current_infected += 1
                self.total_infected += 1
                self.logger.log_interaction(person, random_person, did_infect=True)

    def _infect_newly_infected(self):
        ''' This method should iterate through the list of ._id stored in self.newly_infected
        and update each Person object with the disease. '''
        for id in self.newly_infected:
            self.population[id].infection = self.virus
        self.newly_infected = []

if __name__ == "__main__":
    params = sys.argv[1:]
    virus_name = str(params[0])
    repro_num = float(params[1])
    mortality_rate = float(params[2])

    pop_size = int(params[3])
    vacc_percentage = float(params[4])

    if len(params) == 6:
        initial_infected = int(params[5])
    else:
        initial_infected = 1

    virus = Virus(virus_name, repro_num, mortality_rate)
    sim = Simulation(pop_size, vacc_percentage, virus, initial_infected)
    sim.run()
    #python3 simulation.py Ebola 0.25 0.70 100000 0.90 10
