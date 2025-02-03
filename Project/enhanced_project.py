# import tkinter as tk
# from tkinter import scrolledtext, messagebox, simpledialog
# from threading import Thread
# import logging
# import speech_recognition as sr
# import pyttsx3
# import cv2
# import mediapipe as mp
# import tensorflow as tf
# import numpy as np
# import time

# # Setup logging
# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# # Initialize Text-to-Speech engine globally to avoid reinitialization
# tts_engine = pyttsx3.init()

# # Function to log and display messages in the GUI
# def log_and_display(output_widget, message, level="info"):
#     if level == "info":
#         logging.info(message)
#     elif level == "warning":
#         logging.warning(message)
#     elif level == "error":
#         logging.error(message)
#     output_widget.insert(tk.END, f"{message}\n")
#     output_widget.see(tk.END)

# # Speech to Text Functionality
# def speech_to_text(output_widget):
#     recognizer = sr.Recognizer()
#     with sr.Microphone() as source:
#         log_and_display(output_widget, "Listening...")
#         try:
#             audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
#             log_and_display(output_widget, "Recognizing...")
#             text = recognizer.recognize_google(audio)
#             log_and_display(output_widget, f"Recognized Text: {text}")
#         except sr.WaitTimeoutError:
#             log_and_display(output_widget, "Listening timed out while waiting for phrase to start", "warning")
#         except sr.UnknownValueError:
#             log_and_display(output_widget, "Sorry, I did not understand that.", "warning")
#         except sr.RequestError:
#             log_and_display(output_widget, "Sorry, my speech service is down.", "error")

# # Sign Language Recognition Functionality
# def sign_to_text(output_widget):
#     try:
#         model = tf.keras.models.load_model('sign_model.h5')
#         log_and_display(output_widget, "Model loaded successfully!")
#     except Exception as e:
#         log_and_display(output_widget, f"Error loading model: {e}", "error")
#         return
    
#     mp_hands = mp.solutions.hands
#     hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
#     mp_drawing = mp.solutions.drawing_utils
    
#     cap = cv2.VideoCapture(0)
#     if not cap.isOpened():
#         log_and_display(output_widget, "Error: Could not access the camera.", "error")
#         return
    
#     log_and_display(output_widget, "Starting Sign Language Recognition...")
#     class_names = [chr(i) for i in range(65, 91)]  # A-Z letters
    
#     while True:
#         start_time = time.time()  # Start timing for performance monitoring
        
#         ret, frame = cap.read()
#         if not ret:
#             log_and_display(output_widget, "Failed to grab frame", "error")
#             break
        
#         frame = cv2.flip(frame, 1)
#         rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         result = hands.process(rgb)
        
#         if result.multi_hand_landmarks:
#             for hand_landmarks in result.multi_hand_landmarks:
#                 mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                
#                 landmarks = []
#                 for lm in hand_landmarks.landmark:
#                     landmarks.extend([lm.x, lm.y, lm.z])
                
#                 landmarks = np.array(landmarks).reshape(1, -1)
#                 prediction = model.predict(landmarks)
#                 predicted_class = np.argmax(prediction)
#                 confidence = prediction[0][predicted_class]
                
#                 if confidence > 0.7:
#                     letter = class_names[predicted_class]
#                     log_and_display(output_widget, f"Detected Letter: {letter}")
        
#         cv2.imshow("Sign Language Recognition - Press 'q' to Quit", frame)
        
#         end_time = time.time()  # End timing
#         fps = 1 / (end_time - start_time)  # Calculate FPS
#         logging.info(f"FPS: {fps:.2f}")  # Log FPS
        
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
    
#     cap.release()
#     cv2.destroyAllWindows()
#     hands.close()

# # Text to Speech Functionality
# def text_to_speech_func(input_text):
#     if input_text.strip() == "":
#         return
#     tts_engine.say(input_text)
#     tts_engine.runAndWait()
#     logging.info(f"Converted Text to Speech: {input_text}")

# # Thread Management for Asynchronous Operations
# def on_speech_to_text(output_widget):
#     thread = Thread(target=speech_to_text, args=(output_widget,))
#     thread.start()

# def on_sign_to_text(output_widget):
#     thread = Thread(target=sign_to_text, args=(output_widget,))
#     thread.start()

# def on_text_to_speech(entry_widget):
#     text = entry_widget.get()
#     if text.strip() == "":
#         messagebox.showwarning("Warning", "Please enter text before converting to speech.")
#         return
#     thread = Thread(target=text_to_speech_func, args=(text,))
#     thread.start()

# # Create the main window
# root = tk.Tk()
# root.title("Speech and Sign Language Converter")
# root.geometry("600x600")

# # Create a scrolled text widget for output
# output_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=20)
# output_text.pack(pady=10)

# # Frame for buttons
# button_frame = tk.Frame(root)
# button_frame.pack(pady=10)

# # Speech to Text Button
# speech_button = tk.Button(button_frame, text="Speech to Text", width=20,
#                           command=lambda: on_speech_to_text(output_text))
# speech_button.grid(row=0, column=0, padx=5, pady=5)

# # Sign Language to Text Button
# sign_button = tk.Button(button_frame, text="Sign Language to Text", width=20,
#                         command=lambda: on_sign_to_text(output_text))
# sign_button.grid(row=0, column=1, padx=5, pady=5)

# # Text to Speech Entry and Button
# tts_frame = tk.Frame(root)
# tts_frame.pack(pady=10)

# tts_entry = tk.Entry(tts_frame, width=50)
# tts_entry.grid(row=0, column=0, padx=5)

# tts_button = tk.Button(tts_frame, text="Text to Speech", width=15,
#                        command=lambda: on_text_to_speech(tts_entry))
# tts_button.grid(row=0, column=1, padx=5)

# # Run the application
# root.mainloop()

n = int(input("number - "))
print("Hello, World!")
if n >= 0:
  print ("chodumal")
else: 
  print ("lodumal")