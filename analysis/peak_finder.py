# Author: Marie-Aline Martin
# Edited: Jasmine Oliveira
# Date: 06/16/16

import numpy as np
from math import ceil


def smooth(s_list, n):
    """
    Smooths list by 2*n points
    :param s_list:
    :param n: 1D list of points
    :return: 1D List of smoothed points
    """
    s_smooth = list(s_list)
    for i in range(n, len(s_list) - n):
        s_smooth[i] = np.mean(s_list[i - n:i + n])
    return s_smooth


def peak_finder(s_freq_list, s_int_list, s_autoclean):
    """
     Finds Peaks in 2D data
        (1) Finds and Removes Noise level
        (2) Smooths Functions
        (3) Determines Peaks
    :param s_freq_list: Frequency List (x)
    :param s_int_list: Intensity List (y)
    :param s_autoclean: AutoClean Integer
    :return: Frequency Peak List, Intensity Peak List
    """

    # (1) Find Noise Level
    n_split = 10
    part_len = len(s_freq_list) // n_split
    noise_list = []

    # Append the noise list for each portion
    for i in range(n_split):
        # define the noise as a function of the median times the median
        # this value can be decreased to peak up more weak lines
        if s_autoclean == 0:
            noise = 3.5 * np.median(s_int_list[i * part_len:(i + 1) * part_len])
        else:
            noise = 5 * np.median(s_int_list[i * part_len:(i + 1) * part_len])
        for j in range(i * part_len, (i + 1) * part_len):
            noise_list.append(noise)

    # Complete the noise list so that it has the same length as the frequency list
    for i in range(len(s_freq_list) % n_split):
        noise_list.append(noise)

    # ---------------------------------------------------
    # SMOOTH FUNCTIONs
    # ---------------------------------------------------
    n = int(ceil(len(s_int_list)))
    int_smooth1 = smooth(s_int_list, (n / 500))
    int_smooth2 = smooth(s_int_list, (n / 10000))
    int_smooth3 = smooth(s_int_list, (n / 20000))

    # ---------------------------------------------------
    # PEAK DETECTION
    # ---------------------------------------------------

    peak_int_list = []
    peak_freq_list = []

    ## everything relative to smooth_list can be un-commented to plot the resulting smoothed curve
    # smooth_list = []

    # lower_limit and peak_int_fig are used for the purpose of clarity on the plot only
    lower_limit = 0.2
    peak_int_fig = []

    # The peaks are defined as:
    # - the local maximum of 4 points
    # - an intensity higher than the noise detection limit
    # - an intensity higher that the average of the 3 smooth *2 (purely empirical)
    # That last point is very important and allows to limit the number of peaks,
    # in particular on the shoulder of very intense lines, where local maxima on the noise can be above the intensity threshold (large number of points smoothing)
    # It also allows to not peak very broad features that can't be molecular lines

    for i in range(2, len(s_int_list) - 2):
        if (s_int_list[i - 2] < s_int_list[i - 1] < s_int_list[i] > s_int_list[i + 1] or s_int_list[i - 1] < s_int_list[
            i] > s_int_list[i + 1] > s_int_list[i + 2]) \
                and s_int_list[i] > noise_list[i] \
                and s_int_list[i] > (int_smooth1[i] + int_smooth2[i] + int_smooth3[i]) / 1.5 \
                and 6000 < s_freq_list[i] < 19000:
            peak_int_list.append(s_int_list[i])
            peak_int_fig.append(s_int_list[i] + lower_limit)
            peak_freq_list.append(s_freq_list[i])

    return peak_freq_list, peak_int_list