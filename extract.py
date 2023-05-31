import os
# from tqdm import tqdm
import subprocess
from multiprocessing import Pool
"""
    reader.py extract one .sens file
    usage:
    python reader.py --filename [.sens file to export data from] --output_path [output directory to export data to]
    --export_depth_images: export all depth frames as 16-bit pngs (depth shift 1000)
    --export_color_images: export all color frames as 8-bit rgb jpgs
    --export_poses: export all camera poses (4x4 matrix, camera to world)
    --export_intrinsics: export camera intrinsics (4x4 matrix)
    
    This file extract all .sens file from ./data/scans_test and ./data/scans_train
    
    Dir structure:
    data_downloaded
        scans_test
            scene0707_00
                scene0707_00.sens
            ...
        scans_train
            scene0000_00
                scene0000_00.sens
            ...
    ------After extract.py------
    data_extracted
        scans_test
            scene0707_00
                color
                    000000.jpg
                depth
                    000000.png
                pose
                    000000.txt
                intrinsics_color.txt
                intrinsics_depth.txt
            ...
        scans_train
            ...
"""

def execute_command(command):
    # print("multiprocess pool: ", os.getpid())
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print("multiprocess pool: ", os.getpid(), " subprocess: ", process.pid, " started")
    output, error = process.communicate()
    print("        subprocess", process.pid, " output: ", output, error)
    print("multiprocess pool: ", os.getpid(), " subprocess:", process.pid, " finished")
    

def find_sens_files(path):
    sens_files = []
    for root, dirs, files in os.walk(path):
        # print("*********************\n")
        # print("root: ", root)
        # print("dirs: ", dirs)
        # print("files: ", files)
        for file in files:
            if file.endswith(".sens"):
                sens_files.append(os.path.join(root, file))
    # './data_downloaded/scans_test/scene0707_00/scene0707_00.sens'
    return sens_files


def extract_sens_files_commands(path):
    # path = "./data_downloaded/scans_test" or "./data_downloaded/scans_train"
    sens_files = find_sens_files(path)
    commands = []
    for sens_file in sens_files:
        info = sens_file.split("/") # ['.', 'data_downloaded', 'scans_test', 'scene0707_00', 'scene0707_00.sens']
        file_name = sens_file
        output_path = "./data_extracted/" + info[2] + "/" + info[3]
        command = ["CHANGE TO YOUR python 2.7 interpreter", 
                   "reader.py", 
                   "--filename", 
                   str(file_name), 
                   "--output_path", 
                   str(output_path), 
                   "--export_depth_images", 
                   "--export_color_images", 
                   "--export_poses", 
                   "--export_intrinsics"
                ]
        symbol = " "
        commands.append(symbol.join(command))
    return commands
        


if __name__ == "__main__":
    path_test = "./data_downloaded/scans_test"
    path_train = "./data_downloaded/scans_train"
    print("main pid: ", os.getpid())
    max_processes = 15  # set maximum processing at the same time
    pool = Pool(processes=max_processes)
    test_commands = extract_sens_files_commands(path_test)
    train_commands = extract_sens_files_commands(path_train)

    print("test_commands length: ", len(test_commands)) # 100
    print("train_commands length: ", len(train_commands)) # 1513
    
    
    pool.map(execute_command, train_commands)
    pool.close()
    pool.join()
    print("train finished!")
    
    # subprocess.Popen(test_commands, shell=True)
    
    
