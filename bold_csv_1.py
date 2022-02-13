# -*- coding: utf-8 -*-
#By Sara Camila Laura Manzaneda
"""BOLD-CSV_1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1auokLeJ9dJk7_JMLrC1x4sZy4xTkRJjd
"""

import zipfile

from google.colab import drive
import glob

from google.colab import drive
drive.mount('/content/drive')

A=['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15']
for i in range (8):
  ruta_zip='/content/drive/My Drive/CIDIMEC-RESEARCH/DATSETS/BOLD5000/BOLD5000_Unfiltered_CSI4_sess'+A[i] +'.zip'
  ruta_extraccion = "/content/drive/My Drive/boldcito/BOLD5000_Unfiltered_CSI4_sess"+ A[i]+"/"
  password = None
  archivo_zip = zipfile.ZipFile(ruta_zip, "r")
  try:
      print(archivo_zip.namelist())
      archivo_zip.extractall(pwd=password, path=ruta_extraccion)
  except:
      pass
  archivo_zip.close()

ruta_zip='/content/drive/My Drive/CIDIMEC-RESEARCH/DATSETS/BOLD5000/BOLD5000_Unfiltered_CSI4_sess09.zip'
ruta_extraccion = "/content/drive/My Drive/boldcito/BOLD5000_Unfiltered_CSI4_sess09/"
password = None
archivo_zip = zipfile.ZipFile(ruta_zip, "r")
try:
  print(archivo_zip.namelist())
  archivo_zip.extractall(pwd=password, path=ruta_extraccion)
except:
  pass
archivo_zip.close()

!pip install pydicom

!mkdir '/content/drive/My Drive/CIDIMEC-RESEARCH/DATSETS/BOLD5000 (CSV)/BOLD5000_Unfiltered_CSI1_sess14/02_Unfilt_BOLD_CSI1_Sess-14_Run-2'

!cd 'content/drive/My Drive/boldcito/BOLD5000_Unfiltered_CSI1_sess14/01_Unfilt_BOLD_CSI1_Sess-14_Run-1'

import pydicom as dicom
import numpy as np
from pydicom.data import get_testdata_file
from pydicom import dcmread
fpath = dicom.read_file("/content/drive/My Drive/boldcito/BOLD5000_Unfiltered_CSI1_sess14/01_Unfilt_BOLD_CSI1_Sess-14_Run-1/02-0001-000001.dcm")
print(fpath)

ruta='/content/drive/My Drive/boldcito/BOLD5000_Unfiltered_CSI1_sess14/01_Unfilt_BOLD_CSI1_Sess-14_Run-1/02-0001-000001.dcm'
dcm_file =dicom.read_file(ruta)
pixel_dcm=dcm_file.pixel_array
print(pixel_dcm)
print(type(pixel_dcm))
#new='/content/drive/My Drive/CIDIMEC-RESEARCH/DATSETS/BOLD5000 (CSV)/BOLD5000_Unfiltered_CSI1_sess14/' + '01_Unfilt_BOLD_CSI1_Sess-14_Run-1/02-0001-000001.dcm'
#print (new)
#np.savetxt(new, pixel_dcm, delimiter=";")

from PIL import Image
import matplotlib.pyplot as plt
pixel_dcm=dcm_file.pixel_array
print(pixel_dcm.shape)
#print(dcm_file.Rows)
#print(dcm_file.Columns)
#print(dcm_file.pixel_array[0,0])

plt.imshow(dcm_file.pixel_array,plt.cm.bone)
plt.show()

!pip install pydicom

import pydicom as dicom 
import numpy as np

B=['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15']
C=['01_Unfilt_BOLD_CSI1_Sess-14_Run-1',
   '02_Unfilt_BOLD_CSI1_Sess-14_Run-2',
   '03_Unfilt_BOLD_CSI1_Sess-14_Run-3',
   '04_Unfilt_BOLD_CSI1_Sess-14_Run-4',
   '05_Unfilt_BOLD_CSI1_Sess-14_Run-5',
   '06_Unfilt_SpinEchoFieldMap_pF68_AP_CSI1_Sess-14',
   '07_Unfilt_SpinEchoFieldMap_pF68_PA_CSI1_Sess-14',
   '08_Unfilt_SpinEchoFieldMap_AP_CSI1_Sess-14',
   '09_Unfilt_SpinEchoFieldMap_PA_CSI1_Sess-14',
   '10_Unfilt_OppPhase-BOLD_PA_CSI1_Sess-14',
   '11_Unfilt_BOLD_CSI1_Sess-14_Run-6',
   '12_Unfilt_BOLD_CSI1_Sess-14_Run-7',
   '13_Unfilt_BOLD_CSI1_Sess-14_Run-8',
   '14_Unfilt_BOLD_CSI1_Sess-14_Run-9',
   '15_Unfilt_BOLD_CSI1_Sess-14_SceneLocal']
aa='00000'
bb='0000'
cc='000'
aax=['02','04','06','08','10']
dcm_csv=['.dcm','.csv']
path_total=''
xx=''
for i in range (5):
  dcm_file ='/content/drive/My Drive/boldcito/BOLD5000_Unfiltered_CSI1_sess14/'+C[i]+'/'+aax[i]
  print (dcm_file)
  for j in range (194):
    if (j+1) <10:
      #print ('hola')
      #print(j+1)
      path_total= dcm_file+'-0001-'+ aa + str (j+1)+'.dcm'
      print(path_total)
      xx='-0001-'+aa+ str(i+1)+'csv'
    if (j+1) > 9 and (j+1)<100 :
      print('chau')
      #print(j+1)
      path_total=dcm_file +'-0001-'+ bb + str (j+1)+'.dcm'
      print(path_total)
      xx='-0001-'+bb+ str(i+1)+'.csv'
    if (j+1) >=100:
      print ('bored')
      #print(j+1)
      path_total= dcm_file +'-0001-'+ cc+ str (j+1) +'.dcm'
      print(path_total)
      xx='-0001-'+cc+ str(i+1)+'.csv'
    dicom_array=dicom.read_file(path_total)
    print (path_total)
    numpy_dicom_array=(dicom_array.pixel_array)
    
    new='/content/drive/My Drive/CIDIMEC-RESEARCH/DATSETS/BOLD5000 (CSV)/BOLD5000_Unfiltered_CSI1_sess14/' + C[i]+'/'+aax[i]+xx
    print (new)
    np.savetxt(new, numpy_dicom_array, delimiter=";")

!pip install pydicom

from google.colab import drive
drive.mount('/content/drive')

import pydicom as dicom 
import numpy as np
aa='00000'
bb='0000'
cc='000'
path_1='/content/drive/My Drive/boldcito/BOLD5000_Unfiltered_CSI3_sess10/13_Unfilt_BOLD_CSI3_Sess-10_Run-8/28-0001-'
for i in range (141):
  if i+1 <=9:
    path_2=path_1+aa+str (i+1)+ '.dcm'
    xx=aa+str (i+1)+ '.csv'
  if i+1>=10 and i+1<=99:
    path_2=path_1+bb+str (i+1)+ '.dcm'
    xx=bb+str (i+1)+ '.csv'
  if i+1 >=100:
    path_2=path_1+cc+str (i+1)+ '.dcm'
    xx=cc+str (i+1)+ '.csv'
  dicom_array=dicom.read_file(path_2)
  numpy_dicom_array=(dicom_array.pixel_array)
  #
  new=path_1+xx
  print (new)
  np.savetxt(new, numpy_dicom_array, delimiter=";")
#By Sara Camila Laura Manzaneda