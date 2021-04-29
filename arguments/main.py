# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line
# Assignment Arguments
# Dirk-Jan Vethaak

def greet(name= ' ', greeting='Hello, <name>!'):

    # Replace template <> to variable
    text = greeting.replace('<name>',name )
    
    return text



# Test function 
print(greet('Doc'))
print(greet('Bob', "What's up, <name>!"))




# dictonary planets and gravity hardcode
planet_gravities= {
        'sun' : 274.0,
        'jupiter': 24.9,
        'neptune' : 11.1,
        'saturn': 10.4,
        'earth' : 9.8,
        'uranus' : 8.9,
        'venus' : 8.9,
        'mars' : 3.7,
        'mercury'  : 3.7,
        'moon' : 1.6,
        'pluto' : 0.6
}


def force(mass = 0.0, body='earth'):
    gravity = planet_gravities[body]
    force = mass * gravity
    return force
    
# test function
print(force(mass= 20.0,body='mars'))


def pull(m1,m2,d):
    G = 6.674E-11
    pull = G *((m1*m2)/d**2)
    return pull

# test function
print(pull(1.0,2.0,5.0))