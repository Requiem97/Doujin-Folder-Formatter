# Doujin Folder Formatter
Formats folders downloaded by Hentoid
## Requirements
- Python 3.6
- Downloads from hentoid following the Author - Title - ID format
## How to use
1. Make sure all downloads are located in a single folder
2. Download or clone the repository
3. Copy rename.py and script.py in your doujin folder
4. Run script.py
5. Enjoy!
## Features
- deletes contentV2.json
- changes thumb.png/thumb.jpg into folder.jpg
- Can delete a duplicate thumb image in case of accidental merging
- Renames folders to "[author] title" format
## Rename Sample Cases
**Before**
> name1_name2 - t_i_t_l_e____ - [id-source]

> name1_name2 - t_i_t_l_e_-_o_t_h_e_r - [id-source]

> name1_name2 - name1_name2_t_i_t_l_e_-_o_t_h_e_r - [id-source]

**After**
> [name1 name2] title

> [name1 name2] title - other

> [name1 name2] title - other

Script can also automatically handle some posessives
> \_s\_

becomes
> 's 

> \_t\_

becomes
> 't 

> \_ve\_

becomes
> 've

Other possesives will be added if needed