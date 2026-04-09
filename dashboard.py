import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox
import main

fig, ax = plt.subplots(figsize=(10, 7))
plt.subplots_adjust(top=0.85, bottom=0.15)

def plot_logic(company):
    ax.cla()
    company = company.upper()

    data = main.spot_absorption(company)

    ax.scatter(data["range_pct"], data["z_score"], alpha=0.5, color='gray', label='Normal Days')

    whale_threshold_z = 2.0
    tight_range_threshold = data["range_pct"].median()
    whales = data[(data["z_score"] > whale_threshold_z) & (data["range_pct"] < tight_range_threshold)]
    ax.scatter(whales["range_pct"], whales["z_score"], color='blue', s=100, edgecolors='black', label='Potential Whale')

    ax.axhline(whale_threshold_z, color="red", linestyle="--", alpha=0.6, label="High Volume Trigger")
    ax.set_xlabel("Daily Range % (The 'Result')")
    ax.set_ylabel("Volume Z-Score (The 'Effort')")
    ax.set_title(f"Whale Radar: {company}", pad=20)
    ax.grid(True, linestyle="--", alpha=0.3)

    ax.legend()
    fig.canvas.draw_idle()

plot_logic("AAPL")

axbox = plt.axes([0.3, 0.93, 0.4, 0.05])
text_box = TextBox(axbox, "Search Ticker: ", initial="AAPL")
text_box.on_submit(plot_logic)

plt.show()