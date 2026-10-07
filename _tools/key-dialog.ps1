# Hộp thoại Windows (ô ẩn) để nhập key — set-key.sh gọi khi không có osascript (macOS).
# In key ra stdout cho set-key.sh ghi file; không lưu, không log. Huỷ → exit 1.
param([string]$Name = "KEY")
Add-Type -AssemblyName System.Windows.Forms
$f = New-Object Windows.Forms.Form
$f.Text = "AI Video - nhap key"; $f.Width = 460; $f.Height = 170
$f.StartPosition = "CenterScreen"; $f.TopMost = $true; $f.FormBorderStyle = "FixedDialog"; $f.MaximizeBox = $false
$l = New-Object Windows.Forms.Label
$l.Text = "Dan $Name vao o duoi roi bam OK."; $l.Left = 12; $l.Top = 12; $l.Width = 420
$t = New-Object Windows.Forms.TextBox
$t.UseSystemPasswordChar = $true; $t.Left = 12; $t.Top = 40; $t.Width = 420
$ok = New-Object Windows.Forms.Button
$ok.Text = "OK"; $ok.Left = 272; $ok.Top = 80; $ok.DialogResult = "OK"
$no = New-Object Windows.Forms.Button
$no.Text = "Huy"; $no.Left = 357; $no.Top = 80; $no.DialogResult = "Cancel"
$f.Controls.AddRange(@($l, $t, $ok, $no)); $f.AcceptButton = $ok; $f.CancelButton = $no
$f.Add_Shown({ $f.Activate(); $t.Focus() })
if ($f.ShowDialog() -ne "OK") { exit 1 }
[Console]::Out.Write($t.Text)
