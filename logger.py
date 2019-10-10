from person import Person
from virus import Virus

class Logger(object):
    ''' Utility class responsible for logging all interactions during the simulation. '''
    # TODO: Write a test suite for this class to make sure each method is working
    # as expected.

    # PROTIP: Write your tests before you solve each function, that way you can
    # test them one by one as you write your class.

    def __init__(self, file_name):
        # TODO:  Finish this initialization method. The file_name passed should be the
        # full file name of the file that the logs will be written to.
        self.file_name = file_name

    def write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate,
                       basic_repro_num):
        '''
        The simulation class should use this method immediately to log the specific
        parameters of the simulation as the first line of the file.
        '''
        file = open('answers.txt', 'w')
        file.write("Input data for the simulation: \n")
        file.write("\n")
        file.write(f"       Population size = {str(pop_size)} \n")
        file.write(f"       percent vaccinated = {str(vacc_percentage)} \n")
        file.write(f"       virus name: {str(virus_name)} \n")
        file.write(f"       mortality_rate = {str(mortality_rate)} \n")
        file.write(f"       reproductive rate = {str(basic_repro_num)} \n")
        file.close()
        # self.write_currentinfect_and_dead(current_infected, total_dead)

        file  = open(self.file_name, 'w')
        file.write("Input data for the simulation: \n")
        file.write("\n")
        file.write(f"       Population size = {str(pop_size)} \n")
        file.write(f"       percent vaccinated = {str(vacc_percentage)} \n")
        file.write(f"       virus name: {str(virus_name)} \n")
        file.write(f"       mortality_rate = {str(mortality_rate)} \n")
        file.write(f"       reproductive rate = {str(basic_repro_num)} \n")
        file.close()

        # file = open(self.file_name, 'a')


        # with open(self.file_name) as file:
        #     content = file.read().split("\n")

        # TODO: Finish this method. This line of metadata should be tab-delimited
        # it should create the text file that we will store all logs in.
        # TIP: Use 'w' mode when you open the file. For all other methods, use
        # the 'a' mode to append a new log to the end, since 'w' overwrites the file.
        # NOTE: Make sure to end every line with a '/n' character to ensure that each
        # event logged ends up on a separate line!
    def write_currentinfect_and_dead(self, current_infected, total_dead, pop_size, saved, total_infected):
        file = open('answers.txt', 'a')
        file.write(f"       total percentage of dead Population = {str(round((total_dead/pop_size)*100))}% \n")
        file.write(f"       total interaction with infected person where a vaccination saved a random person from potentially becoming infected = {str(saved)} \n")
        file.write(f"       percentage of population infected at some point before the virus burned out {str(total_infected)}")



    def log_interaction(self, person, random_person, random_person_sick=None,
                        random_person_vacc=None, did_infect=None):
        '''
        The Simulation object should use this method to log every interaction
        a sick person has during each time step.

        The format of the log should be: "{person.ID} infects {random_person.ID} \n"

        or the other edge cases:
            "{person.ID} didn't infect {random_person.ID} because {'vaccinated' or 'already sick'} \n"
        '''
        # TODO: Finish this method. Think about how the booleans passed (or not passed)
        # represent all the possible edge cases. Use the values passed along with each person,
        # along with whether they are sick or vaccinated when they interact to determine
        # exactly what happened in the interaction and create a String, and write to your logfile.

        # self._id = _id  # int
        # self.is_alive = True  # boolean
        # self.is_vaccinated = is_vaccinated  # boolean
        # self.infection = infection  # Virus object or None

        # A sick person only has a chance at infecting healthy, unvaccinated people they encounter.
        file = open(self.file_name, 'a')
        if did_infect:
            file.write(f'{random_person._id} did not infect {person._id} because already sick \n')
        else:
            if random_person_sick:
                file.write(f'1 {random_person._id} infects {person._id} \n')
            elif random_person_vacc:
                file.write(f'{random_person._id} did not infect {person._id} because vaccinated \n')

    def log_infection_survival(self, person, did_die_from_infection):
        ''' The Simulation object uses this method to log the results of every
        call of a Person object's .resolve_infection() method.

        The format of the log should be:
            "{person.ID} died from infection\n" or "{person.ID} survived infection.\n"
        '''
        file = open(self.file_name, 'a')
        if person.is_alive:
            did_die_from_infection = False
            file.write(f'{person.ID} survived infection.\n')
        else:
            did_die_from_infection = True
            file.write(f'{person.ID} died from infection\n')
        # TODO: Finish this method. If the person survives, did_die_from_infection
        # should be False.  Otherwise, did_die_from_infection should be True.
        # Append the results of the infection to the logfile

    def log_time_step(self, time_step_number):
        ''' STRETCH CHALLENGE DETAILS:

        If you choose to extend this method, the format of the summary statistics logged
        are up to you.

        At minimum, it should contain:
            The number of people that were infected during this specific time step.
            The number of people that died on this specific time step.
            The total number of people infected in the population, including the newly infected
            The total number of dead, including those that died during this time step.

        The format of this log should be:
            "Time step {time_step_number} ended, beginning {time_step_number + 1}\n"
        '''
        # TODO: Finish this method. This method should log when a time step ends, and a
        # new one begins.
        # NOTE: Here is an opportunity for a stretch challenge!
        pass

if __name__ == "__main__":
    logger = Logger('answers.txt')
    logger.write_metadata(100000, 0.90, 'Ebola', 0.70, 0.25)
    logger.write_currentinfect_and_dead(current_infected, total_dead)

    # virus ( name, repro_rate, mortality_rate)
    # person (_id, is_vaccinated, infection=None)

    dysentery = Virus("Dysentery", 0.7, 0.2)
    person = Person(4, False)

    bubonic_Plague = Virus("bubonic Plague", 1, 0.6)
    random_person = Person(2, False)

    logger.log_interaction(person, random_person, random_person_sick=None, random_person_vacc=None, did_infect=None)

# python3 simulation.py Ebola 0.25 0.70 100000 0.90 10
def test_write_metadata():
    # create some people to test if our init method works as expected
    logger = Logger('test_write.txt')
    logger.write_metadata(100000, 0.90, 'Ebola', 0.70, 0.25)

    with open('test_write.txt') as f:
        content = f.read().split("\n")
        assert content[0] == '100000'
        assert content[1] == '0.9'
        assert content[2] == 'Ebola'
        assert content[3] == '0.7'
        assert content[4] == '0.25'

def test_log_interaction():
    # virus ( name, repro_rate, mortality_rate)
    # person (_id, is_vaccinated, infection=None)
    logger = Logger('test_interaction.txt')

    dysentery = Virus("Dysentery", 0.7, 0.2)
    person = Person(4, True, dysentery)

    bubonic_Plague = Virus("bubonic Plague", 1, 0.6)
    random_person = Person(2, True, bubonic_Plague)
    # person.infection is not None and random_person.is_vaccinated == False
    logger.log_interaction(person, random_person, random_person_sick=None, random_person_vacc=None, did_infect=None)
