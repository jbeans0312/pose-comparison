from util.move_comparison import compare_positions
import tkinter as tk
from tkinter import messagebox

exercise_dict = {
    'Kneeling Hip Flexor': 'exercise_videos/cornell_kneeling_hip_flexor.mp4',
    'Lat Stepdown': 'exercise_videos/cornell_lat_stepdown.mp4',
    'Standing Lunge': 'exercise_videos/cornell_standing_lunge.mp4',
    'Standing Quad': 'exercise_videos/cornell_standing_quad.mp4'
}

def on_option_selected():
    selected_option = option_var.get()
    if selected_option:
        # Call your function with the selected option
        benchmark_video = exercise_dict[selected_option]
        user_video = 0
        compare_positions(benchmark_video, user_video)
    else:
        messagebox.showwarning("Warning", "Please select an exercise!")

# Create the main window
root = tk.Tk()
root.title("Mr. Pose")
root.geometry('400x200')

# Create a list of options
options = ['Kneeling Hip Flexor', 'Lat Stepdown', 'Standing Lunge', 'Standing Quad']

# Create a variable to store the selected option
option_var = tk.StringVar()

# Create a label and a dropdown menu
label = tk.Label(root, text="Select an exercise:")
label.pack(pady=10)
option_menu = tk.OptionMenu(root, option_var, *options)
option_menu.pack(pady=10)
option_menu.config(width=20)
# Create a button to trigger the function
button = tk.Button(root, text="Begin exercise", command=on_option_selected)
button.pack(pady=10)

# Run the main loop
root.mainloop()
