import os

requirements = [
    "requests",
    "httpx",
]

for requirement in requirements:
    try:
        os.system(f"pip install {requirement}" if os.name == "nt" else f"pip3 install {requirement}")
    except Exception as e:
        print(f"Failed to install {requirement}: use " + f"`pip install {requirement}`" if os.name == "nt" else f"`pip3 install {requirement}`")

os.system("python main.py" if os.name == "nt" else "python3 main.py")