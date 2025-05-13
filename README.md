# 🧗‍♂️ MoonBoard 2016 Route Companion (WIP)

This project is a customized version of [Alessandro Avi's MoonBoard dataset extractor](https://github.com/AlessandroAvi/Moonboard_Dataset), adapted and extended for my own personal project: building a MoonBoard 2016 route companion app that improves route selection, filtering, and Bluetooth LED control.

---

## 🚀 What I'm Building

I'm using this codebase to:
- 🧠 Build a filtered dataset of MoonBoard problems by grade, hold color, and more
- 🤖 Experiment with route prediction using input holds
- 📱 Lay the groundwork for a custom mobile/web app that connects to my gym's 2016 MoonBoard
- 🔗 Eventually interface with Bluetooth to control the LED wall directly (future goal)

---

## 🔍 What This Code Does (as of now)

This repo uses **OpenCV and OCR** to:
- Read MoonBoard problems from screenshots (taken via Android emulator)
- Detect red, green, and blue holds by color masks
- Use circle detection to find the holds' (x, y) coordinates
- Match those to the MoonBoard grid
- Extract problem name and grade
- Store all info in a JSON file

---

## 🛠️ Setup Instructions

1. 📲 Install an Android emulator (e.g. BlueStacks)
2. 🧱 Open the MoonBoard app inside the emulator
3. 🖥️ Adjust screen region settings in the script to fit your monitor
4. 🎯 Run the script to scrape problems and create your local dataset

You can tweak detection settings, crop areas, number of problems, etc.

---

## 📁 Output Example

⚒️ Current Status
✅ Dataset scraping works

🔄 Working on integrating route filtering + ML predictions

📡 Bluetooth support planned (MoonBoard 2016 only)

🙏 Credit
This repo builds on code from:

Alessandro Avi's MoonBoard Dataset Scraper
Massive credit for the OpenCV + OCR pipeline idea and implementation.

✍️ Author
Imaad Fahimuddin
Climber + dev exploring route generation and LED control for MoonBoard 2016 setups.

📝 License
This repo is for educational and personal use only.
Please respect MoonBoard’s original data restrictions.

The script saves a JSON file that looks like:

```json
{
  "problem_id": 1,
  "name": "Benchpress",
  "grade": "6C",
  "holds": [
    { "position": "G5", "type": "start" },
    { "position": "E7", "type": "middle" },
    { "position": "D9", "type": "top" }
  ],
  "benchmark": true
}

⚒️ Current Status
✅ Dataset scraping works

🔄 Working on integrating route filtering + ML predictions

📡 Bluetooth support planned (MoonBoard 2016 only)

🙏 Credit
This repo builds on code from:

Alessandro Avi's MoonBoard Dataset Scraper
Massive credit for the OpenCV + OCR pipeline idea and implementation.

✍️ Author
Imaad Fahimuddin
Climber + dev exploring route generation and LED control for MoonBoard 2016 setups.

📝 License
This repo is for educational and personal use only.
Please respect MoonBoard’s original data restrictions.

