!pip -q install git+https://github.com/huggingface/transformers # need to install from github
!pip -q install accelerate>=0.12.0 

import torch
from transformers import pipeline

# use dolly-v2-12b if you're using Colab Pro+, using pythia-2.8b for Free Colab
generate_text = pipeline(model="databricks/dolly-v2-2-8b", 
                         torch_dtype=torch.bfloat16, 
                         trust_remote_code=True,
                         device_map="auto")

generate_text("Explain to me the difference between nuclear fission and fusion.")

generate_text("Explain self-attention and transformer to me like I'm 5 years old (ELI5).")
