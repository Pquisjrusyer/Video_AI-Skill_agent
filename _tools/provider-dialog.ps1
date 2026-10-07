# Popup Windows "gọi hồn provider" — từng bước: chọn nhà → đã có key chưa? → (hướng dẫn lấy key) → nhập key.
# pick-provider.sh gọi. Dữ liệu nhà cung cấp: providers.json (cùng thư mục) + ~/.config/ai-studio/providers-custom.json.
# stdout (mỗi dòng 1 mục): PROVIDER=<id> · ENV:<TÊN>=<giá trị> · DEFAULT=0|1 · CUSTOM=<json> (chỉ nhà tự thêm). Huỷ → exit 1.
# File lưu UTF-8 có BOM để PowerShell 5.1 hiện đúng tiếng Việt.
param([string]$Task = "image", [string]$Reason = "", [string]$Exclude = "")
Add-Type -AssemblyName System.Windows.Forms, System.Drawing
$ErrorActionPreference = "Stop"
$font = New-Object Drawing.Font("Segoe UI", 9.5)

$data = Get-Content -Raw -Encoding UTF8 (Join-Path $PSScriptRoot "providers.json") | ConvertFrom-Json
$list = @($data.$Task)
$customFile = Join-Path $env:USERPROFILE ".config\ai-studio\providers-custom.json"
if (Test-Path $customFile) {
  $cj = Get-Content -Raw -Encoding UTF8 $customFile | ConvertFrom-Json
  foreach ($p in $cj.PSObject.Properties) {
    $c = $p.Value
    $list = @([pscustomobject]@{ id = "custom:" + $p.Name; label = "$($p.Name) — nhà tự thêm ($($c.model))"; refs = $c.refs; url = "";
      keys = @([pscustomobject]@{ env = $c.key_env; label = "API key"; hidden = $true });
      guide = @("Nhà tự thêm: $($c.base_url)", "Lấy key mới ở trang quản lý API của nhà đó.") }) + $list
  }
}
$skip = $Exclude.Split(",")
$items = @($list | Where-Object { $skip -notcontains $_.id })

function New-Form($title, $h) {
  $f = New-Object Windows.Forms.Form
  $f.Text = $title; $f.Width = 580; $f.Height = $h; $f.Font = $font
  $f.StartPosition = "CenterScreen"; $f.TopMost = $true; $f.FormBorderStyle = "FixedDialog"; $f.MaximizeBox = $false; $f.MinimizeBox = $false
  $f.Add_Shown({ $this.Activate() }); return $f
}
function Add-Label($f, $text, $top, $h) {
  $l = New-Object Windows.Forms.Label; $l.Text = $text; $l.Left = 14; $l.Top = $top; $l.Width = 535; $l.Height = $h; $f.Controls.Add($l); return $l
}
function Add-Btn($f, $text, $left, $top, $w, $result) {
  $b = New-Object Windows.Forms.Button; $b.Text = $text; $b.Left = $left; $b.Top = $top; $b.Width = $w; $b.Height = 30
  $b.DialogResult = $result; $f.Controls.Add($b); return $b
}

$step = "pick"; $sel = $null; $title = "🔮 AI Video — gọi hồn provider"
while ($true) {
  if ($step -eq "pick") {
    $f = New-Form $title 420
    [void](Add-Label $f "$Reason`n`nBước 1/3 — Chọn nhà cung cấp:" 12 62)
    $lb = New-Object Windows.Forms.ListBox; $lb.Left = 14; $lb.Top = 78; $lb.Width = 535; $lb.Height = 230
    foreach ($i in $items) { [void]$lb.Items.Add($i.label) }; $lb.SelectedIndex = 0; $f.Controls.Add($lb)
    $ok = Add-Btn $f "Tiếp ›" 370 325 85 "OK"; [void](Add-Btn $f "Huỷ" 464 325 85 "Cancel")
    $f.AcceptButton = $ok; $lb.Add_DoubleClick({ $f.DialogResult = "OK"; $f.Close() })
    if ($f.ShowDialog() -ne "OK") { exit 1 }
    $sel = $items[$lb.SelectedIndex]; $step = "have"
  }
  elseif ($step -eq "have") {
    $f = New-Form $title 210
    [void](Add-Label $f "Bước 2/3 — Bạn đã có key của:`n$($sel.label)`nchưa?" 12 64)
    $yes = Add-Btn $f "Có rồi › nhập key" 14 100 170 "Yes"
    [void](Add-Btn $f "Chưa / chưa biết lấy ở đâu" 192 100 210 "No")
    [void](Add-Btn $f "‹ Quay lại" 410 100 139 "Retry")
    $f.AcceptButton = $yes
    $r = $f.ShowDialog()
    if ($r -eq "Yes") { $step = "input" } elseif ($r -eq "No") { $step = "guide" } elseif ($r -eq "Retry") { $step = "pick" } else { exit 1 }
  }
  elseif ($step -eq "guide") {
    $n = 0; $txt = ($sel.guide | ForEach-Object { $n++; "$n. $_" }) -join "`n`n"
    $f = New-Form "📖 Hướng dẫn lấy key — $($sel.id)" 430
    [void](Add-Label $f "Bước 2/3 — Làm theo các bước sau, xong bấm Hoàn tất:" 12 22)
    $tb = New-Object Windows.Forms.TextBox; $tb.Multiline = $true; $tb.ReadOnly = $true; $tb.ScrollBars = "Vertical"
    $tb.Left = 14; $tb.Top = 40; $tb.Width = 535; $tb.Height = 270; $tb.Text = $txt -replace "`n", "`r`n"; $f.Controls.Add($tb)
    if ($sel.url) {
      $open = New-Object Windows.Forms.Button; $open.Text = "🌐 Mở trang lấy key"; $open.Left = 14; $open.Top = 325; $open.Width = 170; $open.Height = 30
      $u = $sel.url; $open.Add_Click({ Start-Process $u }.GetNewClosure()); $f.Controls.Add($open)
    }
    $done = Add-Btn $f "Hoàn tất › nhập key" 260 325 170 "OK"; [void](Add-Btn $f "‹ Quay lại" 438 325 111 "Retry")
    $f.AcceptButton = $done
    $r = $f.ShowDialog()
    if ($r -eq "OK") { $step = "input" } elseif ($r -eq "Retry") { $step = "have" } else { exit 1 }
  }
  elseif ($step -eq "input") {
    $isNew = ($sel.id -eq "custom")
    $f = New-Form $title 0
    [void](Add-Label $f "Bước 3/3 — Nhập thông tin $($sel.id) (ô key bị ẩn; để trống = giữ key đã lưu):" 12 22)
    $top = 42; $boxes = @()
    $fields = if ($isNew) { @(
        [pscustomobject]@{ env = "_NAME"; label = "Tên nhà cung cấp (không dấu, VD together)"; hidden = $false },
        [pscustomobject]@{ env = "_BASE"; label = "Base URL (VD https://api.together.xyz/v1)"; hidden = $false },
        [pscustomobject]@{ env = "_MODEL"; label = "Model ảnh (VD black-forest-labs/FLUX.1-schnell)"; hidden = $false },
        [pscustomobject]@{ env = "_KEY"; label = "API key"; hidden = $true }) } else { @($sel.keys) }
    foreach ($k in $fields) {
      [void](Add-Label $f $k.label $top 20)
      $tb = New-Object Windows.Forms.TextBox; $tb.Left = 14; $tb.Top = $top + 21; $tb.Width = 535
      if ($k.hidden) { $tb.UseSystemPasswordChar = $true }
      $f.Controls.Add($tb); $boxes += , @($k.env, $tb); $top += 54
    }
    if ($isNew) { $rf = New-Object Windows.Forms.CheckBox; $rf.Text = "Có ảnh tham chiếu (nhà có /images/edits)"; $rf.Left = 14; $rf.Top = $top; $rf.Width = 535; $f.Controls.Add($rf); $top += 28 }
    $d = New-Object Windows.Forms.CheckBox; $d.Text = "Dùng nhà cung cấp này làm mặc định từ giờ"; $d.Left = 14; $d.Top = $top; $d.Width = 535; $f.Controls.Add($d); $top += 40
    $ok = Add-Btn $f "Dùng ✓" 280 $top 85 "OK"; [void](Add-Btn $f "‹ Quay lại" 373 $top 85 "Retry"); [void](Add-Btn $f "Huỷ" 466 $top 83 "Cancel")
    $f.Height = $top + 80; $f.AcceptButton = $ok
    $f.Add_Shown({ if ($boxes.Count) { $boxes[0][1].Focus() } })
    $r = $f.ShowDialog()
    if ($r -eq "Retry") { $step = "have"; continue }
    if ($r -ne "OK") { exit 1 }
    $out = @()
    if ($isNew) {
      $v = @{}; foreach ($b in $boxes) { $v[$b[0]] = $b[1].Text.Trim() }
      $slug = ($v["_NAME"].ToLower() -replace "[^a-z0-9]", "")
      if (-not $slug -or -not $v["_BASE"] -or -not $v["_MODEL"]) { [Windows.Forms.MessageBox]::Show("Cần đủ Tên, Base URL và Model.") | Out-Null; continue }
      $envName = "CUSTOM_" + $slug.ToUpper() + "_API_KEY"
      $out += "PROVIDER=custom:$slug"
      $out += "ENV:$envName=" + $v["_KEY"]
      $out += "CUSTOM=" + (@{ name = $slug; base_url = $v["_BASE"].TrimEnd("/"); model = $v["_MODEL"]; refs = [bool]$rf.Checked; key_env = $envName } | ConvertTo-Json -Compress)
    } else {
      $out += "PROVIDER=" + $sel.id
      foreach ($b in $boxes) { $out += "ENV:" + $b[0] + "=" + $b[1].Text.Trim() }
    }
    $out += "DEFAULT=" + [int]$d.Checked
    [Console]::OutputEncoding = [Text.Encoding]::UTF8
    [Console]::Out.Write(($out -join "`n") + "`n"); exit 0
  }
}
