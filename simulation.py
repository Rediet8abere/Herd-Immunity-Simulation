import random, sys
# random.seed(42)
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
        # what these two are for
        self.total_infected = 0 # Int
        self.current_infected = 0 # Int

        self.vacc_percentage = vacc_percentage # float between 0 and 1
        # what is this for
        self.total_dead = 0 # Int

        self.file_name = "{}_simulation_pop_{}_vp_{}_infected_{}.txt".format(
            self.virus.name, self.pop_size, self.vacc_percentage, self.initial_infected)
        self.newly_infected = []
        logger = Logger(self.file_name)
        self.logger = logger
        self.population = self._create_population(self.initial_infected) # List of Person objects



    def _create_population(self, initial_infected):
        '''This method will create the initial population.
            Args:
                initial_infected (int): The number of infected people that the simulation
                will begin with.

            Returns:
                list: A list of Person objects.

        '''
        # This method should be called when the simulation
        # begins, to create the population that will be used. This method should return
        # an array filled with Person objects that matches the specifications of the
        # simulation (correct number of people in the population, correct percentage of
        # people vaccinated, correct number of initially infected people).
        # Use the attributes created in the init method to create a population that has
        # the correct intial vaccination percentage and initial infected.
        # python3 simulation.py Ebola 0.25 0.70 100000 0.90 10
        # (self, _id, is_vaccinated, infection=None)
        # create a population object for the population number
        vaccinated = int((self.pop_size - initial_infected) * self.vacc_percentage)
        print("vaccinated", vaccinated)
        unvaccinated = int((self.pop_size - initial_infected) - vaccinated)
        print("unvaccinated", unvaccinated)

        person_list = []
        for num in range(pop_size):
            if num < initial_infected:
                person = Person(num, False, self.virus)
                # print(num, person)
                person_list.append(person)
            elif initial_infected <= num <= unvaccinated:
                person = Person(num, False)
                # print(num, person)
                person_list.append(person)
            else:
                person = Person(num, True)
                # print(num, person)
                person_list.append(person)
        return person_list

        # an array filled with Person objects that matches the specifications of the
        # simulation (correct number of people in the population, correct percentage of
        # people vaccinated, correct number of initially infected people).

        # I have to decide how many true and false to have in a my peroon object based on percentage

        # person = []
        # for num in range(self.pop_size - initial_infected):
        #     person = person(num, )





    def _simulation_should_continue(self):
        ''' The simulation should only end if the entire population is dead
        or everyone is vaccinated.

            Returns:
                bool: True for simulation should continue, False if it should end.
        '''
        # TODO: Complete this helper method.  Returns a Boolean.
        # self population is a list of person
        person_isAlive = []
        for person in self.population:
            person_isAlive.append(person.is_alive)
            # print(person.is_alive)

        if(len(set(person_isAlive))==1):
            # print("All elements in list are same")
            return False
        else:
            # print("All elements in list are not same")
            return True

    def run(self):
        ''' This method should run the simulation until all requirements for ending
        the simulation are met.
        '''
        # TODO: Finish this method.  To simplify the logic here, use the helper method
        # _simulation_should_continue() to tell us whether or not we should continue
        # the simulation and run at least 1 more time_step.

        # TODO: Keep track of the number of time steps that have passed.
        # HINT: You may want to call the logger's log_time_step() method at the end of each time step.
        # TODO: Set this variable using a helper
        time_step_counter = 0
        should_continue = self._simulation_should_continue()
        # print(should_continue)

        while should_continue:
            print('The simulation has ended after {time_step_counter} turns.'.format(time_step_counter))
            time_step_counter += 1
            self.time_step()
            log_time_step(self, time_step_number)

        # TODO: for every iteration of this loop, call self.time_step() to compute another
        # round of this simulation.
        # log_time_step(self, time_step_number)

    def _random_person(self):
        generate = True
        while generate:

            random_person = None
            is_vaccinated = False
            infection = None
            random_id = random.randint(0, (self.pop_size - 1))
            random_num = random.randint(0, 1)

            if random_num is 1:
                is_vaccinated = True
                infection = None
                # print("is vaccinated is True")
            else:
                is_vaccinated = False
                random_id = random.randint(0, (self.pop_size - 1))
                random_num = random.randint(0, 1)
                # print("random number for infection", random_num)
                if random_num is 1:
                    infection = None
                    # print("infection", infection)
                else:
                    infection = self.virus
                    # print("infection", infection)


            if infection == None:
                # print("random_person not infected and is vaccinated")
                # print("is vaccinated", is_vaccinated)
                # print()
                # print("in if")
                # print("random_id passed", random_id)
                # print("is_vaccinated for random person passed could be true or false", is_vaccinated)
                # print("infection for random person passed is none", infection)
                # print()
                random_person = Person(random_id, is_vaccinated)
                # print("random person is vaccinated True in random person if ", random_person.is_vaccinated)
                # print("random person id", random_person._id)
                # print("random person is_vaccinated expecting true or false from the object", random_person.is_vaccinated)
                # print("random person infection excpecting none from the object", random_person.infection)
                # print()
                generate = False
                return random_person
            else:
                # print("is vaccinated", is_vaccinated)
                # print()
                # print("in else")
                # print("random_id passed", random_id)
                # print("is_vaccinated for random person passed expecting flase value", is_vaccinated)
                # print("infection for random person passed expecting virus", infection)
                # print()

                random_person = Person(random_id, is_vaccinated, infection)

                # print("random person id", random_person._id)
                # print("random person is_vaccinated expecting false value from the object", random_person.is_vaccinated)
                # print("random person infection excpecting virus from the object", random_person.infection)
                # print()
                # print("random person is vaccinated False in random person else ", random_person.is_vaccinated)
                survive = random_person.did_survive_infection()
                # print("did random survive", survive)
                if survive:
                    # print("survived")
                    # print()
                    generate = False
                    return random_person
                else:
                    generate = True

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
        # (self, _id, is_vaccinated, infection=None)

        #100 total interactions with a random person for each infected person
            # in the population
            # each infected person interacts with 100 random person
            # am I getting the same random person?
        for person in self.population:
            interaction_counter = 0
            # print("person in self.population", person)
            for num in range(10):
                random_person = self._random_person()
                # print("random person is_vaccinated in time step", random_person.is_vaccinated)
                self.interaction(person, random_person)
                interaction_counter += 1
            # print(f'{person._id} interacts {interaction_counter} times')
            # print()

        # print("interaction_counter", interaction_counter)
        # self._infect_newly_infected()
        # self.newly_infected = []
        # At the end of each time step, call self._infect_newly_infected()
        # and then reset .newly_infected back to an empty list.


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
        # print("random person is vacinated in interaction", random_person.is_vaccinated)

        # TODO: Finish this method.
        #  The possible cases you'll need to cover are listed below:
            # random_person is vaccinated:
            #     nothing happens to random person.
            # random_person is already infected:
            #     nothing happens to random person.
            # random_person is healthy, but unvaccinated:
            #     generate a random number between 0 and 1.  If that number is smaller
            #     than repro_rate, random_person's ID should be appended to
            #     Simulation object's newly_infected array, so that their .infected
            #     attribute can be changed to True at the end of the time step.
        # TODO: Call slogger method during this method.
        # print(" random person", random_person)
        # print("random person is viccinated", random_person.is_vaccinated)
        # print(f"random person is infected {random_person.infection}")
        # print()
        # print("person", person)
        # print("person is viccinated", person.is_vaccinated)
        # print(f"person is infected {person.infection}")
        # print()
        if random_person.is_vaccinated:
            random_person = random_person
            # print("random person is viccinated", random_person.is_vaccinated)
        elif random_person.infection is not None:
            random_person = random_person
            # print("random person is infected", random_person.infection)
        elif random_person.infection is None and random_person.is_vaccinated is False:
            rand_num = random.random()
            round_rand_num = round(rand_num, 1)
            # print(f"random person is not infected {random_person.infection} and not vaccinated {random_person.is_vaccinated}")
            # print(f"{round_rand_num} rounded random number in interaction")
            # print(f"{person.infection.repro_rate} person's infection reproduction rate")
            if round_rand_num < person.infection.repro_rate:
                self.newly_infected.append(random_person._id)

    def _infect_newly_infected(self):
        ''' This method should iterate through the list of ._id stored in self.newly_infected
        and update each Person object with the disease. '''
        # TODO: Call this method at the end of every time step and infect each Person.
        # TODO: Once you have iterated through the entire list of self.newly_infected, remember
        # to reset self.newly_infected back to an empty list.
        for newly_infect in self.newly_infected:
            pass
            # print("loop in infect_newly infect")
            # print(newly_infect)
        # self.newly_infected = []

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
    # sim.run()
    # sim.time_step()
    # sim._infect_newly_infected()
    #python3 simulation.py Ebola 0.25 0.70 100000 0.90 10
