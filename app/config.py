class config:
    '''
    this is a general configuration class
    '''
    pass


class ProdConfig(Config):
    
    '''
    production configuration child class

    Args:
        config:The parent configuration class with general configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    development configuration child class
    Args:
     config:The parent configuration class with general configuration settings
    '''
    pass

    DEBUG = True
    

