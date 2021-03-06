#!/Volumes/Scratch/dblodgett_workspace/pyGDP/venv/bin/python
import os
import subprocess
import time
import shlex
processes = []
max_processes = 12
pause_time=2
file_processing = 1
files=("ACCESS1-0_rcp45_r1i1p1.nc",
"ACCESS1-0_rcp85_r1i1p1.nc",
"BNU-ESM_rcp45_r1i1p1.nc",
"BNU-ESM_rcp85_r1i1p1.nc",
"CCSM4_rcp26_r1i1p1.nc",
# "CCSM4_rcp26_r2i1p1.nc",
"CCSM4_rcp45_r1i1p1.nc",
# "CCSM4_rcp45_r2i1p1.nc",
"CCSM4_rcp60_r1i1p1.nc",
# "CCSM4_rcp60_r2i1p1.nc",
"CCSM4_rcp85_r1i1p1.nc",
"CCSM4_rcp85_r2i1p1.nc",
"CESM1-BGC_rcp45_r1i1p1.nc",
"CESM1-BGC_rcp85_r1i1p1.nc",
"CNRM-CM5_rcp45_r1i1p1.nc",
"CNRM-CM5_rcp85_r1i1p1.nc",
# "CSIRO-Mk3-6-0_rcp26_r10i1p1.nc",
"CSIRO-Mk3-6-0_rcp26_r1i1p1.nc",
# "CSIRO-Mk3-6-0_rcp26_r2i1p1.nc",
# "CSIRO-Mk3-6-0_rcp26_r3i1p1.nc",
# "CSIRO-Mk3-6-0_rcp26_r4i1p1.nc",
# "CSIRO-Mk3-6-0_rcp26_r5i1p1.nc",
# "CSIRO-Mk3-6-0_rcp26_r6i1p1.nc",
# "CSIRO-Mk3-6-0_rcp26_r7i1p1.nc",
# "CSIRO-Mk3-6-0_rcp26_r8i1p1.nc",
# "CSIRO-Mk3-6-0_rcp26_r9i1p1.nc",
# "CSIRO-Mk3-6-0_rcp45_r10i1p1.nc",
"CSIRO-Mk3-6-0_rcp45_r1i1p1.nc",
# "CSIRO-Mk3-6-0_rcp45_r2i1p1.nc",
# "CSIRO-Mk3-6-0_rcp45_r3i1p1.nc",
# "CSIRO-Mk3-6-0_rcp45_r4i1p1.nc",
# "CSIRO-Mk3-6-0_rcp45_r5i1p1.nc",
# "CSIRO-Mk3-6-0_rcp45_r6i1p1.nc",
# "CSIRO-Mk3-6-0_rcp45_r7i1p1.nc",
# "CSIRO-Mk3-6-0_rcp45_r8i1p1.nc",
# "CSIRO-Mk3-6-0_rcp45_r9i1p1.nc",
# "CSIRO-Mk3-6-0_rcp85_r10i1p1.nc",
"CSIRO-Mk3-6-0_rcp85_r1i1p1.nc",
# "CSIRO-Mk3-6-0_rcp85_r2i1p1.nc",
# "CSIRO-Mk3-6-0_rcp85_r3i1p1.nc",
# "CSIRO-Mk3-6-0_rcp85_r4i1p1.nc",
# "CSIRO-Mk3-6-0_rcp85_r5i1p1.nc",
# "CSIRO-Mk3-6-0_rcp85_r6i1p1.nc",
# "CSIRO-Mk3-6-0_rcp85_r7i1p1.nc",
# "CSIRO-Mk3-6-0_rcp85_r8i1p1.nc",
# "CSIRO-Mk3-6-0_rcp85_r9i1p1.nc",
"CanESM2_rcp26_r1i1p1.nc",
# "CanESM2_rcp26_r2i1p1.nc",
# "CanESM2_rcp26_r3i1p1.nc",
# "CanESM2_rcp26_r4i1p1.nc",
# "CanESM2_rcp26_r5i1p1.nc",
"CanESM2_rcp45_r1i1p1.nc",
# "CanESM2_rcp45_r2i1p1.nc",
# "CanESM2_rcp45_r3i1p1.nc",
# "CanESM2_rcp45_r4i1p1.nc",
# "CanESM2_rcp45_r5i1p1.nc",
"CanESM2_rcp85_r1i1p1.nc",
# "CanESM2_rcp85_r2i1p1.nc",
# "CanESM2_rcp85_r3i1p1.nc",
# "CanESM2_rcp85_r4i1p1.nc",
# "CanESM2_rcp85_r5i1p1.nc",
"GFDL-CM3_rcp26_r1i1p1.nc",
"GFDL-CM3_rcp60_r1i1p1.nc",
"GFDL-CM3_rcp85_r1i1p1.nc",
"GFDL-ESM2G_rcp26_r1i1p1.nc",
"GFDL-ESM2G_rcp45_r1i1p1.nc",
"GFDL-ESM2G_rcp60_r1i1p1.nc",
"GFDL-ESM2G_rcp85_r1i1p1.nc",
"GFDL-ESM2M_rcp26_r1i1p1.nc",
"GFDL-ESM2M_rcp45_r1i1p1.nc",
"GFDL-ESM2M_rcp60_r1i1p1.nc",
"GFDL-ESM2M_rcp85_r1i1p1.nc",
"IPSL-CM5A-LR_rcp26_r1i1p1.nc",
# "IPSL-CM5A-LR_rcp26_r2i1p1.nc",
# "IPSL-CM5A-LR_rcp26_r3i1p1.nc",
"IPSL-CM5A-LR_rcp45_r1i1p1.nc",
# "IPSL-CM5A-LR_rcp45_r2i1p1.nc",
# "IPSL-CM5A-LR_rcp45_r3i1p1.nc",
# "IPSL-CM5A-LR_rcp45_r4i1p1.nc",
"IPSL-CM5A-LR_rcp60_r1i1p1.nc",
"IPSL-CM5A-LR_rcp85_r1i1p1.nc",
# "IPSL-CM5A-LR_rcp85_r2i1p1.nc",
# "IPSL-CM5A-LR_rcp85_r3i1p1.nc",
# "IPSL-CM5A-LR_rcp85_r4i1p1.nc",
"IPSL-CM5A-MR_rcp26_r1i1p1.nc",
"IPSL-CM5A-MR_rcp45_r1i1p1.nc",
"IPSL-CM5A-MR_rcp60_r1i1p1.nc",
"IPSL-CM5A-MR_rcp85_r1i1p1.nc",
"MIROC-ESM-CHEM_rcp26_r1i1p1.nc",
"MIROC-ESM-CHEM_rcp45_r1i1p1.nc",
"MIROC-ESM-CHEM_rcp60_r1i1p1.nc",
"MIROC-ESM-CHEM_rcp85_r1i1p1.nc",
"MIROC-ESM_rcp26_r1i1p1.nc",
"MIROC-ESM_rcp45_r1i1p1.nc",
"MIROC-ESM_rcp60_r1i1p1.nc",
"MIROC-ESM_rcp85_r1i1p1.nc",
"MIROC5_rcp26_r1i1p1.nc",
# "MIROC5_rcp26_r2i1p1.nc",
# "MIROC5_rcp26_r3i1p1.nc",
"MIROC5_rcp45_r1i1p1.nc",
# "MIROC5_rcp45_r2i1p1.nc",
# "MIROC5_rcp45_r3i1p1.nc",
"MIROC5_rcp60_r1i1p1.nc",
"MIROC5_rcp85_r1i1p1.nc",
# "MIROC5_rcp85_r2i1p1.nc",
# "MIROC5_rcp85_r3i1p1.nc",
"MPI-ESM-LR_rcp26_r1i1p1.nc",
# "MPI-ESM-LR_rcp26_r2i1p1.nc",
# "MPI-ESM-LR_rcp26_r3i1p1.nc",
"MPI-ESM-LR_rcp45_r1i1p1.nc",
# "MPI-ESM-LR_rcp45_r2i1p1.nc",
# "MPI-ESM-LR_rcp45_r3i1p1.nc",
"MPI-ESM-LR_rcp85_r1i1p1.nc",
# "MPI-ESM-LR_rcp85_r2i1p1.nc",
# "MPI-ESM-LR_rcp85_r3i1p1.nc",
"MPI-ESM-MR_rcp26_r1i1p1.nc",
"MPI-ESM-MR_rcp45_r1i1p1.nc",
# "MPI-ESM-MR_rcp45_r2i1p1.nc",
# "MPI-ESM-MR_rcp45_r3i1p1.nc",
"MPI-ESM-MR_rcp85_r1i1p1.nc",
"MRI-CGCM3_rcp26_r1i1p1.nc",
"MRI-CGCM3_rcp45_r1i1p1.nc",
"MRI-CGCM3_rcp60_r1i1p1.nc",
"MRI-CGCM3_rcp85_r1i1p1.nc",
"NorESM1-M_rcp26_r1i1p1.nc",
"NorESM1-M_rcp45_r1i1p1.nc",
"NorESM1-M_rcp60_r1i1p1.nc",
"NorESM1-M_rcp85_r1i1p1.nc",
"bcc-csm1-1_rcp26_r1i1p1.nc",
"bcc-csm1-1_rcp45_r1i1p1.nc",
"bcc-csm1-1_rcp60_r1i1p1.nc",
"bcc-csm1-1_rcp85_r1i1p1.nc",
"inmcm4_rcp45_r1i1p1.nc",
"inmcm4_rcp85_r1i1p1.nc")
tasmax=True
pr_run=True
while file_processing<=len(files):
    print str(file_processing)
    if pr_run:
        command=shlex.split("python averageBCCA.py /Volumes/temp_striped/data/"+files[file_processing-1]+" BCCA_0-125deg_pr_day_"+files[file_processing-1].replace('.nc','')+" rcp "+files[file_processing-1].replace('.nc','')+"_pr /Volumes/temp_striped/unmerged_pr")
        file_processing+=1
    else:
        if tasmax:
            command=shlex.split("python averageBCCA.py /Volumes/temp_striped/data/"+files[file_processing-1]+" BCCA_0-125deg_tasmax_day_"+files[file_processing-1].replace('.nc','')+" rcp "+files[file_processing-1].replace('.nc','')+"_tasmax /Volumes/temp_striped/unmerged")
            tasmax=False
        else:
            command=shlex.split("python averageBCCA.py /Volumes/temp_striped/data/"+files[file_processing-1]+" BCCA_0-125deg_tasmin_day_"+files[file_processing-1].replace('.nc','')+" rcp "+files[file_processing-1].replace('.nc','')+"_tasmin /Volumes/temp_striped/unmerged")
            file_processing+=1
            tasmax=True
    print(command)
    processes.append(subprocess.Popen(command))
    if len(processes) < max_processes:
		time.sleep(pause_time)
    while len(processes) >= max_processes:
        time.sleep(pause_time*2)
        processes = [proc for proc in processes if proc.poll() is None]
while len(processes) > 0:
    time.sleep(pause_time)
    processes = [proc for proc in processes if proc.poll() is None]
