#!/usr/bin/env python3
# Author: AnalogMan
# Modified Date: 2018-10-08
# Purpose: Splits Nintendo Switch XCI files into parts for installation on FAT32

import os
import argparse
import shutil
from datetime import datetime
startTime = datetime.now()

splitSize = 0xFFFF0000 # 4,294,901,760 bytes
chunkSize = 0x8000 # 32,768 bytes

def splitCopy(filepath):
    fileSize = os.path.getsize(filepath)
    info = shutil.disk_usage(os.path.dirname(os.path.abspath(filepath)))
    if info.free < fileSize*2:
        print('Not enough free space to run. Will require twice the space as the XCI file\n')
        return
    print('Calculating number of splits...\n')
    splitNum = int(fileSize/splitSize)
    if splitNum == 0:
        print('This XCI is under 4GiB and does not need to be split.\n')
        return

    print('Splitting XCI into {0} parts...\n'.format(splitNum + 1))

    # Create directory, delete if already exists
    dir = filepath[:-4]

    remainingSize = fileSize

    print('\n'+ filepath)

    # Open source file and begin writing to output files stoping at splitSize
    with open(filepath, 'rb') as nspFile:
        for i in range(splitNum + 1):
            partSize = 0
            print('Starting part {:02}'.format(i))
            # basename = os.path.splitext(os.path.basename(dir))[0]
            outFile = dir + '.xc' + str(i)
            print('\n'+ outFile)
            with open(outFile, 'wb') as splitFile:
                if remainingSize > splitSize:
                    while partSize < splitSize:
                        splitFile.write(nspFile.read(chunkSize))
                        partSize += chunkSize
                    remainingSize -= splitSize
                else:
                    while partSize < remainingSize:
                        splitFile.write(nspFile.read(chunkSize))
                        partSize += chunkSize
            print('Part {:02} complete'.format(i))
    print('\nXCI successfully split!\n')

def main():
    print('\n========== XCI Splitter ==========\n')

    # Arg parser for program options
    parser = argparse.ArgumentParser(description='Split XCI files into FAT32 compatible sizes')
    parser.add_argument('filepath', help='Path to XCI file')

    # Check passed arguments
    args = parser.parse_args()

    filepath = args.filepath

    # Check if required files exist
    if os.path.isfile(filepath) == False:
        print('XCI cannot be found\n')
        return 1

    splitCopy(filepath)

if __name__ == "__main__":
    main()
