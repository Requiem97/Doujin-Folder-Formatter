# Doujin Folder Formatter
Formats folder names from the folders downloaded by Hentoid
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