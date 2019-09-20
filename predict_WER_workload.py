#!/usr/bin/python
import sys
import pickle

filename = 'scaler_DRAM_model.sav'
scaler = pickle.load(open(filename, 'rb'))

filename = 'KNN_DRAM_model.sav'
clf_classes= pickle.load(open(filename, 'rb'))

nalyze_counters=["l3c0/read-miss/","r110","l3c0/write-need-replacement/","entropy","reuse_time"]

print "Input data"
print "-----------"
reads=float(sys.argv[1])
print "Rate of reads per clock "+str(reads)
reads=reads*1.0e+5

idle_cycles=float(sys.argv[2])
print "Rate of idle cycles "+str(idle_cycles)
idle_cycles=idle_cycles*1.0e+5

writes=float(sys.argv[3])
print "Rate of writes per clock "+str(writes)
writes=writes*1.0e+5

entropy=float(sys.argv[4])
print "Entropy "+str(entropy)

reuse_time=float(sys.argv[5])
print "The reuse time "+str(reuse_time)

refresh_period=float(sys.argv[6])
print "Refresh_period "+str(refresh_period)
refresh_period=refresh_period*1.0e+3

temperature=float(sys.argv[7])
print "Temperature "+str(temperature)

print "-----------"

X_test=[]
X_test.append(reads)
X_test.append(idle_cycles)
X_test.append(writes)
X_test.append(entropy)
X_test.append(reuse_time)
X_test.append(refresh_period)
X_test.append(temperature)


X_test_scale=scaler.transform([X_test])
print "WER " + str((float(clf_classes.predict(X_test_scale))/1.5e+9))
