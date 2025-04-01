# artificial-activity

Some Python to generate artificial git activity

Specifically - wanted to have the GitHub activity graph spell out my name...

Using a font based on this one: https://online-fonts.com/fonts/zelda-dxtt-brk-rus-subrain,
I created the text in a 7 box high grid in a spreadsheet. I set the top left box to be a
suitable Sunday, and then determined the dates that needed activity (some pivot table mangling...)

The used the python script to create some activity by:

- loop through all the determined dates
- create a dummy text file
- commit while over-riding the commit and author dates

push to the repo and...
