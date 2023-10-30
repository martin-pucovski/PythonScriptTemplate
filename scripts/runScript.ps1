$location = Split-Path $PSScriptRoot -Parent
Set-Location $location

# Replace 'path\to\your\venv' with the actual path to your virtual environment.
$venvPath = "venv"

# Replace 'your_script.py' with the name of your Python script.
$scriptName = "src/main.py"

# Activate the virtual environment
$activateScript = Join-Path $venvPath "Scripts/Activate"
if (Test-Path $activateScript) {
    & $activateScript
} else {
    Write-Host "Virtual environment activation script not found. Please check the path."
    exit 1
}

# Run the Python script
$scriptPath = Join-Path (Get-Location) $scriptName
if (Test-Path $scriptPath) {
    python $scriptPath
} else {
    Write-Host "Python script not found. Please check the script name and path."
}

# Deactivate the virtual environment (optional)
# Deactivate the virtual environment after running the script (optional).
deactivate

Read-Host "Press ENTER to exit..."