from ast import While
from pickle import TRUE
import random
import cv2
from keras.models import load_model
import numpy as np
import time

options = ['Rock', 'Paper', 'Scissors']

options_mapped = {
     0: 'Rock', 
     1: 'Paper', 
     2: 'Scissors',
     3: 'Nothing'
}

def play():
    def get_computer_choice():
     computer = random.choice(options)
     print(computer)
     return computer
   
    def countdown(t=3):
        while t:
            


        pass


    def get_player_choice():
     model = load_model('keras_model.h5')
     cap = cv2.VideoCapture(0) #caption for video - numbered cameras
     data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32) # capturing predictions

     while True: 
      ret, frame = cap.read()
      resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
      image_np = np.array(resized_frame)
      normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
      data[0] = normalized_image
      prediction = model.predict(data)
      player = options_mapped[int(np.argmax(prediction))]
      cv2.imshow('frame', frame)


      # Press q to close the window
      print(prediction)
      print(player)
       
      
      if cv2.waitKey(1) & 0xFF == ord('q'): #condition to stop loop
            
       # After the loop release the cap object
       cap.release()
     # Destroy all the windows
      cv2.destroyAllWindows() 
      return player

      
      
    
    def get_winner(computer,player):
      if computer == player:
        return "Draw"
      elif computer == "Rock" and player == "Scissors":
        return "Computer"
      elif computer == "Paper" and player == "Rock":
        return "Computer"
      elif computer == "Scissors" and player == "Paper":
        return "Computer"
      elif player == "-Waiting-":
        return "Error"
      else:
        return "Player"
    
    
    computer = get_computer_choice()
    player = get_player_choice()
    winner = get_winner(computer,player)
    print(str(winner))



play()
