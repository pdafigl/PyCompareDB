import configparser

def get_config(source_db, target_db, ini_file):
    ''' Function to charge the config parameters inside .ini file '''
    # Declare config variable
    config = configparser.ConfigParser()
    config.read(ini_file)
    # Append Source DB config to dictionary
    for (each_key, each_val) in config.items('SOURCE-DB'):
        source_db [each_key] = each_val
    # Append TArget DB config to dictionary
    for (each_key, each_val) in config.items('TARGET-DB'):
        target_db [each_key] = each_val

    # Return variables with values
    return source_db, target_db