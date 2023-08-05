# filter_choices
Filter Project
### Install filter_choices from PyPi.
```bash
pip install Image_Filters
```

### Example of code execution
```python
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import random
from filter_choices import Filters

#Important: Have your desired image to test, add the file to your program.
# Read the image file (valstrax is an example image)
img = mpimg.imread("valstrax.png")

#Initialize
filters = Filters(img)

# Apply desired filter
filtered_img = filters.color_inversion()

# Display the filtered image using Matplotlib
plt.imshow(filtered_img)
plt.show()
```

