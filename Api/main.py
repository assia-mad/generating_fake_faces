import io
from PIL import Image
from fastapi import FastAPI
import numpy as np
from tensorflow.keras.models import load_model
from fastapi.middleware.cors import CORSMiddleware
import numpy as np 
import matplotlib.pyplot as plt  
from fastapi.responses import JSONResponse
import base64

app = FastAPI()
model = load_model('generator_2.h5')



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/generate_image")
def generate_image(num_images: int = 1, square: int = 5, epochs: int = 0):
    plt.figure(figsize=(10, 10))
    for i in range(num_images):
        if epochs != 0:
            if i == num_images // 2:
                plt.title("Generated Image at Epoch:{}\n".format(epochs), fontsize=32, color="black")
        plt.subplot(square, square, i + 1)

        noise = np.random.normal(0, 1, (1, 100))
        img = model(noise)

        plt.imshow(np.clip((img[0, ...] + 1) / 2, 0, 1))

        plt.xticks([])
        plt.yticks([])
        plt.grid()

    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)

    encoded_image = base64.b64encode(buf.getvalue()).decode("utf-8")

    return JSONResponse(content={"image": encoded_image})



