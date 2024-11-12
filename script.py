import asyncio
import importlib
import sys


async def main(script: str):
    """Run the script"""

    print(f"Running script: {script}\n")

    module = importlib.import_module(f"scripts.{script}")
    await module.run()


if __name__ == "__main__":
    asyncio.run(main(script=sys.argv[1]))
