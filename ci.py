import wandb

print(f"The version of wandb is: {wandb.__version__}")

assert wandb.__version__ == wandb.__version__, f"the expected version of wandb is {wandb.__version__}"
