--------------------------------------------------
DFault v.0.1.
--------------------------------------------------
DFault is a Workload-Aware DRAM Error Prediction Framework.

--------------------------------------------------
Description
--------------------------------------------------
The framework uses a ML model (KNN, K-Nearest Neighbors Algorithm
) to predict the rate of single bit errors per 64-bit word (WER) and the probability to obtain an Uncorrectable Error (when > 2 bits are corrupted in a 64-bit word). The model is trained using the results of 6-month DRAM error characterization campaign under varying DRAM voltage, refresh rate and temperature.

The detailed description of the tool is provided in the following paper:

--------------------
How to run?:
--------------------
 ...

--------------------
Acknowledgement:
--------------------
This work is funded by the H2020 Framework Program of the
European Union through the UniServer Project (Grant Agreement
688540) – http://www.uniserver2020.eu.
