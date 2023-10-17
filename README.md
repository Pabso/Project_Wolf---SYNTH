# Project_Wolf---SYNTH
Project Wolf is a synthesizer to AI generated Image Generator 

## Install Procedure

1. **install base programs**
install `Python3` [the download link is here](-----)
intall `miniConda` [the download link is here](https://docs.conda.io/projects/miniconda/en/latest/miniconda-install.html#)

2. **Open up Project folder (In main directory)**

3. **Run the following Commands in order**
    ```
    git clone https://github.com/HelixNGC7293/DeforumStableDiffusionLocal.git
    conda create --name dsd python=3.10.6 -y
    conda activate dsd
    python3 DeforumStableDiffusionLocal/setup.py
    ```

4. **Change the name of "runSettings_Template.txt" to runSettings.txt, and format file in DeforumStableDiffusionLocal**

5. **Install Model files**

You need to put these 3 model files on the `.DeforumStableDiffusionLocal/models` folder:

**`v1-5-pruned-emaonly.ckpt`, can be downloaded from [HuggingFace](https://huggingface.co/runwayml/stable-diffusion-v1-5/tree/main).**

**`dpt_large-midas-2f21e586.pt`, [the download link is here](https://github.com/intel-isl/DPT/releases/download/1_0/dpt_large-midas-2f21e586.pt)**

**`AdaBins_nyu.pt`, [the download link is here](https://cloudflare-ipfs.com/ipfs/Qmd2mMnDLWePKmgfS8m6ntAg4nhV5VkUyAydYBp8cWWeB7/AdaBins_nyu.pt)**


**it should be noted that these processes will take time**


## Running Procedure

Be in the main directory of the git Project_Wolf_SYNTH and run the following 

```
python3 main.py
```

A video should be made in the output folder of the stable diffusion program


