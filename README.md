# Scannet-download-and-extract
scripts for downloading scannet dataset and extract them using multiprocessing to speed up
## Download scannet dataset
[Please refer to scannet official repo for downloading commands.](https://github.com/ScanNet/ScanNet)
## Extract downloaded dataset
The official download script uses python2.7 so we will use multiprocessing library to speed up extraction of .sens files.

The downloaded data structure should be:
```
extract.py
reader.py
SensorData.py
download_scannet.py
download_scannetv2.py

/data_downloaded  
    /scans_test
        /scene0707_00
            scene0707_00.sens
        ...
    /scans_train
        /scene0000_00
            scene0000_00.sens
        ...
```
Then modify the split(train/test) of the file you want to decompress and the path of the python interpreter to use in extract.py

Also, Specify the maxprocess variable in extract.py

After running extract.py, the file structure should be:
```
/data_extracted
  /scans_test
      /scene0707_00
          /color
              000000.jpg
          /depth
              000000.png
          /pose
              000000.txt
          intrinsics_color.txt
          intrinsics_depth.txt
          ...
  /scans_train
       ...
```




