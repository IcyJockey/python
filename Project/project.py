# import tkinter as tk
# from tkinter import scrolledtext
# from threading import Thread

# # Import the functions
# import speech_recognition as sr
# import pyttsx3
# import cv2
# import mediapipe as mp
# import tensorflow as tf
# import numpy as np

# def speech_to_text(output_widget):
#     recognizer = sr.Recognizer()
#     with sr.Microphone() as source:
#         output_widget.insert(tk.END, "Listening...\n")
#         output_widget.see(tk.END)
#         try:
#             audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
#             output_widget.insert(tk.END, "Recognizing...\n")
#             output_widget.see(tk.END)
#             text = recognizer.recognize_google(audio)
#             output_widget.insert(tk.END, f"Text: {text}\n")
#         except sr.WaitTimeoutError:
#             output_widget.insert(tk.END, "Listening timed out while waiting for phrase to start\n")
#         except sr.UnknownValueError:
#             output_widget.insert(tk.END, "Sorry, I did not understand that.\n")
#         except sr.RequestError:
#             output_widget.insert(tk.END, "Sorry, my speech service is down.\n")

# def sign_to_text(output_widget):
#     # Load the pre-trained model
#     try:
#         model = tf.keras.models.load_model('sign_model.h5')
#     except Exception as e:
#         output_widget.insert(tk.END, f"Error loading model: {e}\n")
#         return
    
#     # Initialize Mediapipe
#     mp_hands = mp.solutions.hands
#     hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
    
#     mp_drawing = mp.solutions.drawing_utils
    
#     cap = cv2.VideoCapture(0)
#     output_widget.insert(tk.END, "Starting Sign Language Recognition...\n")
#     output_widget.see(tk.END)
    
#     class_names = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
#                    'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
#                    'U', 'V', 'W', 'X', 'Y', 'Z']
    
#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             output_widget.insert(tk.END, "Failed to grab frame\n")
#             break
        
#         # Flip the frame to avoid mirrored view
#         frame = cv2.flip(frame, 1)
#         rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         result = hands.process(rgb)
        
#         if result.multi_hand_landmarks:
#             for hand_landmarks in result.multi_hand_landmarks:
#                 # Draw landmarks on the frame
#                 mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                
#                 # Extract landmark coordinates
#                 landmarks = []
#                 for lm in hand_landmarks.landmark:
#                     landmarks.extend([lm.x, lm.y, lm.z])
                
#                 # Prepare input for the model
#                 landmarks = np.array(landmarks).reshape(1, -1)
#                 prediction = model.predict(landmarks)
#                 predicted_class = np.argmax(prediction)
#                 confidence = prediction[0][predicted_class]
                
#                 if confidence > 0.7:
#                     letter = class_names[predicted_class]
#                     output_widget.insert(tk.END, f"Detected Letter: {letter}\n")
#                     output_widget.see(tk.END)
        
#         cv2.imshow("Sign Language Recognition - Press 'q' to Quit", frame)
        
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
    
#     cap.release()
#     cv2.destroyAllWindows()
#     hands.close()

# def text_to_speech_func(input_text):
#     if input_text.strip() == "":
#         return
#     engine = pyttsx3.init()
#     engine.say(input_text)
#     engine.runAndWait()

# def on_speech_to_text(output_widget):
#     thread = Thread(target=speech_to_text, args=(output_widget,))
#     thread.start()

# def on_sign_to_text(output_widget):
#     thread = Thread(target=sign_to_text, args=(output_widget,))
#     thread.start()

# def on_text_to_speech(entry_widget):
#     text = entry_widget.get()
#     if text.strip() == "":
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









# yeh naya code hai

# import tkinter as tk
# from tkinter import messagebox, simpledialog
# import speech_recognition as sr
# import cv2
# import pyttsx3
# import tensorflow as tf

# # Load the pre-trained sign language model (Make sure the model file is in the same directory or provide the correct path)
# try:
#     model = tf.keras.models.load_model('sign_model.h5')
#     print("Sign language model loaded successfully!")
# except OSError as e:
#     print(f"Error loading model: {e}")
#     model = None

# def on_speech_to_text():
#     recognizer = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening...")
#         audio = recognizer.listen(source)

#         try:
#             print("Recognizing...")
#             text = recognizer.recognize_google(audio)
#             print(f"Text: {text}")
#             messagebox.showinfo("Speech to Text", f"Recognized Text: {text}")
#             return text
#         except sr.UnknownValueError:
#             messagebox.showwarning("Speech to Text", "Could not understand the audio.")
#         except sr.RequestError:
#             messagebox.showerror("Speech to Text", "Speech recognition service error.")

#     return None

# def on_sign_to_text():
#     if model is None:
#         messagebox.showerror("Sign Language", "Sign language model not loaded.")
#         return
    
#     cap = cv2.VideoCapture(0)

#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             break

#         # Here you would normally process the frame and use the model to predict the sign language gesture
#         # For demonstration, we just show the video feed.
#         cv2.imshow("Sign Language Recognition", frame)

#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     cap.release()
#     cv2.destroyAllWindows()

#     messagebox.showinfo("Sign Language", "Sign language recognition simulation complete!")

# def on_text_to_speech():
#     text = simpledialog.askstring("Input", "Enter text to convert to speech:")
#     if text:
#         engine = pyttsx3.init()
#         engine.say(text)
#         engine.runAndWait()
#         messagebox.showinfo("Text to Speech", "Speech output completed.")

# # Create the main interface
# root = tk.Tk()
# root.title("Speech and Sign Language Converter")

# # Create buttons for each function
# speech_button = tk.Button(root, text="Speech to Text", command=on_speech_to_text)
# sign_button = tk.Button(root, text="Sign Language to Text", command=on_sign_to_text)
# text_speech_button = tk.Button(root, text="Text to Speech", command=on_text_to_speech)

# # Display the buttons on the screen
# speech_button.pack(pady=10)
# sign_button.pack(pady=10)
# text_speech_button.pack(pady=10)

# # Start the application
# root.mainloop()
