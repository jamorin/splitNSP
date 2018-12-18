## The original repository has been forked to use SX OS's split naming scheme as of v2.4.1:

> https://team-xecuter.com/sx-os-v2-4-1-beta-announcement/

# splitNSP

As some have become aware, it's been found out that the official Nintendo SDK contains a PowerShell script for splitting NSP files into 4GiB chunks so that they can be installed from FAT32 filesystems. Seeing as the official script cannot be shared, I re-wrote it in Python3 (which makes it useable on more than just Windows) as well as added in an additional feature.

To run it you'll need Python3 installed. Once installed, call the script from Terminal or Command Prompt with the following:

`python3 splitNSP.py filename.nsp`

By default this will make a copy of the NSP and split it up into parts. Once created, you'll need to open the folder's properties and check the Archive flag. This is easily done on Windows, I'm still working on a way to do it for macOS since file flags aren't saved when copying to FAT32.

You can also activate quick mode with this command:

`python3 splitNSP.py filename.nsp`

This will not make a copy of the NSP and instead will split the original. This is useful if you're running low on space as it only requires that you have 4GiB of temporary space to run it. It's also much faster.

Once the folder is made and the archive flag is set copy it to your SD card (sdmc:/tinfoil/nsp/ if using tinfoil) and install it like any other NSP.

If you have any issues feel free to submit an issue and I'll try my best to work it out.

## splitXCI

`python3 splitXCI.py filename.xci`

This will create [filename].xc0, [filename].xc1, [filename].xc2, etc.. depending on the size of the original XCI file. Copy the files to sdmc:/sxos/xci, hddmc:/sxos/xci, or where ever you store XCI.
