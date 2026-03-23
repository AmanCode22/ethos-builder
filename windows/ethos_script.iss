#define MyAppName "Ethos"
#define MyAppVersion "0.2"
#define MyAppPublisher "Aman Adlakha"
#define MyAppURL "https://github.com/AmanCode22/ethos-lang"
#define MyAppExeName "ethos.exe"
#define MyAppAssocName MyAppName + " Program"
#define MyAppAssocExt ".ethos"
#define MyAppAssocKey StringChange(MyAppAssocName, " ", "") + MyAppAssocExt

[Setup]
AppId={{C6577A9B-DBF4-477C-BEBC-B318B09A8597}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName={autopf}\{#MyAppName}
UninstallDisplayIcon={app}\{#MyAppExeName}
SetupIconFile=..\ethos_logo.ico
ArchitecturesAllowed=x64compatible
ArchitecturesInstallIn64BitMode=x64compatible
DisableProgramGroupPage=yes
OutputBaseFilename=Ethos-v0.2-windows-installer
SolidCompression=yes
WizardStyle=modern dynamic windows11
ChangesEnvironment=yes

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "..\..\ethos.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\..\forge.exe"; DestDir: "{app}"; Flags: ignoreversion

[Registry]
Root: HKA; Subkey: "Software\Classes\{#MyAppAssocExt}\OpenWithProgids"; ValueType: string; ValueName: "{#MyAppAssocKey}"; ValueData: ""; Flags: uninsdeletevalue
Root: HKA; Subkey: "Software\Classes\{#MyAppAssocKey}"; ValueType: string; ValueName: ""; ValueData: "{#MyAppAssocName}"; Flags: uninsdeletekey
Root: HKA; Subkey: "Software\Classes\{#MyAppAssocKey}\DefaultIcon"; ValueType: string; ValueName: ""; ValueData: "{app}\{#MyAppExeName},0"
Root: HKA; Subkey: "Software\Classes\{#MyAppAssocKey}\shell\open\command"; ValueType: string; ValueName: ""; ValueData: """{app}\{#MyAppExeName}"" ""%1"""

[Dirs]
Name: "{%USERPROFILE}\.ethos"
Name: "{%USERPROFILE}\.ethos\traits"
Name: "{%USERPROFILE}\.ethos\traits\hard_traits"

[Code]
const
  EnvironmentKey = 'Environment';
  WM_WININICHANGE = $001A;

procedure CurStepChanged(CurStep: TSetupStep);
var
  Paths: string;
begin
  if CurStep = ssPostInstall then
  begin
    RegQueryStringValue(HKEY_CURRENT_USER, EnvironmentKey, 'Path', Paths);
    if Pos(';' + ExpandConstant('{app}'), ';' + Paths) = 0 then
    begin
      Paths := Paths + ';' + ExpandConstant('{app}');
      RegWriteExpandStringValue(HKEY_CURRENT_USER, EnvironmentKey, 'Path', Paths);
    end;
    SendBroadcastMessage(WM_WININICHANGE, 0, 'Environment');
  end;
end;

procedure CurUninstallStepChanged(CurUninstallStep: TUninstallStep);
var
  Paths: string;
  AppPath: string;
begin
  if CurUninstallStep = usPostUninstall then
  begin
    AppPath := ExpandConstant('{app}');
    if RegQueryStringValue(HKEY_CURRENT_USER, EnvironmentKey, 'Path', Paths) then
    begin
      StringChangeEx(Paths, ';' + AppPath, '', True);
      StringChangeEx(Paths, AppPath + ';', '', True);
      StringChangeEx(Paths, AppPath, '', True);
      RegWriteExpandStringValue(HKEY_CURRENT_USER, EnvironmentKey, 'Path', Paths);
      SendBroadcastMessage(WM_WININICHANGE, 0, 'Environment');
    end;
  end;
end;
