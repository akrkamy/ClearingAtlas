# ClearingAtlas
Long-Evans Rat Clearing Atlas

1. Create folders
    - [animal id]
        - 12bit
            - l
            - r
        - 8bit
            - l
            - r
        - downsample
            - l
            - r
        - concatenated
            - l
            - r
        - trimmed
            - l
            - r
        - xmerged
            - l
            - r
        - ymerged
            - l
            - r
        - zmerged

2. Modify 0_data.py (modify after each step as needed)
3. 1_bit_change
4. 2_downsample
5. 3_concatenate
6. 4_trim
7. check excel file
    there are sectional image with insufficient frames -> 4_trim(manual)
8. 5_xmerge(atbrightest)
9. 6_ymerge(atbrightest)
10. 7_zmerge

Approximate process time (one hemisphere, 2x18, 〜20GB)
    - bit change: 30 min
    - downsample: 30 min
    - concatenate: 1 min
    - trim: 
    - trim(manual): 
    - xmerge(atbrightest): 6 min
    - xmerge(original): 6 min
    - ymerge(atbrightest): 2 min

Attetion:
- Be aware of the file names in the original codes
- This code was written using Mac (Apple Sillicon) with 16 GB memory
