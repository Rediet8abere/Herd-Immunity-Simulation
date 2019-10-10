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
        # TODO: Create a Logger object and bind it to self.logger.
        # Remember to call the appropriate logger method in the corresponding parts of the simulation.
        # TODO: Call self._create_population() and pass in the correct parameters.
        # Store the array that this method will return in the self.population attribute.
        # TODO: Store each newly infected person's ID in newly_infected attribute.
        # At the end of each time step, call self._infect_newly_infected()
        # and then reset .newly_infected back to an empty list.

        self.pop_size = pop_size # Int
        # The next_person_id is the next available id for all created Persons, and should have a unique _id value.
        self.next_person_id = 0 # Int

        self.virus = virus # Virus object
        self.initial_infected = initial_infected # Int
        self.total_infected = 0 # Int
        self.current_infected = initial_infected # Int

        self.vacc_percentage = vacc_percentage # float between 0 and 1
        self.total_dead = 0 # Int

        self.file_name = f"{self.virus.name}_simulation_pop_{self.pop_size}_vp_{self.vacc_percentage}_infected_{self.initial_infected}.txt"
        self.newly_infected = []
        self.logger = Logger(self.file_name)
        self.population = self._create_population(self.initial_infected) # List of Person objects
        self.vaccinated = round((self.pop_size - self.initial_infected) * self.vacc_percentage)
        self.saved = 0



    def _create_population(self, initial_infected):
        '''This method will create the initial population.
            Args:
                initial_infected (int): The number of infected people that the simulation
                will begin with.

            Returns:
                list: A list of Person objects.

        '''
        self.vaccinated  = round((self.pop_size - initial_infected) * self.vacc_percentage)
        print(" self.vaccinated", self.vaccinated)
        unvaccinated = round((self.pop_size - initial_infected) - self.vaccinated)
        print("unvaccinated", unvaccinated)

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
        # TODO: Complete this helper method.  Returns a Boolean.
        # self population is a list of person\
        print(f" self.vaccinated in simulation {self.vaccinated}")
        print(f" self.total_dead in simulation {self.total_dead}")
        print(f'should be equal to total population {self.vaccinated + self.total_dead}')
        if self.vaccinated + self.total_dead >= self.pop_size:
            self.logger.write_currentinfect_and_dead(self.total_dead, self.pop_size, self.saved, self.total_infected)
            return False
        return True

    def run(self):
        ''' This method should run the simulation until all requirements for ending
        the simulation are met.
        '''
        # To simplify the logic here, use the helper method
        # _simulation_should_continue() to tell us whether or not we should continue
        # the simulation and run at least 1 more time_step.

        # TODO: Keep track of the number of time steps that have passed.
        # HINT: You may want to call the logger's log_time_step() method at the end of each time step.
        # TODO: Set this variable using a helper
        time_step_counter = 0
        while self._simulation_should_continue():
            x = self._simulation_should_continue()
            print(x)
            print(f" sum {self.vaccinated + self.total_dead}")
            # print(f'The simulation has ended after {time_step_counter} turns.')
            self.time_step()
            time_step_counter += 1
            print(f"**********************************************{time_step_counter}******************************************************")
            print(f" total infected from the population at some point before the virus burnt out self.total_infected {self.total_infected}")
            print(f" total infected from the population at some point before the virus burnt out self.current_infected {self.current_infected}")
            self.logger.log_time_step(time_step_counter)
        # TODO: for every iteration of this loop, call self.time_step() to compute another
        # round of this simulation.


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
        # HINT: You may want to call the logger's log_time_step() method at the end of each time step.
        # TODO: Set this variable using a helper
        # self.logger.write_currentinfect_and_dead(self.vaccinated, self.total_dead)
        self.logger.write_metadata(self.pop_size, self.vacc_percentage, self.virus.name, self.virus.mortality_rate, self.virus.repro_rate)
        # self.saved = 0
        for person in self.population:
            # print(f"currently infected before.......................... interaction: {self.current_infected}")
            if person.infection and person.is_alive:
                for num in range(100):
                    random_person = self._random_person(person._id)
                    self.interaction(person, random_person)
                survive = person.did_survive_infection()
                print("before logger", person, survive)
                self.logger.log_infection_survival(person, survive)
                print("after logger", person, survive)
                if not survive:
                    self.total_dead += 1
                    # print(f"total dead {self.total_dead}")
                    # print("total dead incremented...................................")

                else:
                    self.vaccinated += 1
                    # print(f"vaccinate {self.vaccinated}")
                    # print("vaccinated incrematened ......................................")
                self.current_infected -= 1
                # self.saved -= 1
            # print(f"currently infected after>>>>>>>>>>>>>>>>>>>>> interaction: {self.current_infected}")

        self._infect_newly_infected()
        # self.logger.log_time_step()

        # At the end of each time step, call self._infect_newly_infected()
        # and then reset .newly_infected back to an empty list.
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
        # Assert statements are included to make sure that only living people are passed
        # in as params
        assert person.is_alive == True
        assert random_person.is_alive == True
        if random_person.is_vaccinated:
            self.logger.log_interaction(person, random_person, random_person_vacc=True)
            self.saved += 1
        elif random_person.infection:
            self.logger.log_interaction(person, random_person, random_person_sick=True)
        elif random_person.infection is None and not random_person.is_vaccinated:
            rand_num = random.random()
            if rand_num  <= person.infection.repro_rate:
                self.newly_infected.append(random_person._id)
                self.current_infected += 1
                print(f"current_infected incremented ......................................{self.current_infected}")
                self.total_infected += 1
                self.logger.log_interaction(person, random_person, did_infect=True)

    def _infect_newly_infected(self):
        ''' This method should iterate through the list of ._id stored in self.newly_infected
        and update each Person object with the disease. '''
        # TODO: Call this method at the end of every time step and infect each Person.
        # TODO: Once you have iterated through the entire list of self.newly_infected, remember
        # to reset self.newly_infected back to an empty list.
        for id in self.newly_infected:
            self.population[id].infection = self.virus
        self.newly_infected = []
        print()

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
