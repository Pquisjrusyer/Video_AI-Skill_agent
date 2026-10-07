# Xử lý link "aivideo-open:<đường dẫn>" từ bảng HTML → mở File Explorer tới file / thư mục đó.
# AN TOÀN: chỉ dùng explorer.exe để MỞ THƯ MỤC hoặc CHỌN file (/select) — không bao giờ chạy / mở file.
# Được đăng ký bởi install-open-handler.ps1 (user tự chạy 1 lần).
param([string]$Url = "")
$p = [Uri]::UnescapeDataString(($Url -replace '^aivideo-open:(//)?', ''))
$p = $p -replace '/', '\'
if (-not $p) { exit 1 }
if (Test-Path -LiteralPath $p -PathType Container) { & explorer.exe $p; exit 0 }
if (Test-Path -LiteralPath $p -PathType Leaf) { & explorer.exe "/select,$p"; exit 0 }
$dir = Split-Path -Parent $p
while ($dir -and -not (Test-Path -LiteralPath $dir -PathType Container)) { $dir = Split-Path -Parent $dir }
if ($dir) { & explorer.exe $dir }
