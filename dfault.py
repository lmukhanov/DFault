#!/usr/bin/python
import sys
import pickle

def dfault_wer_predict_short():
  filename = 'scaler_DRAM_model_WER_short.sav'
  scaler = pickle.load(open(filename, 'rb'))

  filename = 'KNN_DRAM_model_WER_short.sav'
  clf_classes= pickle.load(open(filename, 'rb'))

  print "Predict WER"
  print "Input data"
  print "-----------"
  reads=float(sys.argv[2])

  print "Rate of reads per clock "+str(reads)
  reads=reads*1.0e+5

  writes=float(sys.argv[3])
  print "Rate of writes per clock "+str(writes)
  writes=writes*1.0e+5

  refresh_period=float(sys.argv[4])
  print "Refresh_period "+str(refresh_period)
  refresh_period=refresh_period*1.0e+3

  temperature=float(sys.argv[5])
  print "Temperature "+str(temperature)
  temperature=temperature+3.0

  print "-----------"

  X_test=[]
  vec=[]
  vec.append(reads)
  vec.append(writes)
  vec.append(refresh_period)
  vec.append(temperature)


  X_test.append(vec)
  X_test_scale=scaler.transform(X_test)
  print X_test
  print "-----------"
  print "WER " + str((float(clf_classes.predict(X_test_scale))/1.5e+9))

def dfault_wer_predict():
  filename = 'scaler_DRAM_model_WER_full.sav'
  scaler = pickle.load(open(filename, 'rb'))

  filename = 'KNN_DRAM_model_WER_full.sav'
  clf_classes= pickle.load(open(filename, 'rb'))

  print "Predict WER"
  print "Input data"
  print "-----------"
  reads=float(sys.argv[2])

  print "Rate of reads per clock "+str(reads)
  reads=reads*1.0e+5

  idle_cycles=float(sys.argv[3])
  print "Rate of idle cycles "+str(idle_cycles)
  idle_cycles=idle_cycles*1.0e+5

  writes=float(sys.argv[4])
  print "Rate of writes per clock "+str(writes)
  writes=writes*1.0e+5

  entropy=float(sys.argv[5])
  print "Entropy "+str(entropy)

  reuse_time=float(sys.argv[6])
  print "The reuse time "+str(reuse_time)

  refresh_period=float(sys.argv[7])
  print "Refresh_period "+str(refresh_period)
  refresh_period=refresh_period*1.0e+3

  temperature=float(sys.argv[8])
  print "Temperature "+str(temperature)
  temperature=temperature+3.0

  print "-----------"

  X_test=[]
  vec=[]
  vec.append(reads)
  vec.append(idle_cycles)
  vec.append(writes)
  vec.append(entropy)
  vec.append(reuse_time)
  vec.append(refresh_period)
  vec.append(temperature)


  X_test.append(vec)
  X_test_scale=scaler.transform(X_test)
  print X_test
  print "-----------"
  print "WER " + str((float(clf_classes.predict(X_test_scale))/1.5e+9))

def dfault_intput_parameters():
  print "DFault is Workload-Aware DRAM Error Prediction Framework."
  print "Dfault implements an ML model (KNN) that has been trained using the results of a 3-month DRAM error characterization campaign on an ARMv8 server (Xgene-2) under varying voltage, refresh rate and temperature. For the characterization, we used four DDR3 8GB DIMMs (MT18JSF1G72AZ-1G9) operating at 1866 MHz were used."
  print "\nHow to use the predictor?"
  print "---------------"
  print "1.    WER - the rate of single-bit errors. To estimate WER run dfault.py with the following parameters:"
  print "i)    WER"
  print "ii)   Rate of reads per clock"
  print "iii)  Rate of idle cycles"
  print "iv)   Rate of writes per clock"
  print "v)    Entropy"
  print "vi)   The reuse time"
  print "vii)  Refresh preiod"
  print "viii) The DRAM temperature"
  print "\nExample "
  print "./dfault.py WER 0.004406 0.00125 0.0009 15 3.0 1.783 60"
  print "\n"
  print "---------------"
  print "1a.    WER - the rate of single-bit errors. If the reuse time, entropy, idle cycles are not available, then WER can be estimated the following parameters:"
  print "i)     WER"
  print "ii)    Rate of reads per clock"
  print "iii)   Rate of writes per clock"
  print "iv)    Refresh preiod"
  print "v)     The DRAM temperature"
  print "Note that the WER predictions with this set of program features are less accurate than the WER predictions obtained for the first set of program features."
  print "\nExample "
  print "./dfault.py WER 0.004406 0.0009 1.783 60"
  print "\n"
  print "---------------"
  print "2.    PUE - the rate of single-bit errors. To estimate WER run dfault.py with the following parameters:"
  print "i)    PUE"
  print "ii)   Rate of reads per clock"
  print "iii)  Rate of idle cycles"
  print "iv)   Rate of writes per clock"
  print "vii)  Refresh preiod"
  print "viii) The DRAM temperature"
  sys.exit()

print "------------"
print "DFault v.1.0"
print "------------"

if len(sys.argv) <= 1:
  dfault_intput_parameters()
else:
  if (sys.argv[1] == "WER"):
     if len(sys.argv) == 9:
        dfault_wer_predict()
     elif len(sys.argv) == 6:
        dfault_wer_predict_short()
     else:
        dfault_intput_parameters()
