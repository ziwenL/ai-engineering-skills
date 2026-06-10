param(
    [Parameter(Mandatory=$true)]
    [string]$TargetProject
)

python "$PSScriptRoot\init_submodule_project.py" $TargetProject
