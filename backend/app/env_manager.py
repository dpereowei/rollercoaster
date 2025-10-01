import asyncio

async def provision_environment(name: str):
    cmd = f"echo 'Provisioning environment {name}'"
    process = await asyncio.create_subprocess_shell(cmd)
    await process.communicate()
    return True

async def teardown_environment(name: str):
    cmd = f"echo 'Tearing down environment {name}'"
    process = await asyncio.create_subprocess_shell(cmd)
    await process.communicate()
    return True