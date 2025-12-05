import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# ---- Data ----
labels = [
    "0 - 9", "10 - 19", "20 - 29", "30 - 39", "40 - 49",
    "50 - 59", "60 - 69", "70 - 79", "80 - 89", "90 - 100"
]
values = [2, 0, 0, 2, 5, 10, 25, 15, 6, 5]

# ---- Midpoints (for KPI calculations) ----
midpoints = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]


# ---- KPI Calculations ----
total = sum(values)
weighted_mean = sum(v * m for v, m in zip(values, midpoints)) / total
weighted_median = np.interp(0.5 * total, np.cumsum(values), midpoints)
peak_range = labels[np.argmax(values)]
peak_value = max(values)

# Find lowest and highest non-zero score ranges (and student counts)
non_zero_indices = [i for i, v in enumerate(values) if v > 0]

if non_zero_indices:
    lowest_index = non_zero_indices[0]
    highest_index = non_zero_indices[-1]
    lowest_range = labels[lowest_index]
    lowest_value = values[lowest_index]
    highest_range = labels[highest_index]
    highest_value = values[highest_index]
else:
    lowest_range = highest_range = "N/A"
    lowest_value = highest_value = 0

# ---- Streamlit Layout ----
st.title("Exam 1 statistics")


# KPI cards (two rows)
col1, col2, col3 = st.columns(3)
col1.metric("Average Score", f"{weighted_mean:.1f}")
col2.metric("Median Score", f"{weighted_median:.1f}")
col3.metric("Most Common Range", peak_range, delta=f"{peak_value} students")

col4, col5 = st.columns(2)
col4.metric("Lowest Score Range", lowest_range, delta=f"{lowest_value} students")
col5.metric("Highest Score Range", highest_range, delta=f"{highest_value} students")

# ---- Histogram ----
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(labels, values, color='teal', edgecolor='black', alpha=0.8)
ax.set_xlabel("Score Range")
ax.set_ylabel("Number of Students")
ax.set_title("Exam1 Score Distribution")
ax.grid(axis='y', linestyle='--', alpha=0.6)
plt.xticks(rotation=45, ha='right')
st.pyplot(fig)



