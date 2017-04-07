$VersionControl='git'
$Package='pip'
$Build='python'

$Test='pytest'
$TestInclude='./test/'

$Deploy = 'none'
$Run = 'process'
$RunStartCommand = 'python'
$RunStartArguments = @('-m', './bin/run.py', './config/config.yaml')
