import wandb

print(f"The version of wandb is: {wandb.__version__}")

assert wandb.__version__ == "0.15.8", f"the expected version of wandb is {wandb.__version__}"
