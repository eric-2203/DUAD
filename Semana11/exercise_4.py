class Head:
    def __init__(self):
        pass

class Torso:
    def __init__(self, head, right_arm, left_arm):
        self.right_arm = right_arm
        self.left_arm = left_arm
        self.head = head

class Arms:
    def __init__(self, right_hand, left_hand):
        self.right_hand = right_hand
        self.left_hand = left_hand

class Hand:
    def __init__(self):
        pass
        
        

class Legs: 
    def __init__(self, right_foot, left_foot):
        self.right_foot = right_foot
        self.left_foot = left_foot
        

class Feet:
    def __init__(self):
        pass
    

class Human:
    def __init__(self, head, Torso, legs):
        print("A human has been born.")
        self.head = head
        self.torso = Torso
        self.legs = legs
    
        

left_foot_hairy = Feet()
right_foot_stinky = Feet()
hairy_legs = Legs(right_foot_stinky, left_foot_hairy)
left_hand = Hand()
right_hand = Hand()
muscle_arms = Arms(right_hand, left_hand)
head = Head()
hum_torso = Torso(head, muscle_arms)

my_human = Human(head, hum_torso, hairy_legs)
print(my_human)