# Textbook_simplify
[Used to create training data for brain computer interfaces] Takes a large corpus of text/textbook/paper in a pdf format and uses a language model to summarise and simplify the text and chunks it into separate text files. 

MOTIVATION : scraping information from open source papers and textbooks for BCI training takes a while and the language used in more technical sources is not suitable for some BCI applications (e.g. we want to limit the complexity of sentences) the code also chunks it into suitable sized text files in order to display to a participant. 

The PDF(s) must be placed in a folder titled 'data' and the output simplfied text files are put in a 'processed_data' folder. 
