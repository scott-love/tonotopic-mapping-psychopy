# tonotopic-mapping-psychopy
This code can be used with [PsychoPy](https://www.psychopy.org).

The design of these experiments was heavily based on 
two papers by Langers and colleagues (2014, [1](https://linkinghub.elsevier.com/retrieve/pii/S1053811914006272); [2](https://linkinghub.elsevier.com/retrieve/pii/S1053811914006259))

All experiments presented were designed to be triggered by the MRI scanner. In our context, this requires waiting for a keyboard “s” before starting. This “s” is triggered by the onset of the first fMRI volume acquisition. 

The file **Broadband_tonotopy.psyexp** presents pure tone beeps of different frequencies in either “low” or “high” frequency blocks. A single beep has a duration of 75 ms and it is preceded by 25 ms of silence, so 100 ms total. Within a block, 88 of these 100 ms events (beep + silence) are presented for a total block duration of 8.8 seconds. After each block of beeps there is a 8.8 second block of silence. The order of low and high blocks is randomised for each presentation - The order of 1 repetition of a low and a high block is chosen randomly (e.g., low, silence, high silence) then the order of the second repetition is randomised (e.g., high, silence, low silence) and so on for the total number of repetitions (8). The definition of “low” and “high” frequencies follows that of Langers and colleagues ([2014](https://linkinghub.elsevier.com/retrieve/pii/S1053811914006272))

The file **broadband_tonotopy_abs.psyexp** is the same as Broadband_tonotopy.psyexp except that there is only a silence block after each pair of low and high blocks : low, high silence, low, high, silence. Again the order of low and high blocks is randomised.

This code was created by Camille Pluchot & Scott Love as part of the [SheepVoicefMRI project](https://anr.fr/Project-ANR-20-CE20-0001) funded by the ANR (ANR-20-CE20-0001).
