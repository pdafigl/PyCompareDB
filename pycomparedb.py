# Import Python libraries
import sys
import configparser

# Import Custom fucntions
from functions.help import *
from functions.config import *


# Main function
def main():
    # Check args
    number_of_arguments = len(sys.argv)
    if (number_of_arguments == 1):
        print_help()

    # Charge properties values
    source_db = {}
    target_db = {}
    ini_file = '../config/pycomparedb.ini'
    get_config (source_db, target_db, ini_file)
    
if __name__ == "__main__":
    main()