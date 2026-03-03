import matplotlib.pyplot as plt
import numpy as np
from astropy.io import fits
from astropy.table import Table

from nicer_data_prep import get_evt_data


# Helper functions to plot phase-o-grams
def make_phaseogram(evt_data, nbins=100):
    phases = evt_data["PHASE"]
    phase_o_gram, bin_edges = np.histogram(phases, bins=nbins)
    return phase_o_gram


def normalize_phaseogram(phase_o_gram, norm="std", exposure=None, nbins=100):
    mean = np.mean(phase_o_gram)
    std = np.std(phase_o_gram)

    if norm == "std":
        cal = 1.0
    elif norm == "counts per second" and exposure is not None:
        cal = 100.0 / exposure
    elif norm == "seconds" and exposure is not None:
        cal = 100 * np.sum(phase_o_gram) / exposure
    else:
        raise ValueError(
            "Invalid normalization method or missing exposure time."
        )

    normalized_phase_o_gram = (phase_o_gram - mean) / (std * cal)
    return normalized_phase_o_gram


def plot_phaseogram(phase_o_gram, obsid_str):
    # plt.figure(figsize=(2,2))
    plt.plot(phase_o_gram, drawstyle="steps-mid", color="black")
    # plt.ylim(-2, max(phase_o_gram)*1.1)
    plt.xlabel("Pulse Phase")
    plt.ylabel("Counts")
    plt.title(f"Phase-o-gram for Observation {obsid_str}")
    plt.show()
    return


def combine_phaseograms(obsids, column="PHASE"):
    # Combine multiple obsids into a single phase-o-gram (the pulse profile)
    combined_counts = np.zeros(100)
    for obsid in obsids:
        evt_data = get_evt_data(obsid, post_fix="_barycorr_PHASE")
        phase_o_gram = np.histogram(evt_data[column], bins=100)[0]
        combined_counts = np.add(combined_counts, phase_o_gram)
    return combined_counts


# Helper functions for reading FITS headers
def get_mission_time(obsid):
    event_filename = f"/Users/jacobpayne/Projects/Astronomyprojects/nicer_obs/{obsid}/xti/event_cl/ni{obsid}_0mpu7_cl_barycorr_PHASE.evt"
    hdu_list = fits.open(event_filename, memmap=True)
    evt_data = Table(hdu_list[1].data)
    return evt_data["TIME"][0]


def get_mission_end_time(obsid):
    event_filename = f"/Users/jacobpayne/Projects/Astronomyprojects/nicer_obs/{obsid}/xti/event_cl/ni{obsid}_0mpu7_cl_barycorr_PHASE.evt"
    hdu_list = fits.open(event_filename, memmap=True)
    evt_data = Table(hdu_list[1].data)
    return evt_data["TIME"][-1]


def get_obsid_exposure_time(obsid):
    event_filename = f"/Users/jacobpayne/Projects/Astronomyprojects/nicer_obs/{obsid}/xti/event_cl/ni{obsid}_0mpu7_cl_barycorr_PHASE.evt"
    hdu_list = fits.open(event_filename, memmap=True)
    exposure_time = hdu_list[1].header["EXPOSURE"]
    return exposure_time


def get_obs_interval_time(obsid):
    event_filename = f"/Users/jacobpayne/Projects/Astronomyprojects/nicer_obs/{obsid}/xti/event_cl/ni{obsid}_0mpu7_cl_barycorr_PHASE.evt"
    hdu_list = fits.open(event_filename, memmap=True)
    # datetime object in the format 2017-09-16T00:34:19
    start = np.datetime64(hdu_list[1].header["DATE-OBS"], "s")
    end = np.datetime64(hdu_list[0].header["DATE-END"], "s")
    interval_time = end - start
    return interval_time
