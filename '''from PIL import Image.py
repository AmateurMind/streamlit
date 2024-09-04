'''from PIL import Image

 Open the image from the specified path
image = Image.open("C:\\Users\\suhai\\Desktop\\hello.jpg")
left_co, cent_co,last_co = st.columns(3)
with cent_co:
    st.image(image, caption='My logo')
    
data visualisation
import pandas as pd
import numpy as np
st.title("bar chart")
data=pd.DataFrame(np.random.randn(50,2),columns=['x','y'])
st.bar_chart(data)'''