from flask import Flask, render_template, request
from simulation import run_simulation
from model import predict_efficiency
from utils import (
    save_temperature_plot,
    save_animation,
    save_line_profile,
    save_contour_plot
)

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    try:
        if request.method == "POST":
            length = float(request.form["length"])
            width = float(request.form["width"])
            flow_rate = float(request.form["flow_rate"])
            alpha = float(request.form["alpha"])

            # Run simulation (return final + time series)
            temp_matrix, temp_record = run_simulation(length, width, flow_rate, alpha)
            efficiency = predict_efficiency(length, width, flow_rate, alpha)

            # Save all plots
            plot_path = save_temperature_plot(temp_matrix)
            anim_path = save_animation(temp_record)
            line_path = save_line_profile(temp_matrix)
            contour_path = save_contour_plot(temp_matrix)

            # Dynamic engineering insight
            if efficiency < 60:
                insight = "⚠️ Efficiency is low — consider increasing the flow rate or using a more thermally conductive material."
            elif 60 <= efficiency < 85:
                insight = "⚙️ Moderate performance — consider fine-tuning material properties or geometry."
            else:
                insight = "✅ Excellent performance — your system is operating near optimal thermal efficiency."

            result = {
                "efficiency": round(efficiency, 2),
                "plot": plot_path,
                "anim": anim_path,
                "line": line_path,
                "contour": contour_path,
                "insight": insight
            }

    except Exception as e:
        print("🔥 INTERNAL ERROR:", e)

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=81)