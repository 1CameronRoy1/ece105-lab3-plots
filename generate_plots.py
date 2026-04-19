"""Generate publication-quality sensor data visualizations.

This script creates synthetic temperature sensor data using NumPy
and produces scatter, histogram, and box plot visualizations saved
as PNG files.

Usage
-----
    python generate_plots.py
"""
# Create a function generate_data(seed) that returns sensor_a, sensor_b,
# and timestamps arrays with the same parameters as in the notebook.
# Use NumPy-style docstring with Parameters and Returns sections.

import numpy as np


def generate_data(seed):
    """Generate simulated sensor readings and timestamps.

    Parameters
    ----------
    seed : int
        Seed for ``np.random.default_rng`` to make output reproducible.

    Returns
    -------
    sensor_a : numpy.ndarray
        Array of shape ``(200,)`` with Sensor A temperatures in degrees C,
        drawn from a normal distribution with ``loc=25.0`` and ``scale=3.0``.
    sensor_b : numpy.ndarray
        Array of shape ``(200,)`` with Sensor B temperatures in degrees C,
        drawn from a normal distribution with ``loc=27.0`` and ``scale=4.5``.
    timestamps : numpy.ndarray
        Array of shape ``(200,)`` with timestamps in seconds, drawn from a
        uniform distribution over ``[0.0, 10.0)``.
    """
    rng = np.random.default_rng(seed=seed)

    sensor_a = rng.normal(loc=25.0, scale=3.0, size=200)
    sensor_b = rng.normal(loc=27.0, scale=4.5, size=200)
    timestamps = rng.uniform(low=0.0, high=10.0, size=200)

    return sensor_a, sensor_b, timestamps

# Create plot_scatter(sensor_a, sensor_b, timestamps, ax) that draws
# the scatter plot from the notebook onto the given Axes object.
# NumPy-style docstring. Modifies ax in place, returns None.


def plot_scatter(sensor_a, sensor_b, timestamps, ax):
    """Plot sensor temperature readings versus time on an existing Axes.

    Parameters
    ----------
    sensor_a : numpy.ndarray
        Sensor A temperature readings of shape ``(200,)``.
    sensor_b : numpy.ndarray
        Sensor B temperature readings of shape ``(200,)``.
    timestamps : numpy.ndarray
        Timestamp values in seconds of shape ``(200,)``.
    ax : matplotlib.axes.Axes
        Axes object to draw the scatter plot on. The plot is added in place.

    Returns
    -------
    None
        This function modifies ``ax`` in place and does not return a value.
    """
    ax.scatter(timestamps, sensor_a, s=22, alpha=0.7, label="Sensor A")
    ax.scatter(timestamps, sensor_b, s=22, alpha=0.7, label="Sensor B")
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Temperature (C)")
    ax.set_title("Sensor Temperatures vs Time")
    ax.legend()
    ax.grid(alpha=0.3)

# Create plot_histogram(sensor_a, sensor_b, ax) that draws
# histograms of the sensor temperature data on the given Axes object.
# NumPy-style docstring. Modifies ax in place, returns None.


def plot_histogram(sensor_a, sensor_b, ax):
    """Plot overlaid histograms of sensor temperature distributions.

    Parameters
    ----------
    sensor_a : numpy.ndarray
        Sensor A temperature readings of shape ``(200,)``.
    sensor_b : numpy.ndarray
        Sensor B temperature readings of shape ``(200,)``.
    ax : matplotlib.axes.Axes
        Axes object to draw the histogram plot on. The plot is added in place.

    Returns
    -------
    None
        This function modifies ``ax`` in place and does not return a value.
    """
    mean_a = np.mean(sensor_a)
    mean_b = np.mean(sensor_b)

    ax.hist(sensor_a, bins=30, alpha=0.5, label="Sensor A", color="tab:blue")
    ax.hist(sensor_b, bins=30, alpha=0.5, label="Sensor B", color="tab:orange")
    ax.axvline(
        mean_a,
        color="tab:blue",
        linestyle="--",
        linewidth=2,
        label=f"Sensor A Mean: {mean_a:.2f} C",
    )
    ax.axvline(
        mean_b,
        color="tab:orange",
        linestyle="--",
        linewidth=2,
        label=f"Sensor B Mean: {mean_b:.2f} C",
    )
    ax.set_xlabel("Temperature (C)")
    ax.set_ylabel("Count")
    ax.set_title("Temperature Distribution: Sensor A vs Sensor B")
    ax.legend()
    ax.grid(alpha=0.3)

# Create plot_boxplot(sensor_a, sensor_b, ax) that draws
# box plots of the sensor temperature data on the given Axes object.
# NumPy-style docstring. Modifies ax in place, returns None.


def plot_boxplot(sensor_a, sensor_b, ax):
    """Plot side-by-side box plots of sensor temperature distributions.

    Parameters
    ----------
    sensor_a : numpy.ndarray
        Sensor A temperature readings of shape ``(200,)``.
    sensor_b : numpy.ndarray
        Sensor B temperature readings of shape ``(200,)``.
    ax : matplotlib.axes.Axes
        Axes object to draw the box plot on. The plot is added in place.

    Returns
    -------
    None
        This function modifies ``ax`` in place and does not return a value.
    """
    overall_mean = np.mean(np.concatenate([sensor_a, sensor_b]))

    ax.boxplot([sensor_a, sensor_b], labels=["Sensor A", "Sensor B"])
    ax.set_ylabel("Temperature (deg C)")
    ax.set_title("Sensor Temperature Distributions (Box Plot)")
    ax.axhline(
        overall_mean,
        color="gray",
        linestyle="--",
        linewidth=2,
        label=f"Overall Mean: {overall_mean:.2f} deg C",
    )
    ax.legend()
    ax.grid(axis="y", alpha=0.3)
