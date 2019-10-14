from person import Person
from virus import Virus

class Logger(object):
    ''' Utility class responsible for logging all interactions during the simulation. '''

    def __init__(self, file_name):
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

        file  = open(self.file_name, 'w')
        file.write("Input data for the simulation: \n")
        file.write("\n")
        file.write(f"       Population size = {str(pop_size)} \n")
        file.write(f"       percent vaccinated = {str(vacc_percentage)} \n")
        file.write(f"       virus name: {str(virus_name)} \n")
        file.write(f"       mortality_rate = {str(mortality_rate)} \n")
        file.write(f"       reproductive rate = {str(basic_repro_num)} \n")
        file.close()

    def write_currentinfect_and_dead(self, total_dead, pop_size, saved, current_infected):
        file = open('answers.txt', 'a')
        file.write(f"       total percentage of dead Population = {str(round((total_dead/pop_size)*100))}% \n")
        file.write(f"       total interaction with infected person where a vaccination saved a random person from potentially becoming infected = {str(saved)} \n")
        file.write(f"       percentage of population infected at some point before the virus burned out {str(round((current_infected/pop_size)*100))}%")
        file.close()

    def log_interaction(self, person, random_person, random_person_sick=None,
                        random_person_vacc=None, did_infect=None):
        '''
        The Simulation object should use this method to log every interaction
        a sick person has during each time step.

        The format of the log should be: "{person.ID} infects {random_person.ID} \n"

        or the other edge cases:
            "{person.ID} didn't infect {random_person.ID} because {'vaccinated' or 'already sick'} \n"
        '''
        file = open(self.file_name, 'a')
        if did_infect:
            file.write(f'{person._id} infects {random_person._id} \n')
        else:
            if random_person_sick:
                file.write(f'{person._id} did not infect {random_person._id} because already sick \n')
            elif random_person_vacc:
                file.write(f'{person._id} did not infect {random_person._id} because vaccinated \n')
        file.close()

    def log_infection_survival(self, person, did_die_from_infection):
        ''' The Simulation object uses this method to log the results of every
        call of a Person object's .resolve_infection() method.

        The format of the log should be:
            "{person.ID} died from infection\n" or "{person.ID} survived infection.\n"
        '''
        file = open(self.file_name, 'a')
        if not did_die_from_infection:
            file.write(f'{person._id} survived infection.\n')
        else:
            file.write(f'{person._id} died from infection\n')
        file.close()

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

    dysentery = Virus("Dysentery", 0.7, 0.2)
    person = Person(4, False)

    logger.log_infection_survival(person, True)

    bubonic_Plague = Virus("bubonic Plague", 1, 0.6)
    random_person = Person(2, False)

    logger.log_interaction(person, random_person, random_person_sick=None, random_person_vacc=None, did_infect=None)

# All Test In logger_test.py
