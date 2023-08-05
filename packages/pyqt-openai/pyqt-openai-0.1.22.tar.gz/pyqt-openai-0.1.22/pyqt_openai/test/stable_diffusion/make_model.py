import torch
from diffusers import StableDiffusionPipeline
from torch import autocast
import streamlit as st
from PIL import Image, ImageEnhance
import pandas as pd
import numpy as np

class StableDiffusionLoader:
    """
    Stable Diffusion loader and generator class. 

    Utilises the stable diffusion models from the `Hugging Face`(https://huggingface.co/spaces/stabilityai/stable-diffusion) library

    Attributes
    ----------
    prompt : str
        a text prompt to use to generate an associated image
    pretrain_pipe : str
        a pretrained image diffusion pipeline i.e. CompVis/stable-diffusion-v1-4

    """
    def __init__(self, 
                prompt:str, 
                pretrain_pipe:str='CompVis/stable-diffusion-v1-4'):
        """
        Constructs all the necessary attributes for the diffusion class.

        Parameters
        ----------
            prompt : str
                the prompt to generate the model
            pretrain_pipe : str
                the name of the pretrained pipeline
        """
        self.prompt = prompt
        self.pretrain_pipe = pretrain_pipe
        print(torch.cuda.is_available())
        self.device = "cuda" if torch.cuda.is_available() else "cpu"

        if self.device == 'cpu':
            raise MemoryError('GPU need for inference')

        assert isinstance(self.prompt, str), 'Please enter a string into the prompt field'
        assert isinstance(self.pretrain_pipe, str), 'Please use value such as `CompVis/stable-diffusion-v1-4` for pretrained pipeline'


    def generate_image_from_prompt(self, save_location='prompt.jpg', use_token=False,
                                   verbose=False):

        pipe = StableDiffusionPipeline.from_pretrained(
            self.pretrain_pipe, 
            revision="fp16", torch_dtype=torch.float16, 
            use_auth_token=use_token
            )
        pipe = pipe.to(self.device)
        with autocast(self.device):
            image = pipe(self.prompt)[0][0]
        image.save(save_location)
        if verbose: 
            print(f'[INFO] saving image to {save_location}')
        return image    

    def __str__(self) -> str:
        return f'[INFO] Generating image for prompt: {self.prompt}'

    def __len__(self):
        return len(self.prompt)

if __name__ == '__main__':
    import os
    SAVE_LOCATION = 'prompt.jpg'

    sd = StableDiffusionLoader('toy store')
    sd.generate_image_from_prompt(save_location=SAVE_LOCATION)

    # Open and display the image on the site
    image = Image.open(SAVE_LOCATION)