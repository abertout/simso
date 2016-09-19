#!/usr/bin/python3

"""
Example of a script that uses SimSo.
"""

import sys
from simso.core import Model
from simso.configuration import Configuration


def main(argv):
    if len(argv) == 2:
        # Configuration load from a file.
        configuration = Configuration(argv[1])
    else:
        # Manual configuration:
        configuration = Configuration()

        configuration.cycles_per_ms = 1
 
        configuration.etm = "pwcet"

        configuration.duration = 100 * configuration.cycles_per_ms

        # Add tasks:
        configuration.add_task(name="T1", identifier=1,
                              activation_date=0, pwcet=[(2,1)],pmit=[(5,0.2),(6,0.8)], deadline=6, task_type = "Probabilistic",abort_on_miss=False)

        configuration.add_task(name="T2", identifier=2,
                              activation_date=0, pwcet=[(3,0.9),(4,0.1)],pmit=[(7,1)], deadline=7, task_type = "Probabilistic",abort_on_miss=False)
        # Add a processor:
        configuration.add_processor(name="CPU 1", identifier=1)

        # Add a scheduler:
        configuration.scheduler_info.filename = "simso/schedulers/DM_mono.py"

    # Check the config before trying to run it.
    configuration.check_all()

    # Init a model from the configuration.
    model = Model(configuration)

    # Execute the simulation.
    model.run_model()

    # Print logs.
    for log in model.logs:
        print(log)

main(sys.argv)
