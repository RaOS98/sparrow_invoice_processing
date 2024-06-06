# Check if Python is installed
if (-Not (Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Error "Python is required but it's not installed. Aborting."
    exit 1
}

# Check Python version
$pythonVersion = & python --version 2>&1
Write-Output "Detected Python version: $pythonVersion"
if ($pythonVersion -notmatch "3.10.4") {
    Write-Error "Python version 3.10.4 is required. Current version is $pythonVersion. Aborting."
    exit 1
}

$pythonScriptPath = "engine.py"

# Check if the "ingest" flag is passed
if ($args[0] -eq "ingest") {
    $pythonScriptPath = "ingest.py"
    $args = $args[1..$args.Length] # Shift the arguments to exclude the first one
}

if ($args[0] -eq "assistant") {
    $pythonScriptPath = "assistant.py"
    $args = $args[1..$args.Length] # Shift the arguments to exclude the first one
}

# Run the selected Python script with the remaining arguments
& python $pythonScriptPath @args