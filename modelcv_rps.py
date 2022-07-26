import cv2
from keras.models import load_model
import numpy as np
import random

options = ['rock', 'paper', 'scissors']

options_mapped = {
     0: 'rock', 
     1: 'paper', 
     2: 'scissors',
     3: 'nothing'
}

def mapper(val): #maps to value
    return options_mapped[val]

def who_is_the_winner(player,computer): #works out who has won the round
    if player == computer:
        return print("Draw!")

    if player == "rock":
          if computer == "paper":
              return "computer"
          if computer == "scissors":
              return "player"

    if player == "paper":
          if computer == "rock":
              return "player"
          if computer == "scissors":
              return "computer"

    if player == "scissors":
          if computer == "paper":
              return "player"
          if computer == "rock":
              return "computer"


model = load_model("keras_model.h5") #load model into memory

cap = cv2.VideoCapture(0) #caption for video - numbered cameras (start camera from open cv)

data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32) #capturing predictions
prev_move = None

while True: #continuous loop for user to make move via webcam
    ret, frame = cap.read()
    if not ret:
        continue

    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)

    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image

    prediction = model.predict(data) #predict the player's move
    move_code = np.argmax(prediction[0])
    player_move = mapper(move_code) #probability mapped to rock/paper/scissors
    cv2.imshow('frame', frame)
    
    if prev_move != player_move:
        if player_move != "Nothing":
            computer_move = random.choice(options)
            winner = who_is_the_winner(player_move,computer_move) #calls earlier function to determine winner
        else:
            computer_move = 'none'
            winner = "Waiting..."
    prev_move = player_move

    #make it look pretty and show the info

    cv2.imshow("Rock Paper Scissors", frame)
    # Press q to close the window

    if cv2.waitKey(1) & 0xFF == ord('q'): #condition to stop loop
        break