from pathlib import Path

animal_id = "rbak006"
#hemisphere (left -> "l", right -> "r")
hemi = "l"
#location of rat_id folder
animal_loc = Path("/Volumes/BaffaloSSDPUTU3C1TB/rbak_data") / animal_id

#bit_change
max_intensity = 482

#downsample
divisor = 4
down_x = 2160//divisor
down_y = 4096//divisor

#concatenate
loc_max = 18

#trim
grid = 4
frame_len = 62

#ymerge
# number of tiff images after xmerge
max_pos = 6
