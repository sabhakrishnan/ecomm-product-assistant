




uv python list
uv venv env --python cpython-3.10.18-windows-x86_64-none
uv venv <your-env-name> --python <your-python-version>

Note: please use either 3.10 pr 3.11 or 3.12

Activate the venv:
    - cmd: .\<your-env-name>\scripts\Activate.bat
    - git bash or MAC terminal: source ./<your-env-name>/scripts/Activate

Install the Packages in the requirements.txt
    Why the UV is faster - its written under a RUST language
    - uv pip install -r requirements.txt


