from scipy.optimize import curve_fit
import numpy as np

def fit_gaussian(curve):
    try:
        def gaussian(x, mean):
            amplitude = np.max(curve)
            stddev = np.std(curve)
            return amplitude * np.exp(-((x - mean) / stddev) ** 2)

        x_data = np.arange(curve.size)
        y_data = np.asarray(curve)
        popt, _ = curve_fit(gaussian, x_data, y_data, p0=(np.mean(x_data),), absolute_sigma=True, maxfev=1000)
        return popt[0]
    except:
        return None