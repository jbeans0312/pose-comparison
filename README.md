# Mr. Pose

Mr. Pose allows a user to compare their form to a professional's form during physical therapy exercises.

This prototype contains four exercises from Cornell's pysical therapy [database](https://health.cornell.edu/services/physical-therapy-massage/pt-exercise-videos).

This code is built off of a fork from [PrashantSaikia](https://github.com/PrashantSaikia) and has been updated to include the most recent libraries. The model requires a good amount of RAM to run locally, so we recommend running Mr. Pose on a system with at least 8-10 gb.

## Usage on local machine
1. Install and setup a Python3 environment on your machine, we recommend this [guide](https://realpython.com/installing-python/) from RealPython.
2. Download a copy of this repository to your machine using the following command, or install the .zip release featured on this page.
- `git clone https://github.com/jbeans0312/pose-comparison/`
4. Navigate to the `pose-comparison` folder using the `cd` command. If this is new to you, we recommend this [guide](https://www.digitalcitizen.life/command-prompt-how-use-basic-commands/) from DigitalCitizen.
5. Once in the `pose-comparison` folder, execute the following command to launch Mr. Pose.
- `python MrPose.py`
6. To begin, select an exercise and press the 'Begin Exercise' button. Once you are done, press 'Q' to return to the menu.

### Mr. Pose Menu
<img width="392" alt="Screenshot 2023-12-14 at 11 11 09 PM" src="https://github.com/jbeans0312/pose-comparison/assets/79337640/09b8e1c2-7e1b-405b-978c-f95052d7696d">

### Mr. Pose Posture Detection (Correct)
<img width="1239" alt="Screenshot 2023-12-14 at 11 16 06 PM" src="https://github.com/jbeans0312/pose-comparison/assets/79337640/66c7d158-7de1-4f54-8867-5b9b07d55008">

### Mr. Pose Posture Detection (Incorrect)
<img width="1239" alt="Screenshot 2023-12-14 at 11 21 20 PM" src="https://github.com/jbeans0312/pose-comparison/assets/79337640/ef4b17b7-2963-442f-80e2-f750e3cd42fa">
