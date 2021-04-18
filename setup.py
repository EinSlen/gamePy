from cx_Freeze import setup, Executable
base = None
executablesreatch = [Executable("")]
executables = [Executable("game.py", base=base)]
packages = ["idna", "os", "re", "json"]
options = {
    'build_exe': {    
        'packages':packages,
    },
}
setup(
    name = "GameKit",
    options = options,
    version = "1.0",
    description = 'Play game in python',
    executables = executables, 
)