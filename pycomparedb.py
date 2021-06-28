import configparser

def main():
    # Charge properties values
    config = configparser.ConfigParser()
    config.read('pycomparedb.ini')
    host = config['DB-SOURCE']['host']
    port = config['DB-SOURCE']['port']
    database = config['DB-SOURCE']['database']
    user = config['DB-SOURCE']['user']
    password = config['DB-SOURCE']['password']

    # Print values of properties
    print ("Valores de los parámetros de configuración:")
    print ("Host: "+host)

if __name__ == "__main__":
    main()