# Run PowerShell as Administrator before executing this script
if (-not ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
    Write-Warning "Please run PowerShell as Administrator!"
    exit 1
}

# Optional: Point Vagrant box cache & Hyper-V storage to a secondary drive (e.g., D:\)
$DriveLetter = "D:"
if (Test-Path $DriveLetter) {
    $env:VAGRANT_HOME = "$DriveLetter\VagrantData\.vagrant.d"
    New-Item -ItemType Directory -Force -Path "$DriveLetter\VagrantData\.vagrant.d", "$DriveLetter\HyperV\VirtualHardDisks", "$DriveLetter\HyperV\VirtualMachines" | Out-Null
    Set-VMHost -VirtualHardDiskPath "$DriveLetter\HyperV\VirtualHardDisks" -VirtualMachinePath "$DriveLetter\HyperV\VirtualMachines"
}

# Launch the Ubuntu 22.04 VM using Windows Hyper-V
Set-Location $PSScriptRoot
vagrant up --provider=hyperv
