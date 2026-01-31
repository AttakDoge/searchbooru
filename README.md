search tool for danbooru donmai us that allows for more than 2 tags to be searched

how it works:
- input list >2 tags
- split list by groups of 2 (eg. "touhou dress hat" -> ["touhou dress", "hat"])
- load search pages using new tag array
- add each post id for each search to temp files
- diff temp files and keep only matching across all
- output post ids
    - methods undecided, maybe use html and load search preview images of output posts

making this just because more than 2 tag searches are not allowed on danbooru without gold account and buying is disabled (and has been for quite a while)