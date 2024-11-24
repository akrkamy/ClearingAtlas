# ClearingAtlas
Long-Evans Rat Clearing Atlas

1. Create folders
    follow the folder structures
2. Modify reset.py (modify after each step as needed)
3. 1_bit_change
4. 2_downsample
5. 3_concatenate
6. 4_trim
7. check excel file
    there are sectional image with insufficient frames -> 4_trim(manual)
8. 5_ffc_target
9. 5_ffc
10. 6_xmerge(atbrightest)
11. 7_ymerge(atbrightest)
12. 8_padding
13. 9_zmerge

Approximate process time (one hemisphere, 2x18, 〜20GB)
- bit change: 30 min
- downsample: 30 min
- concatenate: 1 min
- trim: 1 min
- trim(manual): <1 min
- ffc_target: <1 min
- ffc: <1min
- xmerge(atbrightest): 6 min
- xmerge(original): 6 min
- ymerge(atbrightest): 2 min
- zmerge: 10 min

Folder Structure

    - ffc
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
        - ffc
            - l
            - r
        - xmerged
            - l
            - r
        - ymerged
            - l
            - r
        - padding
            - l
            - r
        - zmerged

Note:
- Mac (Apple Sillicon) with 16 GB memory