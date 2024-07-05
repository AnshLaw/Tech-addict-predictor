import tkinter as tk
from pyvirtualdisplay import Display
import pickle
import os
array = []

if os.getenv('HEADLESS', 'false').lower() == 'true':
    display = Display(visible=0, size=(800, 600))
    display.start()

class CheckboxForm(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Checkbox Form")

        # Questions and Options
        self.questions = [
            {
                "question": "What is your age?",
                "options": ["Under 18", "18 and above"]
            },
            {
                "question": "How much is your screen time?",
                "options": ["0-2 hours", "2-5 hours", "5-7 hours", "7+ hours"]
            },
            {
                "question": "Do you feel technology affects your daily life?",
                "options": ["Yes","No"]
            },
            {
                "question": "Do you think you can/want to improve the amount of time you spend on your phone?",
                "options": ["Yes","No"]
            },
            {
                "question": "What are your technology addictions?",
                "options": ["Games","Social Media","Facetime","Online Shopping","Texting","Entertainment"]
            },
            {
                "question": "What apps/websites do you use the most?",
                "options": ["Snapchat","Messages","Facetime","Instagram","Facebook","Tiktok","Dating Apps","YouTube","Netflix","WhatsApp","Reddit","Twitter","Amazon","Discord","Spotify"]
                
            },
            
            
        ]

        self.answers = []

        # Create and display checkboxes
        self.create_checkboxes()

        #Load model
        self.load_model()
        
        # Submit button
        submit_button = tk.Button(self, text="Submit", command=self.submit_form)
        submit_button.pack(pady=10)

    def create_checkboxes(self):
        for question_data in self.questions:
            question_label = tk.Label(self, text=question_data["question"])
            question_label.pack(pady=5)

            options_frame = tk.Frame(self)
            options_frame.pack()

            question_answers = []
            for option in question_data["options"]:
                var = tk.BooleanVar()
                checkbox = tk.Checkbutton(options_frame, text=option, variable=var)
                checkbox.pack(side=tk.LEFT, padx=5)
                question_answers.append((option, var))

            self.answers.append(question_answers)
            
    def load_model(self):
        self.model = pickle.load(open("knn.pkl","rb"))
        
    

    def submit_form(self):
        # Display and populate the array with 1 for True and 0 for False
        result_array = []

        for i, question_data in enumerate(self.questions):
            print(f"{question_data['question']}:")
            for option, var in self.answers[i]:
                if var.get():
                    value = 1
                else:
                    value = 0
                print(f"    {option}: {value}")
                result_array.append(value)


        print("\nResult Array:")
        print(result_array)
        
        if result_array[0] == 1:
            array.append(0)
        else:
            array.append(1)
            
        if result_array[2] == 1:
            array.append(1)
        elif result_array[3] == 1:
            array.append(2)
        elif result_array[4] == 1:
            array.append(3)
        else:
            array.append(4)    
        
            
        if result_array[6] == 1:
            array.append(1)
        else:
            array.append(0)
            
        if result_array[8] == 1:
            array.append(1)
        else:
            array.append(0)
            
        for i in range(10,31):
            array.append(result_array[i])
            
        array_2d = [array]
        predictions = self.model.predict(array_2d)
        if predictions == 1:
            result = "You are Technologically Addicted"
        else:
            result = "You are not Technologically Addicted"
            
        # Create a new window to display the result
        result_window = tk.Toplevel(self)
        result_window.title("Result")

        # Display the result in the new window
        result_label = tk.Label(result_window, text="Result:")
        result_label.pack()

        prediction_label = tk.Label(result_window, text=result)
        prediction_label.pack()
        
        self.model = pickle.load('knn.pkl')
        
        


if __name__ == "__main__":
    app = CheckboxForm()
    app.mainloop()
    if os.getenv('HEADLESS', 'false').lower() == 'true':
        display.stop()
