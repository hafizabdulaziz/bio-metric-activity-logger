

import pandas as pd
import os
from datetime import datetime
import matplotlib.pyplot as plt

FILE_NAME = "running_log.csv"

def add_run():
    date = datetime.now().strftime("%Y-%m-%d")
    try:
        dist = float(input("Enter Distance Covered (km): "))
        mins = int(input("Enter Time Taken (minutes): "))
        feel = input("HGow Did You Feel? (Great/Normal/Tired): ")
        new_data = {
            "Date": [date],
            "Distance (km)": [dist],
            "Time (mins)": [mins],
            "Feel": [feel]
        }
        df = pd.DataFrame(new_data)
        if not os.path.isfile(FILE_NAME):
            df.to_csv(FILE_NAME, index=False)
        else:
            df.to_csv(FILE_NAME, mode='a', header=False, index=False)
        print("\n Run Recorded Successfully!")
    except ValueError:
        print("Error: Please Enter Numbers For Distance And Time.")

def show_graph():
    if os.path.exists(FILE_NAME):
        df = pd.read_csv(FILE_NAME)
        df['Date'] = pd.to_datetime(df['Date'])
        df = df.sort_values(by='Date')
        total_dist = round(df['Distance (km)'].sum(), 2)
        print(f"\n" + "="*40)
        print(f"AZIZ'S FITNESS SUMMARY")
        print(f"Total Distance Covered: {total_dist} km")
        print("="*40)
        plt.figure(figsize=(10, 5))
        plt.style.use('ggplot')
        plt.plot(df['Date'], df['Distance (km)'], marker='o', linestyle='-', color='#2ecc71', linewidth=2, markersize=8, label='Daily Progress')
        plt.gca().set_facecolor("#000000FF")
        plt.title('My Professional Running Tracker', fontsize=14, fontweight='bold')
        plt.xlabel('Date', fontsize=12)
        plt.ylabel('Distance Covered (km)', fontsize=12)
        plt.grid(True, linestyle='--', alpha=0.6)
        plt.legend()
        print("Opening Graph...")
        plt.show()
        print("\n Hope You Liked Your Progress Analysis.")
        print("Redirecting You To The Manu... [Press Any Key To Continue]")
    else:
        print("First Record A Run!")
    
if __name__ == "__main__":
    while True:
        print("\n--- RUNNING TRACKER PRO ---")
        print("1. Record New Run")
        print("2. Show Progress Graph")
        print("3. Exit")

        user_input = input("Enter Choice(1-3): ")

        try:
            choice = int(user_input)
            if choice == 1:
               add_run()
            elif choice == 2:
               show_graph()
               continue
            elif choice == 3:
               print("Keep Running! GoodBye.")
               break
            else:
                ("\n OOPS! Please Enter A Number Between 1 and 3 Only.")
        except ValueError:
            print(f"\n INVALID INPUT! '{user_input}' Is Not A Number.")
            

        