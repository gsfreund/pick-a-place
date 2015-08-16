from flask import Flask 
application = Flask( __name__ ) 

@application.route( '/' ) 
def pick_a_restaurant():
  from random import randint
  with open( 'list.txt' ) as lis:
    restaurants = lis.readlines() 
  return restaurants[ randint( 0, len( restaurants ) ) ] 

if __name__ == '__main__':
  application.run()
