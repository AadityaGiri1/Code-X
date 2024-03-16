import torch
from waveglow import WaveGlow

# Load WaveGlow model
waveglow = WaveGlow().cuda()  # Use .cuda() if you have a GPU, otherwise remove it
waveglow.load_state_dict(torch.load('path/to/waveglow_checkpoint.pt')['model'])
waveglow = waveglow.remove_weightnorm(waveglow)
_ = waveglow.eval()

