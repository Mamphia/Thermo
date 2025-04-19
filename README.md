# 🔥 Thermo: Interactive Heat Transfer & Efficiency Visualizer

**Thermo** is a powerful, web-based simulation tool designed to bring heat transfer to life. It empowers engineers, students, and researchers to interactively model thermal behavior in 2D and visualize efficiency using physics-based methods and machine learning.

🌐 **Live App:** [thermo-app.onrender.com](https://thermo-app.onrender.com)

---

## 🚀 Why Thermo?
Understanding heat transfer is critical in engineering, but traditional equations and static diagrams often fall short. Thermo solves this by:

- 💡 Turning theory into interactive simulations
- 📊 Providing visual insights for thermal performance
- 🔬 Using real physics and ML to predict outcomes
- 🧠 Giving AI-driven suggestions to improve designs

---

## 🎯 Core Features

| Feature                        | Description                                                                 |
|-------------------------------|-----------------------------------------------------------------------------|
| 🔥 2D Thermal Simulation      | Finite Difference Method (FDM) for heat transfer on a customizable grid     |
| 📈 Visual Output              | Includes animated heatmaps, line profiles, and contour plots                |
| 🤖 ML-Based Efficiency Model | XGBoost-powered model predicts system efficiency                            |
| 💬 Engineering Insight        | App delivers tailored design suggestions based on predicted performance     |

---

## 🧠 How It Works

### 🔢 Inputs:
- **Length (m)**
- **Width (m)**
- **Flow Rate (kg/s)**
- **Thermal Diffusivity (alpha)**

### ⚙️ Simulation Parameters:
- Grid size: `50x50` (or optimized to `30x30`)
- Time steps: `100`
- dt = `0.01` seconds
- Initial temperature: `20°C`
- Left boundary heat source: `100°C`

### 🔄 Process:
1. Simulate 2D heat propagation using FDM
2. Track temperature across all time steps
3. Visualize final and intermediate results
4. Predict efficiency using a trained ML model
5. Deliver customized design feedback

---

## 🖼️ Visual Outputs

| Heatmap                       | Animation                        | Line Profile                      | Contour Plot                     |
|------------------------------|-----------------------------------|-----------------------------------|----------------------------------|
| Final temperature distribution | Dynamic heat flow over time       | 1D temperature cut through center | Contour zones of heat intensity  |

---

## 🧰 Tech Stack

**Backend**  | Python, Flask, Gunicorn  
**ML**       | XGBoost, Scikit-learn, Joblib  
**Simulation** | NumPy (Finite Difference)  
**Visualization** | Matplotlib, Pillow (GIFs)  
**Frontend** | HTML, Bootstrap 5, Jinja2  
**Hosting**  | Render (Free Tier)

---

## 📦 Directory Overview

```
thermo-app/
├── static/plots/              # Auto-generated plots & animations
├── templates/index.html       # UI layout (Bootstrap + Jinja2)
├── main.py                    # Flask app logic
├── simulation.py              # 2D FDM thermal model
├── model.py                   # ML model prediction logic
├── utils.py                   # Plot generation helpers
├── requirements.txt
└── README.md
```

---

## ⚡ Quick Start (Local)

```bash
# Clone repo and navigate to app folder
$ git clone https://github.com/Mamphia/Thermo.git
$ cd Thermo/thermo-app

# Create and activate virtual environment
$ python -m venv venv
$ source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
$ pip install -r requirements.txt

# Run the app
$ python main.py

# Access the app at:
http://localhost:81
```

---

## 🌍 Deployment (Render)

- **Root Directory:** `thermo-app`
- **Start Command:** `gunicorn main:app`
- **Auto Deploy:** Enabled on `main` branch push

✅ Live: [thermo-app.onrender.com](https://thermo-app.onrender.com)

---

## 🧠 Built-in Engineering Feedback

| Efficiency (%) | Feedback                                                                 |
|----------------|--------------------------------------------------------------------------|
| < 60           | ⚠️ Low efficiency — Try increasing flow rate or using better materials  |
| 60 - 85        | ⚙️ Moderate — Consider optimizing geometry or tuning thermal properties |
| ≥ 85           | ✅ Excellent — System is operating near optimal performance             |

---

## 👨‍🔬 Author

**Mamphia**  
Physics | Mechanical Engineering | Data Science  
[GitHub](https://github.com/Mamphia) | [LinkedIn](https://www.linkedin.com/in/mamadu-jalloh-bb650a349/)

---

### ⭐ Like the project? Give it a star and share it with others!
