# 🧗‍♂️ MoonBoard 2016 Route Recommender & Generator (WIP)

A personalized training companion for the MoonBoard 2016 setup — combining machine learning, custom route filtering, and future Bluetooth LED integration.

---

## 🚀 Project Overview

This project started as a modification of [Alessandro Avi's dataset extractor](https://github.com/AlessandroAvi/Moonboard_Dataset), and has grown into a full-stack app that helps climbers:

- 🔍 Find problems that match their preferred holds and difficulty
- 🧠 Use ML to recommend routes based on real MoonBoard data
- 🧪 (Coming soon) Generate entirely new climbs based on learned patterns
- 📱 Build an intuitive interface for mobile or web interaction
- 🔗 (Planned) Control the MoonBoard LEDs via Bluetooth

---

## 🧠 Machine Learning Highlights

- Cleaned and structured 1,200+ MoonBoard problems from JSON
- Extracted start, middle, and end holds to build per-route vectors
- Created one-hot encoded binary matrices for route representation
- Built a cosine similarity–based recommender system to return top 5 routes based on user-selected holds and grade
- Enabled grade filtering and style-aware problem matching

---

## 💡 Key Features (so far)

| Feature              | Status     |
|----------------------|------------|
| 🧹 Dataset cleaned & parsed        | ✅ Complete |
| 🧠 ML route recommender            | 🔄 In progress |
| 🎛️ Grade + hold filters           | ✅ Complete |
| 🧗 Route generator (WIP)          | 🔄 In progress |
| 📱 Flutter frontend                | 🔄 Planned |
| 📡 Bluetooth LED integration       | 🔄 Planned |

---

## 🛠️ Getting Started

Clone the repo and open the main Jupyter notebook:

```bash
git clone https://github.com/Daami30330/MoonBoardRecommender.git
cd MoonBoardRecommender


Install dependencies:

pip install -r requirements.txt
Open moonboard_analysis.ipynb to explore the dataset and test the recommender.

📁 Example Output

{
  "Name": "TIRITI",
  "Grade": "6C",
  "StartHolds": ["1J"],
  "EndHolds": ["16F"],
  "MiddleHolds": ["6H", "2G", "10B", "7G"]
}

✍️ Author
Imaad Fahimuddin
CS Grad • Climber • Builder of cool tools that make training better.

🙏 Acknowledgments
This project extends the work of:

Alessandro Avi's MoonBoard dataset scraper

📝 License
This project is for educational and personal use only. Please respect MoonBoard’s content ownership and usage guidelines.