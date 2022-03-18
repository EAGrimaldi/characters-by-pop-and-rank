# characters-by-pop-and-rank

A quick tool for assessing character strength in a video game according to popularity, possibly also weighted by rank.

This was initially built and used to analyze the population of main characters in the Celestial VIP rank of Guilty Gear Strive on the North American server. This dataset is included as an example.

# how to run

In a terminal `python3 <path-to-package>/analysis.py [arguments]` should work from anywhere.

use `--print` to print the results to the terminal

use `--save` to save the results to a file; the name will be chosen automatically according to the name of the input dataset and all parameters; the file is lazily saved into the same directory as the script

use `--sort [method]` to choose a sorting method for the results; `'pop'` sorts by the result of the analysis, and `'name'` sorts by name

use `--gamma [float]` to enable gamma decay and set gamma; gamma=1 disables gamma decay

use `--fp [file path]` if you would like to supply your own dataset

NOTE: make sure your dataset uses the same format as the example dataset

* best player at top descending in order to worst player at bottom
* each line only contains the player's main character
* no ties
* if there are gaps in your data, you need to put a throwaway string on lines corresponding to gaps

# requirements

You just need python 3.6+

I lazily used `distutils.util.strtobool`, which is deprecated and will be removed in python 3.12+ (not relevant yet, but kind of funny)
