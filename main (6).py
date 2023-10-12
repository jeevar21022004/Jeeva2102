'''Implement a class called player that represents a cricket player. The player class should have a
method called play() which prints "The players is playing cricket. Drive a two classes,Batsman and
Blower, from the player class.Override the play() method in each derived class to print "The batsman
is batting" and "The blower is blowing", respectively. Write a program to create subjects or both the
Batsman and Blower classes and call the play() method for each object.'''


# Define the base class Player 
class Player:
      def play(self):
          print("The player is playing cricket.")

# Define the derived class Batsman 
class Batsman(Player):
      def play(self):
          print("The batsman is batting.")

# Define the derived class Blower
class Blower(Player):
      def play(self):
          print("The bowler is bowling.")

# Create objects of Batsman and Blower classes
batsman = Batsman()
blower =Blower()

# Call The play() method for each object
batsman.play()
blower.play()