import subprocess
from pathlib import Path

TEMPLATE_PATH = Path("/app/terraform/templates/basic")
WORKSPACE_ROOT = Path("/tmp/terraform_envs")

def run_terraform(env_id: int):
    env_dir = WORKSPACE_ROOT / f"env_{env_id}"
    env_dir.mkdir(parents=True, exist_ok=True)
    for file in TEMPLATE_PATH.iterdir():
        dest = env_dir / file.name
        if not dest.exists():
            dest.write_text(file.read_text())

    cmds = [
        ["terraform", "init"],
        ["terraform", "apply", "-auto-approve", f"-var=env_id={env_id}"]
    ]

    for cmd in cmds:
        subprocess.run(cmd, cwd=env_dir, check=True)

def destroy_terraform(env_id: int):
    env_dir = WORKSPACE_ROOT / f"env_{env_id}"
    if not env_dir.exists():
        return
    subprocess.run(["terraform", "destroy", "-auto-approve", f"-var=env_id={env_id}"], cwd=env_dir, check=False)