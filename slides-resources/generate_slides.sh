#!/bin/bash

# ---------- #
#  Generate pdf versions of all slides, to be run from main folder
#   source slides-resources/generate_slides.sh
# ---------- #

# Hard code the folder locations
folder_md="slides-resources"
folder_pdf="lessons"
num_lectures=3
counter=0

# Make the lessons folder if it does not exist already
if [ ! -d "$folder_pdf" ]; then
    echo "Making folder: '$folder_pdf'"
    mkdir $folder_pdf
else
    echo "Folder '$folder_pdf' already exists"
fi

# Ensure marp cli is set up: https://github.com/marp-team/marp-cli
marp --version &> /dev/null

# Check the exit status of the previous command
if [ $? -eq 0 ]; then
    echo "Marp CLI is set up."
else
    echo "Marp CLI is not set up. Please install"
fi

# Get list of files
markdown_files=$(ls $folder_md | grep ".md$")

# Loop over each file
for markdown_file in $markdown_files; do
    # Update the counter
    ((counter++))
    if [ $counter -gt $num_lectures ]; then
        echo "Counter exceeds the limit of $num_lectures. Exiting loop."
        break
    fi
    echo "markdown file: "$markdown_file
    file_out="${markdown_file%.md}.pdf"
    echo "counter="$counter
    marp $folder_md/$markdown_file --output $folder_pdf/$file_out --html --allow-local-files --pdf --pdf-notes
done


echo "~~~ End of generate_slides.sh ~~~"
