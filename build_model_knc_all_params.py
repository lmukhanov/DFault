#!/usr/bin/python
import sys
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from matplotlib import cm
import itertools
import os 
from matplotlib import cm
from scipy.interpolate import pchip
import matplotlib.colors as colors

import matplotlib as mpl

from scipy.interpolate import pchip
import matplotlib.ticker as ticker
from scipy.interpolate import spline
import scipy as sp
import scipy.stats
from sklearn import svm
import math
from sklearn import linear_model
from math import log
from math import exp
from sklearn.neighbors.nearest_centroid import NearestCentroid
from sklearn.neighbors import RadiusNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier
import pickle

STEP=10

x = np.arange(10)
ys = [i+x+(i*x)**2 for i in range(10)]
color_custom = cm.rainbow(np.linspace(0, 1, len(ys)))
labeltypes = ['o', 'v', '^', '<', '>', '8', 's', 'p', '*', 'h', 'H', 'D', 'd', 'P', 'X']

font = {'family' : 'normal',
        'weight' : 'normal',
        'size'   : 12}

bench_list=["backprop","backprop(8)","kmeans","kmeans(8)","nw","nw(8)","srad","srad(8)","memcached","fmm","fmm(8)","pagerank","bfs","bc","lulesh(8)"]

perf_counters_list=["cycles","instructions","branch-misses","cache-misses","cache-references","cpu-cycles","instructions","alignment-faults","context-switches","cpu-migrations","dummy","emulation-faults","major-faults","minor-faults","page-faults","cpu-clock","task-clock","L1-dcache-loads","L1-dcache-store-misses","L1-dcache-stores","branch-load-misses","branch-loads","iob0/axi0-read-partial/","iob0/axi0-read/","iob0/axi0-write-partial/","iob0/axi0-write/","iob0/axi1-read-partial/","iob0/axi1-read/","iob0/axi1-write-partial/","iob0/axi1-write/","iob0/csw-inbound-dirty/","iob0/csw-read-block/","iob0/csw-read-partial/","iob0/cycle-count-div-64/","iob0/cycle-count/","l3c0/ackq-full/","l3c0/bank-conflict-fifo-issue/","l3c0/bank-fifo-full/","l3c0/bank-fifo-issue/","l3c0/cycle-count-div-64/","l3c0/cycle-count/","l3c0/odb-full/","l3c0/read-hit/","l3c0/read-miss/","l3c0/tq-full/","l3c0/wbq-full/","l3c0/wdb-full/","l3c0/write-need-replacement/","l3c0/write-not-need-replacement/","mc0/act-cmd-sent/","mc0/collision-queue-full/","mc0/collision-queue-not-empty/","mc0/cycle-count-div-64/","mc0/cycle-count/","mc0/in-rd-collision/","mc0/in-wr-collision/","mc0/mcu-hp-rd-request/","mc0/mcu-rd-proceed-all/","mc0/mcu-rd-proceed-cancel/","mc0/mcu-rd-proceed-speculative-all/","mc0/mcu-rd-proceed-speculative-cancel/","mc0/mcu-rd-request/","mc0/mcu-rd-response/","mc0/mcu-request/","mc0/mcu-wr-proceed-all/","mc0/mcu-wr-proceed-cancel/","mc0/mcu-wr-request/","mc0/pde-cmd-sent/","mc0/pre-cmd-sent/","mc0/prea-cmd-sent/","mc0/rd-cmd-sent/","mc0/rd-rda-cmd-sent/","mc0/rda-cmd-sent/","mc0/ref-cmd-sent/","mc0/sre-cmd-sent/","mc0/wr-cmd-sent/","mc0/wr-wra-cmd-sent/","mc0/wra-cmd-sent/","mc2/act-cmd-sent/","mc2/collision-queue-full/","mc2/collision-queue-not-empty/","mc2/cycle-count-div-64/","mc2/cycle-count/","mc2/in-rd-collision/","mc2/in-wr-collision/","mc2/mcu-hp-rd-request/","mc2/mcu-rd-proceed-all/","mc2/mcu-rd-proceed-cancel/","mc2/mcu-rd-proceed-speculative-all/","mc2/mcu-rd-proceed-speculative-cancel/","mc2/mcu-rd-request/","mc2/mcu-rd-response/","mc2/mcu-request/","mc2/mcu-wr-proceed-all/","mc2/mcu-wr-proceed-cancel/","mc2/mcu-wr-request/","mc2/pde-cmd-sent/","mc2/pre-cmd-sent/","mc2/prea-cmd-sent/","mc2/rd-cmd-sent/","mc2/rd-rda-cmd-sent/","mc2/rda-cmd-sent/","mc2/ref-cmd-sent/","mc2/sre-cmd-sent/","mc2/wr-cmd-sent/","mc2/wr-wra-cmd-sent/","mc2/wra-cmd-sent/","mc3/act-cmd-sent/","mc3/collision-queue-full/","mc3/collision-queue-not-empty/","mc3/cycle-count-div-64/","mc3/cycle-count/","mc3/in-rd-collision/","mc3/in-wr-collision/","mc3/mcu-hp-rd-request/","mc3/mcu-rd-proceed-all/","mc3/mcu-rd-proceed-cancel/","mc3/mcu-rd-proceed-speculative-all/","mc3/mcu-rd-proceed-speculative-cancel/","mc3/mcu-rd-request/","mc3/mcu-rd-response/","mc3/mcu-request/","mc3/mcu-wr-proceed-all/","mc3/mcu-wr-proceed-cancel/","mc3/mcu-wr-request/","mc3/pde-cmd-sent/","mc3/pre-cmd-sent/","mc3/prea-cmd-sent/","mc3/rd-cmd-sent/","mc3/rd-rda-cmd-sent/","mc3/rda-cmd-sent/","mc3/ref-cmd-sent/","mc3/sre-cmd-sent/","mc3/wr-cmd-sent/","mc3/wr-wra-cmd-sent/","mc3/wra-cmd-sent/","mcb0/cancel-read-gack/","mcb0/csw-read/","mcb0/csw-write-request/","mcb0/cycle-count-div-64/","mcb0/cycle-count/","mcb0/mcb-csw-stall/","mcb1/cancel-read-gack/","mcb1/csw-read/","mcb1/csw-write-request/","mcb1/cycle-count-div-64/","mcb1/cycle-count/","mcb1/mcb-csw-stall/","r00","r001","r002","r003","r004","r005","r006","r007","r008","r009","r00a","r00b","r010","r011","r012","r013","r014","r015","r016","r017","r018","r019","r01a","r01b","r01c","r01e","r040","r041","r042","r048","r04c","r04d","r050","r051","r052","r053","r056","r057","r058","r060","r061","r062","r063","r064","r065","r066","r067","r068","r069","r06a","r06c","r06d","r06e","r06f","r070","r071","r072","r073","r074","r075","r076","r078","r079","r07a","r07c","r07d","r07e","r081","r082","r083","r084","r086","r087","r08a","r08b","r08c","r08d","r08e","r08f","r090","r091","r100","r101","r102","r103","r104","r105","r106","r107","r108","r109","r10a","r10b","r10c","r10d","r10e","r10f","r110","r111","r112","r113","r114","r115","r116","CPU","entropy","reuse_time","memory_accesses"]
perfcntrs={}

perfcntrs_corr={}

def get_bench_name(bench):

    std_name=0
    bench_name=""
  
    if len(bench) >=11:
       std_name=0
    else:
       std_name=1
 
    if std_name == 0:
     if bench.find("kmeans_s") >= 0:
       bench_name="kmeans"
     elif bench.find("kmeans") >= 0:
       bench_name="kmeans(8)"
     elif bench.find("backprop_s") >= 0:
       bench_name="backprop"
     elif bench.find("backprop") >= 0:
       bench_name="backprop(8)"
     elif bench.find("srad_s") >= 0:
       bench_name="srad"
     elif bench.find("srad") >= 0:
       bench_name="srad(8)"
     elif bench.find("nw_s") >= 0:
       bench_name="nw"
     elif bench.find("nw") >= 0:
       bench_name="nw(8)"
     elif bench.find("micro_1") >= 0:
       bench_name="checkerboard"
     elif bench.find("micro_3") >= 0:
       bench_name="all0s"
     elif bench.find("micro_4") >= 0:
       bench_name="all1s"
     elif bench.find("micro_5") >= 0:
       bench_name="random"
     elif bench.find("micro_5_8gb") >= 0:
       bench_name="random(8Gb)"
     elif bench.find("dc") >= 0:
       bench_name="memcached"
     elif bench.find("fft") >= 0:
       bench_name="fft"
     elif bench.find("fmm_s") >= 0:
       bench_name="fmm"
     elif bench.find("fmm") >= 0:
       bench_name="fmm(8)"
     elif bench.find("pagerank") >= 0:
       bench_name="pagerank"
     elif bench.find("bfs") >= 0:
       bench_name="bfs"
     elif bench.find("bc") >= 0:
       bench_name="bc"
     elif bench.find("lulesh_s") >= 0:
       bench_name="lulesh"
     elif bench.find("lulesh") >= 0:
       bench_name="lulesh(8)"
     elif bench.find("radix") >= 0:
       bench_name="radix"
    else:
     if bench.find("micro1") >= 0:
       bench_name="checkerboard"
     elif bench.find("micro3") >= 0:
       bench_name="all0s"
     elif bench.find("micro4") >= 0:
       bench_name="all1s"
     elif bench.find("micro5") >= 0:
       bench_name="random"
     elif bench.find("micro5_8gb") >= 0:
       bench_name="random(8Gb)"
     elif bench.find("dc") >= 0:
       bench_name="memcached"
     elif bench.find("fft") >= 0:
       bench_name="fft"
     elif bench.find("fmm_s") >= 0:
       bench_name="fmm"
     elif bench.find("fmm") >= 0:
       bench_name="fmm(8)"
     elif bench.find("pagerank") >= 0:
       bench_name="pagerank"
     elif bench.find("bfs") >= 0:
       bench_name="bfs"
     elif bench.find("bc") >= 0:
       bench_name="bc"
     elif bench.find("lulesh_s") >= 0:
       bench_name="lulesh"
     elif bench.find("lulesh") >= 0:
       bench_name="lulesh(8)"
     elif bench.find("radix") >= 0:
       bench_name="radix"
     else:
       bench_name=bench


    return bench_name
def format_exponent(ax, axis, twin):

    # Change the ticklabel format to scientific format
    ax.ticklabel_format(axis=axis, style='sci', scilimits=(-2, 2))

    # Get the appropriate axis
    if axis == 'y':
        ax_axis = ax.yaxis
        x_pos = 0.0
        y_pos = 1.0
        if twin == 0:
          x_pos = -0.2
          y_pos = 0.95
          horizontalalignment='left'
        else:
          x_pos = 1.0
          y_pos = 1.03
          horizontalalignment='right'
        verticalalignment='bottom'
    else:
        ax_axis = ax.xaxis
        x_pos = 1.0
        y_pos = -0.05
        horizontalalignment='right'
        verticalalignment='top'

    # Run plt.tight_layout() because otherwise the offset text doesn't update
    plt.tight_layout()
    ##### THIS IS A BUG 
    ##### Well, at least it's sub-optimal because you might not
    ##### want to use tight_layout(). If anyone has a better way of 
    ##### ensuring the offset text is updated appropriately
    ##### please comment!

    # Get the offset value
    offset = ax_axis.get_offset_text().get_text()

    if len(offset) > 0:
        # Get that exponent value and change it into latex format
        minus_sign = u'\u2212'
        expo = np.float(offset.replace(minus_sign, '-').split('e')[-1])
        offset_text = r'x$\mathregular{10^{%d}}$' %expo

        # Turn off the offset text that's calculated automatically
        ax_axis.offsetText.set_visible(False)

        # Add in a text box at the top of the y axis
        ax.text(x_pos, y_pos, offset_text, transform=ax.transAxes,
               horizontalalignment=horizontalalignment,
               verticalalignment=verticalalignment)
    return ax

def init_data(stat_dir):
 global error_per_bench
 global err_hash_global
 global X,Y,Z,Y_PLOT3,Y_PLOT4

 err_hash_global={}
 error_per_bench={}

 files = os.listdir(stat_dir)
 for bench in files:
  bench_name=get_bench_name(bench)
  error_per_bench[bench_name]={}

  for i in range(0,130,STEP):
     bench_name=get_bench_name(bench)
     error_per_bench[bench_name][i]=[]

 for i in range(0,130,STEP):
   err_hash_global[i]={}

 X={}
 Y={}
 Z={}
 Y_PLOT3={}
 Y_PLOT4={}


 files = os.listdir(stat_dir)
 for bench in files:
    bench_name=get_bench_name(bench)
    X[bench_name]=[]
    Y[bench_name]=[]
    Z[bench_name]=[]

    Y_PLOT3[bench_name]=[]
    Y_PLOT4[bench_name]=[]


def collect_statistics(stat_dir):
 global error_per_bench
 global err_hash_global
 files = os.listdir(stat_dir)

 for bench in files:
  bench_name=get_bench_name(bench)
  err_dir = os.listdir(stat_dir+"/"+bench)  
  total_time=0.0

  for err_file_name in err_dir:
   if err_file_name.find("trace") >=0:

    err_hash={}
    prev_time=0.0
    total_num_err=0

    stat_info=open(stat_dir+"/"+bench+"/"+err_file_name)

    for line in stat_info:

     start_sym =  line.find("EDAC MC")
     if start_sym >= 0:

        info=line.split(":")
        if line.find("kworker") >= 0 or line.find("imjournal") >=0:
           info=info[1].split(" ")
        elif line.find("rs") >= 0:
           info=info[2].split(" ")
        else:
           info=info[0].split(" ")

        time=float(info[-1])

        if prev_time == 0.0:
           prev_time = time

        total_time+=(time - prev_time)/60.0
        prev_time = time

        id=int(total_time)/10

        if (id*10 >=130):
          break

        if err_hash.has_key(line[start_sym:start_sym+85]):
          total_num_err=total_num_err+1
        else:
          err_hash[line[start_sym:start_sym+85]] = 1

          id=int(total_time)/10
          err_hash_global[id*10][line[start_sym:start_sym+85]]=1

        total_time+=(time - prev_time)/60.0
        if (id*10 >=130):
          break
        else:
          error_per_bench[bench_name][id*10].append(line[start_sym:start_sym+85])
    
    stat_info.close

def process_statistics(stat_dir):

 global error_per_bench
 global err_hash_global
 global X,Y,Z,Y_PLOT3,Y_PLOT4
  
 total_number_unique_errors=0

 for i in range(0,120,STEP):
   total_number_unique_errors+=len(err_hash_global[i])

 files = os.listdir(stat_dir)
 for bench in files:
  bench_name=get_bench_name(bench)
  hash_err_local={}

  total_err_local_num = 0
  total_err_local_num_locations = 0

  for i in range(0,120,STEP):
    dnum=0
    for err_id in error_per_bench[bench_name][i]:
      total_err_local_num = total_err_local_num + 1
      if hash_err_local.has_key(err_id):
         hash_err_local[err_id]=hash_err_local[err_id]+1
      else:
         dnum=dnum+1
         hash_err_local[err_id]=0

    total_err_local_num_locations=total_err_local_num_locations+dnum

    if total_err_local_num_locations ==0:
      Z[bench_name].append(0)
    else:
      Z[bench_name].append(float(dnum)/float(total_err_local_num_locations))
    X[bench_name].append(i)

    if total_number_unique_errors == 0:
      Y[bench_name].append(0)
    else:
      Y[bench_name].append(100*float(len(hash_err_local))/float(total_number_unique_errors))

    Y_PLOT3[bench_name].append(total_err_local_num_locations)
    Y_PLOT4[bench_name].append(total_err_local_num)

def collect_performance_counters():
  global perf_counters_list
  global perfcntrs

  for id in perf_counters_list:
    perfcntrs[id]={}

  for path, subdirs, files in os.walk("../perfs_120718"):
    for name in files:
        file_name=os.path.join(path, name)

        if (path.find("original") >=0):
          if file_name.find("/time_") >= 0:
 
            if (file_name.find("needle") >= 0) and (file_name.find("parallel") >= 0):
               bench_name='nw(8)'

            if (file_name.find("needle") >= 0) and (file_name.find("1thread") >= 0):
               bench_name='nw'

            if (file_name.find("kmeans") >= 0) and (file_name.find("parallel") >= 0):
               bench_name='kmeans(8)'

            if (file_name.find("kmeans") >= 0) and (file_name.find("1thread") >= 0):
               bench_name='kmeans'

            if (file_name.find("backprop") >= 0) and (file_name.find("parallel") >= 0):
               bench_name='backprop(8)'

            if (file_name.find("backprop") >= 0) and (file_name.find("1thread") >= 0):
               bench_name='backprop'

            if (file_name.find("srad") >= 0) and (file_name.find("parallel") >= 0):
               bench_name='srad(8)'

            if (file_name.find("srad") >= 0) and (file_name.find("1thread") >= 0):
               bench_name='srad'

            if (file_name.find("fft") >= 0) and (file_name.find("fft") >= 0):
               bench_name='fft'

            if (file_name.find("fmm") >= 0) and (file_name.find("1thread") >= 0):
               bench_name='fmm'

            if (file_name.find("fmm") >= 0) and (file_name.find("parallel") >= 0):
               bench_name='fmm(8)'

            if (file_name.find("pagerank") >= 0):
               bench_name='pagerank'


            if (file_name.find("bfs") >= 0):
               bench_name='bfs'

            if (file_name.find("bc") >= 0):
               bench_name='bc'

            if (file_name.find("lulesh") >= 0) and (file_name.find("parallel") >= 0):
               bench_name='lulesh(8)'

            if (file_name.find("memcached") >= 0) and (file_name.find("memcached") >= 0):
               bench_name='memcached'

            if (file_name.find("graph-analytics") >= 0) and (file_name.find("graph-analytics") >= 0):
               bench_name='graph-analytics'

            if (file_name.find("web-search") >= 0) and (file_name.find("web-search") >= 0):
               bench_name='web-search'

            for id in perf_counters_list: 
               perfcntrs[id][bench_name]=[]

            stat_info = open(file_name)
            for line in stat_info:
              for id in perf_counters_list:
                if id == "seconds time elapsed":
                  start_sym =  line.find(" "+id)
                  if start_sym >= 0:
                     info=line.split(" "+id)
                     if math.isnan(float(info[0])):
                       perfcntrs[id][bench_name].append(0)
                     elif float(info[0]) > 0:
                       perfcntrs[id][bench_name].append(float(info[0]))
                elif id == "CPU":
                  start_sym =  line.find("%"+id)
                  if start_sym >= 0:
                    info=line.split("%"+id)
                    info=info[0].split(" ")
                    if math.isnan(float(info[-1])):
                       perfcntrs[id][bench_name].append(0)
                    elif (float(info[-1]) > 0):
                       perfcntrs[id][bench_name].append(float(info[-1])/100.0)
                else:
                  start_sym =  line.find("      "+id)
                  if start_sym >= 0:
                    info=line.split("      "+id)
                    if info[0].find(".") >= 0:
                        perfcntrs[id][bench_name].append(float(info[0]))
                    elif info[0].find("not counted") >= 0:
                        perfcntrs[id][bench_name].append(0.0)
                    else:
                      if int(info[0].replace(",", "")) > 0:
                        if math.isnan(float(info[0].replace(",", ""))):
                           perfcntrs[id][bench_name].append(0)
                        else:
                           perfcntrs[id][bench_name].append(float(info[0].replace(",", "")))
            stat_info.close()
 
  perfcntrs["CPU"]["memcached"].append(3.53989)
  perfcntrs["CPU"]["fmm(8)"].append(5.29)
  perfcntrs["CPU"]["fmm"].append(1.0)

  perfcntrs["entropy"]["nw"].append(7.23)
  perfcntrs["entropy"]["srad"].append(17.16)
  perfcntrs["entropy"]["backprop"].append(26.0)
  perfcntrs["entropy"]["kmeans"].append(8.0)
  perfcntrs["entropy"]["nw(8)"].append(7.23)
  perfcntrs["entropy"]["srad(8)"].append(17.16)
  perfcntrs["entropy"]["backprop(8)"].append(26.0)
  perfcntrs["entropy"]["kmeans(8)"].append(8.0)
  perfcntrs["entropy"]["memcached"].append(14.2652243004)
  perfcntrs["entropy"]["fmm"].append(23.9567906916)
  perfcntrs["entropy"]["fmm(8)"].append(23.9567906916)
  perfcntrs["entropy"]["lulesh(8)"].append(24.9555553546)
  perfcntrs["entropy"]["pagerank"].append(14.2652243004)
  perfcntrs["entropy"]["bfs"].append(14.2652243004)
  perfcntrs["entropy"]["bc"].append(14.2652243004)

  perfcntrs["reuse_time"]["backprop"]=1.6115589751
  perfcntrs["reuse_time"]["backprop(8)"]=1.10253815097633
  perfcntrs["reuse_time"]["kmeans"]=0.166458254829
  perfcntrs["reuse_time"]["kmeans(8)"]=0.500130001181
  perfcntrs["reuse_time"]["nw"]=2.283
  perfcntrs["reuse_time"]["nw(8)"]=2.283
  perfcntrs["reuse_time"]["srad"]=2.283
  perfcntrs["reuse_time"]["srad(8)"]=1.88658495748667
  perfcntrs["reuse_time"]["memcached"]=0.09
  perfcntrs["reuse_time"]["fmm"]=2.283
  perfcntrs["reuse_time"]["fmm(8)"]=1.85
  perfcntrs["reuse_time"]["pagerank"]=0.476223908918406
  perfcntrs["reuse_time"]["bfs"]=0.61271676300578
  perfcntrs["reuse_time"]["bc"]=0.566137566137566
  perfcntrs["reuse_time"]["lulesh(8)"]=4.88

def init_performance_counters(name):
  global perfcntrs_corr
  global perf_counters_list

  perfcntrs_corr[name]={}
  for id in perf_counters_list:
    perfcntrs_corr[name][id] = []

def correlate_performance_counters(corr_list,name):
  global perf_counters_list
  global perfcntrs
  global perfcntrs_corr

  for id in perf_counters_list:
    perf_list=[]
    for bench in bench_list:
      bench_name=bench
      if id == "CPU":
        perf_list.append(np.mean(perfcntrs[id][bench_name]))
      elif id == "memory_accesses":
        perf_list.append(np.mean(perfcntrs["l3c0/read-miss/"][bench_name])+np.mean(perfcntrs["l3c0/write-need-replacement/"][bench_name])/np.mean(perfcntrs["cycles"][bench_name]))
      elif id != "seconds time elapsed":
        perf_list.append(np.mean(perfcntrs[id][bench_name])/np.mean(perfcntrs["cycles"][bench_name]))

    r,rho = scipy.stats.spearmanr(perf_list,corr_list)
    perfcntrs_corr[name][id].append(r)
     
X_refr={}
Y_refr={}
Z_refr={}

Y_PLOT3_refr={}
Y_PLOT4_refr={}

refr_list=[]

init_performance_counters("wer")
collect_performance_counters()


dirs=["errors_53_2f2","errors_53_596","errors_53_83a","errors_53_adf","errors_63_2f2","errors_63_596","errors_63_83a","errors_63_adf","errors_73_2f2","errors_73_596"]

for pth in dirs:

  pth="../"+pth
  init_data(pth)

  collect_statistics(pth)

  process_statistics(pth)
  
  refr=str(pth).split("_")
  refr=refr[1]+"_"+refr[2]
  refr_list.append(refr)

  X_refr[refr]=X
  Y_refr[refr]=Y
  Z_refr[refr]=Z

  Y_PLOT3_refr[refr]=Y_PLOT3
  Y_PLOT4_refr[refr]=Y_PLOT4


analyze_counters=["l3c0/read-miss/","r110","l3c0/write-need-replacement/","entropy","reuse_time"]

final_error=[]

X_test=[]
X=[]
wer=[]
wer_test=[]
wer_classes=[]
wer_test_classes=[]
log_wer=[]
desc=[]

val_access_max=0
val_access_min=200000000

val_access_read_max=0
val_access_write_max=0

val_access_read_min=0
val_access_write_min=0
val_read=0
val_write=0
val_access=0


for refr in refr_list:
 for bench in bench_list:
   bench_name=bench

   vec=[]

   for cnt in analyze_counters:
     if cnt == "entropy" or cnt == "reuse_time":
        vec.append(np.mean(perfcntrs[cnt][bench_name]))
     else:
        if cnt == "r110":
           if math.isnan(((np.mean(perfcntrs[cnt][bench_name])*np.mean(perfcntrs["CPU"][bench_name]))/np.mean(perfcntrs["cycles"][bench_name]))*1.0e+5):
              val_access=0
           else:
              val_access=(((np.mean(perfcntrs[cnt][bench_name])*np.mean(perfcntrs["CPU"][bench_name]))/np.mean(perfcntrs["cycles"][bench_name]))*1.0e+5)

           if val_access > val_access_max:
              val_access_max=val_access
           if val_access < val_access_min:
              val_access_min=val_access


        if math.isnan(((np.mean(perfcntrs[cnt][bench_name])*np.mean(perfcntrs["CPU"][bench_name]))/np.mean(perfcntrs["cycles"][bench_name]))*1.0e+5):
           vec.append(0)
        else:
           vec.append(((np.mean(perfcntrs[cnt][bench_name])*np.mean(perfcntrs["CPU"][bench_name]))/np.mean(perfcntrs["cycles"][bench_name]))*1.0e+5)
   info=refr.split("_")
   vec.append(float(int(info[1], 16)))
   vec.append(float(info[0]))

   X.append(vec)
   desc.append(refr+bench_name)

   if bench_name =='random':       
       wer.append((float(Y_PLOT3_refr[refr][bench_name][11])/(28.0*1024*1024*1024/8.0))*1.5e+9)

       if (float(Y_PLOT3_refr[refr][bench_name][11])/(28.0*1024*1024*1024/8.0))*1.5e+9 == 0:
          wer_classes.append(0)       
       elif (float(Y_PLOT3_refr[refr][bench_name][11])/(28.0*1024*1024*1024/8.0))*1.5e+9 <100:
          wer_classes.append(100)
       else:
          wer_classes.append(int(((float(Y_PLOT3_refr[refr][bench_name][11])/(28.0*1024*1024*1024/8.0))*1.5e+9)/100)*100)

   else:
       wer.append((float(Y_PLOT3_refr[refr][bench_name][11])/(8.0*1024*1024*1024/8.0))*1.5e+9)

       if (float(Y_PLOT3_refr[refr][bench_name][11])/(8.0*1024*1024*1024/8.0))*1.5e+9 == 0:
          wer_classes.append(0)
       elif (float(Y_PLOT3_refr[refr][bench_name][11])/(8.0*1024*1024*1024/8.0))*1.5e+9 <100:
          wer_classes.append(100)
       else:
          wer_classes.append(int(((float(Y_PLOT3_refr[refr][bench_name][11])/(8.0*1024*1024*1024/8.0))*1.5e+9)/100)*100)


vec=[]
vec.append(0.00440697382350112*1.0e+5)
vec.append(0.00125172290223123*1.0e+5)
vec.append(0.000905146313444347*1.0e+5)
vec.append(24.9555553546)
vec.append(24.04)
vec.append(float(int('2f2', 16)))
vec.append(float('73'))

X.append(vec)

wer.append(1.685693860054016e-07*1.5e+9)
wer_classes.append(int((1.685693860054016e-07*1.5e+9)/10)*10)


vec=[]
vec.append(0.0024597738094262*1.0e+5)
vec.append(0.00625592621134534*1.0e+5)
vec.append(0.00522653125207264*1.0e+5)
vec.append(24.9555553546)
vec.append(4.97)
vec.append(float(int('2f2', 16)))
vec.append(float('73'))

X.append(vec)
wer.append(2.523884177207947e-07*1.5e+9)
wer_classes.append(int((2.523884177207947e-07*1.5e+9)/10)*10)



vec=[]
vec.append(0.0031642750509013*1.0e+5)
vec.append(0.00786423635121454*1.0e+5)
vec.append(0.00651748237695833*1.0e+5)
vec.append(24.9555553546)
vec.append(4.88)
vec.append(float(int('2f2', 16)))
vec.append(float('73'))

X.append(vec)
wer.append(2.8032809495925903e-07*1.5e+9)
wer_classes.append(int((2.8032809495925903e-07*1.5e+9)/10)*10)


vec=[]
vec.append(0.00776901799852108*1.0e+5)
vec.append(0.0112373405973254*1.0e+5)
vec.append(0.00901609840915047*1.0e+5)
vec.append(24.9555553546)
vec.append(3.31)
vec.append(float(int('2f2', 16)))
vec.append(float('73'))

X.append(vec)
wer.append(3.557652235031128e-07*1.5e+9)
wer_classes.append(int((3.557652235031128e-07*1.5e+9)/10)*10)

X_4c=[]
for item in X:
  if item[4] == 754.0:
    item_new=item
    item_new[4]=float(78)
    X_4c.append(item_new)
    wer.append(0.0)
    wer_classes.append(0.0)

for item in X_4c:
  X.append(item)


X_boost=[]
wer_boost=[]
wer_classes_boost=[]

i=0
for item in X:
  for j in range(0,200):
     X_boost.append(item)
     wer_boost.append(wer[i])
     wer_classes_boost.append(wer_classes[i])
  i=i+1


scaler = preprocessing.StandardScaler().fit(X_boost)
preprocessing.StandardScaler(copy=True, with_mean=True, with_std=True)
X_boost_scale=scaler.transform(X_boost)

clf_classes = KNeighborsClassifier()
clf_classes.fit(X_boost_scale, wer_classes_boost)
KNeighborsClassifier(algorithm='auto', leaf_size=30, metric='minkowski',
           metric_params=None, n_jobs=1, n_neighbors=5, p=2,
           weights='uniform')

filename = 'scaler_DRAM_model.sav'
pickle.dump(scaler, open(filename, 'wb'))

filename = 'SVM_DRAM_model.sav'
pickle.dump(clf_classes, open(filename, 'wb'))

filename = 'testdata_DRAM_model.sav'
pickle.dump(X_test, open(filename, 'wb'))
